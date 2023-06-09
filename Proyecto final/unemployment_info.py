from unemployment_rate import unemployment_rate
from salary import salary_data_by_sex
import tkinter as tk
from scipy import stats
import numpy as np
import math as math

def unemployment_stimation(data_frame):
    rate = unemployment_rate(data_frame)
    population =  1757161
    unemployment_population =  population * rate
    
    confident_level = 0.95
    variance  = rate * ( 1 - rate)
    standard_deviation  = math.sqrt(variance / data_frame['PEA'].value_counts()[1])
    error_standar = standard_deviation * population
    
    conf_int = stats.norm.interval(0.95, loc=unemployment_population, scale=error_standar)
    
    stimation_info = f'''-----------EJERCICIO B ESTIMACIÓN-----------\n
                        \n
                        Estimando que la población activa es de {population} y con una tasa de desemplo de {rate} se puede estimar que:          
                        \na) Población desempleada: {math.ceil(unemployment_population)}
                        \nb) Intervalo de confianza ({confident_level*100}%): {(math.floor(conf_int[0]), math.ceil(conf_int[1]))}'''
                        
    unemployment_rate_2021 = 0.07

    statistic, p_value = stats.ttest_ind([unemployment_rate_2021], rate, alternative='greater')
    
    one_tail = p_value
    
    men_salaries = salary_data_by_sex(data_frame, sex=1)
    woman_salaries = salary_data_by_sex(data_frame, sex=2)
    
    t_statistic, p_value = stats.ttest_ind(men_salaries, woman_salaries)
    
    comparative_info = f'''-----------EJERCICIO C PRUEBA DE HIPÓTESIS-----------\n
                        \n
                        1) Dada una tasa de desempleo en el 2021 de 7,0% Y con una certeza del 95%, se puede decir que:          
                        \n{'Hya una diferencia en la tasa de desempleo ' if one_tail < (1 - confident_level) else 
                        'No se puede asegurar una diferencia en la tasa de desempleo'}
                        p valor = {one_tail}
                        \n\n
                        2) Con una certeza del 99%, si se distingue el salario por genero, se puede decir que:\n
                        {'Hay una diferencia de salarios entre hombres y mujeres' if p_value < (1 - 0.99) else 'No hay una diferencia de salariso entre hombres y mujeres' }'''

    window = tk.Tk()
    tk.Label(window, text=stimation_info, relief="solid", borderwidth=2, font=("Arial", 12)).pack()
    tk.Label(window, text='\n\n\n', font=("Arial", 12)).pack()
    tk.Label(window, text=comparative_info, relief="solid", borderwidth=2, font=("Arial", 12)).pack()
    window.mainloop()
