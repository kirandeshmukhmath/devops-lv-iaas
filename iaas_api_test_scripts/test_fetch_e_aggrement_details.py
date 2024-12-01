import json
import cred
import base64
import requests




#Verify the response by giving valid document ID
def test_fetch_e_aggrement_1():

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
#assert response_status == 200

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
    response_documentID = response_data1["Payload"]["data"]["documentId"]
    response_message = response_data1["Message"]
    #assert response_status1 == 200
    print(response_documentID)


#visit fetch_e_aggrement_details url
    url2 = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_e_agreement_details/"

    payload = json.dumps(
{
  "documentId": response_documentID
})

    headers2 = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response2 = requests.post(url2,  data=payload, headers=headers2)
    response_data2 = response2.json()
    response_status2 = response_data2["Status"]
    response_message2 = response_data2["Message"]
    response_document2 = response_data2["Payload"]["data"]["documentId"]
    assert response_status2 == 200
    print(response_message2)
    print(response_document2)






#Verify the response by giving wrong document ID
def test_fetch_e_aggrement_2():

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
#assert response_status == 200

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
    response_documentID = response_data1["Payload"]["data"]["documentId"]
    response_message = response_data1["Message"]
    #assert response_status1 == 200
    #print(response_documentID)


#visit fetch_e_aggrement_details url
    url2 = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_e_agreement_details/"

    payload = json.dumps(
{
  "documentId": 12345
})

    headers2 = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body

    response2 = requests.post(url2,  data=payload, headers=headers2)
    response_data2 = response2.json()
    response_status2 = response_data2["Status"]
    response_message2 = response_data2["Message"]
    #response_document2 = response_data2["Payload"]["data"]["documentId"]
    assert response_status2 == 452
