from datetime import datetime as dt
from time import time
from pathlib import Path




def data_logger(q, w, e, r):
    path_loger = Path('Homework','HM8','folder', 'logger.csv')
    time = dt.now().strftime('%Y:%m:%d  %H:%M')
    with open(path_loger, 'a') as log_file:
        log_file.write('-----------------------------------------------')
        log_file.write('\nTime of adding new data: {}\n'.format(time))
        
        log_file.write('\nName: {} \nSurename: {} \nSex: {} \nNumber: {}\n'
                        .format(q, w, e, r))
