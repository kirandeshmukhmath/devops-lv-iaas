#import pytest
import PyPDF2
import json
import cred
import base64
import requests

#API URL
url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/cadoc_get_ca_doc/"

payload = json.dumps(
{
  "doctype": "huf",
  "doc_params": {
                "parties": {
                    "trustee": {
                        "name": "VAR - Milestone Trusteeship Services Private Limited",
                        "address": "VAR - registered address of trustee"
                    },
                    "investment_manager": {
                        "name": "VAR - Lets Venture Advisors LLP",
                        "address": "VAR - address of Lets Venture Advisors LLP"
                    },
                    "contributor": {
                        "name": "VAR - Archimedha Mohapatra",
                        "capital_commitment": "VAR - 5000000",
                        "capital_commitment_upfront_drawdown": "VAR - 2600000",
                        "onboarding_fee": "VAR - 25000",
                        "transaction_fee": "var-2%",
                        "management_fee": "VAR - 2%",
                        "placement_fee": "VAR - 3%",
                        "total_fee": "VAR - 49000",
                        "correspondence_address": "VAR - Address of Archimedha Mohapatra",
                        "email_address": "VAR - archimedha@wishworkssolutions.com",
                        "phone_number": "VAR - 8660970120",
                        "net_worth": "VAR - 3Cr"
                    },
                    "witness": {
                        "name": "VAR - Rajat Bora",
                        "title": "VAR - Mr."
                    }
                },
                "fund_details": {
                    "fund_name": "VAR - LV ANGEL FUND",
                    "addressee": "VAR - Rajeev Ranjan",
                    "fund_address": "VAR - Address of LV ANGEL FUND",
                    "fund_email": "VAR - archiem@gmail.com",
                    "notifier_email": "VAR - archiem1410@gmail.com",
                    "fund_manager_name": "VAR - Lets Venture Advisors LLP",
                    "fund_manager_address": "VAR - Address of Lets Venture Advisors LLP",
                    "portfolio_entity_name": "VAR - LV Angel Fund Entity"
                },
                "agreement_details": {
                    "agreement_date": {
                        "date": "VAR - 2022-06-22",
                        "day": "VAR - 22",
                        "month": "VAR - 06",
                        "year": "VAR - 2022"
                    },
                    "agreement_id": "VAR - asdbde1234"
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
print(response_status)

status = response_data["Payload"]["file"]
#print(status)

file_64_decode = base64.b64decode(status) 
file_result = open('sample.pdf', 'wb') 
file_result.write(file_64_decode)


#file = open('sample_decoded7.pdf', 'rb')
#reader = PyPDF2.PdfFileReader(file)
#page1 = reader.getPage(0)

#print(reader.numPages)

#pdfData = page1.extractText()
#print(pdfData)
#assert "VAR - Milestone Trusteeship Services Private Limited" in pdfData
#assert "VAR - Lets Venture Advisors LLP" in pdfData

#page2 = reader.getPage(2)
#print(reader.numPages)
#pdfData = page2.extractText()
#print(pdfData)
#assert "VAR - Milestone Trusteeship Services Private Limited" in pdfData
#assert "VAR - Lets Venture Advisors LLP" in pdfData































INTERVAL = 10 * 60

conn = http.client.HTTPSConnection(host = 'papertrailapp.com')
conn.request(
    method = 'GET',
    url = '/api/v1/events/search.json?' + urllib.urlencode({
        'min_time' : str(int(time.time() - INTERVAL))
    }),
    headers = {
        'X-Papertrail-Token' : os.environ[cred.PAPERTRAIL_TOKEN]
    }
)
response2 = conn.getresponse()
print(response2)
events_no = len(json.loads(response.read())['events'])
print(events_no)






