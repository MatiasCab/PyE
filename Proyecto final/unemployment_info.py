from unemployment_rate import unemployment_rate
from salary import salary_data_by_sex
import tkinter as tk
from scipy import stats
import numpy as np

def unemployment_stimation(data_frame):
    rate = unemployment_rate(data_frame)
    population =  1757161
    unemployment_population =  population * rate
    
    confident_level = 0.95
    error_margin = stats.norm.ppf(1 - (1 - confident_level) / 2) * np.sqrt(rate * (1 - rate) / population)

    confident_interval = (unemployment_population - error_margin, unemployment_population + error_margin)
    
    stimation_info = f'''-----------EJERCICIO B ESTIMACION-----------\n
                        \n
                        Estimando que la poblacion activa es de {population} y con una tasa de desemplo de {rate} se puede estimar que:          
                        \na) Poblacion desempleada: {unemployment_population}
                        \nb) Intervalo de confianza ({confident_level*100}%): {confident_interval}'''
                        
    unemployment_rate_2021 = 0.07
    print(rate)
    statistic, p_value = stats.ttest_ind([unemployment_rate_2021], rate, alternative='greater') #Prueba de una cola.
    #p_value es como el porcentaje de confianza que dice que el primer paramtro es mayor o igual al segundo
    one_tail = p_value
    
    men_salaries = salary_data_by_sex(data_frame, sex=1)
    woman_salaries = salary_data_by_sex(data_frame, sex=2)
    
    t_statistic, p_value = stats.ttest_ind(men_salaries, woman_salaries)
        
    comparative_info = f'''-----------EJERCICIO C PRUEBA DE HIPÓTESIS-----------\n
                        \n
                        1) Dada una tasa de desempleo en el 2021 de 7,0% Y con una certeza del 95%, se puede decir que:          
                        \n{'Si, la tasa de desempleo actual aumento respecto a 2021' if one_tail < (1 - confident_level) else 
                        'No se puede asegurar con certeza el aumento en la tasa de desempleo'}
                        p valor = {one_tail}
                        \n\n
                        2) Con una certeza del 99%, si se distingue el salario por genero, se puede decir que:\n
                        {'Los hombres generalmnete ganan mas que las muejeres' if p_value < (1 - 0.99) else 'Las mujeres generalmnete ganan mas que los hombres' }''' #FIXME ESTA BIEN ESTAS CONCLUSIONES?
        
    
    #En el de los salarios preguntar por la aleatoriedad y el 99%.
    window = tk.Tk()
    tk.Label(window, text=stimation_info, relief="solid", borderwidth=2, font=("Arial", 12)).pack()
    tk.Label(window, text='\n\n\n', font=("Arial", 12)).pack()
    tk.Label(window, text=comparative_info, relief="solid", borderwidth=2, font=("Arial", 12)).pack()
    window.mainloop()

