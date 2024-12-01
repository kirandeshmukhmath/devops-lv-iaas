import pytest
import requests
import json
import cred
import unittest


#Verify the response after giving user_consent value as 'Y', valid pan_number, valid name, valid dob
 
def test_pan_status_check_1():

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
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200


#Verify the response after giving user_consent value as 'Y', valid pan_number, valid name, invalid dob

def test_pan_status_check_2():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_status_check/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N",
  "name": "Kiran",
  "dob": "11/20/1998"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200


#Verify the response after giving user_consent value as 'Y', valid pan_number, invalid name, valid dob

def test_pan_status_check_3():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_status_check/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N",
  "name": 12345,
  "dob": "01/11/1998"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after giving user_consent value as 'Y', invalid pan_number, valid name, valid dob

def test_pan_status_check_4():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_status_check/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732",
  "name": "Kiran",
  "dob": "11/01/1998"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving user_consent value as 'Y', invalid pan_number, invalid name,invalid dob

def test_pan_status_check_5():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_status_check/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732",
  "name": "DYWPK2732",
  "dob": "11/21/1998"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after giving user_consent value as 'N', valid pan_number, valid name, valid dob

def test_pan_status_check_6():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_status_check/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "pan_number": "DYWPK2732N",
  "name": "Kiran",
  "dob": "11/01/1998"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200



#Verify the response after giving user_consent value as 'N', valid pan_number, valid name, invalid dob

def test_pan_status_check_7():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_status_check/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "pan_number": "DYWPK2732N",
  "name": "Kiran",
  "dob": "31/31/2050"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving user_consent value as 'N', valid pan_number, invalid name, valid dob

def test_pan_status_check_8():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_status_check/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "pan_number": "DYWPK2732N",
  "name": 11222222,
  "dob": "01/11/1998"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving user_consent value as 'N', invalid pan_number, valid name, valid dob

def test_pan_status_check_9():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_status_check/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "pan_number": "DYWPNDNDKSNDNDNND",
  "name": "Kiran",
  "dob": "11/01/1998"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving user_consent value as 'N', invalid pan_number, invalid name,invalid dob

def test_pan_status_check_10():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_status_check/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "pan_number": "DYWPKJDNJBSDJSBDJ",
  "name": "1111111111111111111111",
  "dob": "11/31/2050"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving user_consent value as 'Y', valid pan_number, valid name, dob as 'mm/dd/yyyy'
def tests_panstatus11():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_status_check/"

  payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "BQIPV9280L",
  "name": "Annvin Vincent",
  "dob": "01/31/1997"
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

  #Verify the response after giving user_consent value as 'Y', valid pan_number, valid name, dob as 'mm-dd-yyyy'
def tests_panstatus12():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_status_check/"

  payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "BQIPV9280L",
  "name": "Annvin Vincent",
  "dob": "01-31-1997"
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

  #Verify the response after giving user_consent value as 'Y', valid pan_number, valid name, dob as 'mm/yyyy'
def tests_panstatus13():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_status_check/"

  payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "BQIPV9280L",
  "name": "Annvin Vincent",
  "dob": "01/1997"
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

  #Verify the response after giving user_consent value as 'Y', valid pan_number, valid name, dob as 'mm/yyy'
def tests_panstatus14():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_status_check/"

  payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "BQIPV9280L",
  "name": "Annvin Vincent",
  "dob": "01/199"
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

  #Verify the response after giving user_consent value as 'Y', valid pan_number, valid name, dob as 'dd/mm/yyyy'
def tests_panstatus15():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_status_check/"

  payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "BQIPV9280L",
  "name": "Annvin Vincent",
  "dob": "31/01/1997"
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


#Verify the response after giving user_consent value as " ", pan_number as " ", name as " ", dob as " ", Response status should be 452
def tests_panstatus16():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_status_check/"

  payload = json.dumps({
  "user_consent": "",
  "pan_number": "",
  "name": "",
  "dob": ""
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