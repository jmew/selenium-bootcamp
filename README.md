# Selenium-Bootcamp

This bootcamp serves as an introduction point into the Selenium framework. The Selenium framework works with multiple languages but in this guide, I will be using Python.

This bootcamp coverts majority of the common scenarios one might encounter while developing tests for web applications.

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

[PiP] (https://bootstrap.pypa.io/get-pip.py)

##### Objective:
1. Install Python
2. Install PyCharm IDE
3. Use Pip to install seleneium
4. Navigate to google.ca

#####Installation:

Using the links above, download all the necessary tools and install them onto your computer. Select all the text on the Pip link, and save that into a new file named get-pip.py. Then on your command line tool navigate to the directory of your get-pip.py file and run "Python get-pip.py". After pip is installed, navigate to your computers Python folder and go into the scripts folder (ex C:\Python27\Scripts) from command line. Then run the command pip "pip install selenium".

#####Starting your first project:

To start your first project, open PyCharm and select create a new PyCharm project. In that project create a new python file. In that file, make sure you import selenium into your project with the line:

    from selenium import webdriver

Then define your web browser with the line:

    driver = webdriver.Firefox()
 
Note: Other browers are supported, you just need to download their specific webdrivers. Firefox just come supported out of the box. For example, if you wanted to add the Chrome browser, you would go download the Chrome webdriver (https://sites.google.com/a/chromium.org/chromedriver/downloads) and add it to your PATH. Then you can set the driver to be chrome with the line: 

    driver = webdriver.Chrome()

#####Navigating:

In Selenium, the method to go to a link is:

    driver.get(URL)

where URL is the website url you want to navigate to.

#####Running your test case:

Test cases can be run in one of two ways. 

1. From PyCharm. You can run the test in the IDE with the run button [[TODO FINISH]]
2. From command line. Navigate to the directory of python file. Run the command:

    Python (INSERT FILE NAME HERE).py
 
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

#####Challenge:

Try creating a test that goes to google.ca and searches for "cat videos".

## Task #4: Unittest and Asserts

##### Useful material and links: 

[Unittest Tutorial] (http://selenium-python.readthedocs.org/getting-started.html#using-selenium-to-write-tests)

[Asserts Tutorial] (http://engineering.aweber.com/getting-started-with-ui-automated-tests-using-selenium-python/) 

##### Objective:
Assert that 1 equals 1

#####Description:
The unittest framework is. It allows you to create each test case as a method and run them all individually. This makes tests much more organized as tests can now be grouped into similar categories. We can now also introduce the concept of asserts. An assert is a statement that must be true and fails otherwise.

Please read the Unittest Tutorial and Asserts tutorial above. It explains how to implement the unittest framework into your test cases and how to structure your code around it.

A reference to the Web Automation Style Guide can be viewed here https://docs.google.com/document/d/1VhsU2VEBw5eDzs8oEzk_t5bTXcXpwEo7_lR-4WLobHY/

#####Challenge:

Try creating a test that asserts 1 equals 1

## Task #5: Waits

##### Useful  material and links: 

[Selenium Waits Tutorial] (http://selenium-python.readthedocs.org/waits.html) 

##### Objective:
Get the results from a google search

#####Description:
Most websites do not load right away. Many take an extra few seconds to load a page as it may be have to load other resources. This is why when you run driver.find_element_by on the page right after you request the page, it may give you an error as it cannot find the element on the page as it has not been loaded yet.

This is where waits come in. Waits will wait for the element you are looking for to be loaded before it applys an action to it. Read the link above to learn about the different conditions you can wait for.

Note, a very useful method that I created is:

    def waitUntil(driver, timeout, matcher, key):
    try:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((matcher, key)))
    except TimeoutException:
        raise NoSuchElementException("Matcher: '{}' Key: '{}' not found!".format(str(matcher), str(key)))

It will wait for the element to be visible. And if it cannot find the element, it will print a nice error explaining which element could not be found.

#####Challenge:

Try to create a test that runs a google search for "Google" and checks if the first result is google.ca

## Task #6 More Selenium API

#####Description:

For a full list of Selenium's capabilities, please read through [WebDriver API] (http://selenium-python.readthedocs.org/api.html). There are a lot of useful functions you can apply to your tests such as screenshot tools.

#Selenium Intermediate. Page Objects.

## Task #6 Understanding Page Objects

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
