import pytest
import requests
import json
import cred



#Verify the response after giving doctype as "termsheets-standard-draft" and valid "doc_params"
 
def test_fetch_termsheets_1():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 200




#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "company_details": "company_name" as "" and remaining valid values
def test_fetch_termsheets_2():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "company_details": "company_business" as "" and remaining valid values
def test_fetch_termsheets_3():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "company_details": "number_of_shares" as "" and remaining valid values
def test_fetch_termsheets_4():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" remove "company_details": "number_of_shares" and remaining valid values
def test_fetch_termsheets_5():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452






#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "company_details": "paid_up_capital_per_share" as "" and remaining valid values
def test_fetch_termsheets_6():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
    "doctype": "termsheets-standard-draft",
    "doc_params": {
        "company_details": {
            "company_name": "VAR-ABCTech",
            "company_business": "VAR-IT",
            "number_of_shares": "VAR-100000",
            "paid_up_capital_per_share": "",
            "promoters_capital_holding": "VAR-100000",
            "promoters": [
                {
                    "name": "VAR-promoter1",
                    "email": "VAR-promoter1@sdf.com"
                },
                {
                    "name": "VAR-promoter2"
                },
                {
                    "name": "VAR-promoter3"
                }
            ],
            "signatory": {
                "name": "VAR-Archimedha Mohapatra",
                "title": "VAR-Mr"
            }
        },
        "scheme_details": {
            "termsheet_execution_date": "VAR-2022-06-25",
            "preference_share_face_value": "VAR-25`",
            "preference_share_subscription_value": "VAR-15",
            "investment_amount": "VAR-15000000",
            "pre_money_valuation": "VAR-20000000",
            "post_close_number_of_directors": "VAR-5",
            "post_close_number_of_promoter_directors": "VAR-3",
            "promoter_vested_shares": "VAR-15%",
            "promoter_remaining_shares": "VAR-85%",
            "post_close_esop": "VAR-10%",
            "pre_closing_shareholding": [
                {
                    "name": "VAR-P1",
                    "number_shares": "VAR-10000",
                    "percentage_shareholding": "VAR-50"
                },
                {
                    "name": "VAR-P2",
                    "number_shares": "VAR-10000",
                    "percentage_shareholding": "VAR-50"
                }

            ],
            "post_closing_shareholding": [
                {
                    "name": "VAR-P1",
                    "number_shares": "VAR-300000",
                    "percentage_shareholding": "VAR-30"
                },
                {
                    "name": "VAR-P2",
                    "number_shares": "VAR-300000",
                    "percentage_shareholding": "VAR-30"
                },
                {
                    "name": "VAR-P3",
                    "number_shares": "VAR-400000",
                    "percentage_shareholding": "VAR-40"
                }
            ]
        },
        "investor_details": [
            {
                "name": "VAR-Investor1",
                "title": "VAR-Mr.",
                "investment_amount": "VAR-100000",
                "percentage_shareholding": "VAR-20"
            },
            {
                "name": "VAR-Investor2",
                "title": "VAR-Mr.",
                "investment_amount": "VAR-100000",
                "percentage_shareholding": "VAR-20"
            },
            {
                "name": "VAR-Investor3",
                "title": "VAR-Ms.",
                "investment_amount": "VAR-100000",
                "percentage_shareholding": "VAR-20"
            },
            {
                "name": "VAR-Investor4",
                "title": "VAR-Mr.",
                "investment_amount": "VAR-100000",
                "percentage_shareholding": "VAR-20"
            },
            {
                "name": "VAR-Investor5",
                "title": "VAR-Ms.",
                "investment_amount": "VAR-100000",
                "percentage_shareholding": "VAR-20"
            }
        ]
}
})
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "company_details": "promoters_capital_holding" as "" and remaining valid values
def test_fetch_termsheets_7():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "promoters": "name" as "" and remaining valid values
def test_fetch_termsheets_8():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452





#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "promoters": "phone" as "" and remaining valid values   
def test_fetch_termsheets_9():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": ""
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "promoters": "email" as "" and remaining valid values
def test_fetch_termsheets_10():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452





#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "promoters": 2nd "name" as "" and remaining valid values
def test_fetch_termsheets_11():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "promoters": 3rd "name" as "" and remaining valid values
def test_fetch_termsheets_12():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452






#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "signatory": "name" as "" and remaining valid values
def test_fetch_termsheets_13():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "signatory": "title" as "" and remaining valid values
def test_fetch_termsheets_14():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452





#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "scheme_details": "termsheet_execution_date" as "" and remaining valid values
def test_fetch_termsheets_15():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452





#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "scheme_details": "preference_share_face_value" as "" and remaining valid values
def test_fetch_termsheets_16():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "scheme_details":  "preference_share_subscription_value" as "" and remaining valid values
def test_fetch_termsheets_17():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452





#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "scheme_details":  "investment_amount" as "" and remaining valid values
def test_fetch_termsheets_18():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "signatory":  "email" as "" and remaining valid values
def test_fetch_termsheets_19():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "scheme_details":  "pre_money_valuation" as "" and remaining valid values
def test_fetch_termsheets_20():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452





#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "scheme_details":  "post_close_number_of_directors" as "" and remaining valid values
def test_fetch_termsheets_21():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452





#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "scheme_details":  "post_close_number_of_promoter_directors" as "" and remaining valid values
def test_fetch_termsheets_22():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452






#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "scheme_details":  "promoter_vested_shares" as "" and remaining valid values
def test_fetch_termsheets_23():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452





#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "scheme_details":  "promoter_remaining_shares" as "" and remaining valid values
def test_fetch_termsheets_24():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "scheme_details":  "post_close_esop" as "" and remaining valid values
def test_fetch_termsheets_25():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452





#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "pre_closing_shareholding": "name" as "" and remaining valid values
def test_fetch_termsheets_26():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452





#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "pre_closing_shareholding":"number_shares" as "" and remaining valid values
def test_fetch_termsheets_27():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452





#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "pre_closing_shareholding":"percentage_shareholding" as "" and remaining valid values
def test_fetch_termsheets_28():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": ""
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452





#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "pre_closing_shareholding": 2nd "name" as "" and remaining valid values
def test_fetch_termsheets_29():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "pre_closing_shareholding":2nd "number_shares" as "" and remaining valid values
def test_fetch_termsheets_30():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452






#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "pre_closing_shareholding":2nd "percentage_shareholding" as "" and remaining valid values
def test_fetch_termsheets_31():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": ""
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "post_closing_shareholding":"name" as "" and remaining valid values
def test_fetch_termsheets_32():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


######################################################################################################################################################################
######################################################################################################################################################################
#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "post_closing_shareholding":"number_shares" as "" and remaining valid values

 
def test_fetch_termsheets_33():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "post_closing_shareholding":"percentage_shareholding" as "" and remaining valid values
def test_fetch_termsheets_34():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": ""
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "post_closing_shareholding":2nd "name" as "" and remaining valid values
def test_fetch_termsheets_35():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "post_closing_shareholding":2nd "number_shares" as "" and remaining valid values
def test_fetch_termsheets_36():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "post_closing_shareholding":2nd "percentage_shareholding" as "" and remaining valid values
def test_fetch_termsheets_37():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": ""
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452






#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "post_closing_shareholding":3rd "name" as "" and remaining valid values
def test_fetch_termsheets_38():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "post_closing_shareholding":3rd "number_shares" as "" and remaining valid values
def test_fetch_termsheets_39():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "post_closing_shareholding":3rd "percentage_shareholding" as "" and remaining valid values
def test_fetch_termsheets_40():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": ""
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452





#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":"name" as "" and remaining valid values   
def test_fetch_termsheets_41():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":"title" as "" and remaining valid values
def test_fetch_termsheets_42():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452





#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":"investment_amount" as "" and remaining valid values
def test_fetch_termsheets_43():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":"percentage_shareholding" as "" and remaining valid values
def test_fetch_termsheets_44():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452






#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":2nd "name" as "" and remaining valid values
def test_fetch_termsheets_45():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":2nd "title" as "" and remaining valid values
def test_fetch_termsheets_46():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452





#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":2nd "investment_amount" as "" and remaining valid values
def test_fetch_termsheets_47():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452





#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":2nd "percentage_shareholding" as "" and remaining valid values
def test_fetch_termsheets_48():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452




#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":3rd "name" as "" and remaining valid values
def test_fetch_termsheets_49():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452





#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":3rd "title" as "" and remaining valid values
def test_fetch_termsheets_50():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}
#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":3rd "investment_amount" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_51():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":3rd "percentage_shareholding" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_52():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":4th "name" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_53():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":4th "title" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_54():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":4th "investment_amount" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_55():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":4th "percentage_shareholding" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_56():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving doctype as  "termsheets-standard-draft" and  "doc_params" give "investor_details":5th "name" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_57():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":5th "title" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_58():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":5th "investment_amount" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_59():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms",
                    "investment_amount": "",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":5th "percentage_shareholding" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_60():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}   

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452



#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "promoters": 2nd "email" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_61():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "promoters": 2nd "phone" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_62():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": ""
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "promoters": 3rd "email" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_63():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "promoters": 3rd "phone" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_64():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": ""
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "signatory": "phone" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_65():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": ""
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": ""
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":"email" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_66():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": ""
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":"phone" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_67():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": ""
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": ""
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":2nd "email" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_68():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": ""
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":2nd "phone" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_69():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": ""
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": ""
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":3rd "email" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_70():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": ""
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":3rd "phone" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_71():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": ""
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": ""
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":4th "email" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_72():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":4th "phone" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_73():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": ""
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": ""
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452


#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":5th "email" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_74():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": ""
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}


#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452

#Verify the response after giving doctype as "termsheets-standard-draft" and  "doc_params" give "investor_details":5th "phone" as "" and remaining valid values, Response status should be 452
def test_fetch_termsheets_75():

#API URL
        url = "http://iaas-env.eba-aykcnmq8.ap-south-1.elasticbeanstalk.com/fetch_termsheets/"
#Read Input Json file
        payload = json.dumps({
        "doctype": "termsheets-standard-draft",
        "doc_params": {
            "company_details": {
                "company_name": "VAR-ABCTech",
                "company_business": "VAR-IT",
                "number_of_shares": "VAR-100000",
                "paid_up_capital_per_share": "VAR-100",
                "promoters_capital_holding": "VAR-100000",
                "promoters": [
                    {
                        "name": "VAR-promoter1",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter2",
                        "email": "archi.lv@grepdigital.com",
                        "phone": "9741601203"
                    },
                    {
                        "name": "VAR-promoter3",
                        "email": "archi.lv@grepdigital.com",
                        "phone": ""
                    }
                ],
                "signatory": {
                    "name": "VAR-Archimedha Mohapatra",
                    "title": "VAR-Mr",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            },
            "scheme_details": {
                "termsheet_execution_date": "VAR-2022-06-25",
                "preference_share_face_value": "VAR-25`",
                "preference_share_subscription_value": "VAR-15",
                "investment_amount": "VAR-15000000",
                "pre_money_valuation": "VAR-20000000",
                "post_close_number_of_directors": "VAR-5",
                "post_close_number_of_promoter_directors": "VAR-3",
                "promoter_vested_shares": "VAR-15%",
                "promoter_remaining_shares": "VAR-85%",
                "post_close_esop": "VAR-10%",
                "pre_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-10000",
                        "percentage_shareholding": "VAR-50"
                    }

                ],
                "post_closing_shareholding": [
                    {
                        "name": "VAR-P1",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P2",
                        "number_shares": "VAR-300000",
                        "percentage_shareholding": "VAR-30"
                    },
                    {
                        "name": "VAR-P3",
                        "number_shares": "VAR-400000",
                        "percentage_shareholding": "VAR-40"
                    }
                ]
            },
            "investor_details": [
                {
                    "name": "VAR-Investor1",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor2",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor3",
                    "title": "VAR-Ms.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor4",
                    "title": "VAR-Mr.",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                },
                {
                    "name": "VAR-Investor5",
                    "title": "VAR-Ms",
                    "investment_amount": "VAR-100000",
                    "percentage_shareholding": "VAR-20",
                    "email": "archi.lv@grepdigital.com",
                    "phone": "9741601203"
                }
            ]
        }
    })
#headers
        headers = {'Authorization':  cred.authorization,'Content-Type': 'application/json', 'AccessKey':cred.aws_access_key_id,
  'SecretKey':cred.aws_secret_access_key}

#Make post request with json input body
        response = requests.post(url,  data=payload, headers=headers)        
        response_data = response.json()
        status = response_data["Status"]
        assert status == 452