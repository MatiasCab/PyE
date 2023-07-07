from salary import salary_graphics, salary_graphics_by_sex_and_locations
from unemployment_rate import unemployment_rate_graphics
from unemployment_info import unemployment_stimation
import pandas as pd

#FIXME NOMBRES DE CONVENCION

data_path = 'ECH_2022.csv'

data_frame = pd.read_csv(data_path, delimiter= ';')

#unemployment_rate_graphics(data_frame)  
#salary_graphics(data_frame)
#salary_graphics_by_sex_and_locations(data_frame)
unemployment_stimation(data_frame)


#Se descartan datos, maximo de 8 cifras en la parte 2 del 1
#Auth no se que son los datos atipicos.
#Salarios: Salarios>0
#PEA: Ocupados + Desocupados
#Las colas sirven: (Sus analisis son valorados)
