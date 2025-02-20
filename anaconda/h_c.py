import numpy as np

'''
c_p = current_position
c_v = current_value
n_p_p = next_position_position
n_v_p = next_value_positive
n_p_n = next_position_negative
n_v_n = next_value_negative
'''

def hill_climbing(func, start):
    c_p = start
    c_v = func(c_p)
    step_size=0.01
    
    for i in range(1000):
        n_p_p = c_p + step_size
        n_v_p = func(n_p_p)
        
        n_p_n = c_p - step_size
        n_v_n = func(n_p_n)
        
        if n_v_p > c_v and n_v_p >= n_v_n:
            c_p = n_p_p
            c_v = n_v_p
        elif n_v_n > c_v and n_v_n > n_v_p:
            c_p = n_p_n
            c_v = n_v_n
        else:
            break
    
    return c_p, c_v

func_str = input("\nEnter a function of x: ")

func = lambda x: eval(func_str)

start = float(input("\nEnter the starting value to begin the search: "))
maxima, max_value = hill_climbing(func, start)

print(f"The maxima is at x = {maxima}")
print(f"The maximum value obtained is {max_value}")
