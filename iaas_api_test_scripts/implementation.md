# Implementation
*Automating LetsVenture web application API testing using Pytest *

We have used Pytest framework for automating API testing which requires knowledge of python programming language. PyTest is a testing framework that allows users to write test codes using Python programming language. It helps  to write simple and scalable test cases for databases, APIs, or UI. PyTest is mainly used for writing tests for APIs. It helps to write tests from simple unit tests to complex functional tests.  

The API’s are developed to authenticate user's details. There are various API like kyckra_bank_account_verification, kyckra_bank_account_verification_advanced, kyckra_entity_pan_profile, kyckra_pan_authentication, kyckra_pan_status_check, kyckra_entity_gst_authentication, kyckra_entity_gst_search_basis_pan, kyckra_pan_authentication_advanced, kyckra_ckyc_download, kyckra_kyc_ocr, kyckra_ckyc_search, /cadoc_get_ca_doc /, /schemedoc_get_scheme_doc /, lettersandnotices_get_lettersandnotices, initiate_e_agreement, fetch_e_agreement_details, /fetch_termsheet, and Papertrail which sends input payload data to third party organization (Karza) which will verify input data and sends back the response.

**Scope**

For API’s, writing test cases for all the API with positive and negative scenarios. Writing all the test scripts in python on pytest framework and execute. Later pushing the scripts to GitHub repository and creating CI/CD pipeline for nightly execution of all test cases. 

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

***Test cases are written in TESTPAD ( a web-app for writing and running test plans )***

![image](https://user-images.githubusercontent.com/105641357/190244789-87cd16e8-a91b-447d-8dd2-2dfbb246abca.png)


![image](https://user-images.githubusercontent.com/105641357/190244710-3d84956f-6728-4a63-9136-c67ce018dafd.png)


- After writting test cases in TESTPAD, we have to execute the test cases now


**Now create a .py file for writing python script**
- Create .py files of respective API's as shown below:

![image](https://user-images.githubusercontent.com/105641357/190251754-b15511f0-4943-431f-a474-bcd005f9ab8c.png)

- Install dependencies (pytest, request)

- Open a test_api_name.py test file and import all the required dependencies required:

![image](https://user-images.githubusercontent.com/105641357/190252237-6facfc0b-9dd1-4763-9271-c94be482d052.png)

- Create a folder 'cred' which will contain URL, API key, api url, aws_access_key, aws_secret_access_key and papertrail token.

![image](https://user-images.githubusercontent.com/105641357/190253184-50851312-33e7-4dbf-aef6-3bff3b306e80.png)

- Now let us write test script for checking the response from the swagger

![image](https://user-images.githubusercontent.com/105641357/190253461-ba305b44-1015-43ca-a7b7-857bea9ad935.png)


After writing various test scripts for different scenario, type '**pytest name_of_file**' in the command line for running tests.

![Output2](https://user-images.githubusercontent.com/105641357/188853918-fb92b670-3436-499d-8c42-915c0e0ac23a.JPG)

As you can see in the above picture, all test cases status will be displayed in green font.

Later we have to update the test cases status in TESTPAD.

In the same way all the test scripts in the  **devops-lv-iaas/iaas_api_test_scripts/** repository can be run.

