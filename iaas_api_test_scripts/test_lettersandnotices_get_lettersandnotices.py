import pytest
import requests
import json
import cred
import unittest



#Verify the response after giving doctype as "drawdown-notice", template as "drawdown-notice.html" and valid "doc_params"
def test_lettersandnotices_get_lettersandnotices_1():

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
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200



#Verify the response after giving doctype as "", template as "drawdown-notice.html" and valid "doc_params"
def test_lettersandnotices_get_lettersandnotices_2():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/lettersandnotices_get_lettersandnotices/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "",
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
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving doctype as "drawdown-notice", template as "drawdown-notice.html" and in "doc_params" keep "notice_date" as " " and remaing parameters valid.
def test_lettersandnotices_get_lettersandnotices_3():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/lettersandnotices_get_lettersandnotices/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "drawdown-notice",
        "template": "drawdown-notice.html",
        "doc_params":
            {
                "notice_date": "",
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
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving doctype as "drawdown-notice", template as "drawdown-notice.html" and in "doc_params" keep "trustee_name" as " " and remaing parameters valid.
def test_lettersandnotices_get_lettersandnotices_4():

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
                "trustee_name": "",
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
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "drawdown-notice", template as "drawdown-notice.html" and in "doc_params" keep "investment_manager_name" as " " and remaing parameters valid.
def test_lettersandnotices_get_lettersandnotices_5():

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
                "investment_manager_name": "",
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
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving doctype as "drawdown-notice", template as "drawdown-notice.html" and in "doc_params" keep "payment_amount" as " " and remaing parameters valid.
def test_lettersandnotices_get_lettersandnotices_6():

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
                "payment_amount": "",
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
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "drawdown-notice", template as "drawdown-notice.html" and in "doc_params" keep "investment_amount" as " " and remaing parameters valid.
def test_lettersandnotices_get_lettersandnotices_7():

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
                "investment_amount": "",
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
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "drawdown-notice", template as "drawdown-notice.html" and in "doc_params" keep "transaction_fee" as " " and remaing parameters valid.
def test_lettersandnotices_get_lettersandnotices_8():

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
                "transaction_fee": "",
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
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "drawdown-notice", template as "drawdown-notice.html" and in "doc_params" keep "onboarding_fee" as " " and remaing parameters valid.
def test_lettersandnotices_get_lettersandnotices_9():

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
                "onboarding_fee": "",
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
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving doctype as "drawdown-notice", template as "drawdown-notice.html" and in "doc_params" keep "total_to_transfer" as " " and remaing parameters valid.
def test_lettersandnotices_get_lettersandnotices_10():

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
                "total_to_transfer": "",
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
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "drawdown-notice", template as "drawdown-notice.html" and in "doc_params" keep "account_number" as " " and remaing parameters valid.
def test_lettersandnotices_get_lettersandnotices_11():

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
                "account_number": "",
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
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "drawdown-notice", template as "drawdown-notice.html" and in "doc_params" keep "beneficiary_name:" as " " and remaing parameters valid.
def test_lettersandnotices_get_lettersandnotices_12():

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
                "beneficiary_name:": "",
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
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200




#Verify the response after giving doctype as "drawdown-notice", template as "drawdown-notice.html" and in "doc_params" keep "ifsc" as " " and remaing parameters valid.
def test_lettersandnotices_get_lettersandnotices_13():

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
                "ifsc": "",
                "swift": "var-ICICINBBCTS",
                "branch": "var-Koramangala, Bangalore",
                "cheque_in_favor": "var-LV Angel Fund",
                "cheque_attention": "var-Sanjay Kumar Jha",
                "cheque_address": "var-5th Floor, IndiQube Penta, 2, Shanthala Nagar, Richmond Town, Bengaluru - 560025",
                "cheque_email": "var-sanjay@letsventure.com"
            }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving doctype as "drawdown-notice", template as "drawdown-notice.html" and in "doc_params" keep "swift" as " " and remaing parameters valid.
def test_lettersandnotices_get_lettersandnotices_14():

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
                "swift": "",
                "branch": "var-Koramangala, Bangalore",
                "cheque_in_favor": "var-LV Angel Fund",
                "cheque_attention": "var-Sanjay Kumar Jha",
                "cheque_address": "var-5th Floor, IndiQube Penta, 2, Shanthala Nagar, Richmond Town, Bengaluru - 560025",
                "cheque_email": "var-sanjay@letsventure.com"
            }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "drawdown-notice", template as "drawdown-notice.html" and in "doc_params" keep "branch" as " " and remaing parameters valid.
def test_lettersandnotices_get_lettersandnotices_15():

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
                "branch": "",
                "cheque_in_favor": "var-LV Angel Fund",
                "cheque_attention": "var-Sanjay Kumar Jha",
                "cheque_address": "var-5th Floor, IndiQube Penta, 2, Shanthala Nagar, Richmond Town, Bengaluru - 560025",
                "cheque_email": "var-sanjay@letsventure.com"
            }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200




#Verify the response after giving doctype as "drawdown-notice", template as "drawdown-notice.html" and in "doc_params" keep "cheque_in_favor" as " " and remaing parameters valid.
def test_lettersandnotices_get_lettersandnotices_16():

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
                "cheque_in_favor": "",
                "cheque_attention": "var-Sanjay Kumar Jha",
                "cheque_address": "var-5th Floor, IndiQube Penta, 2, Shanthala Nagar, Richmond Town, Bengaluru - 560025",
                "cheque_email": "var-sanjay@letsventure.com"
            }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "drawdown-notice", template as "drawdown-notice.html" and in "doc_params" keep "cheque_attention" as " " and remaing parameters valid.
def test_lettersandnotices_get_lettersandnotices_17():

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
                "cheque_attention": "",
                "cheque_address": "var-5th Floor, IndiQube Penta, 2, Shanthala Nagar, Richmond Town, Bengaluru - 560025",
                "cheque_email": "var-sanjay@letsventure.com"
            }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "drawdown-notice", template as "drawdown-notice.html" and in "doc_params" keep "cheque_address" as " " and remaing parameters valid.
def test_lettersandnotices_get_lettersandnotices_18():

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
                "cheque_address": "",
                "cheque_email": "var-sanjay@letsventure.com"
            }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "drawdown-notice", template as "drawdown-notice.html" and in "doc_params" keep "cheque_email" as " " and remaing parameters valid.
def test_lettersandnotices_get_lettersandnotices_19():

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
                "cheque_email": ""
            }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving doctype as "drawdown-notice", template as "drawdown-notice.html" and in "doc_params" give invalid "ifsc"
def test_lettersandnotices_get_lettersandnotices_20():

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
                "ifsc": "",
                "swift": "var-ICICINBBCTS",
                "branch": "var-Koramangala, Bangalore",
                "cheque_in_favor": "var-LV Angel Fund",
                "cheque_attention": "var-Sanjay Kumar Jha",
                "cheque_address": "var-5th Floor, IndiQube Penta, 2, Shanthala Nagar, Richmond Town, Bengaluru - 560025",
                "cheque_email": "var-sanjay@letsventure.com"
            }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving doctype as "drawdown-notice", template as "drawdown-notice.html" and in "doc_params" give invalid "account_number
def test_lettersandnotices_get_lettersandnotices_21():

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
                "account_number": "",
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
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after giving doctype as "drawdown-notice", template as "drawdown-notice.html" and in "doc_params" give invalid "swift""
def test_lettersandnotices_get_lettersandnotices_22():

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
                "swift": "",
                "branch": "var-Koramangala, Bangalore",
                "cheque_in_favor": "var-LV Angel Fund",
                "cheque_attention": "var-Sanjay Kumar Jha",
                "cheque_address": "var-5th Floor, IndiQube Penta, 2, Shanthala Nagar, Richmond Town, Bengaluru - 560025",
                "cheque_email": "var-sanjay@letsventure.com"
            }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving doctype as "consent-letter", template as "consent-letter.html" and valid "doc_params"  
def test_lettersandnotices_get_lettersandnotices_23():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/lettersandnotices_get_lettersandnotices/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "consent-letter",
        "template": "consent-letter.html",
        "doc_params":
            {
                "additional": "var-Additional",
"investment_scheme": "var-LV Angel Fund",
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
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200




#Verify the response after giving doctype as "" , template as  "consent-letter.html" and valid "doc_params"
def test_lettersandnotices_get_lettersandnotices_24():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/lettersandnotices_get_lettersandnotices/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "",
        "template": "consent-letter.html",
        "doc_params":
            {
                "additional": "var-Additional",
"investment_scheme": "var-LV Angel Fund",
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
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving doctype as "consent-letter" , template as  "consent-letter.html" and in "doc_params" keep "additional" as ""
def test_lettersandnotices_get_lettersandnotices_25():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/lettersandnotices_get_lettersandnotices/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "consent-letter",
        "template": "consent-letter.html",
        "doc_params":
            {
                "additional": "",
"investment_scheme": "var-LV Angel Fund",
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
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "consent-letter" , template as  "consent-letter.html" and in "doc_params" keep "additional" as "investment_scheme"
def test_lettersandnotices_get_lettersandnotices_26():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/lettersandnotices_get_lettersandnotices/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "consent-letter",
        "template": "consent-letter.html",
        "doc_params":
            {
                "additional": "investment_scheme",
"investment_scheme": "var-LV Angel Fund",
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
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200



