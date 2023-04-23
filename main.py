import time
import schedule
from feeder import get_all_chain_balances
from bot import send_message

links = {}


def set_linked_and_pinned():
    data = get_all_chain_balances()
    text = "Chain Balances:\n"
    for chain in data:
        t = f"""Chain: {chain["chainName"]} 
Type: {chain["chainType"]}

Contract Address: `{chain["blockScanAddress"].split("/")[-1]}`

Wallet Address: `{chain["wallet"]}`"""
        response = send_message(str(t))
        message_id = response["result"]["message_id"]
        links[chain["chainName"]
              ] = f"https://t.me/unitapchainbalances/{message_id}"

    c = 0
    p = "Gas Tap Chains:\n\n"
    for chain in data:
        if c % 2 == 0:
            p += "\u25AA"
        else:
            p += "\u25AB"
        p += f"""[{chain["chainName"]}]({links[chain["chainName"]]})\n"""
    
    resp = send_message(p)
    


set_linked_and_pinned()

# schedule the function to run every 6 hours
# schedule.every(6).hours.do()

# while True:
#     schedule.run_pending()
#     time.sleep(69)
