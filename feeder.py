import json
import requests


def get_chain_list():
    url = 'https://api.unitap.app/api/v1/chain/small-list/'
    data = requests.get(url).json()
    return data


def get_chain_balance(chain_id):
    url = f'https://api.unitap.app/api/v1/chain/{chain_id}/balance/'
    data = requests.get(url).json()
    return data


def get_all_chain_balances():
    chains = get_chain_list()
    balances = []
    for chain in chains:
        try:
            balances.append(get_chain_balance(chain['pk']))
        except json.decoder.JSONDecodeError:
            print(f"error for chain {chain['pk']}")
    return balances
