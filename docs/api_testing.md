# API Testing

API Testing is a crucial part of the software development life cycle as it determines if the applications perfectly meet the expectations for functionality, performance, reliability, and security of the system. API Testing can be broadly classified into two categories: 


   ![API-Testing](https://user-images.githubusercontent.com/105641357/188853182-77e509c6-e537-4bef-baec-77debc0c45a4.png)


• **Manual Testing**: Humans manually execute the APIs, verify the test cases and report the results.
    
• **Automation Testing**: Machines automatically execute the APIs, verify the test cases, and report the results.

Let us focus on automated testing !!

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

## Sample Example

After downloading and installing all the dependencies as mentioned above, 
Now let us write code for testing API response using assertion:

![Sample2code](https://user-images.githubusercontent.com/105641357/188855127-407b4832-f1e6-4b39-ba8b-778d9c1e5fb3.JPG)

After writing various test scripts for different scenario, type '**pytest name_of_file**' in the command line for running tests.

![Output2](https://user-images.githubusercontent.com/105641357/188853918-fb92b670-3436-499d-8c42-915c0e0ac23a.JPG)

As you can see in the above picture, all test cases status will be displayed in green font.

In the same way all the test scripts in the  **devops-lv-iaas/iaas_api_test_scripts/** repository can be run.
