# Selenium-Bootcamp

This bootcamp serves as an introduction point into the Selenium framework. The Selenium framework works with multiple languages but in this guide, I will be using Python.

Bootcamp coverts majority of the common scenarios one might encounter while developing tests for web applications.

Fork this repo and request evaluation from QA members experienced in developing Espresso tests.

Software:

    * PyCharm
    * Python 2.7
    * Selenium


#Selenium basics

## Task #1: Setup

##### Useful  material and links: 

[Python 2.7 Download] (https://www.python.org/downloads/)

[PyCharm Download Community Edition] (https://www.jetbrains.com/pycharm/download/)

[Selenium setup instructions] (http://selenium-python.readthedocs.org/installation.html)

[Pip] (https://bootstrap.pypa.io/get-pip.py)

##### Objective:
1. Install Python
2. Install PyCharm IDE
3. Use Pip to install seleneium
4. Navigate to google.ca

#####Installation:

Using the links above, download all the necessary tools and install them onto your computer. Select all the text on the Pip link, and save that into a new file named get-pip.py. Then on your command line tool navigate to the directory of your get-pip.py file and run "Python get-pip.py". After pip is installed, navigate to your computers Python folder and go into the scripts folder (ex C:\Python27\Scripts) from command line. Then run the command pip "pip install selenium".

#####Starting your first project

To start your first project, open PyCharm and select create a new PyCharm project. In that project create a new python file. In that file, make sure you import selenium into your project with the line:

    * from selenium import webdriver

Then define your web browser with the line:

    * driver = webdriver.Firefox()
 
Note: Other browers are supported, you just need to download their specific webdrivers. Firefox just come supported out of the box. For example, if you wanted to add the Chrome browser, you would go download the Chrome webdriver (https://sites.google.com/a/chromium.org/chromedriver/downloads) and add it to your PATH. Then you can set the driver to be chrome with the line: 

    * driver = webdriver.Chrome()

#####Navigating

In Selenium, the method to go to a link is:

    * driver.get(URL)

where URL is the website url you want to navigate to.

#####Running your test case

Test cases can be run in one of two ways. 

1. From PyCharm. You can run the test in the IDE with the run button [[TODO FINISH]]
2. From command line. Navigate to the directory of python file. Run the command:

    * Python (INSERT FILE NAME HERE).py
 
#####Challenge

Try creating a test that opens a browser and navigates to google.ca

## Task #2: Locating Elements

##### Useful  material and links: 

[Selenium locating elements tutorial] (http://selenium-python.readthedocs.org/locating-elements.html) 

##### Objective:
Finding the search box

#####Description:

Main difference between two tools is that hierarchy viewer provides you with ENTIRE hierarchy, including items that are not visible (invisbile, gone), while uiatomatorviewer 
shows only visible views. This discrepancy is important to remember as there is a fundamental difference between a view that doesn't exist and view that is not visible.

## Task #3: Actions

##### Objective:
Add a test that Changes the location in settings and verifies that the new location is saved in the settings

#####Description:
Same as #2 this task is just for exploring capabilities of out-of-the box features of espresso library.
Please don't test anything other than UI. Only validate that settings accepted your change. Don't test network responses and data integrity.

## Task #4: Waits

##### Objective:
Add a pull to refresh test. Verify that snackbar is displayed.

#####Description:
Don't test anything other than snackbar.


#Espresso Intermediate. Page Objects.

## Task #5 Understanding onData

##### Useful  material and links: 

[Advanced espresso guide] (https://google.github.io/android-testing-support-library/docs/espresso/advanced/index.html)

##### Objective:
Add a test that changes the  temperature units using onData()

#####Description:

Whenever you encounter a list view in the hierarchy, this is an indication that onView() doesn't work here any more. onView will only work for items that are currently visible on the screen.
However, if an item is off the screen onView will produce view not found exception and fail the test.
onData doesn't take a view matcher, but instea it's looking for a data matcher, which matches the data in the adapter behind the ListView.
Making assertions with onData will automatically scroll to the view if it's not displayed.

Before starting the test investigate what kind of data the adapter holds in the unit selection dialog. You can write a failing test that will show you data type in the exception log.
