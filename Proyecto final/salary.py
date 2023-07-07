import matplotlib.pyplot as plt
import pandas as pd
from statistics import median, mode
from numpy import mean
#FIXME PREGUNTAR ESTO.
def salary_data(data_frame, min_salary = 0, max_salary = 100000000):
    data_frame['Salario'] = pd.to_numeric(data_frame['Salario'], errors='coerce')
    valid_salary = data_frame[(data_frame['Salario'] > min_salary) & (data_frame['Salario'] <= max_salary)]
    return valid_salary['Salario']

def salary_data_by_sex(data_frame, min_salary = 0, max_salary = 100000000, sex=1):
    data_frame['Salario'] = pd.to_numeric(data_frame['Salario'], errors='coerce')
    valid_salary = data_frame[(data_frame['Sexo'] == sex) & (data_frame['Salario'] > min_salary) & (data_frame['Salario'] <= max_salary)]
    return valid_salary['Salario']

def salary_data_by_location(data_frame, min_salary = 0, max_salary = 100000000, locations=[]):
    data_frame['Salario'] = pd.to_numeric(data_frame['Salario'], errors='coerce')
    valid_salary = data_frame[(data_frame['region'].isin(locations)) & (data_frame['Salario'] > min_salary) & (data_frame['Salario'] <= max_salary)]
    return valid_salary['Salario']

def salary_graphics(data_frame):
    fig, ((hist1, hist2), (box1, box2)) = plt.subplots(2, 2, figsize=(12, 9))
    
    unlimited_data = salary_data(data_frame)
    hist1.hist(unlimited_data, color="Red",bins = int(180/5))
    
    limited_data = salary_data(data_frame, min_salary=1, max_salary=9999999)
    hist2.hist(limited_data, color="Blue",bins = 150)
    box1.boxplot(limited_data)
    box2.boxplot(limited_data, showfliers=False)
    
    min_value = limited_data.min()
    max_value = limited_data.max()
    Q1 = limited_data.quantile(0.25)
    Q2 = limited_data.quantile(0.5)
    Q3 = limited_data.quantile(0.75)
    text = f'Mediana: {median(limited_data)}\nModa: {mode(limited_data)}\nMedia: {round(mean(limited_data), 2)}\nMinimo: {min_value}\nMaximo: {max_value}\nCuartil Q1: {Q1}\nCuartil Q2: {Q2}\nCuartil Q3: {Q3}'
    box2.text(0.04, 0.5, text, transform=box2.transAxes, fontsize=10,
                 bbox=dict(facecolor='white', edgecolor='black', alpha=0.6),
                 ha='left')
    
    
    plt.tight_layout()
    plt.show()

def box_info(graph, data):
    min_value = data.min()
    max_value = data.max()
    Q1 = data.quantile(0.25)
    Q2 = data.quantile(0.5)
    Q3 = data.quantile(0.75)
    text = f'Mediana: {median(data)}\nModa: {mode(data)}\nMedia: {round(mean(data), 2)}\nMinimo: {min_value}\nMaximo: {max_value}\nCuartil Q1: {Q1}\nCuartil Q2: {Q2}\nCuartil Q3: {Q3}'
    graph.text(0.04, 0.5, text, transform=graph.transAxes, fontsize=10,
                 bbox=dict(facecolor='white', edgecolor='black', alpha=0.6),
                 ha='left')

def salary_graphics_by_sex_and_locations(data_frame):
    fig, ((box1, box2), (box3, box4)) = plt.subplots(2, 2, figsize=(12, 9))
    
    salary_by_sex_men = salary_data_by_sex(data_frame, sex=1)
    box1.boxplot(salary_by_sex_men)
    box1.set_title('Hombres')
    
    
    salary_by_sex_woman = salary_data_by_sex(data_frame, sex=2)
    box2.boxplot(salary_by_sex_woman)
    box2.set_title('Mujeres')
    
    salary_by_location_capital = salary_data_by_location(data_frame, locations=[1])
    box3.boxplot(salary_by_location_capital)
    box3.set_title('Capital')
    
    salary_by_location_inter = salary_data_by_location(data_frame, locations=[2, 3])
    box4.boxplot(salary_by_location_inter)
    box4.set_title('Interior')
    
    box_info(box1, salary_by_sex_men)
    box_info(box2, salary_by_sex_woman)
    box_info(box3, salary_by_location_capital)  
    box_info(box4, salary_by_location_inter)
    
    plt.tight_layout()
    plt.show()