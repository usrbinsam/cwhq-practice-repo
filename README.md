# Git and VSCode

This repository is designed to be used for you to practice getting your
development environment setup to work with a team on a simple Flask project.


# What You Need

- A Windows or macOS computer.
  - Linux based OSes will work too, but you are on your own!
- VSCode (see prerequisites below)
- Git SCM (see prerequisites below)
- A GitHub account

# Prerequisites

- Install VSCode for your operating system: https://code.visualstudio.com/
  - You may leave all installer options at the default selections.
- Install Git for your operating: https://git-scm.com/
  - Click the Next button leaving all the installer options as the default, until you reach "Which editor would you like Git to use?" and select "Use Visual Studio Code as Git's default editor"
  - All other options may be left as default.
- Python 3 - see the Python Installation section below for your operating system.


# Step 1: Python Installation

## Windows

- Visit https://www.python.org/ then hover over the **Downloads** link, and click the "Python 3.X.Y" (version number may vary)

  ![Python Download for Windows](screenshots/PythonDownloadButton.png)
- :warning: Before clicking **Install Now**, tick the box next to "Add Python 3.X to PATH" :warning:

  ![Python Installer for Windows](screenshots/PythonInstallerAddToPATH.png)

- Click **Install Now** and let the installer complete.

## macOS

TODO

# Step 2: Clone this repository with Git

Before starting, create a projects folder somewhere on your computer where you will remember. All of your git projects should be stored in this folder.

A good could be a Projects folder created inside your Documents folder.

- Open VSCode for the first time.
- Launch the Command Palette (Windows: `Ctrl+Shift+P`, macOS: `⌘⇧P`) and type in `clone`
- **Git: Clone** will appear - press `Enter`
- Paste in the URL for this repository: `https://github.com/codewizardshq/apps.git` and press `Enter`
- A folder window will appear. Navigate to the projects folder you created and click the **Select Repository Location** button.
- You may be asked to enter your GitHub credentials. Enter the username and password to your GitHub account if prompted.
- VSCode will offer to open the project for you - go ahead and click Open Project.
- VSCode will notify you that this workspace has extension recommandations - click **Install All**
  ![Extension Recommandations](screenshots/codeRecommendations.png)


# Step 3: VSCode Setup

Before beginning development, we want to perform some basic setup in Visual Studio Code.

## Select Default Terminal (Windows only)

On Windows, the VSCode Terminal will be PowerShell which is not friendly for this type of work. To change it to the
standard cmd.exe:

- Use `Ctrl+Shift+P` to open the command pallette.
- Start typing in "select default shell" until `Terminal: Select Default Shell` is highlighted, then press `Enter`
- Click the `Command Prompt` option


# Step 4 Python Module Setup

## Windows Step Only: Modify your PATH variable

In order for Pipenv and Flask to work on the command line, we need to tell Windows where these new programs will be installed. To do so, you must edit your environment's PATH variables.

- Open the start menu and start typing "path" until you see "Edit the system environment variables" and hit Enter
  ![Start Menu PATH](screenshots/startPath.png)
- Click "Environment Variables"

  ![Environment Variables](screenshots/envVars.png)
- In the upper box, click "Path" under "User variables for `username`
- Click Edit

  ![User PATH](screenshots/userPathEdit.png)
- Add 2 new entries, - :warning: Make sure you replace the username part with your Windows username!

  - `C:\Users\YOURUSERNAMEHERE\AppData\Local\Programs\Python\Python38-32\`
  - `C:\Users\YOURUSERNAMEHERE\AppData\Local\Programs\Python\Python38-32\Scripts\`
  ![New Entries](screenshots/newEnvVar.png)

- Reboot your computer before continuing to the next step.

## Step 4a: Pipenv

All Flask projects require some 3rd party modules - the Flask library is written in Python but it does not come with the default Python installer. We need to install Flask ourselves, but luckily this is very easy with `pipenv` which can install 3rd party modules like Flask with minimal effort. It also manages the versions of these 3rd party modules we depend about.

- Open a new terminal within VS Code using Ctrl+` (this is the backtick key, it is found below the Esc key)
- Type in `pip install -U pip pipenv` and press `Enter` to ensure pip is at the latest version, and to install pipenv
  - :warning: If this step fails, you forgot to check the "Add Python 3.X to PATH" checkbox while installing Python. Go back to that step and re-install python.
- Type in `pipenv install --dev` to install all 3rd party requirements specific to this project
- Type in `pipenv shell` to enter into the Python environment
- Restart VSCode (required for Step 4b)


## Step 4b: Select Python Interpreter

Pipenv creates an isolated version of your installed Python. We need to tell VSCode to use this interpreter, otherwise
when we go to launch our Flask application, the 3rd party modules won't be found. You need to perform this step any time
you create a new pipenv environment (number 3 in step 4a)

- Use `Ctrl+Shift+P` to open the command pallete.
- Start typing in "interpreter" until `Python: Select Interpreter` appears and hit `Enter`
- You may be prompted to select the workspace, choose the first entry
  ![Select Workspace](screenshots/selectInterpreter1.png)

- Select the interpreter that has `pipenv` in the name and matches the name of the workspace you chose.
  ![Select Workspace](screenshots/selectInterpreter2.png)

## Launching Flask

Flask applications can be launched several different ways, but the most common way is on the command line using the `flask` command that comes with the flask pip package.

- Open a terminal in VSCode either via the Command Palette or with Ctrl Shift `
  ![Create New Terminal](screenshots/createTerminal.png)
- Type in the following commands:
  - `set FLASK_APP=app.py`
  - `set FLASK_ENV=development`
  - `flask run`

  ![Flask Run](screenshots/flaskrun.png)

- Open a web browser tab  to the link shown in your terminal, most likely `http://127.0.0.1:5000`

If everything installed correctly, you should see a screen like this:

![Hello World](screenshots/helloWorld.png)


# VSCode Useful Shortcuts

- Command Palette
  - Windows/Linux: `Ctrl+Shift+P`
  - macOS: `⌘⇧P`
