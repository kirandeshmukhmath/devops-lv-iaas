import pytest
import requests
import json
import cred


#Verify the response after giving user_consent value as 'Y', valid ifsc, valid account_number, valid account_holder_name, name_match_type as individual.

def test_bank_account_verification_advanced_1():

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
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200


#Verify the response after giving user_consent value as 'Y', valid ifsc, valid account_number, valid account_holder_name, name_match_type as entity.

def test_bank_account_verification_advanced_2():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification_advanced/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "ifsc": "SBIN0040015",
  "account_number": "37480068886",
  "account_holder_name": "Kiran",
  "name_match_type": "entity"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200


#Verify the response after giving user_consent value as 'Y', invalid ifsc, valid account_number, valid account_holder_name, name_match_type as individual

def test_bank_account_verification_advanced_3():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification_advanced/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "ifsc": "SBIN",
  "account_number": "37480068886",
  "account_holder_name": "Kiran",
  "name_match_type": "individual"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after giving user_consent value as 'Y', invalid ifsc, valid account_number, valid account_holder_name, name_match_type as entity.

def test_bank_account_verification_advanced_4():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification_advanced/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "ifsc": "SBIN",
  "account_number": "37480068886",
  "account_holder_name": "Kiran",
  "name_match_type": "entity"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after giving user_consent value as 'Y', valid ifsc, invalid account_number, valid account_holder_name, name_match_type as individual.

def test_bank_account_verification_advanced_5():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification_advanced/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "ifsc": "SBIN0040015",
  "account_number": "372",
  "account_holder_name": "Kiran",
  "name_match_type": "individual"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after giving user_consent value as 'Y', valid ifsc, invalid account_number, valid account_holder_name, name_match_type as entity.
def test_bank_account_verification_advanced_6():
#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification_advanced/"
        payload = json.dumps({
  "user_consent": "Y",
  "account_number": "540",
  "ifsc": "SBIN0018240",
  "account_holder_name": "Annvin Vincent",
  "name_match_type": "entity"
})


#headers

        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

        response = requests.post(url,  data=payload, headers=headers)
        response_data = response.json()
#print(response_data)
        status = response_data["Status"]
#print(status)
        assert status == 452



#Verify the response after giving user_consent value as 'Y', valid ifsc, valid account_number, invalid account_holder_name, name_match_type as individual.

def test_bank_account_verification_advanced_7():

        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification_advanced/"

        payload = json.dumps({
  "user_consent": "Y",
  "account_number": "54060381981",
  "ifsc": "SBIN0018240",
  "account_holder_name": 123,
  "name_match_type": "individual"
})


#headers

        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

        response = requests.post(url,  data=payload, headers=headers)
        response_data = response.json()
#print(response_data)
        status = response_data["Status"]
#print(status)
        assert status == 452

#Verify the response after giving user_consent value as 'Y', valid ifsc, valid account_number, invalid account_holder_name, name_match_type as entity.

def test_bank_account_verification_advanced_8():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification_advanced/"

  payload = json.dumps({
  "user_consent": "Y",
  "account_number": "54060381981",
  "ifsc": "SBIN0018240",
  "account_holder_name": 123,
  "name_match_type": "entity"
})


#headers

  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

#Verify the response after giving user_consent value as 'Y',and ifsc, account_number, account_holder_name, name_match_type.as " ".

def test_bank_account_verification_advanced_9():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification_advanced/"

  payload = json.dumps({
  "user_consent": "Y",
  "account_number": "",
  "ifsc": "",
  "account_holder_name": "",
  "name_match_type": ""
})


#headers

  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

#Verify the response after giving user_consent value as 'N', valid ifsc, valid account_number, valid account_holder_name, name_match_type as individual.
def test_bank_account_verification_advanced_10():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification_advanced/"

  payload = json.dumps({
  "user_consent": "N",
  "account_number": "54060381981",
  "ifsc": "SBIN0018240",
  "account_holder_name": "Annvin Vincent",
  "name_match_type": "individual"
})


#headers

  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 200


#Verify the response after giving user_consent value as 'N', valid ifsc, valid account_number, valid account_holder_name, name_match_type as entity.
def test_bank_account_verification_advanced_11():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification_advanced/"

  payload = json.dumps({
  "user_consent": "N",
  "account_number": "54060381981",
  "ifsc": "SBIN0018240",
  "account_holder_name": "Annvin Vincent",
  "name_match_type": "entity"
})


#headers

  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 200

#Verify the response after giving user_consent value as 'N', invalid ifsc, valid account_number, valid account_holder_name, name_match_type as individual.
def test_bank_account_verification_advanced_12():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification_advanced/"

  payload = json.dumps({
  "user_consent": "N",
  "account_number": "54060381981",
  "ifsc": "SBI",
  "account_holder_name": "Annvin Vincent",
  "name_match_type": "individual"
})


#headers

  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

#Verify the response after giving user_consent value as 'N', invalid ifsc, valid account_number, valid account_holder_name, name_match_type as entity.
def test_bank_account_verification_advanced_13():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification_advanced/"

  payload = json.dumps({
  "user_consent": "N",
  "account_number": "54060381981",
  "ifsc": "SBI",
  "account_holder_name": "Annvin Vincent",
  "name_match_type": "entity"
})


#headers

  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

#Verify the response after giving user_consent value as 'N', valid ifsc, invalid account_number, valid account_holder_name, name_match_type as individual.
def test_bank_account_verification_advanced_14():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification_advanced/"

  payload = json.dumps({
  "user_consent": "N",
  "account_number": "540",
  "ifsc": "SBIN0018240",
  "account_holder_name": "Annvin Vincent",
  "name_match_type": "individual"
})


#headers

  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

#Verify the response after giving user_consent value as 'N', valid ifsc, invalid account_number, valid account_holder_name, name_match_type as entity.
def test_bank_account_verification_advanced_15():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification_advanced/"

  payload = json.dumps({
  "user_consent": "N",
  "account_number": "540",
  "ifsc": "SBIN0018240",
  "account_holder_name": "Annvin Vincent",
  "name_match_type": "entity"
})


#headers

  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

#Verify the response after giving user_consent value as 'N', valid ifsc, valid account_number, invalid account_holder_name, name_match_type as individual.
def test_bank_account_verification_advanced_16():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification_advanced/"

  payload = json.dumps({
  "user_consent": "N",
  "account_number": "54060381981",
  "ifsc": "SBIN0018240",
  "account_holder_name": 123,
  "name_match_type": "individual"
})


#headers

  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

#Verify the response after giving user_consent value as 'N', valid ifsc, valid account_number, invalid account_holder_name, name_match_type as entity.
def test_bank_account_verification_advanced_17():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification_advanced/"

  payload = json.dumps({
  "user_consent": "N",
  "account_number": "54060381981",
  "ifsc": "SBIN0018240",
  "account_holder_name": 123,
  "name_match_type": "entity"
})


#headers

  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

#Verify the response after giving user_consent value as 'N', valid ifsc, valid account_number, valid account_holder_name, name_match_type as individual.
def test_bank_account_verification_advanced_18():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification_advanced/"

  payload = json.dumps({
  "user_consent": "N",
  "account_number": "54060381981",
  "ifsc": "SBIN0018240",
  "account_holder_name": 123,
  "name_match_type": "entity"
})


#headers

  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

#Verify the response after giving user_consent value as 'N', valid ifsc, valid account_number, valid account_holder_name, name_match_type as individual.
def test_bank_account_verification_advanced_19():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification_advanced/"

  payload = json.dumps({
  "user_consent": "N",
  "account_number": "54060381981",
  "ifsc": "SBIN0018240",
  "account_holder_name": 123,
  "name_match_type": "entity"
})


#headers

  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

#Verify the response after giving user_consent value as 'N',and ifsc, account_number, account_holder_name, name_match_type.as " ".
def test_bank_account_verification_advanced_20():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification_advanced/"

  payload = json.dumps({
  "user_consent": "N",
  "account_number": "",
  "ifsc": "",
  "account_holder_name": "",
  "name_match_type": ""
})


#headers

  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452

#Verify the response after giving user_consent as "Y", valid ifsc, valid account_number, valid account_holder_name, name_match_type.as "ind ".
def test_bank_account_verification_advanced_21():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_bank_account_verification_advanced/"

  payload = json.dumps({
  "user_consent": "Y",
  "account_number": "54060381981",
  "ifsc": "SBIN0018240",
  "account_holder_name": "Annvin Vincent",
  "name_match_type": "ind"
})


#headers

  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
#print(response_data)
  status = response_data["Status"]
#print(status)
  assert status == 452