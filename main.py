import time
import schedule
from feeder import get_all_chain_balances
from bot import send_message, pin_message, send_message_plain

links = {}


def set_linked_and_pinned():
    data = get_all_chain_balances()
    text = "Chain Balances:\n"
    for chain in data:
        t = f"""Chain: {str(chain["chainName"]).replace('-', ' ').replace("(", "").replace(")", "")} 
Type: {chain["chainType"]}

Contract Address: `{chain["blockScanAddress"].split("/")[-1]}`

Wallet Address: `{chain["wallet"]}`"""
        response = send_message(str(t))
        try:
            message_id = response["result"]["message_id"]
        except KeyError:
            print(response)

        links[chain["chainName"]
              ] = f"https://t.me/unitapchainbalances/{message_id}"

    c = 0
    p = "Gas Tap Chains:\n\n"
    for chain in data:
        if c % 2 == 0:
            p += "\u25AA"
        else:
            p += "\u25AB"
        p += f"""[{chain["chainName"].replace('-', ' ').replace("(", "").replace(")", "")}]({links[chain["chainName"]]})\n"""
        c += 1

    resp = send_message(p)
    # pin_message(resp["result"]["message_id"])


green_circle = "\U0001F7E2"
red_circle = "\U0001F534"
tick = "\u2714"
cross = "\u274C"


def report():
    data = get_all_chain_balances()
    t = "Chains:\n\n"
    for chain in data:
        print(chain["needsFunding"])
        # circle color
        if chain["needsFunding"] is True:
            t += red_circle
        elif chain["needsFunding"] is False:
            t += green_circle

        # space
        t += " "

        # chain name
        t += f"{chain['chainName']}:"

        # 4 spaces
        t += " "*4

        # contract balance
        t += f"""C: {str(chain['contractBalance'] / 10**18)[:4]} {chain['symbol']} {tick if chain["hasEnoughFunds"] is True else cross}"""

        # 4 spaces
        t += " "*4

        # wallet balance
        t += f"""W: {str(chain['walletBalance'] / 10**18)[:4]} {chain['symbol']} {tick if chain["hasEnoughFees"] is True else cross}"""

        # \n
        t += "\n"

    # print(t)
    r = send_message_plain(str(t))
    print(r)


set_linked_and_pinned()
# report()

# schedule the function to run every 6 hours
# schedule.every(6).hours.do()

# while True:
#     schedule.run_pending()
#     time.sleep(69)
