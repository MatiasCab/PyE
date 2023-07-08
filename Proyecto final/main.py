from salary import salary_graphics, salary_graphics_by_sex_and_locations
from unemployment_rate import unemployment_rate_graphics
from unemployment_info import unemployment_stimation
import pandas as pd

#FIXME NOMBRES DE CONVENCION

data_path = 'ECH_2022.csv'

data_frame = pd.read_csv(data_path, delimiter= ';')

unemployment_rate_graphics(data_frame)  
salary_graphics(data_frame)
salary_graphics_by_sex_and_locations(data_frame)
unemployment_stimation(data_frame)


#Se descartan datos, maximo de 8 cifras en la parte 2 del 1
#Auth no se que son los datos atipicos.
#Salarios: Salarios>0
#PEA: Ocupados + Desocupados
#Las colas sirven: (Sus analisis son valorados)



#No puedo decir que el valor de tasa de desempleo es mas grande.
#Preguntar lo del boxplot
#Explicar lo de H0
#Por la ley de grades numeros supones que nuestra muestra es representativa del total.
#Se pone el decimel en cantidad de desempleados? Se saca eldecimla y se redondea para arriba.
#en el intervalo de confianza el de abajo para abajo el de arriba para arriba.
#LO DEDIVIDIR LA DIFERENCIA DE LMENOOR Y MAYOR CON EL UN MILON PARA TENER ELÑ PORCENTAJE DE DIFERENCIA


#Poner que son distintas
#Widh de 20 pone guolle.
#Inferir lo de los hombres.

#El de hist es por rango de edad
#El de la torta del total.

#Varianza Tada de Desempelo = Tasa desempleo * (1 - Tasa desempleo)
#desvio estandar de la muestra = sqr(Varianza TDesempelo / PEA de la muestra (mi muestra))
#desvio estandar desempleo = PEA del 2021 (el millon y pico.) * desvio estandar de la muestra
