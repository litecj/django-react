from datetime import datetime
from icecream import ic
import time
from datetime import datetime

def time_format():
    return f'{datetime.now()}|> '

# ic.configureOutput(prefix=time_format)

ic('=======================================')
ic('======== Django REST Framework ========')
ic(time_format())
ic('=======================================')

# for _ in range(3):
#     time.sleep(1)  #sleep : 3번씩 찍어라
#     ic('Hello')