import pandas as pd

data = pd.read_csv('input.csv')

data['Вес'] = data['Тип операции'].map({'Привоз': 1, 'Вывоз': -1})

data['Баланс'] = data['Объем груза'] * data['Вес']

answer = (data.groupby('Фамилия водителя', as_index = False)['Баланс'].sum().rename(columns = {'Баланс': 'Объем груза'}))

answer = answer.sort_values(by = ['Объем груза', 'Фамилия водителя'], ascending = [False, True])

answer.to_csv('output.csv', index = False)
