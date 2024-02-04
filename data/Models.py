import requests
import json


async def create_profile(user_id):
    requests.post('https://chupa-pupa-29ab2bbfb5f8.herokuapp.com//createProfile/'
                  + str(user_id))


async def edit_profile(user_id, value):
    headers = {'Content-Type': 'application/json'}
    body = [user_id, value]
    requests.post('https://chupa-pupa-29ab2bbfb5f8.herokuapp.com/editValue',
                  json=body, headers=headers)


def return_value(user_id):
    response = requests.get('https://chupa-pupa-29ab2bbfb5f8.herokuapp.com/balanceValue/'
                            + str(user_id))
    result = json.loads(response.text)
    return result['balance']


def check_user(user_id):
    response = requests.get('https://chupa-pupa-29ab2bbfb5f8.herokuapp.com/checkUser/'
                            + str(user_id))
    result = json.loads(response.text)
    return result['check']
