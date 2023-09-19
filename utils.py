import logging
import os
import os.path
from datetime import datetime

FIRST_LOCK = "./first_msg.txt"

def claim_exists():
    return os.path.exists(FIRST_LOCK)

async def remove_old_claim():
    if not claim_exists():
        return
   
    cur_day = datetime.today().date()
    prev_day_claimed = datetime.fromtimestamp(os.path.getctime(FIRST_LOCK)).date()
    if cur_day > prev_day_claimed:
        os.remove(FIRST_LOCK)
        logging.debug(f"Claim from {prev_day_claimed} removed.")
    else:
        logging.debug(f"Claim from {prev_day_claimed} not removed.")

