# Selenium-Bootcamp

This bootcamp serves as an introduction point into the Selenium framework. The Selenium framework supports multiple languages, but in this guide, I will be using Python.

This bootcamp covers a majority of the common scenarios one might encounter while developing tests for web applications.

Software:

    * PyCharm
    * Python 2.7
    * Selenium

#Selenium Basics

## Task #1: Setup

##### Useful  material and links: 

[Python 2.7 Download] (https://www.python.org/downloads/)

[PyCharm Download Community Edition] (https://www.jetbrains.com/pycharm/download/)

[Selenium setup instructions] (http://selenium-python.readthedocs.org/installation.html)

[PiP] (https://bootstrap.pypa.io/get-pip.py)

##### Objective:
1. Install Python
2. Install PyCharm IDE
3. Use Pip to install seleneium
4. Navigate to google.ca

#####Installation:

Using the links above, download all the necessary tools and install them onto your computer. Select all the text on the Pip link, and save that into a new file named get-pip.py. Then on your command line tool navigate to the directory of your get-pip.py file and run "Python get-pip.py". After pip is installed, navigate to your computers Python folder and go into the scripts folder (ex C:\Python27\Scripts) from command line. Then run the command pip "pip install selenium".

#####Starting your first project:

To start your first project, open PyCharm and select create a new PyCharm project. In that project create a new python file. In that file, make sure you import selenium modules into your project with the line:

    from selenium import webdriver

WebDriver is the browser that Selenium will use. Then define your web browser with the line:

    driver = webdriver.Firefox()
 
Note: Other browers are supported, you just need to download their specific webdrivers. Firefox just naturally comes supported out of the box. For example, if you wanted to add the Chrome browser, you would go download the Chrome webdriver (https://sites.google.com/a/chromium.org/chromedriver/downloads) and add it to your PATH. Then you can set the driver to be chrome with the line: 

    driver = webdriver.Chrome()

#####Navigating:

In Selenium, the method to go to a link is:

    driver.get(URL)

where URL is the website url you want to navigate to.

#####Running your test case:

Test cases can be run in one of two ways. 

1. From PyCharm: You can run the test in the IDE by right clicking your python file and clicking "Run"
2. From command line: Navigate to the directory of python file. Run the command: "Python (INSERT FILE NAME HERE).py"
 
#####Challenge:

Try creating a test that opens a browser and navigates to google.ca

## Task #2: Locating Elements

##### Useful  material and links: 

[Selenium locating elements tutorial] (http://selenium-python.readthedocs.org/locating-elements.html) 

##### Objective:
Learn about the different ways to locate elements on a web page

#####Description:
Read the link above. It does a good job explaining all the different locator methods and how to use them.

To find attributes to find your element by, you can right click that element on the page, and click "inspect element". It should open up a new screen that displays all the information about that element, such as ID, Class Name, Tag Name, and other useful attributes.

## Task #3: Actions

##### Objective:
Make a google search

#####Description:
There are 3 main actions:

1. Click (clicks an element on the page) - .click()
2. Type (types text into a textbox on the page) - .send_keys("TEXT TO BE TYPED")
3. Clear (clears the text in a textbox on the page) - .clear()

To perform one of these actions on an element, you first need to locate the element. For example, if I want to click an element, I would use this line;

    driver.find_element_by_id("Example ID").click()

These are the main actions that you will be using in your tests. For a list of all actions, read below about the Webdriver API.

#####Challenge:

Try creating a test that goes to google.ca and searches for "cat videos".

## Task #4: Unittest and Asserts

##### Useful material and links: 

[Unittest Tutorial] (http://selenium-python.readthedocs.org/getting-started.html#using-selenium-to-write-tests)

[Asserts Tutorial] (http://engineering.aweber.com/getting-started-with-ui-automated-tests-using-selenium-python/) 

##### Objective:

Modify your code to use the unittest framework and use assert statements.

#####Description:
The unittest framework is standard unit test framework for Python. It allows you to create each test case as a method, run them all individually and get information about each test run. This makes your tests much more organized as they can now be grouped into similar categories and placed in separate files. We can now also introduce the concept of asserts. An assert is a statement that must be true and fails otherwise. We can use asserts to verify things such as checking if elements on the page exist or checking if the current url is correct. Each test case should have at least one assert statement.

Please read the Unittest Tutorial and Asserts tutorial above. It explains how to implement the unittest framework into your test cases and how to structure your code around it.

A reference to the Web Automation Style Guide can be viewed here https://docs.google.com/document/d/1VhsU2VEBw5eDzs8oEzk_t5bTXcXpwEo7_lR-4WLobHY/

#####Challenge:

Try creating a test that goes to google.ca and asserts that the current url is google.ca (Hint, there is a .current_url function in selenium)

## Task #5: Waits

##### Useful  material and links: 

[Selenium Waits Tutorial] (http://selenium-python.readthedocs.org/waits.html) 

##### Objective:
Get the results from a google search

#####Description:
Most websites do not load right away. Many take an extra few seconds to load a page as it may be have to get other resources or dependencies. This is why when you run driver.find_element_by on the page right after you request the page, it may give you an error as it cannot find the element on the page since the page has not been loaded yet.

This is where waits come in. Waits will wait for the element you are looking for to be loaded before it applys an action to it. Read the link above to learn about the different conditions you can wait for.

Note, a very useful method that I created is:

    def waitUntil(driver, timeout, matcher, key):
    try:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((matcher, key)))
    except TimeoutException:
        raise NoSuchElementException("Matcher: '{}' Key: '{}' not found!".format(str(matcher), str(key)))

The waitUntil function takes in:
 * driver - the driver you are currently using
 * timeout - the amount of seconds it should wait for (ex, 30)
 * matcher - how you are locating the element (ex By.ID)
 * key - the attribute you are using to look for the element (ex, "userId")

When you use "waitUntil", it will wait for the element to be visible for the timeout length in seconds. And if it cannot find the element, it will print a nice error explaining which element could not be found.

#####Challenge:

Try to create a test that runs a google search for "Google" and asserts that the first result is google.ca

## Task #6 More Selenium API

#####Description:

For a full list of Selenium's capabilities, please read through [WebDriver API] (http://selenium-python.readthedocs.org/api.html). There are a lot of useful functions you can apply to your tests such as screenshot tools.

#Selenium Intermediate. Page Objects.

## Task #7 Understanding Page Objects

##### Useful  material and links: 

[Page Object Documentation] (http://selenium-python.readthedocs.org/page-objects.html)
[Page Object Example] (https://justin.abrah.ms/python/selenium-page-object-pattern--the-key-to-maintainable-tests.html)

##### Objective:
Create a page object

#####Description:
Selenium code looks very messy. Also if the developers change the source code, it could break many of your tests. Page objects are a good tool to use to organize your code and make it more adaptable to changes.

The concept behind Page Objects is to make each page an object. Such object will have methods that will do something on that page. For example, in a Sign In Page Object, it would have methods do to things on the page such as entering your user name, and entering your password. Then whenever you need to do something on the Sign In Page in your test, you could just call SignInPage.enterUsername("BillyBob"). This is much cleaner and more readable, and if the source code ever changes, you can easilly change the enterUsername method to fix all the instances of it.

#####Challenge:

Try creating a page object for Google.ca, and make methods to enter your search and click the search button

#Examples

Look in this repository for test samples and a page object example.

#Other Tips

1. Also a really useful function to help you with debugging is "raw_input()". Basically, raw_input() is a psudo breakpoint for your code and will pause whenever it reaches the line. For example, if you want to find out why a certain line in your code is crashing, you could put a raw_input() before that line and try to debug what is wrong with that line.
2. If you are writing tests to create accounts on a website, you will probably run into an error that you cannot use the same userid for each signup. A good work around is to use the current time in unix as your userid. This way, your userid will never be the same when you run your tests.
