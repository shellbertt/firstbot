import os.path

FIRST_LOCK = "./first_msg.txt"

async def first_msg_exists():
    return os.path.exists(FIRST_LOCK)
