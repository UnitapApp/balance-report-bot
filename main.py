import time
import schedule
from feeder import get_all_chain_balances
from bot import send_message


def report():
    data = get_all_chain_balances()
    send_message(data)


report()

# schedule the function to run every 6 hours
# schedule.every(6).hours.do()

# while True:
#     schedule.run_pending()
#     time.sleep(69)
