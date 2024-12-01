import pytest
import requests
import json
import cred


#Verify the response after giving user_consent value as 'Y', valid ifsc, valid account_number.

def test_bank_account_verification_1():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "ifsc": "SBIN0040995",
  "account_number": "37433068886"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200

#Verify the response after giving user_consent value as 'Y', valid ifsc, invalid account_number.

def test_bank_account_verification_2():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "ifsc": "SBIN0040015",
  "account_number": "12"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving user_consent value as 'Y', invalid ifsc, valid account_number.

def test_bank_account_verification_3():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "ifsc": "SBIN",
  "account_number": "37480338886"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving user_consent value as 'N', valid ifsc, valid account_number.

def test_bank_account_verification_4():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "ifsc": "SBIN0033015",
  "account_number": "37480338886"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200


#Verify the response after giving user_consent value as 'N,'valid ifsc, invalid account_number.

def test_bank_account_verification_5():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "ifsc": "SBIN0330033",
  "account_number": "3733006888111111111111111111111111111111"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving user_consent value as 'N', invalid ifsc, valid account_number..

def test_bank_account_verification_6():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "ifsc": "SBIN",
  "account_number": "37433068886"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after keeping user_consent , ifsc, account_number values as ""

def test_bank_account_verification_7():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "",
  "ifsc": "",
  "account_number": ""
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after keeping user_consent value as ""  and giving valid ifsc, valid account_number

def test_bank_account_verification_8():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "",
  "ifsc": "SBIN0043315",
  "account_number": "33380068886"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after giving valid user_consent and valid account_number and keeping ifsc value as ""

def test_bank_account_verification_9():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "ifsc": "",
  "account_number": "37480033386"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after giving valid user_consent and valid ifsc and keeping account_number value as ""

def test_bank_account_verification_10():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "ifsc": "SBIN0040015",
  "account_number": ""
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452   



#Verify the response after keeping user_consent value as ""  and giving invalid ifsc, valid account_number.

def tests_bankver_11():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification/"

  payload = json.dumps({
  "user_consent": "",
  "ifsc": "SBIN00",
  "account_number": "54060381981"
  
})
#headers
  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
  response = requests.post(url,  data=payload, headers=headers)        
  response_data = response.json()
  status = response_data["Status"]
  assert status == 452




#Verify the response after keeping user_consent value as ""  and giving valid ifsc, invalid account_number
def tests_bankver_12():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification/"

  payload = json.dumps({
  "user_consent": "",
  "ifsc": "SB",
  "account_number": "540"
  
})
#headers
  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
  response = requests.post(url,  data=payload, headers=headers)        
  response_data = response.json()
  status = response_data["Status"]
  assert status == 452
