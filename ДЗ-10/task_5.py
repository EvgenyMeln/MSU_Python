import pandas as pd

data = pd.read_csv('input.csv')

data['Маршрут'] = data['Город прибытия'] + '-' + data['Город отправления']

answer = data.groupby('Номер борта')['Маршрут'].nunique().reset_index()

answer.rename(columns={'Маршрут': 'Уникальных маршрутов'}, inplace = True)

answer.sort_values(by = ['Уникальных маршрутов', 'Номер борта'], ascending = [False, True], inplace = True)

answer.to_csv('output.csv', index = False)
