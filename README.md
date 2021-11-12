# Airtraffic-Control-Simulation-System

The system for our CS 3354 Systems Engineering Course

## Project Structure

.kv files are "kivy" files, a file type specific to our front-end implementation

<<<<<<< HEAD
- main.py - *Contains the app definition, loads main.kv and Screens.py*
- main.kv  - *Loads individual screens and sets up window manager*
- Screens.py - *Contains class defintions for screens*
- Screens - *Contains .kv files that contain kivy widget defintions. Each file corresponds to a class in Screens.py*
  - ...

## Setup
1. Clone git repo:
   > git clone https://github.com/PickleMustard/Airtraffic-Control-Simulation-System.git
2. Move current directory to Airtraffic-Control-Simulation-System
3. Install [python 3.9.7](https://www.python.org/downloads/release/python-397/)
4. Install [pipenv](https://github.com/pypa/pipenv#installation)
5. > pipenv install --dev
6. Switch to your branch with 
   > git checkout *branch*

## Update Development Environment
   Install dependencies
   > pipenv install --dev

   Ensure that it **is** "--dev" and **not** "-dev"

## Basic Git Instructions

### Pull Updates
> git pull

### Update YOUR branch
1. Navigate to the directory your branch is in
2. > git add .
3. > git commit -m "*message*" -a
4. > git push origin *branch*

### Push to a different branch
1. Navigate to the directory your branch is in
2. > git add .
3. > git commit -m "*message*" -a
4. > git push origin *sourceBranch*:*destinationBranch*

## Kivy Instructions

#Creating the Database
To ensure the database is able to run, take these steps
1. Ensure that mySQL is installed on your computer
	>https://dev.mysql.com/downloads
	>Go to terminal and type mysql, if nothing occurs, it needs to be installed
	>Go to the link above and follow steps to setup on your machine
2. Create a user that has all permissions with a unique username and password
3. Go into CreateDatabase.py and MasterLogAccess.py and change the username and password to the unique ones created
4. Run CreateDatabase.py
	>This will create the database and tables that we use
5. The database should be prepped along with the code

### Run the app
> pipenv run python main.py
