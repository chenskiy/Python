from datetime import datetime as dt
from time import time
from pathlib import Path




def data_logger(x, y, z):
    path_add = Path("HM7", "classmates.csv")
    path_loger = Path("HM7", "logger.csv")
    time = dt.now().strftime('%H:%M')
    with open(path_loger, 'a') as log_file:
        log_file.write('-----------------------------------------------')
        log_file.write('\nTime of adding new data: {}\n'.format(time))
        
        # log_file = csv.writer(path_loger, delimiter = ",", lineterminator="\r")
        log_file.write('\nName: {} \nNumber: {} \nCity: {}\n'
                        .format(x, y, z))
