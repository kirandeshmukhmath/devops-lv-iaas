import pytest
import requests
import json
import cred
import ocr

#Verify the response after keeping "file_B64" as ""
def tests_ocr1():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_kyc_ocr/"

  payload = json.dumps({
  "file_B64":""
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




#Verify the response after giving a valid  "file_B64" value 
def tests_ocr2():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_kyc_ocr/"

  payload = json.dumps({
  "file_B64": ocr.ocrimg
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






#Verify the response after removing  "file_B64" parameter 
def tests_ocr3():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_kyc_ocr/"

  payload = json.dumps({
  
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