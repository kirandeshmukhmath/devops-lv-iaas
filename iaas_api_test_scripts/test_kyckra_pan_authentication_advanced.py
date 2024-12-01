import pytest
import requests
import json
import cred
import ocr

#Verify the response after keeping "user_consent" value as "" and remaining values as valid
def tests_panad1():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_authentication_advanced/"

  payload = json.dumps({
  "user_consent": "",
  "pan_number": "DYWPK2732N",
  "name": "Kiran",
  "fathers_name": "Deshmukhmath",
  "husband_name": "Kiran",
  "dob": "31/07/1971",
  "ocr_image_url": "https://base64.guru/converter/decode/pdf",
  "face_image_url": "https://base64.guru/converter/decode/pdf",
  "ocr_image_B64": ocr.ocrimg,
  "face_image_B64": ocr.faceimg,
  "addresses": [
   "Bengaluru"
  ],
  "notification": {
    "webhook": "name",
    "emails": [
      "annvinvincent@gmail.com"
    ],
    "webhook_config": {
      "url": "https://base64.guru/converter/encode/image/jpg"
    }
  }
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





#Verify the response after giving invalid pan number and remaining values as valid

def tests_panad2():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_authentication_advanced/"

  payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK",
  "name": "Kiran",
  "fathers_name": "Deshmukhmath",
  "husband_name": "Kiran",
  "dob": "31/07/1971",
  "ocr_image_url": "https://base64.guru/converter/decode/pdf",
  "face_image_url": "https://base64.guru/converter/decode/pdf",
  "ocr_image_B64": ocr.ocrimg,
  "face_image_B64": ocr.faceimg,
  "addresses": [
   "Bengaluru"
  ],
  "notification": {
    "webhook": "name",
    "emails": [
      "annvinvincent@gmail.com"
    ],
    "webhook_config": {
      "url": "https://base64.guru/converter/encode/image/jpg"
    }
  }
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






  #Verify the response after keeping "name" value as "" and remaining values as valid
def tests_panad3():
  #API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_authentication_advanced/"

  payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N",
  "name": "",
  "fathers_name": "Deshmukhmath",
  "husband_name": "Kiran",
  "dob": "31/07/1971",
  "ocr_image_url": "https://base64.guru/converter/decode/pdf",
  "face_image_url": "https://base64.guru/converter/decode/pdf",
  "ocr_image_B64": ocr.ocrimg,
  "face_image_B64": ocr.faceimg,
  "addresses": [
   "Bengaluru"
  ],
  "notification": {
    "webhook": "name",
    "emails": [
      "annvinvincent@gmail.com"
    ],
    "webhook_config": {
      "url": "https://base64.guru/converter/encode/image/jpg"
    }
  }
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





  #Verify the response after keeping "fathers_name" value as "" and remaining values as valid
def tests_panad4():
  #API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_authentication_advanced/"

  payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N",
  "name": "Kiran",
  "fathers_name": "",
  "husband_name": "Kiran",
  "dob": "31/07/1971",
  "ocr_image_url": "https://base64.guru/converter/decode/pdf",
  "face_image_url": "https://base64.guru/converter/decode/pdf",
  "ocr_image_B64": ocr.ocrimg,
  "face_image_B64": ocr.faceimg,
  "addresses": [
   "Bengaluru"
  ],
  "notification": {
    "webhook": "name",
    "emails": [
      "annvinvincent@gmail.com"
    ],
    "webhook_config": {
      "url": "https://base64.guru/converter/encode/image/jpg"
    }
  }
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






#Verify the response after keeping "husband_name" value as "" and remaining values as valid
def tests_panad5():
  #API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_authentication_advanced/"

  payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N",
  "name": "Kiran",
  "fathers_name": "Deshmukhmath",
  "husband_name": "",
  "dob": "31/07/1971",
  "ocr_image_url": "https://base64.guru/converter/decode/pdf",
  "face_image_url": "https://base64.guru/converter/decode/pdf",
  "ocr_image_B64": ocr.ocrimg,
  "face_image_B64": ocr.faceimg,
  "addresses": [
   "Bengaluru"
  ],
  "notification": {
    "webhook": "name",
    "emails": [
      "annvinvincent@gmail.com"
    ],
    "webhook_config": {
      "url": "https://base64.guru/converter/encode/image/jpg"
    }
  }
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






  #Verify the response after giving invalid "dob" and remaining values as valid
def tests_panad6():
  #API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_authentication_advanced/"

  payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N",
  "name": "Kiran",
  "fathers_name": "Deshmukhtmath",
  "husband_name": "Kiran",
  "dob": "3",
  "ocr_image_url": "https://base64.guru/converter/decode/pdf",
  "face_image_url": "https://base64.guru/converter/decode/pdf",
  "ocr_image_B64": ocr.ocrimg,
  "face_image_B64": ocr.faceimg,
  "addresses": [
   "Bengaluru"
  ],
  "notification": {
    "webhook": "name",
    "emails": [
      "annvinvincent@gmail.com"
    ],
    "webhook_config": {
      "url": "https://base64.guru/converter/encode/image/jpg"
    }
  }
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







  #Verify the response after giving  "ocr_image_url"  as ""  and remaining values as valid
def tests_panad7():
  #API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_authentication_advanced/"

  payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N",
  "name": "Kiran",
  "fathers_name": "Deshmukhmath",
  "husband_name": "Kiran",
  "dob": "31/07/1971",
  "ocr_image_url": "",
  "face_image_url": "https://base64.guru/converter/decode/pdf",
  "ocr_image_B64": ocr.ocrimg,
  "face_image_B64": ocr.faceimg,
  "addresses": [
   "Bengaluru"
  ],
  "notification": {
    "webhook": "name",
    "emails": [
      "annvinvincent@gmail.com"
    ],
    "webhook_config": {
      "url": "https://base64.guru/converter/encode/image/jpg"
    }
  }
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





  #Verify the response after giving  "face_image_url"  as ""  and remaining values as valid
def tests_panad8():
  #API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_authentication_advanced/"

  payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N",
  "name": "Kiran",
  "fathers_name": "deshmukhtmath",
  "husband_name": "Kiran",
  "dob": "31/07/1971",
  "ocr_image_url": "https://base64.guru/converter/decode/pdf",
  "face_image_url": "",
  "ocr_image_B64": ocr.ocrimg,
  "face_image_B64": ocr.faceimg,
  "addresses": [
   "Bengaluru"
  ],
  "notification": {
    "webhook": "name",
    "emails": [
      "annvinvincent@gmail.com"
    ],
    "webhook_config": {
      "url": "https://base64.guru/converter/encode/image/jpg"
    }
  }
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






  #Verify the response after giving  "ocr_image_B64"  as ""  and remaining values as valid
def tests_panad9():
  #API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_authentication_advanced/"

  payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N",
  "name": "Kiran",
  "fathers_name": "Deshmukhtmath",
  "husband_name": "Kiran",
  "dob": "31/07/1971",
  "ocr_image_url": "https://base64.guru/converter/decode/pdf",
  "face_image_url": "https://base64.guru/converter/decode/pdf",
  "ocr_image_B64": "",
  "face_image_B64": ocr.faceimg,
  "addresses": [
   "Bengaluru"
  ],
  "notification": {
    "webhook": "name",
    "emails": [
      "annvinvincent@gmail.com"
    ],
    "webhook_config": {
      "url": "https://base64.guru/converter/encode/image/jpg"
    }
  }
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






  #Verify the response after giving  "addresses"  as ""  and remaining values as valid
def tests_panad10():
  #API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_authentication_advanced/"

  payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N",
  "name": "Kiran",
  "fathers_name": "desh",
  "husband_name": "Kiran",
  "dob": "31/07/1971",
  "ocr_image_url": "https://base64.guru/converter/decode/pdf",
  "face_image_url": "https://base64.guru/converter/decode/pdf",
  "ocr_image_B64": ocr.ocrimg,
  "face_image_B64": ocr.faceimg,
  "addresses": [
   ""
  ],
  "notification": {
    "webhook": "name",
    "emails": [
      "annvinvincent@gmail.com"
    ],
    "webhook_config": {
      "url": "https://base64.guru/converter/encode/image/jpg"
    }
  }
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






  #Verify the response after giving  "webhook"  as ""  and remaining values as valid
def tests_panad11():
  #API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_authentication_advanced/"

  payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N",
  "name": "Kiran",
  "fathers_name": "desh",
  "husband_name": "Kiran",
  "dob": "31/07/1971",
  "ocr_image_url": "https://base64.guru/converter/decode/pdf",
  "face_image_url": "https://base64.guru/converter/decode/pdf",
  "ocr_image_B64": ocr.ocrimg,
  "face_image_B64": ocr.faceimg,
  "addresses": [
   "Bengaluru"
  ],
  "notification": {
    "webhook": "",
    "emails": [
      "annvinvincent@gmail.com"
    ],
    "webhook_config": {
      "url": "https://base64.guru/converter/encode/image/jpg"
    }
  }
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






#Verify the response after giving  "emails"  as ""  and remaining values as valid
def tests_panad12():
  #API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_authentication_advanced/"

  payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N",
  "name": "Kiran",
  "fathers_name": "desh",
  "husband_name": "Kiran",
  "dob": "31/07/1971",
  "ocr_image_url": "https://base64.guru/converter/decode/pdf",
  "face_image_url": "https://base64.guru/converter/decode/pdf",
  "ocr_image_B64": ocr.ocrimg,
  "face_image_B64": ocr.faceimg,
  "addresses": [
   "Bengaluru"
  ],
  "notification": {
    "webhook": "name",
    "emails": [
      ""
    ],
    "webhook_config": {
      "url": "https://base64.guru/converter/encode/image/jpg"
    }
  }
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






  #Verify the response after giving  "url"  as ""  and remaining values as valid
def tests_panad13():
  #API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_authentication_advanced/"

  payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N",
  "name": "Kiran",
  "fathers_name": "desh",
  "husband_name": "Kiran",
  "dob": "31/07/1971",
  "ocr_image_url": "https://base64.guru/converter/decode/pdf",
  "face_image_url": "https://base64.guru/converter/decode/pdf",
  "ocr_image_B64": ocr.ocrimg,
  "face_image_B64": ocr.faceimg,
  "addresses": [
   "Bengaluru"
  ],
  "notification": {
    "webhook": "name",
    "emails": [
      "annvinvincent@gmail.com"
    ],
    "webhook_config": {
      "url": ""
    }
  }
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






  #Verify the response after giving all the valid values

def tests_panad14():
#API URL
  url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/kyckra_pan_authentication_advanced/"

  payload = json.dumps({
  "user_consent": "Y",
  "pan_number": "DYWPK2732N",
  "name": "Kiran",
  "fathers_name": "Deshmukhmath",
  "husband_name": "Kiran",
  "dob": "31/07/1971",
  "ocr_image_url": "https://base64.guru/converter/decode/pdf",
  "face_image_url": "https://base64.guru/converter/decode/pdf",
  "ocr_image_B64": ocr.ocrimg,
  "face_image_B64": ocr.faceimg,
  "addresses": [
   "Bengaluru"
  ],
  "notification": {
    "webhook": "name",
    "emails": [
      "annvinvincent@gmail.com"
    ],
    "webhook_config": {
      "url": "https://base64.guru/converter/encode/image/jpg"
    }
  }
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
