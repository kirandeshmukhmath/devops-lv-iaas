# API Testing

API Testing is a crucial part of the software development life cycle as it determines if the applications perfectly meet the expectations for functionality, performance, reliability, and security of the system. API Testing can be broadly classified into two categories: 


   ![API-Testing](https://user-images.githubusercontent.com/105641357/188853182-77e509c6-e537-4bef-baec-77debc0c45a4.png)


• **Manual Testing**: Humans manually execute the APIs, verify the test cases and report the results.
    
• **Automation Testing**: Machines automatically execute the APIs, verify the test cases, and report the results.

Let us focus on automated testing !!

*We have used Pytest framwork for automating API testing,*

## What is Pytest ?

Pytest is a Python testing framework that originated from the PyPy project. It can be used to write various types of software tests, including unit tests, integration tests, end-to-end tests, and functional tests. PyTest is a testing framework that allows users to write test codes using Python programming language. It helps  to write simple and scalable test cases for databases, APIs, or UI. PyTest is mainly used for writing tests for APIs. The Pytest logo is as shown below,

![image](https://user-images.githubusercontent.com/105641357/189534251-6ba5c632-bfdf-444a-a5bd-8a438654f174.png)


## Requiements

• **Any IDE** (Visual studio Code by Microsoft).

• **Python 3.x** version plus.

• **Pytest** ( A software test framework, which means pytest is a command-line tool that automatically finds tests you've written, runs the tests, and reports the results.).

• **requests** ( A HTTP library for the Python programming language, requests module allows you to send HTTP requests using Python. The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).).

• **Platform** : Linux , Mac and Windows

## Installing the requirements

- **Visual studio** code can be downloaded by tying 'VScode download' in browser or by clicking on this link https://code.visualstudio.com/download.
- **Python** latest version can be downloaded from the browser or by clicking on this link https://www.python.org/downloads/
- After downloading and installing IDE and python, create a folder and name as you wish and open the same folder with VScode.
- Create a virtual environment by typing '**python -m venv name**' in the command line for windows and '**virtualenv virtualenv_name**' for linux.
- **Pytest** can be downloaded from the command line by typing '**pip install pytest**.
- **requests** can be downloaded from the command line by typing '**pip install requests**'.

## Installation procedure with an example

**Open the visual studio**

![image](https://user-images.githubusercontent.com/105641357/189535012-117ea795-abc3-4e66-9846-4437743ec576.png)

**Create a new folder and name it as you wish like 'iaas_test' and create a new file with .py extention. **

(*Note - Always add 'test_' to your .py file like 'test_bank_account_verification_api' because Pytest will only be able to detect file starting with 'test'*)
Create a virtual environment by typing '**python -m venv name**' in the command line for windows and '**virtualenv virtualenv_name**' for linux so all dependecies stays intact. 

![image](https://user-images.githubusercontent.com/105641357/189534785-6c15baf8-06e1-4a65-8b66-94b7158b718d.png)

***Make sure you have installed python in your system***

**Now let us install Pytest from command line using pip, just type 'pip install pytest'.**

![image](https://user-images.githubusercontent.com/105641357/189535286-3941918a-f856-4b80-beb5-594d8c86d062.png)

**Now let us install requests package by typing 'pip install requests'**

![image](https://user-images.githubusercontent.com/105641357/189535356-b7936c96-7e09-41db-b0f9-dbe598d35be9.png)


Good Work !!

**Now create a .py file for writing python script**
**Now let us write code for testing API response using assertion:**

***Note: Create a folder 'cred' which will contain URL, API key, api url, aws_access_key, aws_secret_access_key and papertrail token.***

![image](https://user-images.githubusercontent.com/105641357/189534696-5d726393-dfed-4a51-afd1-5fe208845335.png)


After writing various test scripts for different scenario, type '**pytest name_of_file**' in the command line for running tests.

![Output2](https://user-images.githubusercontent.com/105641357/188853918-fb92b670-3436-499d-8c42-915c0e0ac23a.JPG)

As you can see in the above picture, all test cases status will be displayed in green font.

In the same way all the test scripts in the  **devops-lv-iaas/iaas_api_test_scripts/** repository can be run.

