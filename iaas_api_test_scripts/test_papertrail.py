import http.client, urllib, time, os, httplib2, requests
from numpy import datetime64, datetime_as_string, datetime_data
import re
from urllib3 import request
import PyPDF2
import json
import cred
from datetime import datetime 
import base64
import requests 
#import request
import django
import ocr
import logging
from rest_framework.response import Response
logger_info = logging.getLogger('info_logs')
logger_error = logging.getLogger('error_logs')



#Verify if the service_request_id of ca_doc with doc_type "corporate" request is reflecting in papertrail log.
def test_papertrail_2():
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

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
    response_status = response_data["Status"]
    print(response_status)

    status = response_data["Payload"]["additional_info"]["coordinates"]["Message"]
    print(status)
    selected_status = status.split(" ")[13]
#service request ID will be printed
    print(selected_status)
    time.sleep(5)
# Fetching data from papertrail
                           
    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if selected_status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'



#Verify if the service_request_id of ca_doc with doc_type  "huf" request is reflecting in papertrail log.
def test_papertrail_3():
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

    payload = json.dumps(
{
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
    response_status = response_data["Status"]
    print(response_status)

    status = response_data["Payload"]["additional_info"]["coordinates"]["Message"]
    print(status)
    selected_status = status.split(" ")[13]
#service request ID will be printed
    print(selected_status)
    time.sleep(5)
# Fetching data from papertrail
                           
    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if selected_status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'


        
#Verify if the service_request_id of ca_doc with doc_type  "joint" request is reflecting in papertrail log.

def test_papertrail_4():
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

    payload = json.dumps(
{
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
    response_status = response_data["Status"]
    print(response_status)

    status = response_data["Payload"]["additional_info"]["coordinates"]["Message"]
    print(status)
    selected_status = status.split(" ")[13]
#service request ID will be printed
    print(selected_status)
    time.sleep(5)
# Fetching data from papertrail
                           
    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if selected_status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'




#Verify if the service_request_id of ca_doc with doc_type  "side_letter" request is reflecting in papertrail log.
def test_papertrail_5():
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

    payload = json.dumps(
{
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
    response_status = response_data["Status"]
    print(response_status)

    status = response_data["Payload"]["additional_info"]["coordinates"]["Message"]
    print(status)
    selected_status = status.split(" ")[13]
#service request ID will be printed
    print(selected_status)
    time.sleep(5)
# Fetching data from papertrail
                           
    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if selected_status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'




#Verify if the service_request_id of ca_doc with doc_type  "individual" request is reflecting in papertrail log.
def test_papertrail_6():
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

    payload = json.dumps(
{
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
    response_status = response_data["Status"]
    print(response_status)

    status = response_data["Payload"]["additional_info"]["coordinates"]["Message"]
    print(status)
    selected_status = status.split(" ")[13]
#service request ID will be printed
    print(selected_status)
    time.sleep(5)
# Fetching data from papertrail
                           
    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if selected_status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'





#Verify if the service_request_id of ca_doc with doc_type  "partnership" request is reflecting in papertrail log.
def test_papertrail_7():
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

    payload = json.dumps(
{
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
    response_status = response_data["Status"]
    print(response_status)

    status = response_data["Payload"]["additional_info"]["coordinates"]["Message"]
    print(status)
    selected_status = status.split(" ")[13]
#service request ID will be printed
    print(selected_status)
    time.sleep(5)
# Fetching data from papertrail
                           
    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if selected_status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'


#Verify if the service_request_id of scheme_doc with doc_type  "invester_scheme" request is reflecting in papertrail log.
def test_papertrail_9():
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"

    payload = json.dumps(
{
        "doctype": "investor-scheme",
        "template": "investor-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Status"]
    print(response_status)

    status = response_data["Message"]
    print(status)
    selected_status = status.split(" ")[8]
#service request ID will be printed
    print(selected_status)
    time.sleep(5)
# Fetching data from papertrail
                           
    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if selected_status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'





#Verify if the service_request_id of scheme_doc with doc_type  "lead_scheme" request is reflecting in papertrail log.
def test_papertrail_10():
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"

    payload = json.dumps(
{
        "doctype": "lead-scheme",
        "template": "lead-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Status"]
    print(response_status)

    status = response_data["Message"]
    print(status)
    selected_status = status.split(" ")[8]
#service request ID will be printed
    print(selected_status)
    time.sleep(5)
# Fetching data from papertrail
                           
    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if selected_status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'




# Verify if the service_request_id of 'fetch_e_agreement_details' request is reflecting in papertrail log.
def test_papertrail_12():
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

    payload = json.dumps(
    {
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Kiran",
                        "email": "kirandeshmukh.lv@grepdigital.com",
                        "phone": "8147357822",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Annvin",
                        "email": "annvin.lv@grepdigital.com",
                        "phone": "0000000000",
                        "address": "Bangalore",
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
    response_status = response_data["Status"]
#assert response_status == 200

    Base64File = response_data["Payload"]["file"]
    Payload1 = response_data["Payload"]["additional_info"]["coordinates"]["Payload"]

    #visit initial_e_aggrement link
    url1 = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/initiate_e_agreement/"

    payload = json.dumps(
{
  "file": {
    "file": Base64File,
    "name": "Test-Demo"
  },
  "invitees": Payload1
})

    headers1 = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response1 = requests.post(url1,  data=payload, headers=headers1)
    response_data1 = response1.json()
    response_status1 = response_data1["Status"]
    response_documentID = response_data1["Payload"]["data"]["documentId"]
    response_message = response_data1["Message"]
    #assert response_status1 == 200
    print(response_documentID)


#visit fetch_e_aggrement_details url
    url2 = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_e_agreement_details/"

    payload = json.dumps(
{
  "documentId": response_documentID
})

    headers2 = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response2 = requests.post(url2,  data=payload, headers=headers2)
    response_data2 = response2.json()
    response_status2 = response_data2["Status"]
    response_message2 = response_data2['Request_details']['service_request_id']
    response_document2 = response_data2["Payload"]["data"]["documentId"]
    assert response_status2 == 200
    print(response_message2)
#print(response_document2)
    status = response_data2['Request_details']['service_request_id']
    print(status)
    selected_status = status
#service request ID will be printed
    print(selected_status)
    time.sleep(5)

    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if selected_status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'



# Verify if the service_request_id of 'fetch_termsheets' request is reflecting in papertrail log.
def test_papertrail_13():
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"

    payload = json.dumps(
{
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Status"]
    print(response_status)

    status = response_data["Message"]
    print(status)
    selected_status = status.split(" ")[8]
#service request ID will be printed
    print(selected_status)
    time.sleep(5)
# Fetching data from papertrail
                           
    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if selected_status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'




# Verify if the service_request_id of 'initiate_e_agreement' request is reflecting in papertrail log.
def test_papertrail_14():
    #API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

    payload = json.dumps(
    {
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Kiran",
                        "email": "kirandeshmukh.lv@grepdigital.com",
                        "phone": "8147357822",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Annvin",
                        "email": "annvin.lv@grepdigital.com",
                        "phone": "0000000000",
                        "address": "Bangalore",
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
    response_status = response_data["Status"]
    assert response_status == 200

    Base64File = response_data["Payload"]["file"]
    Payload1 = response_data["Payload"]["additional_info"]["coordinates"]["Payload"]

    #visit initial_e_aggrement link
    url1 = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/initiate_e_agreement/"

    payload = json.dumps(
{
  "file": {
    "file": Base64File,
    "name": "Test-Demo"
  },
  "invitees": Payload1
})

    headers1 = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response1 = requests.post(url1,  data=payload, headers=headers1)
    response_data1 = response1.json()
    response_status1 = response_data1["Status"]
    response_payload = response_data1["Payload"]
    status = response_data1["Request_details"]["service_request_id"]

    #status = response_data["Request_details"]["service_request_id"]
    print(status)
    time.sleep(5)
    #selected_status = status.split(" ")[13]
#service request ID will be printed
    #print(selected_status)

# Fetching data from papertrail
                           
    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'






#  Verify if the service_request_id of 'kyckra_bank_account_verification' request is reflecting in papertrail log.
def test_papertrail_15():
    #API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification/"
#Read Input Json file
    payload = json.dumps({
  "user_consent": "Y",
  "ifsc": "SBIN0040015",
  "account_number": "37480068886"
})


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Status"]
    print(response_status)

    status = response_data["Request_details"]["service_request_id"]
    print(status)
    time.sleep(5)
    #selected_status = status.split(" ")[13]
#service request ID will be printed
    #print(selected_status)

# Fetching data from papertrail
                           
    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'



# Verify if the service_request_id of 'kyckra_bank_account_verification_advanced' request is reflecting in papertrail log.
def test_papertrail_16():
    #API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification_advanced/"
#Read Input Json file
    payload = json.dumps({
  "user_consent": "Y",
  "ifsc": "SBIN0040015",
  "account_number": "37480068886",
  "account_holder_name": "Kiran",
  "name_match_type": "individual"
})


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Status"]
    print(response_status)

    status = response_data["Request_details"]["service_request_id"]
    print(status)
    time.sleep(5)
    #selected_status = status.split(" ")[13]
#service request ID will be printed
    #print(selected_status)

# Fetching data from papertrail
                           
    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'



# Verify if the service_request_id of 'kyckra_ckyc_download' request is reflecting in papertrail log.
def test_papertrail_17():
    #API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_download/"

    payload = json.dumps({
  "user_consent": "Y",
  "ckyc_id":"12345678912345"
})


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Status"]
    print(response_status)

    status = response_data["Request_details"]["service_request_id"]
    print(status)
    selected_status = status
#service request ID will be printed
    print(selected_status)
    time.sleep(5)

    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if selected_status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'





# Verify if the service_request_id of 'kyckra_ckyc_search' request is reflecting in papertrail log.
def test_papertrail_18():
    #API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_search/"
#Read Input Json file
    payload = json.dumps({
  "user_consent": "Y",
  "id_type": "PAN",
  "id_value": "DWYPK2732N"
})


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Request_details"]["service_request_id"]
    print(response_status)

    status = response_data["Request_details"]["service_request_id"]
    print(status)
    selected_status = status
#service request ID will be printed
    print(selected_status)
    time.sleep(5)

    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if selected_status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'





# Verify if the service_request_id of 'kyckra_entity_gst_authentication' request is reflecting in papertrail log.
def test_papertrail_19():
    #API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_gst_authentication/"
#Read Input Json file
    payload = json.dumps({
  "user_consent": "Y",
  "gstin": "29GGGGG1314R9Z6"
})


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Request_details"]["service_request_id"]
    print(response_status)
    status = response_data["Request_details"]["service_request_id"]
    print(status)
    selected_status = status
#service request ID will be printed
    print(selected_status)
    time.sleep(5)

    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if selected_status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'





#  Verify if the service_request_id of 'kyckra_entity_gst_search_basis_pan' request is reflecting in papertrail log.
def test_papertrail_20():
    #API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_gst_search_basis_pan/"
#Read Input Json file
    payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N"
})


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Request_details"]["service_request_id"]
    print(response_status)
    status = response_data["Request_details"]["service_request_id"]
    print(status)
    selected_status = status
#service request ID will be printed
    print(selected_status)
    time.sleep(5)

    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if selected_status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'




# Verify if the service_request_id of 'kyckra_entity_pan_profile' request is reflecting in papertrail log.
def test_papertrail_21():
    #API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_pan_profile/"
#Read Input Json file
    payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N",
  "month_year_of_birth": "01-1998",
  "case_id": 1
})


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Request_details"]["service_request_id"]
    print(response_status)

    status = response_data["Request_details"]["service_request_id"]
    print(status)
    selected_status = status
#service request ID will be printed
    print(selected_status)
    time.sleep(5)

    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if selected_status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'




# Verify if the service_request_id of 'kyckra_kyc_ocr' request is reflecting in papertrail log.
def test_papertrail_22():
    #API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_kyc_ocr/"

    payload = json.dumps({
  "file_B64": ocr.ocrimg
  })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    #response_status = response_data["Request_details"]["service_request_id"]
    #print(response_status)
    status = response_data["Request_details"]["service_request_id"]
    print(status)
    selected_status = status
#service request ID will be printed
    print(selected_status)
    time.sleep(5)

    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if selected_status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'



# Verify if the service_request_id of 'kyckra_pan_authentication' request is reflecting in papertrail log.
def test_papertrail_23():
    #API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_authentication/"
#Read Input Json file
    payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N"
})


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Request_details"]["service_request_id"]
    print(response_status)
    status = response_data["Request_details"]["service_request_id"]
    print(status)
    selected_status = status
#service request ID will be printed
    print(selected_status)
    time.sleep(5)

    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if selected_status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'





# Verify if the service_request_id of 'kyckra_pan_status_check' request is reflecting in papertrail log.
def test_papertrail_24():
    #API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_status_check/"
#Read Input Json file
    payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N",
  "name": "Kiran",
  "dob": "11/01/1998"
})


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Request_details"]["service_request_id"]
    print(response_status)

    status = response_data["Request_details"]["service_request_id"]
    print(status)
    selected_status = status
#service request ID will be printed
    print(selected_status)
    time.sleep(5)

    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if selected_status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'





# Verify if the service_request_id of 'kyckra_pan_authentication_advanced' request is reflecting in papertrail log.
def test_papertrail_25():
    #API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_authentication_advanced/"

    payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N",
  "name": "Kiran",
  "fathers_name": "Deshmukhmath",
  "husband_name": "Kiran",
  "dob": "01/07/1971",
  "ocr_image_url": "https://base64.guru/converter/decode/pdf",
  "face_image_url": "https://base64.guru/converter/decode/pdf",
  "ocr_image_B64": ocr.ocrimg,
  "face_image_B64": ocr.faceimg,
  "addresses": [
   "Bengaluru"
  ],
  "notification": {
    "webhook": "name",
    "emails": [
      "annvinvincent@gmail.com"
    ],
    "webhook_config": {
      "url": "https://base64.guru/converter/encode/image/jpg"
    }
  }
})


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    #response_status = response_data["Request_details"]["service_request_id"]
    #print(response_status)
    status = response_data["Request_details"]["service_request_id"]
    print(status)
    selected_status = status
#service request ID will be printed
    print(selected_status)
    time.sleep(5)

    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if selected_status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'




# Verify if the service_request_id of 'lettersandnotices_get_lettersandnotices' request is reflecting in papertrail log.
def test_papertrail_26():
    #API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/lettersandnotices_get_lettersandnotices/"
#Read Input Json file
    payload = json.dumps({
        "doctype": "drawdown-notice",
        "template": "drawdown-notice.html",
        "doc_params":
            {
                "notice_date": "var-2022-06-23",
                "addressee": "var-Archimedha Mohapatra",
                "trustee_name": "var-Milestone Trusteeship Services Private Limited",
                "investment_manager_name": "var- Lets Venture Advisors LLP",
                "payment_amount": "var-12100",
                "investment_amount": "var-1000",
                "transaction_fee": "var-2100",
                "onboarding_fee": "var-200",
                "total_to_transfer": "var-12100",
                "account_number": "var-166705000236 ",
                "beneficiary_name:": "var-LV Angel Fund",
                "ifsc": "var-ICIC0001667",
                "swift": "var-ICICINBBCTS",
                "branch": "var-Koramangala, Bangalore",
                "cheque_in_favor": "var-LV Angel Fund",
                "cheque_attention": "var-Sanjay Kumar Jha",
                "cheque_address": "var-5th Floor, IndiQube Penta, 2, Shanthala Nagar, Richmond Town, Bengaluru - 560025",
                "cheque_email": "var-sanjay@letsventure.com"
            }
    })


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Status"]
    print(response_status)

    status = response_data["Message"]
    print(status)
    selected_status = status.split(" ")[8]
#service request ID will be printed
    print(selected_status)

    time.sleep(5)

    logger_info.info("get_papertrail_logs Post function called")
    conn = http.client.HTTPSConnection(host='papertrailapp.com')
    papertrail_base_url = '/api/v1/events/search.json'
    conn.request(
            method='GET',
            url='/api/v1/events/search.json',
            headers={'X-Papertrail-Token': 'Hh9In2SxaPytEDHivXg'})
    response = conn.getresponse()
    output_json = json.loads(response.read())
    output = output_json['events']
    length = len(output)
#Total length of the papertrail data will be printed (i.e, 1000)
    print(length)
#Since the total length of the data is 1000 and in python indexing starts from 0 so for finding last recored data using 1000 - 1 = 999
    o = output[length - 1]
    filter = o['message']
    print(filter)
    if selected_status in filter:
        print("ID Found")
        a = 'ID Found'
    else:
        print("ID not found")
        a = 'ID not Found'

    assert a == 'ID Found'