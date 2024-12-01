import pytest
import requests
import json
import cred
import creds



#Verify the response after giving doctype as "investor-scheme", template as "investor-scheme.html" and valid "doc_params"

def test_schemedoc_get_scheme_doc_1():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "investor-scheme",
        "template": "investor-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 200



#Verify the response after giving doctype as " " , tmeplate as "investor-scheme.html" and valid "doc_params"

def test_schemedoc_get_scheme_doc_2():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "",
        "template": "investor-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452    



#Verify the response after giving doctype as "investor-scheme", template as " " and valid "doc_params"

def test_schemedoc_get_scheme_doc_3():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "investor-scheme",
        "template": "",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 200 



#Verify the response after giving doctype as "investor-scheme", template as "investor-scheme.html" and in "doc_params" keep "angel_fund_name" as " " and remaing parameters valid.


def test_schemedoc_get_scheme_doc_4():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "investor-scheme",
        "template": "investor-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452




#Verify the response after giving doctype as "investor-scheme", template as "investor-scheme.html" and in "doc_params" keep "sebi_registration_number" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_5():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "investor-scheme",
        "template": "investor-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452





#Verify the response after giving doctype as "investor-scheme", template as "investor-scheme.html" and in "doc_params" keep "investment_scheme_name" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_6():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "investor-scheme",
        "template": "investor-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452




#Verify the response after giving doctype as "investor-scheme", template as "investor-scheme.html" and in "doc_params" keep "lead_investor_name" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_7():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "investor-scheme",
        "template": "investor-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 200




#Verify the response after giving doctype as "investor-scheme", template as "investor-scheme.html" and in "doc_params" keep "portfolio_entity_name" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_8():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "investor-scheme",
        "template": "investor-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452





#Verify the response after giving doctype as "investor-scheme", template as "investor-scheme.html" and in "doc_params" keep "portfolio_entity_premoney_valuation" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_9():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "investor-scheme",
        "template": "investor-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": "",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 200



#Verify the response after giving doctype as "investor-scheme", template as "investor-scheme.html" and in "doc_params" keep "scheme_investment_limit" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_10():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "investor-scheme",
        "template": "investor-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": ""
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452




#Verify the response after giving doctype as "investor-scheme", template as "investor-scheme.html" and in "doc_params" keep "security_type" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_11():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "investor-scheme",
        "template": "investor-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452




#Verify the response after giving doctype as "investor-scheme", template as "investor-scheme.html" and in "doc_params" keep "ccds" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_12():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "investor-scheme",
        "template": "investor-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 200



#Verify the response after giving doctype as "investor-scheme", template as "investor-scheme.html" and in "doc_params" keep "number_of_securities" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_13():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "investor-scheme",
        "template": "investor-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452



#Verify the response after giving doctype as "investor-scheme", template as "investor-scheme.html" and in "doc_params" keep "price_per_share" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_14():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "investor-scheme",
        "template": "investor-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452



#Verify the response after giving doctype as "investor-scheme", template as "investor-scheme.html" and in "doc_params" keep "conversion_price_ccps" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_15():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "investor-scheme",
        "template": "investor-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 200


#Verify the response after giving doctype as "investor-scheme", template as "investor-scheme.html" and in "doc_params" keep "transaction_fee" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_16():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "investor-scheme",
        "template": "investor-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452



#Verify the response after giving doctype as "investor-scheme", template as "investor-scheme.html" and in "doc_params" keep "last_date_of_consent" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_17():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "investor-scheme",
        "template": "investor-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": ""
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452




#Verify the response after giving doctype as "investor-scheme", template as "investor-scheme.html" and in "doc_params" keep "contributor_share" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_18():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "investor-scheme",
        "template": "investor-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452



#Verify the response after giving doctype as "investor-scheme", template as "investor-scheme.html" and in "doc_params" keep "others_share" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_19():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "investor-scheme",
        "template": "investor-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": ""
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452




#Verify the response after giving doctype as "investor-scheme", template as "investor-scheme.html" and in "doc_params" remove "conversion_price_ccps  and remaing parameters valid.

def test_schemedoc_get_scheme_doc_20():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "investor-scheme",
        "template": "investor-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 200




####################################      lead_scheme      ##############################################

#Verify the response after giving doctype as "investor-scheme", template as "investor-scheme.html" and valid "doc_params"

def test_schemedoc_get_scheme_doc_21():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "lead-scheme",
        "template": "lead-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 200

#Verify the response after giving doctype as " " , template as "lead-scheme.html" and valid "doc_params"

def test_schemedoc_get_scheme_doc_22():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "",
        "template": "lead-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452

#Verify the response after giving doctype as "lead-scheme", template as " " and valid "doc_params"

def test_schemedoc_get_scheme_doc_23():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "lead-scheme",
        "template": "",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 200

#Verify the response after giving doctype as "lead-scheme", template as "lead-scheme.html" and in "doc_params" keep "angel_fund_name" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_24():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "lead-scheme",
        "template": "lead-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452

#Verify the response after giving doctype as "lead-scheme", template as "lead-scheme.html" and in "doc_params" keep "sebi_registration_number" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_25():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "lead-scheme",
        "template": "lead-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452

#Verify the response after giving doctype as"lead-scheme", template as "lead-scheme.html" and in "doc_params" keep "investment_scheme_name" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_26():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "lead-scheme",
        "template": "lead-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452

#Verify the response after giving doctype as "lead-scheme", template as"lead-scheme.html" and in "doc_params" keep "lead_investor_name" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_27():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "lead-scheme",
        "template": "lead-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 200

#Verify the response after giving doctype as "lead-scheme", template as "lead-scheme.html" and in "doc_params" keep "portfolio_entity_name" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_28():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "lead-scheme",
        "template": "lead-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452

#Verify the response after giving doctype as "lead-scheme", template as "lead-scheme.html" and in "doc_params" keep "portfolio_entity_profile" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_29():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "lead-scheme",
        "template": "lead-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452

#Verify the response after giving doctype as "lead-scheme", template as "lead-scheme.html" and in "doc_params" keep "portfolio_entity_industry" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_30():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "lead-scheme",
        "template": "lead-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452





#Verify the response after giving doctype as "lead-scheme", template as "lead-scheme.html" and in "doc_params" keep "portfolio_entity_premoney_valuation" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_31():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "lead-scheme",
        "template": "lead-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": "",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 200

#Verify the response after giving doctype as "lead-scheme", template as "lead-scheme.html" and in "doc_params" keep "investment_highlights": "total_round_size" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_32():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "lead-scheme",
        "template": "lead-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452

#Verify the response after giving doctype as "lead-scheme", template as "lead-scheme.html" and in "doc_params" keep "investment_highlights": "scheme_investment_limit" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_33():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "lead-scheme",
        "template": "lead-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": ""
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452

#Verify the response after giving doctype as "lead-scheme", template as "lead-scheme.html" and in "doc_params" keep "security_type" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_34():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "lead-scheme",
        "template": "lead-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452

#Verify the response after giving doctype as "lead-scheme" template as "lead-scheme.html" and in "doc_params" keep "ccds" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_35():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "lead-scheme",
        "template": "lead-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 200

#Verify the response after giving doctype as "lead-scheme" template as "lead-scheme.html" and in "doc_params" keep "number_of_securities" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_36():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "lead-scheme",
        "template": "lead-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452


#Verify the response after giving doctype as "lead-scheme" template as "lead-scheme.html" and in "doc_params" keep "price_per_share" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_37():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "lead-scheme",
        "template": "lead-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452

#Verify the response after giving doctype as "lead-scheme" template as "lead-scheme.html" and in "doc_params" keep "conversion_price_ccps" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_38():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "lead-scheme",
        "template": "lead-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 200

#Verify the response after giving doctype as "lead-scheme" template as "lead-scheme.html" and in "doc_params" keep "transaction_fee as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_39():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "lead-scheme",
        "template": "lead-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452

#Verify the response after giving doctype as "lead-scheme" template as "lead-scheme.html" and in "doc_params" keep "distribution_waterfall": "contributor_share" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_40():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "lead-scheme",
        "template": "lead-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "",
                    "others_share": "5"
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452

#Verify the response after giving doctype as "lead-scheme" template as "lead-scheme.html" and in "doc_params" keep "distribution_waterfall": "others_share" as " " and remaing parameters valid.

def test_schemedoc_get_scheme_doc_41():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "lead-scheme",
        "template": "lead-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": ""
                },
                "last_date_of_consent": "June 30 2022"
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452

#Verify the response after giving doctype as "lead-scheme", template as "lead-scheme.html" and valid "doc_params"

def test_schemedoc_get_scheme_doc_42():

#API URL
    urls = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/schemedoc_get_scheme_doc/"
#Read Input Json file
    payload = json.dumps(

  {
        "doctype": "lead-scheme",
        "template": "lead-scheme.html",
        "doc_params":
            {
                "angel_fund_name": "LV Angel Fund",
                "sebi_registration_number": "IN/AIF1/18-19/0585",
                "investment_scheme_name": "required",
                "lead_investor_name": "eunimart scheme3",
                "portfolio_entity_name": "eunimart",
                "portfolio_entity_profile": "The Portfolio Entity is engaged in the business of testing",
                "portfolio_entity_industry": "Retail, Logistics, AI, E-commerce, Platform",
                "portfolio_entity_premoney_valuation": " 15,00,00,000",
                "investment_highlights": {
                    "total_round_size":  "20,000",
                    "scheme_investment_limit": "2,00,00,000"
                },
                "security_type": "CCDS",
                "ccds": "ccds",
                "number_of_securities": "12121211",
                "price_per_share": "121211",
                "conversion_price_ccps": "Not Applicable",
                "transaction_fee": "1",
                "distribution_waterfall": {
                    "contributor_share": "95",
                    "others_share": "5"
                },
                "last_date_of_consent": ""
            }
    })
#headers
    headers = {'Authorization':  cred.authorization1,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
    response = requests.post(urls,  data=payload, headers=headers)        
    response_data = response.json()
    status = response_data["Status"]
    assert status == 452