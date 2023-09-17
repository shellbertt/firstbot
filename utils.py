import os
import os.path
from datetime import datetime

FIRST_LOCK = "./first_msg.txt"

def first_msg_exists():
    return os.path.exists(FIRST_LOCK)

async def reset_old_first():
    if not first_msg_exists():
        return
   
   cur_day = datetime.today().date()
   last_claimed_day = date.fromtimestamp(os.path.getctime(FIRST_LOCK)).date()
   if cur_day > last_claimed_day:
       os.remove(FIRST_LOCK)

