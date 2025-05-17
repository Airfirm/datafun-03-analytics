# datafun-03-analytics
""" This is a new repo folder for Python Data Project in Module 3.
I had created a .gitignore, requirements.txt with external dependency
'requests' as the content of my requirements file and all other comments 
commented out!

Author: O S

"""






"""
File: dirbot_oluwafemi.py

Purpose: Automate the creation of project folders 
(and demonstrate basic Python coding skills).

Author: O S

"""

#####################################
# Import Modules at the Top
#####################################

# Import from the Python Standard library
import pathlib
import sys   
import os 
import logging
import time
from typing import Union

# Import packages from requirements.txt
import loguru   

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
import utils_oluwafemi

#####################################
# Configure Logger and Verify
#####################################

logger = loguru.logger
logger.add("project.log", level="INFO", rotation="100 KB") 
logger.info("Logger loaded.")

#####################################
# Declare global variables
#####################################

# Create a project path object for the root directory of the project.
ROOT_DIR = pathlib.Path.cwd()

REGIONS = [
    "North America", 
    "South America", 
    "Europe", 
    "Asia", 
    "Africa", 
    "Oceania", 
    "Middle East"
]

#####################################
# Define Function 1. For item in Range: 
# Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################


def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.

    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''

    # Log function name and parameters
    logger.info("FUNCTION: create_folders_for_range()")
    logger.info(f"PARAMETERS: start_year = {start_year}, end_year = {end_year}")

    for year in range(start_year, end_year + 1):     # loop through years
        year_path = ROOT_DIR / str(year)             # creating folder using ROOT_DIR
        year_path.mkdir(exist_ok=True)               # avoids program from crashing if folder already exists
        logger.info(f"Created folder: {year_path}")  # log message for each folder created



#####################################
# Define Function 2. For Item in List: 
# Create folders from a list of names.
# Pass in a list of folder names 
# After everything else is working, 
# add options to force lowercase and remove spaces
#####################################


def create_folders_from_list(folder_list: list) -> None:
    '''
    Create folders based on a list of folder names.
    Convert names to lowercase and remove spaces.
    
    Arguments:
    folder_list -- A list of strings representing folder names.
    lowercase -- Convert folder names to lowercase (default: False).
    remove_spaces -- Remove spaces from folder names (default: False).
    '''

    logger.info("FUNCTION: create_folders_from_list()")
    logger.info(f"PARAMETER: folder_list = {folder_list}")
    # logger.info(f"OPTIONS: lowercase = False, remove_spaces = False")

    for name in folder_list: # loop through folder lists
        processed_name = name.lower().replace(" ", "")       # convert to lowercase and remove spaces
        folder_path = ROOT_DIR / processed_name              # creating folder using ROOT_DIR
        folder_path.mkdir(exist_ok=True)                     # avoids program from crashing if folder already exists
        logger.info(f"Created folder: {folder_path}")        # log message for each folder created

    # pass


  
#####################################
# Define Function 3. List Comprehension: 
# Create a function to create prefixed folders by transforming a list of names 
# and combining each with a prefix (e.g., "output-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'output-') to add to each
#####################################

def create_prefixed_folders_using_list_comprehension(folder_list: list, prefix: str) -> None:
    '''
    Create folders by adding a prefix to each item in a list 
    using a concise form of a for loop called a list comprehension.

    Arguments:
    folder_list -- A list of strings (e.g., ['csv', 'excel']).
    prefix -- A string to prefix each name (e.g., 'output-').
    '''

    logger.info("FUNCTION: create_prefixed_folders()")
    logger.info(f"PARAMETERS: folder_list = {folder_list}, prefix = {prefix}")


    # list comprehension to generate prefixed paths
    prefixed_paths = [ROOT_DIR / f"{prefix}{name}" for name in folder_list]  # list comprehension to generate prefixed paths
    for path in prefixed_paths:                                              # loop through prefixed paths
        path.mkdir(exist_ok=True)                                            # create each folder
        logger.info(f"Created folder: {path}")                               # log message for each folder created

    # pass

  

#####################################
# Define Function 4. While Loop: 
# Write a function to create folders periodically 
# (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int = 5) -> None:
    '''
    Create folders periodically over time.

    Arguments:
    duration_seconds -- The number of seconds to wait between folder creations.
    '''    
    logger.info("FUNCTION: create_folders_periodically()")
    logger.info(f"PARAMETER: duration_seconds = {duration_seconds}")
    

    # if isinstance(folder_names, int):  # check if folder_names is an int
    folder_names = ['periodic_1', 'periodic_2', 'periodic_3']               # create a list of folder names
    # duration_seconds = 5  # set the duration in seconds

    counter = 0                                                              # initialize a counter
    while counter < len(folder_names):                                       # loop until all folders are created
        folder_name = folder_names[counter]                                  # get the current folder name
        folder_path = ROOT_DIR / folder_name                                 # create the full path
        folder_path.mkdir(exist_ok=True)                                     # create the folder
        logger.info(f"Created folder: {folder_path}")                        # log message for each folder created
        time.sleep(duration_seconds)  # wait for the specified duration
        counter += 1                                                         # increment the counter
    # pass


#####################################
# Define Function 5. For Item in List: 
# Create folders from a list of names.
# Pass in a list of folder names 
# Add options to force lowercase AND remove spaces
#####################################

def create_standardized_folders(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:
    '''
    Create folders from a list of names with options to standardize names.

    Arguments:
    folder_list -- A list of strings representing folder names.
    to_lowercase -- If True, convert names to lowercase.
    remove_spaces -- If True, remove spaces from names.
    '''

    logger.info("FUNCTION: create_standardized_folders()")
    logger.info(f"PARAMETERS: folder_list = {folder_list}, to_lowercase = {to_lowercase}, remove_spaces = {remove_spaces}")

    for folder_name in folder_list:
        proc_name = folder_name
        if to_lowercase:
            proc_name = proc_name.lower()
        if remove_spaces:
            proc_name = proc_name.replace(" ", "")
        folder_path = ROOT_DIR / proc_name                  # creating folder using ROOT_DIR
        folder_path.mkdir(exist_ok=True)                    # avoids program from crashing if folder already exists
        logger.info(f"Created folder: {folder_path}")       # log message for each folder created

    # pass
  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    logger.info("#####################################")
    logger.info("# Starting execution of main()")
    logger.info("#####################################\n")

    logger.info(f"Byline: {utils_oluwafemi.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using list comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'output-'
    create_prefixed_folders_using_list_comprehension(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Call function 5 to create standardized folders, no spaces, lowercase
    create_standardized_folders(REGIONS, to_lowercase=True, remove_spaces=True)

    logger.info("\n#####################################")
    logger.info("# Completed execution of main()")
    logger.info("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()



















    

# datafun-02-automation
This is for Python Automation Project

# Pro Analytics 01: Setup and Workflow Guide

This repository provides a clear, concise guide to help set up a machine for Python projects, 
initialize a new Python project, and follow a repeatable project workflow 
when developing professional Python projects. 

The instructions are divided into three main sections.

## First: Set Up Machine & Sign up for GitHub
Go to [01-machine-setup](01-machine-setup/MACHINE-SETUP.md) to prepare for Python projects.
Start here to set up a machine for the first time (or to upgrade or verify professional tools).

This section contains **one-time tasks** including:
1. View file extensions and hidden files and folders.
2. Optional: Install (or verify) a package manager for your operating system.
3. Install Python, Git, and Visual Studio (VS) Code for your operating system.
4. Configure Git
5. Install common VS Code extensions.
6. Create a folder on your machine to hold your GitHub projects. 
7. Create a GitHub account (join 100 Million Developers!)

---

## Second: Initialize a Project
Go to [02-Project-Initialization](./02-project-initialization/PROJECT-INITIALIZATION.md) when **starting a new project**.

This section walks you through the steps to either:
1. Copy an existing project OR start a new project from scratch.
2. Clone your new GitHub repo to your machine. 
3. Add common files such as .gitignore and requirements.txt.
4. Git add-commit-push the changes to GitHub.
5. Create a local project virtual environment for Python.

---

## Third: Work on the Project Over Time
Go to [03-Repeatable-Workflow](./03-repeatable-workflow/REPEATABLE-WORKFLOW.md) for ongoing project development.

This section provides the **repeatable steps** for working on Python projects. 
These steps are typically followed whenever we make changes to a project. The workflow includes:
1. Pull any recent changes from GitHub.
2. Activate the virtual environment.
3. Install dependencies.
4. Run scripts and/or Jupyter notebooks.
5. Make updates, verify the code still runs, and git add-commit-push to GitHub. 

---

## Important

- Follow the instructions carefully.
- Follow the instructions in the recommended order.
- Verify each step before proceeding. 

## Celebrate
Follow each step carefully. 
We have helped hundreds of new analysts get started with professional Python. 
Verify you can run both a script and a notebook successfully. 
Then, celebrate - that's a big iceberg needed to get started with Professional Python.

## Follow The Proven Path Provided
Hopefully, each step is not too bad and things go well. 
When they don't - that's to be expected. 
Part of the reason we get hired is to "figure things out" and we are here to help you do that. 
Learn to do a web search, and experiment with free AI assistants to help explain and provide any additional details needed. 
Remember, YOU are in charge. 
This is the process we support and these instructions work. 
Do NOT deviate unless you agree to invest time and energy to ensure any of the many alternate paths work for you throughout the program. 

## Explore

AFTER that is where the power and joy of working with Python begins. 
Keep good notes. 
Save the working versions and then, change things. For example:

- Rename a variable. 
- Add a new statement. 
- Comment things out.
- Rename a function. 
- View the logs. Log something new (e.g., every function when called and before returning a value).

Working with code is a fun, safe, rewarding way to learn. 
If you enjoy puzzles, getting value from Python is a great way to earn a living. 

## CheatSheet: Commands to Manage Virtual Environment

For Windows PowerShell (change if using Mac/Linux). 
Keep these notes in every project README.md.

```powershell
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade -r requirements.txt
```

## CheatSheet: Commands to Run Python Scripts

Remember to activate your .venv (and install packages if they haven't been installed yet) before running files.
Verify that all external packages imported into a file are included in requirements.txt (and have NOT been commented out).

```shell
py demo_script.py
py do_stats.py
py draw_chart.py
py greet_user.py
```

## CheatSheet: Commands to Git add-commit-push

```shell
git add .
git commit -m "custom message"
git push -u origin main
