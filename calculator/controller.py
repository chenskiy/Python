import model_sub as sub
import model_mult as mult
import model_sum as sum
from logger import data_logger
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    znak = view.get_znak()

    # model.init(value_a, value_b)
    
    if znak == '+':
        sum.init(value_a, value_b)
        result = sum.do_it()
    elif znak == '*':
        mult.init(value_a, value_b)
        result = mult.do_it()
    elif znak == '-':
        sub.init(value_a, value_b)
        result = sub.do_it()   

    view.view_data(result, 'result')
    
    
    data_logger(value_a, value_b, result, znak)