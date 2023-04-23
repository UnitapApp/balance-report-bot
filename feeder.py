import requests


def get_chain_list():
    url = 'https://stage.unitap.app/api/v1/chain/small-list/'
    data = requests.get(url).json()
    return data


def get_chain_balance(chain_id):
    url = f'https://stage.unitap.app/api/v1/chain/{chain_id}/balance/'
    data = requests.get(url).json()
    return data


def get_all_chain_balances():
    chains = get_chain_list()
    balances = []
    for chain in chains:
        balances.append(get_chain_balance(chain['pk']))
    return balances
