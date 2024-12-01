import json
import cred
import base64
import requests




#Verify the response by giving correct file and invitees details. (Execute side_letter cadoc first and copy details from side_letter response)
def test_initiate_e_aggrement_1():

#API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

    payload = json.dumps(
    {
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Kiran",
                        "email": "kirandeshmukh.lv@grepdigital.com",
                        "phone": "8147357822",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Annvin",
                        "email": "annvin.lv@grepdigital.com",
                        "phone": "0000000000",
                        "address": "Bangalore",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Status"]
    assert response_status == 200

    Base64File = response_data["Payload"]["file"]
    Payload1 = response_data["Payload"]["additional_info"]["coordinates"]["Payload"]

    #visit initial_e_aggrement link
    url1 = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/initiate_e_agreement/"

    payload = json.dumps(
{
  "file": {
    "file": Base64File,
    "name": "Test-Demo"
  },
  "invitees": Payload1
})

    headers1 = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response1 = requests.post(url1,  data=payload, headers=headers1)
    response_data1 = response1.json()
    response_status1 = response_data1["Status"]
    response_payload = response_data1["Payload"]
    response_message = response_data1["Message"]
    assert response_status1 == 200

    





#Verify the response by giving file: file input as " " and remaining value correct
def test_initiate_e_aggrement_2():

#API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

    payload = json.dumps(
    {
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Kiran",
                        "email": "kirandeshmukh.lv@grepdigital.com",
                        "phone": "8147357822",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Annvin",
                        "email": "annvin.lv@grepdigital.com",
                        "phone": "0000000000",
                        "address": "Bangalore",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Status"]
    assert response_status == 200

    Base64File = response_data["Payload"]["file"]
    Payload1 = response_data["Payload"]["additional_info"]["coordinates"]["Payload"]

    #visit initial_e_aggrement link
    url1 = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/initiate_e_agreement/"

    payload = json.dumps(
{
  "file": {
    "file": "",
    "name": "Test-Demo"
  },
  "invitees": Payload1
})

    headers1 = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response1 = requests.post(url1,  data=payload, headers=headers1)
    response_data1 = response1.json()
    response_status1 = response_data1["Status"]
    response_payload = response_data1["Payload"]
    response_message = response_data1["Message"]
    assert response_status1 == 452








#Verify the response by giving file: name: " " and remaining value correct
def test_initiate_e_aggrement_3():

#API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

    payload = json.dumps(
    {
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Kiran",
                        "email": "kirandeshmukh.lv@grepdigital.com",
                        "phone": "8147357822",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Annvin",
                        "email": "annvin.lv@grepdigital.com",
                        "phone": "0000000000",
                        "address": "Bangalore",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Status"]
    assert response_status == 200

    Base64File = response_data["Payload"]["file"]
    Payload1 = response_data["Payload"]["additional_info"]["coordinates"]["Payload"]

    #visit initial_e_aggrement link
    url1 = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/initiate_e_agreement/"

    payload = json.dumps(
{
  "file": {
    "file": Base64File,
    "name": ""
  },
  "invitees": Payload1
})

    headers1 = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response1 = requests.post(url1,  data=payload, headers=headers1)
    response_data1 = response1.json()
    response_status1 = response_data1["Status"]
    response_payload = response_data1["Payload"]
    response_message = response_data1["Message"]
    assert response_status1 == 200






#Verify the response by giving invitees: name as " " and remaining value correct for first invitee
def test_initiate_e_aggrement_4():

#API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

    payload = json.dumps(
    {
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Kiran",
                        "email": "kirandeshmukh.lv@grepdigital.com",
                        "phone": "8147357822",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Annvin",
                        "email": "annvin.lv@grepdigital.com",
                        "phone": "0000000000",
                        "address": "Bangalore",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Status"]
    assert response_status == 200

    Base64File = response_data["Payload"]["file"]
    Payload1 = response_data["Payload"]["additional_info"]["coordinates"]["Payload"]

    #visit initial_e_aggrement link
    url1 = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/initiate_e_agreement/"

    payload = json.dumps(
{
  "file": {
    "file": Base64File,
    "name": "Test"
  },
  "invitees": [{
            "party_in_doc_params": "No",
            "name": "",
            "email": "archi.lv@grepdigital.com",
            "phone": "9741601203",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "420",
                "y2": "496",
                "page": [
                  3
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "No",
            "name": "Investment Manager",
            "email": "rajeev.lv@grepdigital.com",
            "phone": "8660970120",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "201",
                "y2": "278",
                "page": [
                  3
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "Yes",
            "name": "Kiran",
            "email": "kirandeshmukh.lv@grepdigital.com",
            "phone": "8147357822",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "632",
                "y2": "704",
                "page": [
                  4
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "Yes",
            "name": "Annvin",
            "email": "annvin.lv@grepdigital.com",
            "phone": "0000000000",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "489",
                "y2": "567",
                "page": [
                  4
                ]
              }
            ]
          }]
})

    headers1 = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response1 = requests.post(url1,  data=payload, headers=headers1)
    response_data1 = response1.json()
    response_status1 = response_data1["Status"]
    response_payload = response_data1["Payload"]
    response_message = response_data1["Message"]
    assert response_status1 == 452






#Verify the response by giving invitees: email as " " and remaining value correct for first invitee
def test_initiate_e_aggrement_5():

#API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

    payload = json.dumps(
    {
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Kiran",
                        "email": "kirandeshmukh.lv@grepdigital.com",
                        "phone": "8147357822",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Annvin",
                        "email": "annvin.lv@grepdigital.com",
                        "phone": "0000000000",
                        "address": "Bangalore",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Status"]
    assert response_status == 200

    Base64File = response_data["Payload"]["file"]
    Payload1 = response_data["Payload"]["additional_info"]["coordinates"]["Payload"]

    #visit initial_e_aggrement link
    url1 = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/initiate_e_agreement/"

    payload = json.dumps(
{
  "file": {
    "file": Base64File,
    "name": "Test"
  },
  "invitees": [{
            "party_in_doc_params": "No",
            "name": "Archi",
            "email": "",
            "phone": "9741601203",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "420",
                "y2": "496",
                "page": [
                  3
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "No",
            "name": "Investment Manager",
            "email": "rajeev.lv@grepdigital.com",
            "phone": "8660970120",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "201",
                "y2": "278",
                "page": [
                  3
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "Yes",
            "name": "Kiran",
            "email": "kirandeshmukh.lv@grepdigital.com",
            "phone": "8147357822",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "632",
                "y2": "704",
                "page": [
                  4
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "Yes",
            "name": "Annvin",
            "email": "annvin.lv@grepdigital.com",
            "phone": "0000000000",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "489",
                "y2": "567",
                "page": [
                  4
                ]
              }
            ]
          }]
})

    headers1 = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response1 = requests.post(url1,  data=payload, headers=headers1)
    response_data1 = response1.json()
    response_status1 = response_data1["Status"]
    response_payload = response_data1["Payload"]
    response_message = response_data1["Message"]
    assert response_status1 == 452







#Verify the response by giving invitees: phone as " " and remaining value correct for first invitee
def test_initiate_e_aggrement_6():

#API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

    payload = json.dumps(
    {
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Kiran",
                        "email": "kirandeshmukh.lv@grepdigital.com",
                        "phone": "8147357822",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Annvin",
                        "email": "annvin.lv@grepdigital.com",
                        "phone": "0000000000",
                        "address": "Bangalore",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Status"]
    assert response_status == 200

    Base64File = response_data["Payload"]["file"]
    Payload1 = response_data["Payload"]["additional_info"]["coordinates"]["Payload"]

    #visit initial_e_aggrement link
    url1 = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/initiate_e_agreement/"

    payload = json.dumps(
{
  "file": {
    "file": Base64File,
    "name": "Test"
  },
  "invitees": [{
            "party_in_doc_params": "No",
            "name": "Archi",
            "email": "archi.lv@grepdigital.com",
            "phone": "",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "420",
                "y2": "496",
                "page": [
                  3
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "No",
            "name": "Investment Manager",
            "email": "rajeev.lv@grepdigital.com",
            "phone": "8660970120",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "201",
                "y2": "278",
                "page": [
                  3
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "Yes",
            "name": "Kiran",
            "email": "kirandeshmukh.lv@grepdigital.com",
            "phone": "8147357822",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "632",
                "y2": "704",
                "page": [
                  4
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "Yes",
            "name": "Annvin",
            "email": "annvin.lv@grepdigital.com",
            "phone": "0000000000",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "489",
                "y2": "567",
                "page": [
                  4
                ]
              }
            ]
          }]
})

    headers1 = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response1 = requests.post(url1,  data=payload, headers=headers1)
    response_data1 = response1.json()
    response_status1 = response_data1["Status"]
    response_payload = response_data1["Payload"]
    response_message = response_data1["Message"]
    assert response_status1 == 452


def test_initiate_e_aggrement_7():

#API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

    payload = json.dumps(
    {
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Kiran",
                        "email": "kirandeshmukh.lv@grepdigital.com",
                        "phone": "8147357822",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Annvin",
                        "email": "annvin.lv@grepdigital.com",
                        "phone": "0000000000",
                        "address": "Bangalore",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
    

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Status"]
    assert response_status == 200

    Base64File = response_data["Payload"]["file"]
    Payload1 = response_data["Payload"]["additional_info"]["coordinates"]["Payload"]
    #print(Payload1)




    url1 = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/initiate_e_agreement/"

    payload = json.dumps(
{
  "file": {
    "file": Base64File,
    "name": "Test-Demo"
  },
  "invitees": [{
            "party_in_doc_params": "No",
            "name": "trustee",
            "email": "archi.lv@grepdigital.com",
            "phone": "9741601203",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "420",
                "y2": "496",
                "page": [
                  
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "No",
            "name": "Investment Manager",
            "email": "rajeev.lv@grepdigital.com",
            "phone": "8660970120",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "201",
                "y2": "278",
                "page": [
                  
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "Yes",
            "name": "Kiran",
            "email": "kirandeshmukh.lv@grepdigital.com",
            "phone": "8147357822",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "632",
                "y2": "704",
                "page": [
                  
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "Yes",
            "name": "Annvin",
            "email": "annvin.lv@grepdigital.com",
            "phone": "0000000000",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "489",
                "y2": "567",
                "page": [
                  
                ]
              }
            ]
          }]
})

    headers1 = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body

    response1 = requests.post(url1,  data=payload, headers=headers1)
    response_data1 = response1.json()
    response_status1 = response_data1["Status"]
    response_payload = response_data1["Payload"]
    response_message = response_data1["Message"]
    assert response_status1 == 452


def test_initiate_e_aggrement_8():

#API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

    payload = json.dumps(
    {
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Kiran",
                        "email": "kirandeshmukh.lv@grepdigital.com",
                        "phone": "8147357822",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Annvin",
                        "email": "annvin.lv@grepdigital.com",
                        "phone": "0000000000",
                        "address": "Bangalore",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
    

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Status"]
    assert response_status == 200

    Base64File = response_data["Payload"]["file"]
    Payload1 = response_data["Payload"]["additional_info"]["coordinates"]["Payload"]
    #print(Payload1)




    url1 = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/initiate_e_agreement/"

    payload = json.dumps(
{
  "file": {
    "file": Base64File,
    "name": "Test-Demo"
  },
  "invitees": [{
            "party_in_doc_params": "No",
            "name": "trustee",
            "email": "archi.lv@grepdigital.com",
            "phone": "9741601203",
            "appearances": [
              {
                "x1": "",
                "x2": "295",
                "y1": "420",
                "y2": "496",
                "page": [3
                  
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "No",
            "name": "Investment Manager",
            "email": "rajeev.lv@grepdigital.com",
            "phone": "8660970120",
            "appearances": [
              {
                "x1": "",
                "x2": "295",
                "y1": "201",
                "y2": "278",
                "page": [3
                  
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "Yes",
            "name": "Kiran",
            "email": "kirandeshmukh.lv@grepdigital.com",
            "phone": "8147357822",
            "appearances": [
              {
                "x1": "",
                "x2": "295",
                "y1": "632",
                "y2": "704",
                "page": [4
                  
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "Yes",
            "name": "Annvin",
            "email": "annvin.lv@grepdigital.com",
            "phone": "0000000000",
            "appearances": [
              {
                "x1": "",
                "x2": "295",
                "y1": "489",
                "y2": "567",
                "page": [4
                  
                ]
              }
            ]
          }]
})

    headers1 = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body

    response1 = requests.post(url1,  data=payload, headers=headers1)
    response_data1 = response1.json()
    response_status1 = response_data1["Status"]
    response_payload = response_data1["Payload"]
    response_message = response_data1["Message"]
    assert response_status1 == 452

def test_initiate_e_aggrement_9():

#API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

    payload = json.dumps(
    {
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Kiran",
                        "email": "kirandeshmukh.lv@grepdigital.com",
                        "phone": "8147357822",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Annvin",
                        "email": "annvin.lv@grepdigital.com",
                        "phone": "0000000000",
                        "address": "Bangalore",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
    

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Status"]
    assert response_status == 200

    Base64File = response_data["Payload"]["file"]
    Payload1 = response_data["Payload"]["additional_info"]["coordinates"]["Payload"]
    #print(Payload1)




    url1 = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/initiate_e_agreement/"

    payload = json.dumps(
{
  "file": {
    "file": Base64File,
    "name": "Test-Demo"
  },
  "invitees": [{
            "party_in_doc_params": "No",
            "name": "trustee",
            "email": "archi.lv@grepdigital.com",
            "phone": "9741601203",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "",
                "y2": "496",
                "page": [3
                  
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "No",
            "name": "Investment Manager",
            "email": "rajeev.lv@grepdigital.com",
            "phone": "8660970120",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "",
                "y2": "278",
                "page": [3
                  
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "Yes",
            "name": "Kiran",
            "email": "kirandeshmukh.lv@grepdigital.com",
            "phone": "8147357822",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "",
                "y2": "704",
                "page": [4
                  
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "Yes",
            "name": "Annvin",
            "email": "annvin.lv@grepdigital.com",
            "phone": "0000000000",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "",
                "y2": "567",
                "page": [4
                  
                ]
              }
            ]
          }]
})

    headers1 = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body

    response1 = requests.post(url1,  data=payload, headers=headers1)
    response_data1 = response1.json()
    response_status1 = response_data1["Status"]
    response_payload = response_data1["Payload"]
    response_message = response_data1["Message"]
    assert response_status1 == 452

def test_initiate_e_aggrement_10():

#API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

    payload = json.dumps(
    {
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Kiran",
                        "email": "kirandeshmukh.lv@grepdigital.com",
                        "phone": "8147357822",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Annvin",
                        "email": "annvin.lv@grepdigital.com",
                        "phone": "0000000000",
                        "address": "Bangalore",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
    

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Status"]
    assert response_status == 200

    Base64File = response_data["Payload"]["file"]
    Payload1 = response_data["Payload"]["additional_info"]["coordinates"]["Payload"]
    #print(Payload1)




    url1 = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/initiate_e_agreement/"

    payload = json.dumps(
{
  "file": {
    "file": Base64File,
    "name": "Test-Demo"
  },
  "invitees": [{
            "party_in_doc_params": "No",
            "name": "trustee",
            "email": "archi.lv@grepdigital.com",
            "phone": "9741601203",
            "appearances": [
              {
                "x1": "64",
                "x2": "",
                "y1": "420",
                "y2": "496",
                "page": [3
                  
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "No",
            "name": "Investment Manager",
            "email": "rajeev.lv@grepdigital.com",
            "phone": "8660970120",
            "appearances": [
              {
                "x1": "64",
                "x2": "",
                "y1": "201",
                "y2": "278",
                "page": [3
                  
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "Yes",
            "name": "Kiran",
            "email": "kirandeshmukh.lv@grepdigital.com",
            "phone": "8147357822",
            "appearances": [
              {
                "x1": "64",
                "x2": "",
                "y1": "632",
                "y2": "704",
                "page": [4
                  
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "Yes",
            "name": "Annvin",
            "email": "annvin.lv@grepdigital.com",
            "phone": "0000000000",
            "appearances": [
              {
                "x1": "64",
                "x2": "",
                "y1": "489",
                "y2": "567",
                "page": [4
                  
                ]
              }
            ]
          }]
})

    headers1 = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body

    response1 = requests.post(url1,  data=payload, headers=headers1)
    response_data1 = response1.json()
    response_status1 = response_data1["Status"]
    response_payload = response_data1["Payload"]
    response_message = response_data1["Message"]
    assert response_status1 == 452


def test_initiate_e_aggrement_11():

#API URL
    url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

    payload = json.dumps(
    {
        "doctype": "side-letter-joint-agreement",
        "template": "side-letter-joint-agreement.html",
        "doc_params":
            {
                "letter_date": "2022-06-25",
                "parties": {
                    "first_party": {
                        "name": "Kiran",
                        "email": "kirandeshmukh.lv@grepdigital.com",
                        "phone": "8147357822",
                        "address": "Bangalore"
                    },
                    "second_party": {
                        "name": "Annvin",
                        "email": "annvin.lv@grepdigital.com",
                        "phone": "0000000000",
                        "address": "Bangalore",
                        "relationship_with_first_contributor": "Brother"
                    }
                }
            }
    })


#headers

    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
    

#Make post request with json input body

    response = requests.post(url,  data=payload, headers=headers)
    response_data = response.json()
    response_status = response_data["Status"]
    assert response_status == 200

    Base64File = response_data["Payload"]["file"]
    Payload1 = response_data["Payload"]["additional_info"]["coordinates"]["Payload"]
    #print(Payload1)




    url1 = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/initiate_e_agreement/"

    payload = json.dumps(
{
  "file": {
    "file": Base64File,
    "name": "Test-Demo"
  },
  "invitees": [{
            "party_in_doc_params": "No",
            "name": "trustee",
            "email": "archi.lv@grepdigital.com",
            "phone": "9741601203",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "420",
                "y2": "",
                "page": [3
                  
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "No",
            "name": "Investment Manager",
            "email": "rajeev.lv@grepdigital.com",
            "phone": "8660970120",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "201",
                "y2": "",
                "page": [3
                  
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "Yes",
            "name": "Kiran",
            "email": "kirandeshmukh.lv@grepdigital.com",
            "phone": "8147357822",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "632",
                "y2": "",
                "page": [4
                  
                ]
              }
            ]
          },
          {
            "party_in_doc_params": "Yes",
            "name": "Annvin",
            "email": "annvin.lv@grepdigital.com",
            "phone": "0000000000",
            "appearances": [
              {
                "x1": "64",
                "x2": "295",
                "y1": "489",
                "y2": "",
                "page": [4
                  
                ]
              }
            ]
          }]
})

    headers1 = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body

    response1 = requests.post(url1,  data=payload, headers=headers1)
    response_data1 = response1.json()
    response_status1 = response_data1["Status"]
    response_payload = response_data1["Payload"]
    response_message = response_data1["Message"]
    assert response_status1 == 452