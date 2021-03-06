# Python Sudoku-MySQL-Insert_Games

### [Downloads](https://github.com/VarunS2002/Python-Sudoku-MySQL-InsertGames/releases)

This is a tool to insert new games in the database for the Python-Sudoku-MySQL program

Python-Sudoku-MySQL program:
[Downloads](https://github.com/VarunS2002/Python-Sudoku-MySQL/releases)

## Usage:

-Default values of host, username and password for connecting to MySQL are localhost, root and *no password* respectively

-To change these values place the mysql_config.txt file in the same folder as the insert games program

-The main part of the config file should look like this:


host:<br />
localhost<br />
username:<br />
root<br />
password:<br />
testpass<br />


-localhost, root and testpass are the custom values for host, username and password respectively

-If any of these lines are left empty the program will use the default values for the particular field

## Note:

-No code changes have to be made in the sudoku program after adding new games 

-Adding incorrect values, rows or columns in the database may cause the program to not function correctly and result in errors 

## Features:

-Sudoku like grid for ease of entering values

-Insert games into start table

-Insert games into solved table

-Option to commit values at the end

-Validation for values entered

-Only int from 0-9 allowed in start and int from 1-9 allowed in solved

-About option with version, link for releases and for sources

-PEP 8 format

-Object Oriented

-Comments to easily understand code
