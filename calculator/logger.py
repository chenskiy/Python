from datetime import datetime as dt
from time import time
from pathlib import Path




def data_logger(x, y, z, l):
   
    path_loger = Path("calculator", "logger.csv")
    time = dt.now()#.strftime('%H:%M')
    with open(path_loger, 'a') as log_file:
        log_file.write('-----------------------------------------------')
        
        log_file.write('\nTime of adding new data: {}\n'.format(time))
        
        log_file.write('\nNum1: {} {} Num2: {} \nResult: {}\n'
                        .format(x, l, y, z))
