import pytest
import requests
import json
import cred
import unittest


#Verify the response after giving user_consent value as 'Y', valid pan_number, valid month_year_of_birth, valid case_id
def test_entity_pan_profile_1():

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
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200


#Verify the response after giving user_consent value as 'Y', invalid pan_number, valid month_year_of_birth, valid case_id

def test_entity_pan_profile_2():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_pan_profile/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732",
  "month_year_of_birth": "01-1998",
  "case_id": 1
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving user_consent value as 'Y', valid pan_number, invalid month_year_of_birth, valid case_id

def test_entity_pan_profile_3():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_pan_profile/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N",
  "month_year_of_birth": "21-1998",
  "case_id": 1
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving user_consent value as 'Y', valid pan_number, valid month_year_of_birth, invalid case_id

def test_entity_pan_profile_4():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_pan_profile/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N",
  "month_year_of_birth": "01-1998",
  "case_id": "A"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving user_consent value as 'Y', invalid pan_number, invalid month_year_of_birth, invalid case_id

def test_entity_pan_profile_5():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_pan_profile/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732",
  "month_year_of_birth": "21-1998",
  "case_id": "B"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving user_consent value as 'Y', pan_number, month_year_of_birth, case_id values as " "

def test_entity_pan_profile_6():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_pan_profile/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "",
  "month_year_of_birth": "",
  "case_id": ""
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after giving user_consent value as 'N', valid pan_number, valid month_year_of_birth, valid case_id

def test_entity_pan_profile_7():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_pan_profile/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "pan_number": "DYWPK2732N",
  "month_year_of_birth": "11-1998",
  "case_id": 6
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200


#Verify the response after giving user_consent value as 'N', invalid pan_number, valid month_year_of_birth, valid case_id

def test_entity_pan_profile_8():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_pan_profile/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "pan_number": "DY",
  "month_year_of_birth": "11-1998",
  "case_id": "2"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving user_consent value as 'N', valid pan_number, invalid month_year_of_birth, valid case_id


def test_entity_pan_profile_9():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_pan_profile/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "pan_number": "DYWPK2732N",
  "month_year_of_birth": "222-1998",
  "case_id": "2"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after giving user_consent value as 'N', valid pan_number, valid month_year_of_birth, invalid case_id

def test_entity_pan_profile_10():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_pan_profile/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "pan_number": "DYWPK2732N",
  "month_year_of_birth": "11-1998",
  "case_id": "@@@@@@@"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving user_consent value as 'N', invalid pan_number, invalid month_year_of_birth, invalid case_id
def test_entity_pan_profile_11():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_pan_profile/"
  payload = json.dumps({"user_consent": "N","pan_number": "BQIP","month_year_of_birth": "01-199","case_id": "abc"})
#headers
  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}#Make post request with json input body
  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
  status = response_data["Status"]
  assert status == 452 

#Verify the response after giving user_consent value as 'N', pan_number, month_year_of_birth, case_id values as " "
def test_entity_pan_profile_12():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_pan_profile/"
  payload = json.dumps({"user_consent": "N","pan_number": "","month_year_of_birth": "","case_id": ""})
#headers
  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}#Make post request with json input body
  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
  status = response_data["Status"]
  assert status == 452 

#Verify the response after giving user_consent , pan_number, month_year_of_birth, case_id values as " "
def test_entity_pan_profile_13():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_pan_profile/"
  payload = json.dumps({"user_consent": "","pan_number": "","month_year_of_birth": "","case_id": ""})
#headers
  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}#Make post request with json input body
  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
  status = response_data["Status"]
  assert status == 452 

#Verify the response after giving user_consent value as 'Y',valid  pan_number,  month_year_of_birth as 'mm-yyyy, valid case_id 
def test_entity_pan_profile_14():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_pan_profile/"
  payload = json.dumps({"user_consent": "Y","pan_number": "BQIPV9280L","month_year_of_birth": "01-1997","case_id": 1})
#headers
  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}#Make post request with json input body
  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
  status = response_data["Status"]
  assert status == 200 

#Verify the response after giving user_consent value as 'Y',valid  pan_number,  month_year_of_birth as 'mm/yyyy, valid case_id 
def test_entity_pan_profile_15():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_pan_profile/"
  payload = json.dumps({"user_consent": "Y","pan_number": "BQIPV9280L","month_year_of_birth": "01/1997","case_id": 1})
#headers
  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}#Make post request with json input body
  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
  status = response_data["Status"]
  assert status == 452

#Verify the response after giving user_consent value as 'Y', valid pan_number,  month_year_of_birth as 'dd-yyyy, valid case_id 
def test_entity_pan_profile_16():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_pan_profile/"
  payload = json.dumps({"user_consent": "Y","pan_number": "BQIPV9280L","month_year_of_birth": "21-1997","case_id": 1})
#headers
  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}#Make post request with json input body
  response = requests.post(url,  data=payload, headers=headers)
  response_data = response.json()
  status = response_data["Status"]
  assert status == 452




#Verify the response after giving user_consent value as 'Y', valid pan_number,  month_year_of_birth as 'mm-yy, valid case_id 

def test_entity_pan_profile_17():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_pan_profile/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N",
  "month_year_of_birth": "11-98",
  "case_id": "3"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving user_consent value as 'Y', valid pan_number, valid month_year_of_birth , case_id as "one"

def test_entity_pan_profile_18():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_pan_profile/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N",
  "month_year_of_birth": "01-1998",
  "case_id": "one"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after giving user_consent value as 'Yes', valid pan_number, valid month_year_of_birth , case_id as "one"

def test_entity_pan_profile_19():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_pan_profile/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Yes",
  "pan_number": "DYWPK2732N",
  "month_year_of_birth": "01-1998",
  "case_id": "one"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after giving user_consent value as 'No', valid pan_number, valid month_year_of_birth , case_id as "one"

def test_entity_pan_profile_20():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_pan_profile/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "No",
  "pan_number": "DYWPK2732N",
  "month_year_of_birth": "01-1998",
  "case_id": "one"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after giving user_consent value as 'Yes', invalid pan_number, valid month_year_of_birth , case_id as "one"

def test_entity_pan_profile_21():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_pan_profile/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Yes",
  "pan_number": "DYWP",
  "month_year_of_birth": "01-1998",
  "case_id": "one"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after giving user_consent value as 'Yes',invalid pan_number, month_year_of_birth as 'm-yyyy' , case_id as "one"

def test_entity_pan_profile_22():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_pan_profile/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Yes",
  "pan_number": "DYWP",
  "month_year_of_birth": "1-1998",
  "case_id": "one"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452