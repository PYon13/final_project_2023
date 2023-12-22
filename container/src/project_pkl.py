import joblib
import pandas as pd

# Указываете путь к вашему файлу Pickle
pickle_file_path = './pipeline_rf.pkl'

# Загрузка модели из файла
loaded_model = joblib.load(pickle_file_path)

# Создаём список необходимых признаков
features = ['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 
            'Balance', 'HasCrCard', 'NumOfProducts', 'IsActiveMember', 
            'EstimatedSalary', 'Exited']

# Фиксируем конечную выборку 
last_df = pd.DataFrame(columns=features)

# Устанавливаем мигалку 
run = True

# Запускаем цикл бесконечности 
while run:
    print('Укажите метод подачи данных: \n 1 - Загрузка таблицы \n 2 - Ручной ввод данных')
    print(f'При загрузки таблицы, она должна содержать признаки: \n {features}')
    method = int(input('Укажите метод: '))

    # Фиксируем индекс 
    index = 0

    # Условие выбора метода 
    if method == 2:
    
        print('Для предсказания необходи ввести данные клиента. \n')
        # Добавляем блоки исключения под каждый признак 
        try:
            CreditScore = int(input('Введите кредитный рейтинг: '))
        except:
            print('Это не число!')
            break
        print('')

        try:
            print('Укажите страну: \n 1 - Германия \n 2 - Франция \n 3 - Испания')
            Geography = int(input('Укажите число: '))
        except:
            print('Это не число!')
            break
        print('')

        try:
            print('Укажите пол: \n 1 - Мужчина \n 2 - Женщина')
            Gender = int(input('Введите цифру: '))
        except:
            print('Это не число!')
            break
        print('')

        try: 
            Age = int(input('Введите возраст: '))
        except:
            print('Это не число!')
            break
        print('')

        try:
            Tenure = int(input('Введите количество лет работы с банком: '))
        except:
            print('Это не число!')
            break
        print('')

        try:
            Balance = float(input('Введите баланс на счетах: '))
        except:
            print('Это не число!')
            break
        print('')

        try:
            print('Укажите наличие кредитной карты: \n 1 - Нет \n 2 - Есть')
            HasCrCard = int(input('Введите число: '))
        except: 
            print('Это не число!')
            break
        print('')

        try: 
            NumOfProducts = int(input('Введите количество продуктов: '))
        except:
            print('Это не число!')
            break
        print('')

        try: 
            print('Укажите активность: \n 1 - Не активный \n 2 - Активный')
            IsActiveMember = int(input('Введите число: '))
        except:
            print('Это не число!')
            break
        print('')

        try:
            EstimatedSalary = float(input('Укажите сумму заработной платы: '))
        except: 
            print('Это не число!')
            break

        # Редактируем полученные данные для подачи в модель 
        if Geography == 1:
            Geography = 1
        elif Geography == 2:
            Geography = 0
        elif Geography == 3:
            Geography = 2
        else:
            print('Вы ввели неверные данные!')
            break 

        if Gender == 1:
            Gender = 1
        elif Gender == 2:
            Gender = 0
        else: 
            print('Вы ввели неверные данные!')
            break

        if HasCrCard == 1:
            HasCrCard = 0
        elif HasCrCard == 2:
            HasCrCard = 1
        else: 
            print('Вы ввели неверные данные!')
            break
    
        if IsActiveMember == 1:
            IsActiveMember = 0
        elif IsActiveMember == 2:
            IsActiveMember = 1
        else: 
            print('Вы ввели неверные данные!')
            break
    
        # Теперь формируем словарь с данными 
        df_dict = {
            'CreditScore': [CreditScore],
            'Geography': [Geography],
            'Gender': [Gender],
            'Age': [Age],
            'Tenure': [Tenure],
            'Balance': [Balance],
            'HasCrCard': [HasCrCard],
            'NumOfProducts': [NumOfProducts],
            'IsActiveMember': [IsActiveMember],
            'EstimatedSalary': [EstimatedSalary]
        }

        # Превращаем словарь в таблицу 
        df = pd.DataFrame(df_dict)

        # Получаем предсказание 
        predict_model_rf = loaded_model.predict(df)

        # Выводим результат 
        if predict_model_rf == 0:
            print('Лояльный клиент.\n')
            df['Exited'] = 'Лояльный'
        elif predict_model_rf == 1:
            print('Ушедший клиент.\n')
            df['Exited'] = 'Ушедший'
        print(df)
        print('')

        # Данные заносим в конечную выборку 
        last_df = pd.concat([last_df, df], ignore_index=True)

        # Уточняем продолжение 
        print('Продолжаем? \n 1 - Нет \n 2 - Да')
        run_go = int(input('Введите число: '))
        if run_go == 1:
            run = False
            print('Окончательные данные: \n')
            print(last_df)
            print('Всего доброго!\n')
        elif run_go == 2:
            run = True
            index += 1
            print('')
        else:
            print('Вы ввели неверные данные!\n')
            break
    
    elif method == 1:
        # Уточняем путь данных 
        way_df = input('Укажите путь к данным: ')
        df = pd.read_csv(f'./{way_df}')

        # Предсказываем 
        predict_model_rf = loaded_model.predict(df)

        # Добавляем предсказания 
        df['Exited'] = predict_model_rf

        # Выводим 10 строк таблица 
        df.head(10)

        # Данные заносим в конечную выборку 
        last_df = pd.concat([last_df, df], ignore_index=True)

        # Уточняем продолжение 
        print('Продолжаем? \n 1 - Нет \n 2 - Да')
        run_go = int(input('Введите число: '))
        if run_go == 1:
            run = False
            print('Окончательные данные: \n')
            print(last_df)
            print('Всего доброго!\n')
        elif run_go == 2:
            run = True
            index += 1
            print('')
        else:
            print('Вы ввели неверные данные!\n')
            break
    else:
        print('Вы ввели невернный ответ!')
        break
# Выводим конечную выборку 
last_df

# Сохраняем данные в папку output 
last_df.to_csv('/src/output/result.csv', index=False)