import pytest
import requests
import json
import cred

#Verify the response after giving user consent as "Y" and valid ckyc_id.
def tests_download1():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_download/"

  payload = json.dumps({
  "user_consent": "Y",
  "ckyc_id":"12345678912345"
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






#Verify the response after giving user consent as "" and valid ckyc_id.
def tests_download2():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_download/"

  payload = json.dumps({
  "user_consent": "",
  "ckyc_id":"12345678912345"
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






#Verify the response after giving user consent as "" and ckyc_id.as ""
def tests_download3():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_download/"

  payload = json.dumps({
  "user_consent": "",
"ckyc_id":""
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






#Verify the response after giving user consent as "Y" and ckyc_id as ""
def tests_download4():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_download/"

  payload = json.dumps({
  "user_consent": "Y",
  "ckyc_id":""
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





#Verify the response after giving user consent as "N" and valid ckyc_id.
def tests_download5():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_download/"

  payload = json.dumps({
  "user_consent": "N",
  "ckyc_id":"12345678912345"
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



#Verify the response after giving user consent as "N" and ckyc_id.as "".

def tests_download6():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_download/"

  payload = json.dumps({
  "user_consent": "N",
  "ckyc_id":""
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



#Verify the response after giving user consent as "Y" and give less than 14 digit ckyc _id

def tests_download7():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_download/"

  payload = json.dumps({
  "user_consent": "Y",
  "ckyc_id":"123"
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



#Verify the response after giving user consent as "Y" and give more than 14 digit ckyc _id

def tests_download8():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_download/"

  payload = json.dumps({
  "user_consent": "Y",
  "ckyc_id":"111111111111111111111111111111111111111111111111111111111111111111"
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




#Verify the response after giving user consent as "N" and give less than 14 digit ckyc _id

def tests_download9():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_download/"

  payload = json.dumps({
  "user_consent": "N",
  "ckyc_id":"12345"
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




#Verify the response after giving user consent as "N" and give more than 14 digit ckyc _id

def tests_download10():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_ckyc_download/"

  payload = json.dumps({
  "user_consent": "N",
  "ckyc_id":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
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