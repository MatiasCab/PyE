import matplotlib.pyplot as plt

def unemployment_rate(data_frame):
    pea = data_frame['PEA'].value_counts()[1]
    unemployment_people = data_frame['Desempleo'].value_counts()[1]
    return unemployment_people/pea

def unemployment_rate_by_age(data_frame, min_age, max_age):
    min_age = min_age if min_age > 13 else 14
    max_age = max_age if max_age > 13 else 100
    
    pea = data_frame[(data_frame['PEA'] == 1) & (data_frame['Edad'] >= min_age) & (data_frame['Edad'] <= max_age)]
    unemployment_people_count = pea['Desempleo'].value_counts()[1]
    return unemployment_people_count/ len(pea)

def unemployment_rate_graphics(data_frame):
    fig, ((bar, pie)) = plt.subplots(1, 2, figsize=(7, 2))
    ages_interval = [(14, 17), (18, 25), (26, 40), (41, -1)]
    ages_intervals_info = {}
    
    for i in ages_interval:
        age_unemployment_rate = unemployment_rate_by_age(data_frame, i[0], i[1])#FIXME PODIRA IR EN OTRO LADO
        label = ''
        if (i[0] < 14):
            label = f'Menor a {i[1]}'
        elif (i[1] < 14):
            label = f'Mayor a {i[0]}'
        else:
            label = f'{i[0]} - {i[1]}'
        
        ages_intervals_info[label] = age_unemployment_rate

    pie.pie(ages_intervals_info.values(), labels=ages_intervals_info.keys(), autopct='%1.2f%%')
    bar.bar(ages_intervals_info.keys(), ages_intervals_info.values())
    
    rate = unemployment_rate(data_frame)*100
    text = f"La tasa de desempleo es de {round(rate, 2)}%"
    
    plt.tight_layout()
    plt.title(text)
    plt.axis('equal')
    plt.show()