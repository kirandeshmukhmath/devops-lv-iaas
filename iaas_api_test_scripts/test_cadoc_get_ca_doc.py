import pytest
import requests
import json
import cred




###############################################  CORPORTE  ################################################################

#Verify the response after giving doctype as "corporate" and valid "doc_params"
def tests_cadoc1():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
        "doctype": "corporate",
        "doc_params": {
            "parties": {
                "trustee": {
                    "name": "VAR - Milestone Trusteeship Services Private Limited",
                    "address": "VAR - registered address of trustee",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "8660970120"
                },
                "investment_manager": {
                    "name": "VAR - Lets Venture Advisors LLP",
                    "address": "VAR - address of Lets Venture Advisors LLP",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "8660970120"
                },
                "contributor": {
                    "name": "VAR - Archimedha Mohapatra",
                    "capital_commitment": "VAR - 5000000",
                    "capital_commitment_upfront_drawdown": "VAR - 2600000",
                    "onboarding_fee": "VAR - 25000",
                    "transaction_fee": "var-2%",
                    "management_fee": "VAR - 2%",
                    "placement_fee": "VAR - 3%",
                    "total_fee": "VAR - 49000",
                    "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "8660970120",
                    "net_worth": "VAR - 3Cr"
                },
                "witness": {
                    "name": "VAR - Rajat Bora",
                    "title": "VAR - Mr.",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "8660970120"
                }
            },
            "fund_details": {
                "fund_name": "VAR - LV ANGEL FUND",
                "addressee": "VAR - Rajeev Ranjan",
                "fund_address": "VAR - Address of LV ANGEL FUND",
                "fund_email": "VAR - archiem@gmail.com",
                "notifier_email": "VAR - archiem1410@gmail.com",
                "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                "portfolio_entity_name": "VAR - LV Angel Fund Entity"
            },
            "agreement_details": {
                "agreement_date": {
                    "date": "VAR - 2022-06-22",
                    "day": "VAR - 22",
                    "month": "VAR - 06",
                    "year": "VAR - 2022"
                },
                "agreement_id": "VAR - asdbde1234"
            }
        }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 200




#Verify the response after giving doctype as "" and valid "doc_params"
def tests_cadoc2():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
        "doctype": "",
        "doc_params": {
            "parties": {
                "trustee": {
                    "name": "VAR - Milestone Trusteeship Services Private Limited",
                    "address": "VAR - registered address of trustee",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "8660970120"
                },
                "investment_manager": {
                    "name": "VAR - Lets Venture Advisors LLP",
                    "address": "VAR - address of Lets Venture Advisors LLP",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "8660970120"
                },
                "contributor": {
                    "name": "VAR - Archimedha Mohapatra",
                    "capital_commitment": "VAR - 5000000",
                    "capital_commitment_upfront_drawdown": "VAR - 2600000",
                    "onboarding_fee": "VAR - 25000",
                    "transaction_fee": "var-2%",
                    "management_fee": "VAR - 2%",
                    "placement_fee": "VAR - 3%",
                    "total_fee": "VAR - 49000",
                    "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "8660970120",
                    "net_worth": "VAR - 3Cr"
                },
                "witness": {
                    "name": "VAR - Rajat Bora",
                    "title": "VAR - Mr.",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "8660970120"
                }
            },
            "fund_details": {
                "fund_name": "VAR - LV ANGEL FUND",
                "addressee": "VAR - Rajeev Ranjan",
                "fund_address": "VAR - Address of LV ANGEL FUND",
                "fund_email": "VAR - archiem@gmail.com",
                "notifier_email": "VAR - archiem1410@gmail.com",
                "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                "portfolio_entity_name": "VAR - LV Angel Fund Entity"
            },
            "agreement_details": {
                "agreement_date": {
                    "date": "VAR - 2022-06-22",
                    "day": "VAR - 22",
                    "month": "VAR - 06",
                    "year": "VAR - 2022"
                },
                "agreement_id": "VAR - asdbde1234"
            }
        }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "corporate" and the "doc_params" has trustee: name as ""  and keep remaining values valid
def tests_cadoc3():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
         "doctype": "corporate",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        "name": ""
                    },
                    "investment_manager": {
                        "name": "LetsVenture",
                        "address": "MG Road Bengaluru"
                    },
                    "contributor": {
                        "name": "Kiran",
                        "capital_commitment": "2000000",
                        "capital_commitment_upfront_drawdown": "2000000",
                        "onboarding_fee": "25000",
                        "management_fee": "5000",
                        "placement_fee": "6000",
                        "total_fee": "36000",
                        "correspondence_address": "Whitefield,Bengaluru",
                        "email_address": "hello@gmail.com",
                        "phone_number": "8147357822",
                        "net_worth": "24004500"
                    },
                    "witness": {
                        "name": "Annvin",
                        "title": "student"
                    }
                },
                "fund_details": {
                    "fund_name": "LV",
                    "addressee": "MG Road Benagluru",
                    "fund_address": "S building M G Road",
                    "fund_email": "hi1234@gmail.com",
                    "notifier_email": "sdhvndnv@gmail.com",
                    "fund_manager_name": "ManagerName",
                    "fund_manager_address": "ManagerAddress",
                    "portfolio_entity_name": "ENTITY99"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "12/June/2022",
                        "day": "12",
                        "month": "June",
                        "year": "2022"
                    },
                    "agreement_id": "10"
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

#Verify if the doctype is "corporate" and the "doc_params" the trustee: name is removed and keep remaining values valid

def tests_cadoc4():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
         "doctype": "corporate",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        
                        
                    },
                    "investment_manager": {
                        "name": "LetsVenture",
                        "address": "MG Road Bengaluru"
                    },
                    "contributor": {
                        "name": "Kiran",
                        "capital_commitment": "2000000",
                        "capital_commitment_upfront_drawdown": "2000000",
                        "onboarding_fee": "25000",
                        "management_fee": "5000",
                        "placement_fee": "6000",
                        "total_fee": "36000",
                        "correspondence_address": "Whitefield,Bengaluru",
                        "email_address": "hello@gmail.com",
                        "phone_number": "8147357822",
                        "net_worth": "24004500"
                    },
                    "witness": {
                        "name": "Annvin",
                        "title": "student"
                    }
                },
                "fund_details": {
                    "fund_name": "LV",
                    "addressee": "MG Road Benagluru",
                    "fund_address": "S building M G Road",
                    "fund_email": "hi1234@gmail.com",
                    "notifier_email": "sdhvndnv@gmail.com",
                    "fund_manager_name": "ManagerName",
                    "fund_manager_address": "ManagerAddress",
                    "portfolio_entity_name": "ENTITY99"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "12/June/2022",
                        "day": "12",
                        "month": "June",
                        "year": "2022"
                    },
                    "agreement_id": "10"
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

#Verify if the doctype is "corporate" and the "doc_params" the investment_manager: name is "" and address "" and keep remaining values valid

def tests_cadoc5():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
         "doctype": "corporate",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        "name":"milestone"
                        
                    },
                    "investment_manager": {
                        "name": "",
                        "address": ""
                    },
                    "contributor": {
                        "name": "Kiran",
                        "capital_commitment": "2000000",
                        "capital_commitment_upfront_drawdown": "2000000",
                        "onboarding_fee": "25000",
                        "management_fee": "5000",
                        "placement_fee": "6000",
                        "total_fee": "36000",
                        "correspondence_address": "Whitefield,Bengaluru",
                        "email_address": "hello@gmail.com",
                        "phone_number": "8147357822",
                        "net_worth": "24004500"
                    },
                    "witness": {
                        "name": "Annvin",
                        "title": "student"
                    }
                },
                "fund_details": {
                    "fund_name": "LV",
                    "addressee": "MG Road Benagluru",
                    "fund_address": "S building M G Road",
                    "fund_email": "hi1234@gmail.com",
                    "notifier_email": "sdhvndnv@gmail.com",
                    "fund_manager_name": "ManagerName",
                    "fund_manager_address": "ManagerAddress",
                    "portfolio_entity_name": "ENTITY99"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "12/June/2022",
                        "day": "12",
                        "month": "June",
                        "year": "2022"
                    },
                    "agreement_id": "10"
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

#Verify if the doctype is "corporate" and the "doc_params" the investment_manager: name and address is removed and keep remaining values valid

def tests_cadoc6():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
         "doctype": "corporate",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        "name":"milestone"
                        
                    },
                    "investment_manager": {
                        
                    },
                    "contributor": {
                        "name": "Kiran",
                        "capital_commitment": "2000000",
                        "capital_commitment_upfront_drawdown": "2000000",
                        "onboarding_fee": "25000",
                        "management_fee": "5000",
                        "placement_fee": "6000",
                        "total_fee": "36000",
                        "correspondence_address": "Whitefield,Bengaluru",
                        "email_address": "hello@gmail.com",
                        "phone_number": "8147357822",
                        "net_worth": "24004500"
                    },
                    "witness": {
                        "name": "Annvin",
                        "title": "student"
                    }
                },
                "fund_details": {
                    "fund_name": "LV",
                    "addressee": "MG Road Benagluru",
                    "fund_address": "S building M G Road",
                    "fund_email": "hi1234@gmail.com",
                    "notifier_email": "sdhvndnv@gmail.com",
                    "fund_manager_name": "ManagerName",
                    "fund_manager_address": "ManagerAddress",
                    "portfolio_entity_name": "ENTITY99"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "12/June/2022",
                        "day": "12",
                        "month": "June",
                        "year": "2022"
                    },
                    "agreement_id": "10"
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

#Verify if the doctype is "corporate" and the "doc_params" the contributor: name, capital_commitment,capital_commitment_upfront_drawdown,onboarding_fee,management_fee,placement_fee,total_fee,correspondence_address,email_address,phone_number,net_worth is "" and keep remaining values valid

def tests_cadoc7():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
         "doctype": "corporate",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        "name":"milestone"
                        
                    },
                    "investment_manager": {
                        "name": "LetsVenture",
                        "address": "MG Road Bengaluru"
                    },
                    "contributor": {
                        "name": "",
                        "capital_commitment": "",
                        "capital_commitment_upfront_drawdown": "",
                        "onboarding_fee": "",
                        "management_fee": "",
                        "placement_fee": "",
                        "total_fee": "",
                        "correspondence_address": "",
                        "email_address": "",
                        "phone_number": "",
                        "net_worth": ""
                    },
                    "witness": {
                        "name": "Annvin",
                        "title": "student"
                    }
                },
                "fund_details": {
                    "fund_name": "LV",
                    "addressee": "MG Road Benagluru",
                    "fund_address": "S building M G Road",
                    "fund_email": "hi1234@gmail.com",
                    "notifier_email": "sdhvndnv@gmail.com",
                    "fund_manager_name": "ManagerName",
                    "fund_manager_address": "ManagerAddress",
                    "portfolio_entity_name": "ENTITY99"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "12/June/2022",
                        "day": "12",
                        "month": "June",
                        "year": "2022"
                    },
                    "agreement_id": "10"
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

#Verify if the doctype is "corporate" and the "doc_params" the contributor: name, capital_commitment,capital_commitment_upfront_drawdown,onboarding_fee,management_fee,placement_fee,total_fee,correspondence_address,email_address,phone_number,net_worth is removed and keep remaining values valid

def tests_cadoc8():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
         "doctype": "corporate",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        "name":"milestone"
                        
                    },
                    "investment_manager": {
                        "name": "LetsVenture",
                        "address": "MG Road Bengaluru"
                    },
                    "contributor": {
                        
                    },
                    "witness": {
                        "name": "Annvin",
                        "title": "student"
                    }
                },
                "fund_details": {
                    "fund_name": "LV",
                    "addressee": "MG Road Benagluru",
                    "fund_address": "S building M G Road",
                    "fund_email": "hi1234@gmail.com",
                    "notifier_email": "sdhvndnv@gmail.com",
                    "fund_manager_name": "ManagerName",
                    "fund_manager_address": "ManagerAddress",
                    "portfolio_entity_name": "ENTITY99"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "12/June/2022",
                        "day": "12",
                        "month": "June",
                        "year": "2022"
                    },
                    "agreement_id": "10"
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

#Verify if the doctype is "corporate" and the "doc_params" the witness: name, title as "" and keep remaining values valid

def tests_cadoc9():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
         "doctype": "corporate",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        "name":"milestone"
                        
                    },
                    "investment_manager": {
                        "name": "LetsVenture",
                        "address": "MG Road Bengaluru"
                    },
                    "contributor": {
                        "name": "Kiran",
                        "capital_commitment": "2000000",
                        "capital_commitment_upfront_drawdown": "2000000",
                        "onboarding_fee": "25000",
                        "management_fee": "5000",
                        "placement_fee": "6000",
                        "total_fee": "36000",
                        "correspondence_address": "Whitefield,Bengaluru",
                        "email_address": "hello@gmail.com",
                        "phone_number": "8147357822",
                        "net_worth": "24004500"
                        
                    },
                    "witness": {
                        "name": "",
                        "title": ""
                    }
                },
                "fund_details": {
                    "fund_name": "LV",
                    "addressee": "MG Road Benagluru",
                    "fund_address": "S building M G Road",
                    "fund_email": "hi1234@gmail.com",
                    "notifier_email": "sdhvndnv@gmail.com",
                    "fund_manager_name": "ManagerName",
                    "fund_manager_address": "ManagerAddress",
                    "portfolio_entity_name": "ENTITY99"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "12/June/2022",
                        "day": "12",
                        "month": "June",
                        "year": "2022"
                    },
                    "agreement_id": "10"
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify if the doctype is "corporate" and the "doc_params" the witness: name, title is removed and keep remaining values valid

def test_cadoc_get_ca_doc_10():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"
#Read Input Json file
    payload = json.dumps(

{
        "doctype": "corporate",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        "name": "milestone"
                    },
                    "investment_manager": {
                        "name": "LetsVenture",
                        "address": "MG Road Bengaluru"
                    },
                    "contributor": {
                        "name": "Kiran",
                        "capital_commitment": "25674738",
                        "capital_commitment_upfront_drawdown": "25672827",
                        "onboarding_fee": "25000",
                        "management_fee": "5",
                        "placement_fee": "6000",
                        "total_fee": "36000",
                        "correspondence_address": "Whitefield,Bengaluru",
                        "email_address": "hello@gmail.com",
                        "phone_number": "8147357822",
                        "net_worth": "277004500"
                    },
                    "witness": {
                       
                    }
                },
                "fund_details": {
                    "fund_name": "LV",
                    "addressee": "MG Road Benagluru",
                    "fund_address": "S building M G Road",
                    "fund_email": "fundemail@gmail.com",
                    "notifier_email": "notifier_email@gmail.com",
                    "fund_manager_name": "ManagerName",
                    "fund_manager_address": "ManagerAddress",
                    "portfolio_entity_name": "ENTITY99"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "12/June/2022",
                        "day": "12",
                        "month": "June",
                        "year": "2022"
                    },
                    "agreement_id": "10"
                }
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452



#Verify if the doctype is "corporate" and the "doc_params" the fund_details: fund_name, addressee, fund_address, fund_email,notifier_email,fund_manager_name,fund_manager_address,portfolio_entity_name is "" and keep remaining values valid

def test_cadoc_get_ca_doc_11():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"
#Read Input Json file
    payload = json.dumps(

{
        "doctype": "corporate",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        "name": "milestone"
                    },
                    "investment_manager": {
                        "name": "LetsVenture",
                        "address": "MG Road Bengaluru"
                    },
                    "contributor": {
                        "name": "Kiran",
                        "capital_commitment": "25674738",
                        "capital_commitment_upfront_drawdown": "25672827",
                        "onboarding_fee": "25000",
                        "management_fee": "5",
                        "placement_fee": "6000",
                        "total_fee": "36000",
                        "correspondence_address": "Whitefield,Bengaluru",
                        "email_address": "hello@gmail.com",
                        "phone_number": "8147357822",
                        "net_worth": "277004500"
                    },
                    "witness": {
                        "name": "Annvin",
                        "title": "student"
                    }
                },
                "fund_details": {
                    "fund_name": "",
                    "addressee": "",
                    "fund_address": "",
                    "fund_email": "",
                    "notifier_email": "",
                    "fund_manager_name": "",
                    "fund_manager_address": "",
                    "portfolio_entity_name": ""
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "12/June/2022",
                        "day": "12",
                        "month": "June",
                        "year": "2022"
                    },
                    "agreement_id": "10"
                }
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452



#Verify if the doctype is "corporate" and the "doc_params" the fund_details: fund_name, addressee, fund_address, fund_email,notifier_email,fund_manager_name,fund_manager_address,portfolio_entity_name is removed and keep remaining values valid

def test_cadoc_get_ca_doc_12():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"
#Read Input Json file
    payload = json.dumps(

{
        "doctype": "corporate",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        "name": "milestone"
                    },
                    "investment_manager": {
                        "name": "LetsVenture",
                        "address": "MG Road Bengaluru"
                    },
                    "contributor": {
                        "name": "Kiran",
                        "capital_commitment": "25674738",
                        "capital_commitment_upfront_drawdown": "25672827",
                        "onboarding_fee": "25000",
                        "management_fee": "5",
                        "placement_fee": "6000",
                        "total_fee": "36000",
                        "correspondence_address": "Whitefield,Bengaluru",
                        "email_address": "hello@gmail.com",
                        "phone_number": "8147357822",
                        "net_worth": "277004500"
                    },
                    "witness": {
                        "name": "Annvin",
                        "title": "student"
                    }
                },
                "fund_details": {

                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "12/June/2022",
                        "day": "12",
                        "month": "June",
                        "year": "2022"
                    },
                    "agreement_id": "10"
                }
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452



#Verify if the doctype is "corporate" and the "doc_params" agreement_details: agreement_date,date,day,month,year as "" and keep remaining values valid

def test_cadoc_get_ca_doc_13():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"
#Read Input Json file
    payload = json.dumps(

{
        "doctype": "corporate",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        "name": "milestone"
                    },
                    "investment_manager": {
                        "name": "LetsVenture",
                        "address": "MG Road Bengaluru"
                    },
                    "contributor": {
                        "name": "Kiran",
                        "capital_commitment": "25674738",
                        "capital_commitment_upfront_drawdown": "25672827",
                        "onboarding_fee": "25000",
                        "management_fee": "5",
                        "placement_fee": "6000",
                        "total_fee": "36000",
                        "correspondence_address": "Whitefield,Bengaluru",
                        "email_address": "hello@gmail.com",
                        "phone_number": "8147357822",
                        "net_worth": "277004500"
                    },
                    "witness":  {
                        "name": "Annvin",
                        "title": "student"
                    }
                },
                "fund_details": {
                    "fund_name": "LV",
                    "addressee": "MG Road Benagluru",
                    "fund_address": "S building M G Road",
                    "fund_email": "fundemail@gmail.com",
                    "notifier_email": "notifier_email@gmail.com",
                    "fund_manager_name": "ManagerName",
                    "fund_manager_address": "ManagerAddress",
                    "portfolio_entity_name": "ENTITY99"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "",
                        "day": "",
                        "month": "",
                        "year": ""
                    },
                    "agreement_id": "10"
                }
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452





#Verify if the doctype is "corporate" and the "doc_params" agreement_details: agreement_date,date,day,month,year is removed and keep remaining values valid

def test_cadoc_get_ca_doc_14():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"
#Read Input Json file
    payload = json.dumps(

{
        "doctype": "corporate",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        "name": "milestone"
                    },
                    "investment_manager": {
                        "name": "LetsVenture",
                        "address": "MG Road Bengaluru"
                    },
                    "contributor": {
                        "name": "Kiran",
                        "capital_commitment": "25674738",
                        "capital_commitment_upfront_drawdown": "25672827",
                        "onboarding_fee": "25000",
                        "management_fee": "5",
                        "placement_fee": "6000",
                        "total_fee": "36000",
                        "correspondence_address": "Whitefield,Bengaluru",
                        "email_address": "hello@gmail.com",
                        "phone_number": "8147357822",
                        "net_worth": "277004500"
                    },
                    "witness":  {
                        "name": "Annvin",
                        "title": "student"
                    }
                },
                "fund_details": {
                    "fund_name": "LV",
                    "addressee": "MG Road Benagluru",
                    "fund_address": "S building M G Road",
                    "fund_email": "fundemail@gmail.com",
                    "notifier_email": "notifier_email@gmail.com",
                    "fund_manager_name": "ManagerName",
                    "fund_manager_address": "ManagerAddress",
                    "portfolio_entity_name": "ENTITY99"
                },
                "agreement_details": {
                    "agreement_date": {

                    },
                    "agreement_id": "10"
                }
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452





#Verify if the doctype is "corporate" and the "doc_params" agreement_id: is "" and keep remaining values valid

def test_cadoc_get_ca_doc_15():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"
#Read Input Json file
    payload = json.dumps(

{
        "doctype": "corporate",
        "doc_params": {
            "parties": {
                "trustee": {
                    "name": "VAR - Milestone Trusteeship Services Private Limited",
                    "address": "VAR - registered address of trustee",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "8660970120"
                },
                "investment_manager": {
                    "name": "VAR - Lets Venture Advisors LLP",
                    "address": "VAR - address of Lets Venture Advisors LLP",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "8660970120"
                },
                "contributor": {
                    "name": "VAR - Archimedha Mohapatra",
                    "capital_commitment": "VAR - 5000000",
                    "capital_commitment_upfront_drawdown": "VAR - 2600000",
                    "onboarding_fee": "VAR - 25000",
                    "transaction_fee": "var-2%",
                    "management_fee": "VAR - 2%",
                    "placement_fee": "VAR - 3%",
                    "total_fee": "VAR - 49000",
                    "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "8660970120",
                    "net_worth": "VAR - 3Cr"
                },
                "witness": {
                    "name": "VAR - Rajat Bora",
                    "title": "VAR - Mr.",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "8660970120"
                }
            },
            "fund_details": {
                "fund_name": "VAR - LV ANGEL FUND",
                "addressee": "VAR - Rajeev Ranjan",
                "fund_address": "VAR - Address of LV ANGEL FUND",
                "fund_email": "VAR - archiem@gmail.com",
                "notifier_email": "VAR - archiem1410@gmail.com",
                "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                "portfolio_entity_name": "VAR - LV Angel Fund Entity"
            },
            "agreement_details": {
                "agreement_date": {
                    "date": "VAR - 2022-06-22",
                    "day": "VAR - 22",
                    "month": "VAR - 06",
                    "year": "VAR - 2022"
                },
                "agreement_id": ""
            }
        }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 200






#Verify if the doctype is "corporate" and the "doc_params" agreement_id: is  removed and keep remaining values valid

def test_cadoc_get_ca_doc_16():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"
#Read Input Json file
    payload = json.dumps(

{
        "doctype": "corporate",
        "doc_params": {
            "parties": {
                "trustee": {
                    "name": "VAR - Milestone Trusteeship Services Private Limited",
                    "address": "VAR - registered address of trustee",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "8660970120"
                },
                "investment_manager": {
                    "name": "VAR - Lets Venture Advisors LLP",
                    "address": "VAR - address of Lets Venture Advisors LLP",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "8660970120"
                },
                "contributor": {
                    "name": "VAR - Archimedha Mohapatra",
                    "capital_commitment": "VAR - 5000000",
                    "capital_commitment_upfront_drawdown": "VAR - 2600000",
                    "onboarding_fee": "VAR - 25000",
                    "transaction_fee": "var-2%",
                    "management_fee": "VAR - 2%",
                    "placement_fee": "VAR - 3%",
                    "total_fee": "VAR - 49000",
                    "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "8660970120",
                    "net_worth": "VAR - 3Cr"
                },
                "witness": {
                    "name": "VAR - Rajat Bora",
                    "title": "VAR - Mr.",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "8660970120"
                }
            },
            "fund_details": {
                "fund_name": "VAR - LV ANGEL FUND",
                "addressee": "VAR - Rajeev Ranjan",
                "fund_address": "VAR - Address of LV ANGEL FUND",
                "fund_email": "VAR - archiem@gmail.com",
                "notifier_email": "VAR - archiem1410@gmail.com",
                "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                "portfolio_entity_name": "VAR - LV Angel Fund Entity"
            },
            "agreement_details": {
                "agreement_date": {
                    "date": "VAR - 2022-06-22",
                    "day": "VAR - 22",
                    "month": "VAR - 06",
                    "year": "VAR - 2022"
                },
                
            }
        }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 200



########################################################################  HUF  ###################################################################################



#Verify the response after giving doctype as "huf" and valid "doc_params"
def tests_cadoc18():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 200




#Verify the response after giving doctype as "" and valid huf "doc_params"
def tests_cadoc19():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452


#Verify the response  if the doctype is "huf" and the "doc_params" has trustee: name as ""  and keep remaining values valid
def tests_cadoc20():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "huf" and the "doc_params" has trustee: address as ""  and keep remaining values valid
def tests_cadoc21():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": ""
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "huf" and the "doc_params" has investment_manager: name as ""  and keep remaining values valid
def tests_cadoc22():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "huf" and the "doc_params" has investment_manager: address as ""  and keep remaining values valid
def tests_cadoc23():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": ""
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "huf" and the "doc_params" has contributor: name as ""  and keep remaining values valid
def tests_cadoc24():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "huf" and the "doc_params" has contributor: capital_commitment as ""  and keep remaining values valid
def tests_cadoc25():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "huf" and the "doc_params" has contributor: capital_commitment_upfront_drawdown as ""  and keep remaining values valid
def tests_cadoc26():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "huf" and the "doc_params" has contributor: onboarding_fee as ""  and keep remaining values valid
def tests_cadoc27():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "huf" and the "doc_params" has contributor: transaction_fee as ""  and keep remaining values valid
def tests_cadoc28():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "huf" and the "doc_params" has contributor: management_fee as ""  and keep remaining values valid
def tests_cadoc29():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452






#Verify the response  if the doctype is "huf" and the "doc_params" has contributor: placement_fee as ""  and keep remaining values valid
def tests_cadoc30():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "huf" and the "doc_params" has contributor: total_fee as ""  and keep remaining values valid
def tests_cadoc31():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response  if the doctype is "huf" and the "doc_params" has contributor: correspondence_address as ""  and keep remaining values valid
def tests_cadoc32():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "huf" and the "doc_params" has contributor: email_address as ""  and keep remaining values valid
def tests_cadoc33():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "huf" and the "doc_params" has contributor: phone_number as ""  and keep remaining values valid
def tests_cadoc34():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response  if the doctype is "huf" and the "doc_params" has contributor: net_worth as ""  and keep remaining values valid
def tests_cadoc35():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": ""
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "huf" and the "doc_params" has witness: name as ""  and keep remaining values valid
def tests_cadoc36():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "huf" and the "doc_params" has witness: title as ""  and keep remaining values valid
def tests_cadoc37():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": ""
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "huf" and the "doc_params" has fund_details: fund_name as ""  and keep remaining values valid
def tests_cadoc38():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "huf" and the "doc_params" has fund_details: addressee as ""  and keep remaining values valid
def tests_cadoc39():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "huf" and the "doc_params" has fund_details: fund_address as ""  and keep remaining values valid
def tests_cadoc40():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "Addresss",
                    "fund_address": "",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "huf" and the "doc_params" has fund_details: fund_email as ""  and keep remaining values valid
def tests_cadoc41():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "huf" and the "doc_params" has fund_details: notifier_email as ""  and keep remaining values valid
def tests_cadoc42():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "huf" and the "doc_params" has fund_details: fund_manager_name as ""  and keep remaining values valid
def tests_cadoc43():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "huf" and the "doc_params" has fund_details: fund_manager_address as ""  and keep remaining values valid
def tests_cadoc44():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response  if the doctype is "huf" and the "doc_params" has fund_details: portfolio_entity_name as ""  and keep remaining values valid
def tests_cadoc45():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": ""
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "huf" and the "doc_params" has agreement_details: agreement_date as ""  and keep remaining values valid
def tests_cadoc46():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "kiran"
                },
                "agreement_details": {
                    "agreement_date": {},
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "huf" and the "doc_params" has agreement_details: agreement_id as ""  and keep remaining values valid
def tests_cadoc47():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "Kiran"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": ""
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 200


################################################   JOINT   ##########################################################################


#Verify the response after giving doctype as "joint" and valid "doc_params"
def tests_cadoc49():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 200




#Verify the response after giving doctype as "" and valid joint "doc_params"
def tests_cadoc50():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452


#Verify the response  if the doctype is "joint" and the "doc_params" has trustee: name as ""  and keep remaining values valid
def tests_cadoc51():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "joint" and the "doc_params" has trustee: address as ""  and keep remaining values valid
def tests_cadoc52():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": ""
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "joint" and the "doc_params" has investment_manager: name as ""  and keep remaining values valid
def tests_cadoc53():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "joint" and the "doc_params" has investment_manager: address as ""  and keep remaining values valid
def tests_cadoc54():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": ""
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "joint" and the "doc_params" has contributor: name as ""  and keep remaining values valid
def tests_cadoc55():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

#Verify the response  if the doctype is "joint" and the "doc_params" has contributor: dob as ""  and keep remaining values valid
def tests_cadoc56():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response  if the doctype is "joint" and the "doc_params" has contributor: dob_place as ""  and keep remaining values valid
def tests_cadoc57():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "",
                        "name": "",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "joint" and the "doc_params" has contributor: capital_commitment as ""  and keep remaining values valid
def tests_cadoc58():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "joint" and the "doc_params" has contributor: capital_commitment_upfront_drawdown as ""  and keep remaining values valid
def tests_cadoc59():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "joint" and the "doc_params" has contributor: onboarding_fee as ""  and keep remaining values valid
def tests_cadoc60():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "joint" and the "doc_params" has contributor: transaction_fee as ""  and keep remaining values valid
def tests_cadoc61():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "joint" and the "doc_params" has contributor: management_fee as ""  and keep remaining values valid
def tests_cadoc62():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452






#Verify the response  if the doctype is "joint" and the "doc_params" has contributor: placement_fee as ""  and keep remaining values valid
def tests_cadoc63():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "joint" and the "doc_params" has contributor: total_fee as ""  and keep remaining values valid
def tests_cadoc64():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response  if the doctype is "joint" and the "doc_params" has contributor: correspondence_address as ""  and keep remaining values valid
def tests_cadoc65():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "joint" and the "doc_params" has contributor: email_address as ""  and keep remaining values valid
def tests_cadoc66():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "joint" and the "doc_params" has contributor: phone_number as ""  and keep remaining values valid
def tests_cadoc67():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response  if the doctype is "joint" and the "doc_params" has contributor: net_worth as ""  and keep remaining values valid
def tests_cadoc68():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": ""
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "joint" and the "doc_params" has witness: name as ""  and keep remaining values valid
def tests_cadoc69():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "joint" and the "doc_params" has witness: title as ""  and keep remaining values valid
def tests_cadoc70():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": ""
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "joint" and the "doc_params" has fund_details: fund_name as ""  and keep remaining values valid
def tests_cadoc71():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "joint" and the "doc_params" has fund_details: addressee as ""  and keep remaining values valid
def tests_cadoc72():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "joint" and the "doc_params" has fund_details: fund_address as ""  and keep remaining values valid
def tests_cadoc73():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "Addresss",
                    "fund_address": "",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "joint" and the "doc_params" has fund_details: fund_email as ""  and keep remaining values valid
def tests_cadoc74():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "joint" and the "doc_params" has fund_details: notifier_email as ""  and keep remaining values valid
def tests_cadoc75():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "joint" and the "doc_params" has fund_details: fund_manager_name as ""  and keep remaining values valid
def tests_cadoc76():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "joint" and the "doc_params" has fund_details: fund_manager_address as ""  and keep remaining values valid
def tests_cadoc77():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response  if the doctype is "joint" and the "doc_params" has fund_details: portfolio_entity_name as ""  and keep remaining values valid
def tests_cadoc78():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": ""
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "joint" and the "doc_params" has agreement_details: agreement_date as ""  and keep remaining values valid
def tests_cadoc79():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "kiran"
                },
                "agreement_details": {
                    "agreement_date": {},
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "joint" and the "doc_params" has agreement_details: agreement_id as ""  and keep remaining values valid
def tests_cadoc80():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "Kiran"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": ""
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 200



  ################################################################  PARTNERSHIP  ###################################################################################





  #Verify the response after giving doctype as "partnership" and valid "doc_params"
def tests_cadoc82():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 200




#Verify the response after giving doctype as "" and valid partnership "doc_params"
def tests_cadoc83():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452


#Verify the response  if the doctype is "partnership" and the "doc_params" has trustee: name as ""  and keep remaining values valid
def tests_cadoc84():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "partnership" and the "doc_params" has trustee: address as ""  and keep remaining values valid
def tests_cadoc85():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": ""
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "partnership" and the "doc_params" has investment_manager: name as ""  and keep remaining values valid
def tests_cadoc86():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "partnership" and the "doc_params" has investment_manager: address as ""  and keep remaining values valid
def tests_cadoc87():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": ""
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "partnership" and the "doc_params" has contributor: name as ""  and keep remaining values valid
def tests_cadoc88():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "partnership" and the "doc_params" has contributor: capital_commitment as ""  and keep remaining values valid
def tests_cadoc89():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "partnership" and the "doc_params" has contributor: capital_commitment_upfront_drawdown as ""  and keep remaining values valid
def tests_cadoc90():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "partnership" and the "doc_params" has contributor: onboarding_fee as ""  and keep remaining values valid
def tests_cadoc91():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "partnership" and the "doc_params" has contributor: transaction_fee as ""  and keep remaining values valid
def tests_cadoc92():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "partnership" and the "doc_params" has contributor: management_fee as ""  and keep remaining values valid
def tests_cadoc93():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452






#Verify the response  if the doctype is "partnership" and the "doc_params" has contributor: placement_fee as ""  and keep remaining values valid
def tests_cadoc94():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "partnership" and the "doc_params" has contributor: total_fee as ""  and keep remaining values valid
def tests_cadoc95():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response  if the doctype is "partnership" and the "doc_params" has contributor: correspondence_address as ""  and keep remaining values valid
def tests_cadoc96():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "partnership" and the "doc_params" has contributor: email_address as ""  and keep remaining values valid
def tests_cadoc97():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "partnership" and the "doc_params" has contributor: phone_number as ""  and keep remaining values valid
def tests_cadoc98():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response  if the doctype is "partnership" and the "doc_params" has contributor: net_worth as ""  and keep remaining values valid
def tests_cadoc99():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": ""
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "partnership" and the "doc_params" has witness: name as ""  and keep remaining values valid
def tests_cadoc100():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "partnership" and the "doc_params" has witness: title as ""  and keep remaining values valid
def tests_cadoc101():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": ""
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "partnership" and the "doc_params" has fund_details: fund_name as ""  and keep remaining values valid
def tests_cadoc102():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "partnership" and the "doc_params" has fund_details: addressee as ""  and keep remaining values valid
def tests_cadoc103():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "partnership" and the "doc_params" has fund_details: fund_address as ""  and keep remaining values valid
def tests_cadoc104():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "Addresss",
                    "fund_address": "",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "partnership" and the "doc_params" has fund_details: fund_email as ""  and keep remaining values valid
def tests_cadoc105():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "partnership" and the "doc_params" has fund_details: notifier_email as ""  and keep remaining values valid
def tests_cadoc106():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "partnership" and the "doc_params" has fund_details: fund_manager_name as ""  and keep remaining values valid
def tests_cadoc107():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "partnership" and the "doc_params" has fund_details: fund_manager_address as ""  and keep remaining values valid
def tests_cadoc108():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response  if the doctype is "partnership" and the "doc_params" has fund_details: portfolio_entity_name as ""  and keep remaining values valid
def tests_cadoc109():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": ""
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "partnership" and the "doc_params" has agreement_details: agreement_date as ""  and keep remaining values valid
def tests_cadoc110():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "kiran"
                },
                "agreement_details": {
                    "agreement_date": {},
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "partnership" and the "doc_params" has agreement_details: agreement_id as ""  and keep remaining values valid
def tests_cadoc111():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "partnership",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "Kiran"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": ""
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 200





################################################  INDIVIDUAL  #########################################################


  #Verify the response after giving doctype as "individual" and valid "doc_params"
def tests_cadoc113():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 200




#Verify the response after giving doctype as "" and valid individual "doc_params"
def tests_cadoc114():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452


#Verify the response  if the doctype is "individual" and the "doc_params" has trustee: name as ""  and keep remaining values valid
def tests_cadoc115():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "individual" and the "doc_params" has trustee: address as ""  and keep remaining values valid
def tests_cadoc116():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": ""
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "individual" and the "doc_params" has investment_manager: name as ""  and keep remaining values valid
def tests_cadoc117():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "individual" and the "doc_params" has investment_manager: address as ""  and keep remaining values valid
def tests_cadoc118():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": ""
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "individual" and the "doc_params" has contributor: name as ""  and keep remaining values valid
def tests_cadoc119():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "individual" and the "doc_params" has contributor: capital_commitment as ""  and keep remaining values valid
def tests_cadoc120():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "individual" and the "doc_params" has contributor: capital_commitment_upfront_drawdown as ""  and keep remaining values valid
def tests_cadoc121():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "individual" and the "doc_params" has contributor: onboarding_fee as ""  and keep remaining values valid
def tests_cadoc122():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "individual" and the "doc_params" has contributor: transaction_fee as ""  and keep remaining values valid
def tests_cadoc123():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "individual" and the "doc_params" has contributor: management_fee as ""  and keep remaining values valid
def tests_cadoc124():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452






#Verify the response  if the doctype is "individual" and the "doc_params" has contributor: placement_fee as ""  and keep remaining values valid
def tests_cadoc125():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "individual" and the "doc_params" has contributor: total_fee as ""  and keep remaining values valid
def tests_cadoc126():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response  if the doctype is "individual" and the "doc_params" has contributor: correspondence_address as ""  and keep remaining values valid
def tests_cadoc127():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "individual" and the "doc_params" has contributor: email_address as ""  and keep remaining values valid
def tests_cadoc128():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "individual" and the "doc_params" has contributor: phone_number as ""  and keep remaining values valid
def tests_cadoc129():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response  if the doctype is "individual" and the "doc_params" has contributor: net_worth as ""  and keep remaining values valid
def tests_cadoc130():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": ""
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "individual" and the "doc_params" has witness: name as ""  and keep remaining values valid
def tests_cadoc131():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "individual" and the "doc_params" has witness: title as ""  and keep remaining values valid
def tests_cadoc132():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": ""
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "individual" and the "doc_params" has fund_details: fund_name as ""  and keep remaining values valid
def tests_cadoc133():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "individual" and the "doc_params" has fund_details: addressee as ""  and keep remaining values valid
def tests_cadoc134():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "individual" and the "doc_params" has fund_details: fund_address as ""  and keep remaining values valid
def tests_cadoc135():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "Addresss",
                    "fund_address": "",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "individual" and the "doc_params" has fund_details: fund_email as ""  and keep remaining values valid
def tests_cadoc136():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "individual" and the "doc_params" has fund_details: notifier_email as ""  and keep remaining values valid
def tests_cadoc137():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "individual" and the "doc_params" has fund_details: fund_manager_name as ""  and keep remaining values valid
def tests_cadoc138():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "individual" and the "doc_params" has fund_details: fund_manager_address as ""  and keep remaining values valid
def tests_cadoc139():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response  if the doctype is "individual" and the "doc_params" has fund_details: portfolio_entity_name as ""  and keep remaining values valid
def tests_cadoc140():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": ""
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452





#Verify the response  if the doctype is "individual" and the "doc_params" has agreement_details: agreement_date as ""  and keep remaining values valid
def tests_cadoc141():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "kiran"
                },
                "agreement_details": {
                    "agreement_date": {},
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response  if the doctype is "individual" and the "doc_params" has agreement_details: agreement_id as ""  and keep remaining values valid
def tests_cadoc142():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "individual",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "Kiran"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": ""
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 200



####################################################################  Side-letter-joint-agreement  ###################################################################


#Verify the response after giving doctype as "Side-letter-joint-agreement" , template as "side-letter-joint-agreement.html" and valid doc_params
def tests_cadoc144():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Archimedha Mohapatra",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Rajeev Ranjan",
                        "email": "rajeev.lv@grepdigital.com",
                        "phone": "8660970120",
                        "address": "London",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 200



#Verify the response after giving doctype as "" , template as "side-letter-joint-agreement.html" and valid doc_params
def tests_cadoc145():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
        "doctype": "",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Archimedha Mohapatra",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Rajeev Ranjan",
                        "email": "rajeev.lv@grepdigital.com",
                        "phone": "8660970120",
                        "address": "London",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response after giving doctype as "Side-letter-joint-agreement" , template as "" and valid doc_params
def tests_cadoc146():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
        "doctype": "side-letter-joint-agreement",
        "template": "",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Archimedha Mohapatra",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Rajeev Ranjan",
                        "email": "rajeev.lv@grepdigital.com",
                        "phone": "8660970120",
                        "address": "London",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 200



#Verify the response after giving doctype as "Side-letter-joint-agreement" , template as "side-letter-joint-agreement.html" and in doc_params keep "letter_date" as " ".
def tests_cadoc147():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "",
                "parties": {
                    "first_party": {
                        "name": "Archimedha Mohapatra",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Rajeev Ranjan",
                        "email": "rajeev.lv@grepdigital.com",
                        "phone": "8660970120",
                        "address": "London",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452


#Verify the response after giving doctype as "Side-letter-joint-agreement" , template as "side-letter-joint-agreement.html" and in doc_params keep "parties" "first_party". name as " ".
def tests_cadoc148():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Rajeev Ranjan",
                        "email": "rajeev.lv@grepdigital.com",
                        "phone": "8660970120",
                        "address": "London",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response after giving doctype as "Side-letter-joint-agreement" , template as "side-letter-joint-agreement.html" and in doc_params keep "parties" "first_party". email as " ".
def tests_cadoc149():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Archimedha Mohapatra",
                        "email": "",
                        "phone": "9741601203",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Rajeev Ranjan",
                        "email": "rajeev.lv@grepdigital.com",
                        "phone": "8660970120",
                        "address": "London",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response after giving doctype as "Side-letter-joint-agreement" , template as "side-letter-joint-agreement.html" and in doc_params keep "parties" "first_party". phone as " ".
def tests_cadoc150():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Archimedha Mohapatra",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Rajeev Ranjan",
                        "email": "rajeev.lv@grepdigital.com",
                        "phone": "8660970120",
                        "address": "London",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452


#Verify the response after giving doctype as "Side-letter-joint-agreement" , template as "side-letter-joint-agreement.html" and in doc_params keep "parties" "first_party". address as " ".
def tests_cadoc151():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Archimedha Mohapatra",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203",
                        "address": ""
                    },
                    "second_party": {
                        "name": "Rajeev Ranjan",
                        "email": "rajeev.lv@grepdigital.com",
                        "phone": "8660970120",
                        "address": "London",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response after giving doctype as "Side-letter-joint-agreement" , template as "side-letter-joint-agreement.html" and in doc_params keep "parties" "second_party". name as " ".
def tests_cadoc152():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Archimedha Mohapatra",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "",
                        "email": "rajeev.lv@grepdigital.com",
                        "phone": "8660970120",
                        "address": "London",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response after giving doctype as "Side-letter-joint-agreement" , template as "side-letter-joint-agreement.html" and in doc_params keep "parties" "second_party". email as " ".
def tests_cadoc153():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Archimedha Mohapatra",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Rajeev Ranjan",
                        "email": "",
                        "phone": "8660970120",
                        "address": "London",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response after giving doctype as "Side-letter-joint-agreement" , template as "side-letter-joint-agreement.html" and in doc_params keep "parties" "second_party". phone as " ".
def tests_cadoc154():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Archimedha Mohapatra",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Rajeev Ranjan",
                        "email": "rajeev.lv@grepdigital.com",
                        "phone": "",
                        "address": "London",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response after giving doctype as "Side-letter-joint-agreement" , template as "side-letter-joint-agreement.html" and in doc_params keep "parties" "second_party". address as " ".
def tests_cadoc155():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Archimedha Mohapatra",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Rajeev Ranjan",
                        "email": "rajeev.lv@grepdigital.com",
                        "phone": "8660970120",
                        "address": "",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response after giving doctype as "Side-letter-joint-agreement" , template as "side-letter-joint-agreement.html" and in doc_params keep "parties" "second_party". relationship_with_first_contributor as " ".
def tests_cadoc156():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Archimedha Mohapatra",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Rajeev Ranjan",
                        "email": "rajeev.lv@grepdigital.com",
                        "phone": "8660970120",
                        "address": "London",
                        "relationship_with_first_contributor": ""
                    }
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452






############################################################# Continuation of HUF test cases #########################################################################

#Verify the response after giving doctype as "huf" and by removing "trustee" name and address but keep remaining values correct. Response status should be 452
def tests_cadoc_159():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response after giving doctype as "huf" and by removing "investment_manager": name and address but keep remaining values correct. Response status should be 452
def tests_cadoc_160():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response after giving doctype as "huf" and by removing "contributor": name, capital_commitment, capital_commitment_upfront_drawdown, onboarding_fee, transaction_fee, management_fee, placement_fee, total_fee, correspondence_address, email_address, phone_number, net_worth but keep remaining values correct. Response status should be 452
def tests_cadoc_161():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452


#Verify the response after giving doctype as "huf" and by removing "witness": name and title but keep remaining values correct. Response status should be 452
def tests_cadoc_162():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response after giving doctype as "huf" and by removing "fund_details": fund_name, addressee, fund_address, fund_email, notifier_email, fund_manager_name, fund_manager_address, portfolio_entity_name but keep remaining values correct. Response status should be 452
def tests_cadoc_163():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response after giving doctype as "huf" and valid "doc_params"
def tests_cadoc_164():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




########################################################### Continuation of Joint test cases ##########################################################

#Verify the response after giving doctype as "joint" and by removing "trustee" name and address but keep remaining values correct. Response status should be 452
def tests_cadoc_166():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452


#Verify the response after giving doctype as "joint" and by removing "investment_manager": name and address but keep remaining values correct. Response status should be 452
def tests_cadoc_167():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response after giving doctype as "joint" and by removing "contributor": dob, dob_place, name, capital_commitment, capital_commitment_upfront_drawdown, onboarding_fee, transaction_fee, management_fee, placement_fee, total_fee, correspondence_address, email_address, phone_number, net_worth but keep remaining values correct. Response status should be 452
def tests_cadoc_168():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452


#Verify the response after giving doctype as "joint" and by removing "witness": name and title but keep remaining values correct. Response status should be 452
def tests_cadoc_169():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#Verify the response after giving doctype as "joint" and by removing "fund_details": fund_name, addressee, fund_address, fund_email, notifier_email, fund_manager_name, fund_manager_address, portfolio_entity_name but keep remaining values correct. Response status should be 452
def tests_cadoc_170():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



#Verify the response after giving doctype as "joint" and by removing "agreement_details": "agreement_date" : date, day, month, year but keep remaining values correct. Response status should be 452
def tests_cadoc_171():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
  "doctype": "joint",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "dob": "VAR - 1976-11-17",
                        "dob_place": "VAR - Mombasa, Kenya",
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        
                    },
                    "agreement_id": "VAR - asdbde1234"
                }
            }
})


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




#################################################################### Continuation of Partership ###########################################################################

#Verify the response after giving doctype as "partnership" and by removing "trustee" name and address but keep remaining values correct. Response status should be 452

def tests_cadoc173():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
         "doctype": "partnership",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        
                        
                    },
                    "investment_manager": {
                        "name": "LetsVenture",
                        "address": "MG Road Bengaluru"
                    },
                    "contributor": {
                        "name": "Kiran",
                        "capital_commitment": "2000000",
                        "capital_commitment_upfront_drawdown": "2000000",
                        "onboarding_fee": "25000",
                        "management_fee": "5000",
                        "placement_fee": "6000",
                        "total_fee": "36000",
                        "correspondence_address": "Whitefield,Bengaluru",
                        "email_address": "hello@gmail.com",
                        "phone_number": "8147357822",
                        "net_worth": "24004500"
                        
                    },
                    "witness": {
                        "name": "",
                        "title": ""
                    }
                },
                "fund_details": {
                    "fund_name": "LV",
                    "addressee": "MG Road Benagluru",
                    "fund_address": "S building M G Road",
                    "fund_email": "hi1234@gmail.com",
                    "notifier_email": "sdhvndnv@gmail.com",
                    "fund_manager_name": "ManagerName",
                    "fund_manager_address": "ManagerAddress",
                    "portfolio_entity_name": "ENTITY99"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "12/June/2022",
                        "day": "12",
                        "month": "June",
                        "year": "2022"
                    },
                    "agreement_id": "10"
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452


#Verify the response after giving doctype as "partnership" and by removing "investment_manager": name and address but keep remaining values correct. Response status should be 452

def tests_cadoc174():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
         "doctype": "partnership",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        "name":"milestone"
                        
                    },
                    "investment_manager": {
                        
                    },
                    "contributor": {
                        "name": "Kiran",
                        "capital_commitment": "2000000",
                        "capital_commitment_upfront_drawdown": "2000000",
                        "onboarding_fee": "25000",
                        "management_fee": "5000",
                        "placement_fee": "6000",
                        "total_fee": "36000",
                        "correspondence_address": "Whitefield,Bengaluru",
                        "email_address": "hello@gmail.com",
                        "phone_number": "8147357822",
                        "net_worth": "24004500"
                        
                    },
                    "witness": {
                        "name": "",
                        "title": ""
                    }
                },
                "fund_details": {
                    "fund_name": "LV",
                    "addressee": "MG Road Benagluru",
                    "fund_address": "S building M G Road",
                    "fund_email": "hi1234@gmail.com",
                    "notifier_email": "sdhvndnv@gmail.com",
                    "fund_manager_name": "ManagerName",
                    "fund_manager_address": "ManagerAddress",
                    "portfolio_entity_name": "ENTITY99"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "12/June/2022",
                        "day": "12",
                        "month": "June",
                        "year": "2022"
                    },
                    "agreement_id": "10"
                }
            }
    })

#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

#Verify the response after giving doctype as "partnership" and by removing "contributor": name, capital_commitment, capital_commitment_upfront_drawdown, onboarding_fee, transaction_fee, management_fee, placement_fee, total_fee, correspondence_address, email_address, phone_number, net_worth but keep remaining values correct. Response status should be 452

def tests_cadoc175():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
         "doctype": "partnership",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        "name":"milestone"
                        
                    },
                    "investment_manager": {
                        "name": "LetsVenture",
                        "address": "MG Road Bengaluru"
                    },
                    "contributor": {
                        
                        
                    },
                    "witness": {
                        "name": "",
                        "title": ""
                    }
                },
                "fund_details": {
                    "fund_name": "LV",
                    "addressee": "MG Road Benagluru",
                    "fund_address": "S building M G Road",
                    "fund_email": "hi1234@gmail.com",
                    "notifier_email": "sdhvndnv@gmail.com",
                    "fund_manager_name": "ManagerName",
                    "fund_manager_address": "ManagerAddress",
                    "portfolio_entity_name": "ENTITY99"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "12/June/2022",
                        "day": "12",
                        "month": "June",
                        "year": "2022"
                    },
                    "agreement_id": "10"
                }
            }
    })

#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452


#Verify the response after giving doctype as "partnership" and by removing "witness": name and title but keep remaining values correct. Response status should be 452
def tests_cadoc176():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
         "doctype": "partnership",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        "name":"milestone"
                        
                    },
                    "investment_manager": {
                        "name": "LetsVenture",
                        "address": "MG Road Bengaluru"
                    },
                    "contributor": {
                        "name": "Kiran",
                        "capital_commitment": "2000000",
                        "capital_commitment_upfront_drawdown": "2000000",
                        "onboarding_fee": "25000",
                        "management_fee": "5000",
                        "placement_fee": "6000",
                        "total_fee": "36000",
                        "correspondence_address": "Whitefield,Bengaluru",
                        "email_address": "hello@gmail.com",
                        "phone_number": "8147357822",
                        "net_worth": "24004500"
                        
                    },
                    "witness": {
                       
                    }
                },
                "fund_details": {
                    "fund_name": "LV",
                    "addressee": "MG Road Benagluru",
                    "fund_address": "S building M G Road",
                    "fund_email": "hi1234@gmail.com",
                    "notifier_email": "sdhvndnv@gmail.com",
                    "fund_manager_name": "ManagerName",
                    "fund_manager_address": "ManagerAddress",
                    "portfolio_entity_name": "ENTITY99"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "12/June/2022",
                        "day": "12",
                        "month": "June",
                        "year": "2022"
                    },
                    "agreement_id": "10"
                }
            }
    })
#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452


  #Verify the response after giving doctype as "partnership" and by removing "fund_details": fund_name, addressee, fund_address, fund_email, notifier_email, fund_manager_name, fund_manager_address, portfolio_entity_name but keep remaining values correct. Response status should be 452
def tests_cadoc177():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
         "doctype": "partnership",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        "name":"milestone"
                        
                    },
                    "investment_manager": {
                        "name": "LetsVenture",
                        "address": "MG Road Bengaluru"
                    },
                    "contributor": {
                        "name": "Kiran",
                        "capital_commitment": "2000000",
                        "capital_commitment_upfront_drawdown": "2000000",
                        "onboarding_fee": "25000",
                        "management_fee": "5000",
                        "placement_fee": "6000",
                        "total_fee": "36000",
                        "correspondence_address": "Whitefield,Bengaluru",
                        "email_address": "hello@gmail.com",
                        "phone_number": "8147357822",
                        "net_worth": "24004500"
                        
                    },
                    "witness": {
                        "name": "",
                        "title": ""
                    }
                },
                "fund_details": {
                    
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "12/June/2022",
                        "day": "12",
                        "month": "June",
                        "year": "2022"
                    },
                    "agreement_id": "10"
                }
            }
    })

#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

  #Verify the response after giving doctype as "partnership" and by removing "agreement_details": "agreement_date" : date, day, month, year but keep remaining values correct. Response status should be 452
def tests_cadoc178():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
         "doctype": "partnership",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        "name":"milestone"
                        
                    },
                    "investment_manager": {
                        "name": "LetsVenture",
                        "address": "MG Road Bengaluru"
                    },
                    "contributor": {
                        "name": "Kiran",
                        "capital_commitment": "2000000",
                        "capital_commitment_upfront_drawdown": "2000000",
                        "onboarding_fee": "25000",
                        "management_fee": "5000",
                        "placement_fee": "6000",
                        "total_fee": "36000",
                        "correspondence_address": "Whitefield,Bengaluru",
                        "email_address": "hello@gmail.com",
                        "phone_number": "8147357822",
                        "net_worth": "24004500"
                        
                    },
                    "witness": {
                        "name": "",
                        "title": ""
                    }
                },
                "fund_details": {
                     "fund_name": "LV",
                    "addressee": "MG Road Benagluru",
                    "fund_address": "S building M G Road",
                    "fund_email": "hi1234@gmail.com",
                    "notifier_email": "sdhvndnv@gmail.com",
                    "fund_manager_name": "ManagerName",
                    "fund_manager_address": "ManagerAddress",
                    "portfolio_entity_name": "ENTITY99"
                },
                
                "agreement_details": {
                    "agreement_date": {
                        "date": "12/June/2022",
                        "day": "12",
                        "month": "June",
                        "year": "2022"
                    },
                    "agreement_id": "10"
                }
            }
    })

#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452




########################################################## Continuation of Individual ###################################################################

#Verify the response after giving doctype as "individual" and by removing "trustee" name and address but keep remaining values correct. Response status should be 452
def tests_cadoc180():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
         "doctype": "individual",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        
                        
                    },
                    "investment_manager": {
                        "name": "LetsVenture",
                        "address": "MG Road Bengaluru"
                    },
                    "contributor": {
                        "name": "Kiran",
                        "capital_commitment": "2000000",
                        "capital_commitment_upfront_drawdown": "2000000",
                        "onboarding_fee": "25000",
                        "management_fee": "5000",
                        "placement_fee": "6000",
                        "total_fee": "36000",
                        "correspondence_address": "Whitefield,Bengaluru",
                        "email_address": "hello@gmail.com",
                        "phone_number": "8147357822",
                        "net_worth": "24004500"
                        
                    },
                    "witness": {
                        "name": "",
                        "title": ""
                    }
                },
                "fund_details": {
                     "fund_name": "LV",
                    "addressee": "MG Road Benagluru",
                    "fund_address": "S building M G Road",
                    "fund_email": "hi1234@gmail.com",
                    "notifier_email": "sdhvndnv@gmail.com",
                    "fund_manager_name": "ManagerName",
                    "fund_manager_address": "ManagerAddress",
                    "portfolio_entity_name": "ENTITY99"
                },
                
                "agreement_details": {
                    "agreement_date": {
                        "date": "12/June/2022",
                        "day": "12",
                        "month": "June",
                        "year": "2022"
                    },
                    "agreement_id": "10"
                }
            }
    })

#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

  
  
   #Verify the response after giving doctype as "individual" and by removing "investment_manager": name and address but keep remaining values correct. Response status should be 452
def tests_cadoc181():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
         "doctype": "individual",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        
                        "name":"milestone"
                    },
                    "investment_manager": {
                        
                    },
                    "contributor": {
                        "name": "Kiran",
                        "capital_commitment": "2000000",
                        "capital_commitment_upfront_drawdown": "2000000",
                        "onboarding_fee": "25000",
                        "management_fee": "5000",
                        "placement_fee": "6000",
                        "total_fee": "36000",
                        "correspondence_address": "Whitefield,Bengaluru",
                        "email_address": "hello@gmail.com",
                        "phone_number": "8147357822",
                        "net_worth": "24004500"
                        
                    },
                    "witness": {
                        "name": "",
                        "title": ""
                    }
                },
                "fund_details": {
                     "fund_name": "LV",
                    "addressee": "MG Road Benagluru",
                    "fund_address": "S building M G Road",
                    "fund_email": "hi1234@gmail.com",
                    "notifier_email": "sdhvndnv@gmail.com",
                    "fund_manager_name": "ManagerName",
                    "fund_manager_address": "ManagerAddress",
                    "portfolio_entity_name": "ENTITY99"
                },
                
                "agreement_details": {
                    "agreement_date": {
                        "date": "12/June/2022",
                        "day": "12",
                        "month": "June",
                        "year": "2022"
                    },
                    "agreement_id": "10"
                }
            }
    })

#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452


#Verify the response after giving doctype as "individual" and by removing "contributor": name, capital_commitment, capital_commitment_upfront_drawdown, onboarding_fee, transaction_fee, management_fee, placement_fee, total_fee, correspondence_address, email_address, phone_number, net_worth but keep remaining values correct. Response status should be 452
def tests_cadoc182():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
         "doctype": "individual",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        "name":"milestone"
                        
                    },
                    "investment_manager": {
                        "name": "LetsVenture",
                        "address": "MG Road Bengaluru"
                    },
                    "contributor": {
                        
                        
                    },
                    "witness": {
                        "name": "",
                        "title": ""
                    }
                },
                "fund_details": {
                    "fund_name": "LV",
                    "addressee": "MG Road Benagluru",
                    "fund_address": "S building M G Road",
                    "fund_email": "hi1234@gmail.com",
                    "notifier_email": "sdhvndnv@gmail.com",
                    "fund_manager_name": "ManagerName",
                    "fund_manager_address": "ManagerAddress",
                    "portfolio_entity_name": "ENTITY99"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "12/June/2022",
                        "day": "12",
                        "month": "June",
                        "year": "2022"
                    },
                    "agreement_id": "10"
                }
            }
    })

#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

  #Verify the response after giving doctype as "individual" and by removing "witness": name and title but keep remaining values correct. Response status should be 452
def tests_cadoc183():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
         "doctype": "individual",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        "name":"milestone"
                        
                    },
                    "investment_manager": {
                        "name": "LetsVenture",
                        "address": "MG Road Bengaluru"
                    },
                    "contributor": {
                        "name": "Kiran",
                        "capital_commitment": "2000000",
                        "capital_commitment_upfront_drawdown": "2000000",
                        "onboarding_fee": "25000",
                        "management_fee": "5000",
                        "placement_fee": "6000",
                        "total_fee": "36000",
                        "correspondence_address": "Whitefield,Bengaluru",
                        "email_address": "hello@gmail.com",
                        "phone_number": "8147357822",
                        "net_worth": "24004500"
                        
                        
                    },
                    "witness": {
                       
                    }
                },
                "fund_details": {
                    "fund_name": "LV",
                    "addressee": "MG Road Benagluru",
                    "fund_address": "S building M G Road",
                    "fund_email": "hi1234@gmail.com",
                    "notifier_email": "sdhvndnv@gmail.com",
                    "fund_manager_name": "ManagerName",
                    "fund_manager_address": "ManagerAddress",
                    "portfolio_entity_name": "ENTITY99"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "12/June/2022",
                        "day": "12",
                        "month": "June",
                        "year": "2022"
                    },
                    "agreement_id": "10"
                }
            }
    })

#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

  
   #Verify the response after giving doctype as "individual" and by removing "fund_details": fund_name, addressee, fund_address, fund_email, notifier_email, fund_manager_name, fund_manager_address, portfolio_entity_name but keep remaining values correct. Response status should be 452
def tests_cadoc184():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
         "doctype": "individual",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        "name":"milestone"
                        
                    },
                    "investment_manager": {
                        "name": "LetsVenture",
                        "address": "MG Road Bengaluru"
                    },
                    "contributor": {
                        "name": "Kiran",
                        "capital_commitment": "2000000",
                        "capital_commitment_upfront_drawdown": "2000000",
                        "onboarding_fee": "25000",
                        "management_fee": "5000",
                        "placement_fee": "6000",
                        "total_fee": "36000",
                        "correspondence_address": "Whitefield,Bengaluru",
                        "email_address": "hello@gmail.com",
                        "phone_number": "8147357822",
                        "net_worth": "24004500"
                        
                        
                    },
                    "witness": {
                        "name": "",
                        "title": ""
                    }
                },
                "fund_details": {
                    
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "12/June/2022",
                        "day": "12",
                        "month": "June",
                        "year": "2022"
                    },
                    "agreement_id": "10"
                }
            }
    })

#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

  
  #Verify the response after giving doctype as "individual" and by removing "agreement_details": "agreement_date" : date, day, month, year but keep remaining values correct. Response status should be 452
def tests_cadoc185():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
         "doctype": "individual",
        "doc_params":
            {
                "parties": {
                    "trustee": {
                        "name":"milestone"
                        
                    },
                    "investment_manager": {
                        "name": "LetsVenture",
                        "address": "MG Road Bengaluru"
                    },
                    "contributor": {
                        "name": "Kiran",
                        "capital_commitment": "2000000",
                        "capital_commitment_upfront_drawdown": "2000000",
                        "onboarding_fee": "25000",
                        "management_fee": "5000",
                        "placement_fee": "6000",
                        "total_fee": "36000",
                        "correspondence_address": "Whitefield,Bengaluru",
                        "email_address": "hello@gmail.com",
                        "phone_number": "8147357822",
                        "net_worth": "24004500"
                        
                    },
                    "witness": {
                        "name": "",
                        "title": ""
                    }
                },
                "fund_details": {
                    "fund_name": "LV",
                    "addressee": "MG Road Benagluru",
                    "fund_address": "S building M G Road",
                    "fund_email": "hi1234@gmail.com",
                    "notifier_email": "sdhvndnv@gmail.com",
                    "fund_manager_name": "ManagerName",
                    "fund_manager_address": "ManagerAddress",
                    "portfolio_entity_name": "ENTITY99"
                },
                "agreement_details": {
                    
                    "agreement_id": "10"
                }
            }
    })



#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452



####################################################################  Continuation of side_letter test cases  ###################################################################


#Verify the response after giving doctype as "side_letter" and by removing "first parties" from parties but keep remaining values correct. Response status should be 452
def tests_cadoc_187():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        
                    },
                    "second_party": {
                        "name": "Rajeev Ranjan",
                        "email": "rajeev.lv@grepdigital.com",
                        "phone": "8660970120",
                        "address": "London",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452  



#Verify the response after giving doctype as "side_letter" and by removing "second parties" from parties but keep remaining values correct. Response status should be 452
def tests_cadoc_188():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

  payload = json.dumps({
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Archimedha Mohapatra",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        
                    }
                }
            }
    })


#headers

  headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452
