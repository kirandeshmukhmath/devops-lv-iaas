import pytest
import requests
import json
import cred
import unittest


#Verify the response after giving user_consent value as 'Y' and invalid pan_number
 
def test_entity_gst_search_basis_plan_1():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_gst_search_basis_pan/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after giving user_consent value as 'Y' and valid pan_number

def test_entity_gst_search_basis_plan_2():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_gst_search_basis_pan/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200


#Verify the response after giving user_consent value as 'N' and valid pan_number

def test_entity_gst_search_basis_plan_3():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_gst_search_basis_pan/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "pan_number": "DYWPK2732N"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200


#Verify the response after giving user_consent value as 'N' and invalid pan_number

def test_entity_gst_search_basis_plan_4():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_gst_search_basis_pan/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "pan_number": "DYWPK2732"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after giving user_consent value as '' " and  pan_number value as '' "

def test_entity_gst_search_basis_plan_5():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_gst_search_basis_pan/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "",
  "pan_number": ""
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving user_consent value as '' " and  valid pan_number value

def test_entity_gst_search_basis_plan_6():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_gst_search_basis_pan/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "",
  "pan_number": "DYWPK2732N"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving user_consent value as 'Y' and  pan_number value as " "

def test_entity_gst_search_basis_plan_7():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_gst_search_basis_pan/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "pan_number": ""
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving user_consent value as 'N' and  pan_number value as '' "

def test_entity_gst_search_basis_plan_8():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_gst_search_basis_pan/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "pan_number": ""
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving user_consent value as '' " and  invalid pan_number value
def tests_gstsearch_9():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_gst_search_basis_pan/"

  payload = json.dumps({
  "user_consent": " ",
  "pan_number":"BQIPV"
})

  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
  response = requests.post(url,  data=payload, headers=headers)        
  response_data = response.json()
  status = response_data["Status"]
  assert status == 452