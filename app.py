from flask import Flask, render_template_string, __version__
import platform
import sys
import re
from subprocess import check_output, CalledProcessError

app = Flask(__name__)


MATCH_GIT_VERSION = re.compile(r"^git version ([0-9]+)\.([0-9]+)\.([0-9]+)")


@app.route("/")
def index():

    try:
        import pymysql
        pymysql_version = pymysql.__version__
    except ImportError:
        pymysql_version = "(not installed)"

    components = []

    try:
        git_version = check_output("git --version", shell=True).decode("utf8").strip()
    except (CalledProcessError, FileNotFoundError):
        git_version = "(not installed)"

    git_version_tuple = None
    match = MATCH_GIT_VERSION.search(git_version)  # type: re.Match
    if match is not None:
        major, minor, patch = match.group(1, 2, 3)
        git_version_tuple = (int(major), int(minor), int(patch))

    try:
        code_version = check_output(["code", "--version"], shell=True).decode("utf8")
        code_version = code_version.split("\n")[0]
        code_python_ext = check_output(["code", "--list-extensions"], shell=True).decode("utf8")
    except (CalledProcessError, FileNotFoundError):
        code_version = "(not installed)"
        code_python_ext = "(not installed)"

    components.append({
        "name": "Operating System",
        "installed_version": platform.system(),
        "required_version": "Darwin (macOS) or Windows",
        "pass_fail": platform.system().lower() in ("windows", "darwin")
    })

    components.append({
        "name": "git",
        "installed_version": f"{git_version_tuple} ({git_version})",
        "required_version": "2.18+",
        "pass_fail": git_version_tuple is not None and git_version_tuple >= (2, 18)
    })

    components.append({
        "name": "Python",
        "installed_version": platform.python_version(),
        "required_version": "3.6+",
        "pass_fail": sys.version_info >= (3, 6)
    })

    components.append({
        "name": "Flask",
        "installed_version": __version__,
        "required_version": "1.1+",
        "pass_fail": __version__.startswith("1.1")
    })

    components.append({
        "name": "PyMySQL",
        "installed_version": pymysql_version,
        "required_version": "any",
        "pass_fail": pymysql_version != "(not installed)"
    })

    components.append({
        "name": "Visual Studio Code",
        "installed_version": code_version,
        "required_version": "any",
        "pass_fail": code_version != "(not installed)"
    })

    if platform.system() != "darwin":
        py_installed = "ms-python.python" if "ms-python.python" in code_python_ext else "(not installed)"
        gl_installed = "eamodio.gitlens" if "eamodio.gitlens" in code_python_ext else "(not installed)"
    else:
        py_installed = "(unable to check on macOS)"
        gl_installed = "(unable to check on macOS)"

    components.append({
        "name": "VSCode Python Extension",
        "installed_version": py_installed,
        "required_version": "N/A",
        "pass_fail": "ms-python.python" in code_python_ext
    })

    components.append({
        "name": "VSCode GitLens Extension",
        "installed_version": gl_installed,
        "required_version": "N/A",
        "pass_fail": "eamodio.gitlens" in code_python_ext
    })

    return render_template_string(
        """
        <!DOCTYPE html>
        <html>
            <head>

            <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
            <!-- <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script> -->

            <style>
            .pass {
                color: lightgreen;
                font-weight: bold;
            }
            .fail {
                color: red;
                font-weight: bold;
            }
            </style>

            </head>
                <body>

                <div class="container">

                <h1>Hello World!</h1>
                <p>Check the table below for any fields that indicate failure.</p>


                <h2>System Check</h2>

                <table class="table">
                <thead>

                    <tr>
                        <th>Component</th>
                        <th>Detected Version</th>
                        <th>Required Version</th>
                        <th>Pass/Fail</th>
                    </tr>
                </thead>
                <tbody>

                    {% for component in components %}

                    <tr>
                        <td>{{ component.name }}</td>
                        <td>{{ component.installed_version }}</td>
                        <td>{{ component.required_version }}</td>
                        <td>
                        {% if component.pass_fail %}
                            <span class="pass">PASS</span>
                        {% else %}
                            <span class="fail">FAIL</span>
                        {% endif %}
                        </td>
                    </tr>

                    {% endfor %}
                </tbody>
                </table>
                </div>
            </body>
        </html>
    """, components=components)


if __name__ == "__main__":
    app.debug = True
    app.run()