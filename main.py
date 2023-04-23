import time
import schedule
from feeder import get_all_chain_balances
from bot import send_message

links = {}


def report():
    data = get_all_chain_balances()
    text = "Chain Balances:\n"
    # for chain in data:
    t = """Chain: Fantom 
Type: EVM

Contract Address: 6284758451:AAELuZzT9h2ZCubQ_LxWwTPoqYFe3lR9CsI

Wallet Address: 0xB10f8E218A9cD738b0F1E2f7169Aa3c0897F2d83"""
    send_message(str(data))


report()

# schedule the function to run every 6 hours
# schedule.every(6).hours.do()

# while True:
#     schedule.run_pending()
#     time.sleep(69)
