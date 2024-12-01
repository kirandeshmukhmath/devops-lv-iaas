# devops-lv-iaas

This repository contains test scripts for API's, source code of API's and documentations of the same.

The test scripts were written on python using pytest framework for validating the required API response. The API were related to authentication of PAN details, bank details, gst authentication, verifying log messages in papertrail and ..

## Folder structure


    ├── docs       
    │   ├── api_code.md                
    │   └── api_testing.md                    # Information about API testing 
    │
    ├── iaas_api_code_image
    │   ├──.github
    │   │   └── workflows
    │   │       └── docker_image.yml          # This file is used for creating CI pipeline
    │   │
    │   ├── djangoproject                     # djangoproject conatins files required for running django project.
    │   │   
    │   ├── kyc                               # kyc folder is an application folder which conatins the source code views, credentials, models required for running application. 
    │   │
    │   ├── utilities                         # This folder conatins the authentication data
    │   │   
    │   ├── db.sqlite3                        # This is database file where all the data that you will be generating will be stored. It is a local file as Django is a server-side framework and it treats your computer as the host when you actually run the server in command line/terminal.
    │   │
    │   ├── django.md                         # Information on Django framework with example
    │   │      
    │   ├── dockerfile                        # This is the configuration file
    │   │
    │   │     
    │   ├── manage.py                         #  manage.py is automatically created in each Django project. It does the same thing as django-admin but also sets the DJANGO_SETTINGS_MODULE environment variable so that it points to your project's settings.py file.
    │   │
    │   │     
    │   └── requirments.txt                   # This file conatins alll the packages names which are essential for the project to run.
    │   
    │
    │
    ├── iaas_api_test_scripts
    │   ├──.github
    │   │   └── workflows
    │   │       └── docker_image.yml          # This file is used for creating CI pipeline    
    │   │
    │   ├──.coverage
    │   ├── README.md
    │   ├── cred.py 
    │   ├── creds.py
    │   ├── ocr.py
    │   ├── swagger.md                        # Information on Swagger
    │   ├── test_bank_account_verification.py 
    │   ├── test_bank_account_verification_advanced.py
    │   ├── test_ca.py
    │   ├── test_cadoc_get_ca_doc.py
    │   ├── test_entity_gst_authentication.py
    │   ├── test_entity_gst_search_basis_plan.py
    │   ├── test_entity_pan_profile.py
    │   ├── test_fetch_e_aggrement_details.py
    │   ├──  test_fetch_termsheets.py
    │   ├── test_initiate_e_aggrement.py
    │   ├── test_kyckra_ckyc_download.py
    │   ├── test_kyckra_ckyc_search.py
    │   ├── test_kyckra_kyc_ocr.py
    │   ├── test_kyckra_pan_authentication_advanced.py
    │   ├── test_lettersandnotices_get_lettersandnotices.py
    │   ├── test_pan_authentication.py
    │   ├── test_pan_status_check.py
    │   ├── test_papertrail.py
    │   ├── test_pan_authentication.py
    │   └── test_schemedoc_get_scheme_doc.py
    │
    └── README.md  # You are here ! 


