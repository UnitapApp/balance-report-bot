import time
import schedule
from feeder import get_all_chain_balances
from bot import send_message

links = {}


def report():
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
        
        print(links)


report()

# schedule the function to run every 6 hours
# schedule.every(6).hours.do()

# while True:
#     schedule.run_pending()
#     time.sleep(69)
