# Django

## What is Django?
Django is a Python framework that makes it easier to create web sites using Python.

Django takes care of the difficult stuff so that you can concentrate on building your web applications.

Django emphasizes reusability of components, also referred to as DRY (Don't Repeat Yourself), and comes with ready-to-use features like login system, database connection and CRUD operations (Create Read Update Delete).

Django is especially helpful for database driven websites.

## How does Django Work?
Django follows the MVT design pattern (Model View Template).

Model - The data you want to present, usually data from a database.
View - A request handler that returns the relevant template and content - based on the request from the user.
Template - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data.

### Model
The model provides data from the database.

In Django, the data is delivered as an Object Relational Mapping (ORM), which is a technique designed to make it easier to work with databases.

The most common way to extract data from a database is SQL. One problem with SQL is that you have to have a pretty good understanding of the database structure to be able to work with it.

Django, with ORM, makes it easier to communicate with the database, without having to write complex SQL statements.

The models are usually located in a file called models.py.

### View
A view is a function or method that takes http requests as arguments, imports the relevant model(s), and finds out what data to send to the template, and returns the final result.

The views are usually located in a file called views.py.

### Template
A template is a file where you describe how the result should be represented.

Templates are often .html files, with HTML code describing the layout of a web page, but it can also be in other file formats to present other results, but we will concentrate on .html files.

Django uses standard HTML to describe the layout, but uses Django tags to add logic:

<h1>My Homepage</h1>

<p>My name is {{ firstname }}.</p>
The templates of an application is located in a folder named templates.

### URLs
Django also provides a way to navigate around the different pages in a website.

When a user requests a URL, Django decides which view it will send it to.

This is done in a file called urls.py.

## So, What is Going On?
When you have installed Django and created you first Django web application, and the browser requests the URL, this is basically what happens:

Django receives the URL, checks the urls.py file, and calls the view that matches the URL.
The view, located in views.py, checks for relevant models.
The models are imported from the models.py file.
The view then sends the data to a specified template in the template folder.
The template contains HTML and Django tags, and with the data it returns finished HTML content back to the browser.
Django can do a lot more than this, but this is basically what you will learn in this tutorial, and are the basic steps in a simple web application made with Django.

### Django History
Django was invented by Lawrence Journal-World in 2003, to meet the short deadlines in the newspaper and at the same time meeting the demands of experienced web developers.

## Getting Started with Django

### Django Requires Python
To check if your system has Python installed, run this command in the command prompt:

*python --version*

If Python is installed, you will get a result with the version number, like this

*Python 3.9.2*

If you find that you do not have Python installed on your computer, then you can download it for free from the following website: https://www.python.org/

### PIP

To install Django, you must use a package manager like PIP, which is included in Python from version 3.4.

To check if your system has PIP installed, run this command in the command prompt:

*pip --version*

If PIP is installed, you will get a result with the version number.

For me, on a windows machine, the result looks like this:

pip 20.2.3 from c:\python39\lib\site-packages\pip (python 3.9)

If you do not have PIP installed, you can download and install it from this page: https://pypi.org/project/pip/

### Virtual Environment
It is suggested to have a dedicated virtual environment for each Django project, and one way to manage a virtual environment is venv, which is included in Python.

With venv, you can create a virtual environment by typing this in the command prompt, remember to navigate to where you want to create your project:

Windows:

py -m venv myproject
Unix/MacOS:

python -m venv myproject
This will set up a virtual environment, and create a folder named "myproject" with subfolders and files, like this:

myproject
  Include
  Lib
  Scripts
  pyvenv.cfg
Then you have to activate the environment, by typing this command:

Windows:

myproject\Scripts\activate.bat
Unix/MacOS:

source myproject/bin/activate
Once the environment is activated, you will see this result in the command prompt:

Windows:

(myproject) C:\Users\Your Name>
Unix/MacOS:

(myproject) ... $
Note: You must activate the virtual environment every time you open the command prompt to work on your project.

### Install Django
Finally, we can install Django.

Remember to install Django while you are in the virtual environment!

Django is installed using pip, with this command:

Windows:

(myproject) C:\Users\Your Name>py -m pip install Django
Unix/MacOS:

(myproject) ... $ python -m pip install Django
Which will give a result that looks like this (at least on my Windows machine):

Collecting Django
  Downloading Django-4.0.3-py3-none-any.whl (8.0 MB)
      |████████████████████████████████| 8.0 MB 2.2 MB/s
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.2-py3-none-any.whl (42 kB)
Collecting asgiref<4,>=3.4.1
  Downloading asgiref-3.5.0-py3-none-any.whl (22 kB)
Collecting tzdata; sys_platform == "win32"
  Downloading tzdata-2021.5-py2.py3-none-any.whl (339 kB)
      |████████████████████████████████| 339 kB 6.4 MB/s
Installing collected packages: sqlparse, asgiref, tzdata, Django
Successfully installed Django-4.0.3 asgiref-3.5.0 sqlparse-0.4.2 tzdata-2021.5
WARNING: You are using pip version 20.2.3; however, version 22.0.4 is available.
You should consider upgrading via the 'C:\Users\Your Name\myproject\Scripts\python.exe -m pip install --upgrade pip' command.
That's it" Now you have installed Django in your new project, running in a virtual environment!

### Windows, Mac, or Unix?
You can run this project on either one. There are some small differences, like when writing commands in the command prompt, Windows uses py as the first word in the command line, while Unix and MacOS use python:

Windows:

py --version
Unix/MacOS:

python --version
In the rest of this tutorial, we will be using the Windows command.

### Check Django Version
You can check if Django is installed by asking for its version number like this:

(myproject) C:\Users\Your Name>django-admin --version
If Django is installed, you will get a result with the version number:

4.0.3

## Create Django project

### My First Project
Once you have come up with a suitable name for your Django project, like mine: myworld, navigate to where in the file system you want to store the code (in the virtual environment), and run this command in the command prompt:

**django-admin startproject myworld**

Django creates a myworld folder on my computer, with this content:

myworld
    manage.py
    myworld/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
These are all files and folders with a specific meaning, you will learn about some of them later in this tutorial, but for now, it is more important to know that this is the location of your project, and that you can start building applications in it.

### Run the Django Project
Now that you have a Django project, you can run it, and see what it looks like in a browser.

Navigate to the /myworld folder and execute this command in the command prompt:

**py manage.py runserver**

Which will produce this result in command prompt as shown below:

![image](https://user-images.githubusercontent.com/105641357/190238004-587c5105-85ff-4020-9a36-25f3f2b31ebe.png)


Open a new browser window and type 127.0.0.1:8000 in the address bar.

The result:

![image](https://user-images.githubusercontent.com/105641357/190237418-e1c329f0-6cac-41ea-9ccf-bf4cebf4124f.png)

### Creating Django app

### What is an App?

An app is a web application that has a specific meaning in your project, like a home page, a contact form, or a members database.

In this tutorial we will create an app that allows us to list and register members in a database.

But first, let's just create a simple Django app that displays "Hello World!".

### Create App
I will name my app members.

Start by navigating to the selected location where you want to store the app, and run the command below.

If the server is still running, and you are not able to write commands, press [CTRL] [BREAK] to stop the server and you should be back in the virtual environment.

**py manage.py startapp members**

Django creates a folder named members in my project, with this content:

![image](https://user-images.githubusercontent.com/105641357/190238400-4c5b1adc-9fa8-4c97-be70-e1913a775b8d.png)


These are all files and folders with a specific meaning. You will learn about most of them later in this tutorial.

First, take a look at the file called views.py.

This is where we gather the information we need to send back a proper response.

## Lets add some info to our website

***Will start with the views.py file**

## Views
Django views are Python functions that takes http requests and returns http response, like HTML documents.

A web page that uses Django is full of views with different tasks and missions.

Views are usually put in a file called views.py located on your app's folder.

There is a views.py in your members folder that looks like this:

![image](https://user-images.githubusercontent.com/105641357/190239063-866e7ec7-d77e-43ef-9157-5c588b6f1eb3.png)


Find it and open it, and replace the content with this:

![image](https://user-images.githubusercontent.com/105641357/190239162-ed6e4ea0-a633-47de-bb76-2a27f1349b26.png)


This is a simple example on how to send a response back to the browser.

But how can we execute the view? Well, we must call the view via a URL.

## URLs
Create a file named urls.py in the same folder as the views.py file, and type this code in it:

![image](https://user-images.githubusercontent.com/105641357/190239325-902323f6-05d5-46fa-9b5c-dbb2d8aa8b5f.png)


The urls.py file you just created is specific for the members application. We have to do some routing in the root directory myworld as well. This may seem complicated, but for now, just follow the instructions below.

There is a file called urls.py on the myworld folder, open that file and add the include module in the import statement, and also add a path() function in the urlpatterns[] list, with arguments that will route users that comes in via 127.0.0.1:8000/members/.

Then your file will look like this:

![image](https://user-images.githubusercontent.com/105641357/190239446-8bb37a9b-4b95-4f74-9c07-febbcd4b5f70.png)


If the server is not running, navigate to the /myworld folder and execute this command in the command prompt:

py manage.py runserver
In the browser window, type 127.0.0.1:8000/members/ in the address bar.

![image](https://user-images.githubusercontent.com/105641357/190239537-7373e108-680e-4ab3-bfdc-f4089b22b2b0.png)

***You can create very interactive websites using Django with practice***
