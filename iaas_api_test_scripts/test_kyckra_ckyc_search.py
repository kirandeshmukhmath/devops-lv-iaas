
import cred
import pytest
import json
import requests



#Verify the response after giving "user consent" as "Y", valid "ID Type", and valid "ID value".


def test_kyckra_ckyc_search_1():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_search/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "id_type": "PAN",
  "id_value": "DWYPK2732N"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200




#Verify the response after giving "user consent" as "Y", invalid "ID Type", and valid "ID value".


def test_kyckra_ckyc_search_2():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_search/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "id_type": "Credit Card",
  "id_value": "DWYPK2732N"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452





#Verify the response after giving "user consent" as "Y", valid "ID Type", and "ID value" as value "".

def test_kyckra_ckyc_search_3():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_search/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "id_type": "PAN",
  "id_value": ""
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving "user consent" as "N", valid "ID Type", and valid "ID value".

def test_kyckra_ckyc_search_4():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_search/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "id_type": "PAN",
  "id_value": "DYWPK2732N"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200



#Verify the response after giving "user consent" as "N", invalid "ID Type", and valid "ID value".

def test_kyckra_ckyc_search_5():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_search/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "id_type": "Debit Card",
  "id_value": "DYWPK2732N"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving "user consent" as "N", valid "ID Type", and invalid "ID value".


def test_kyckra_ckyc_search_6():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_search/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "id_type": "PAN",
  "id_value": 123
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving "user consent" as "", "ID Type" as "", and "ID value".as "".

def test_kyckra_ckyc_search_7():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_search/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "",
  "id_type": "",
  "id_value": ""
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving "user consent" as "Y", "ID Type" as "", and "ID value".as "".

def test_kyckra_ckyc_search_8():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_search/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "id_type": "",
  "id_value": ""
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving "user consent" as "Y", valid "ID Type", and "ID value".as "".

def test_kyckra_ckyc_search_9():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_search/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "id_type": "PAN",
  "id_value": ""
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving "user consent" as "Y", "ID Type" as "", and valid "ID value".

def test_kyckra_ckyc_search_10():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_search/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "id_type": "",
  "id_value": "DWYPK2732N"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving "user consent" as "N", "ID Type" as "", and "ID value".as "".

def test_kyckra_ckyc_search_11():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_search/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "id_type": "",
  "id_value": ""
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving "user consent" as "N", valid "ID Type", and "ID value".as "".

def test_kyckra_ckyc_search_12():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_search/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "id_type": "PAN",
  "id_value": ""
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after giving "user consent" as "N", "ID Type" as "", and valid "ID value".

def test_kyckra_ckyc_search_13():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_search/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "N",
  "id_type": "",
  "id_value": "DWYPK2732N"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving "user consent" as "Y", valid "ID Type - PASSPORT", and valid "ID value"., Response status should be 200

def test_kyckra_ckyc_search_14():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_search/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "id_type": "PASSPORT",
  "id_value": "DWYPK2732N"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200

#Verify the response after giving "user consent" as "Y", valid "ID Type - VOTER", and valid "ID value"., Response status should be 200

def test_kyckra_ckyc_search_15():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_search/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "id_type": "VOTER",
  "id_value": "DWYPK2732N"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200


#Verify the response after giving "user consent" as "Y", valid "ID Type - DL", and valid "ID value"., Response status should be 200
def test_kyckra_ckyc_search_16():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_search/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "id_type": "DL",
  "id_value": "DWYPK2732N"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200



#Verify the response after giving "user consent" as "Y", valid "ID Type - UID", and valid "ID value"., Response status should be 200
def test_kyckra_ckyc_search_17():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_search/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "id_type": "UID",
  "id_value": "DWYPK2732N"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200



#Verify the response after giving "user consent" as "Y", valid "ID Type - NREGAID", and valid "ID value"., Response status should be 200
def test_kyckra_ckyc_search_18():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_search/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "id_type": "NREGAID",
  "id_value": "DWYPK2732N"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200



#Verify the response after giving "user consent" as "Y", valid "ID Type - NPRL", and valid "ID value"., Response status should be 200
def test_kyckra_ckyc_search_19():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_search/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "id_type": "NPRL",
  "id_value": "DWYPK2732N"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200

#Verify the response after giving "user consent" as "Y", valid "ID Type - CKYCID", and valid "ID value"., Response status should be 200
def test_kyckra_ckyc_search_20():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_search/"
#Read Input Json file
        payload = json.dumps({
  "user_consent": "Y",
  "id_type": "CKYCID",
  "id_value": "DWYPK2732N"
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200