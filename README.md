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

    from selenium import webdriver

Then define your web browser with the line:

    driver = webdriver.Firefox()
 
Note: Other browers are supported, you just need to download their specific webdrivers. Firefox just come supported out of the box. For example, if you wanted to add the Chrome browser, you would go download the Chrome webdriver (https://sites.google.com/a/chromium.org/chromedriver/downloads) and add it to your PATH. Then you can set the driver to be chrome with the line: 

    driver = webdriver.Chrome()

#####Navigating

In Selenium, the method to go to a link is:

    driver.get(URL)

where URL is the website url you want to navigate to.

#####Running your test case

Test cases can be run in one of two ways. 

1. From PyCharm. You can run the test in the IDE with the run button [[TODO FINISH]]
2. From command line. Navigate to the directory of python file. Run the command:

    Python (INSERT FILE NAME HERE).py
 
#####Challenge

Try creating a test that opens a browser and navigates to google.ca

## Task #2: Locating Elements

##### Useful  material and links: 

[Selenium locating elements tutorial] (http://selenium-python.readthedocs.org/locating-elements.html) 

##### Objective:
Finding the search box

#####Description:
Read the link above.

To find attributes to find your element by, you can right click that element on the page, and click "inspect element". It should open up a new screen that displays all the information about that element, such as ID, Class Name, Tag Name, and other useful attributes.

## Task #3: Actions

##### Objective:
Make a google search

#####Description:
There are 3 main actions:
1. Click (clicks an element on the page)
2. Type (types text into a textbox on the page)
3. Clear (clears the text in a textbox on the page)

Click - .click()
Type - .send_keys("TEXT TO BE TYPED")
Clear - .clear()

To perform one of these actions on an element, you first need to locate the element.

For example, if I want to click an element, I would use this line;

    driver.find_element_by_id("Example ID").click()

#####Challenge

Try creating a test that goes to google.ca and searches for "cat videos".

## Task #4: Waits

##### Objective:
Add a pull to refresh test. Verify that snackbar is displayed.

#####Description:
Don't test anything other than snackbar.

The most common function that I use is:

    def waitUntil(driver, timeout, matcher, key):
    try:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((matcher, key)))
    except TimeoutException:
        raise NoSuchElementException("Matcher: '{}' Key: '{}' not found!".format(str(matcher), str(key)))

#Espresso Intermediate. Page Objects.

## Task #5 Understanding Page Objects

##### Useful  material and links: 

[Page Object Documentation] (http://selenium-python.readthedocs.org/page-objects.html)
[Page Object Example] (https://justin.abrah.ms/python/selenium-page-object-pattern--the-key-to-maintainable-tests.html)

##### Objective:
Create a page object

#####Description:
Selenium code looks very messy. Also if the developers change the source code, it could break many of your tests.
