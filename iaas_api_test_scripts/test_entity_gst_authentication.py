import pytest
import requests
import json
import cred
import unittest


#Verify the response after giving user_consent value as 'Y' and invalid gstin
 
def test_entity_gst_authentication_1():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_gst_authentication/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "gstin": "29GGGGG131"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after giving user_consent value as 'Y' and valid gstin

def test_entity_gst_authentication_2():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_gst_authentication/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "gstin": "29GGGGG1314R9Z6"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200


#Verify the response after giving user_consent value as 'N' and valid gstin

def test_entity_gst_authentication_3():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_gst_authentication/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "gstin": "29GGGGG1314R9Z6"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200


#Verify the response after giving user_consent value as 'N' and invalid gstin
 
def test_entity_gst_authentication_4():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_gst_authentication/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "gstin": "29GGGGG131"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after giving user_consent value as '' " and  gstin value as '' "

def test_entity_gst_authentication_5():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_gst_authentication/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "",
  "gstin": ""
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving user_consent value as '' " and  valid gstin value

def test_entity_gst_authentication_6():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_gst_authentication/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "",
  "gstin": "29GGGGG1314R9Z6"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving user_consent value as 'Y' and  gstin value as " "

def test_entity_gst_authentication_7():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_gst_authentication/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "gstin": ""
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving user_consent value as 'N' and  gstin value as '' "

def test_entity_gst_authentication_8():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_gst_authentication/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "gstin": ""
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving user_consent value as '' " and  invalid gstin value
def tests_pangst_9():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_entity_gst_authentication/"

  payload = json.dumps({
  "user_consent": " ",
  "gstin":"123 "
})


#headers

  headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
  response = requests.post(url,  data=payload, headers=headers)        
  response_data = response.json()
  status = response_data["Status"]
  assert status == 452