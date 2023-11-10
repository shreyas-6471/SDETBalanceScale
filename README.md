Running the Selenium Script for the SDET Challenge
Overview
This guide details the steps to run a Python script using Selenium for solving a specific challenge at "http://sdetchallenge.fetch.com/". The script facilitates automated interaction with web page elements to complete the challenge.

Prerequisites
To execute this script, the following prerequisites should be downloaded and set up:

Python: The script is in Python, hence Python should be downloaded and installed on your system. It is available at python.org.

Selenium WebDriver: Selenium is essential for web automation. It should be downloaded via pip with the command:
pip install selenium
WebDriver for Firefox: Since the script operates with Firefox, the geckodriver, which enables Selenium to interact with Firefox, should be downloaded. It is obtainable from Mozilla's GitHub repository. Ensure it's included in your system's PATH.
Execution Instructions
Script Download: Save the provided Python script to a local directory.

WebDriver Setup: Ensure the geckodriver is positioned in a directory that is part of your system's PATH.

Script Execution: Open a command line interface, navigate to where the script is saved and get into the venv by sourcing and then execute:

python [script_name].py
Here, [script_name] should be replaced with the actual file name of your script.

Script Breakdown
Purpose
The script automates the process to solve a weight comparison challenge on a webpage. It employs Selenium for browser control, simulating clicks and keystrokes, and retrieving webpage content.

Core Functions
fill_board: Inputs values into the webpage's text fields once they become accessible.
weigh_bars: Sets up and performs a weight comparison between two sets of items, resets the current configuration, and initiates the weighing process.
perform_search: A recursive function employing a divide-and-conquer approach to pinpoint the counterfeit bar by segmenting the set of bars, comparing their weights, and refining the search based on these comparisons.

Execution Flow::
Initiation through perform_search with a preliminary range of bars(in our case it's between 0-8) since we have gold bars labelled 0-8.
weigh_bars function is called  for weight comparisons and fill_board for scale preparation.
Based on the results from weigh_bars Recursive narrowing of the search area following the outcome of each weight comparison is done.
The recursion is carried out, and whenever start==end,ie we have only one bar in the search space we would have found the fake bar.
After the fake bar is found, the button is clicked and Alert will be shown on the screen
