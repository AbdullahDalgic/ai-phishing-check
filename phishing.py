import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os
import time

from colorama import Fore, Back, Style

model_file = 'model/phishing-model.joblib'
dataset_file = "dataset/Phishing_Email.csv"

raw_mail_data = pd.read_csv(dataset_file)
mail_data = raw_mail_data.where((pd.notnull(raw_mail_data)), '')

mail_data.loc[mail_data['Email Type'] == 'Safe Email', 'Email Type'] = 0
mail_data.loc[mail_data['Email Type'] == 'Phishing Email', 'Email Type'] = 1

X = mail_data['Email Text']
Y = mail_data['Email Type']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

feature_extraction = TfidfVectorizer(min_df = 1, stop_words='english', lowercase=True)

X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)

# Y_train ve Y_test değerlerini tam sayılara dönüştürün
Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')

clear = lambda: os.system('cls')
clear()
print(Fore.YELLOW, "Sistem hazırlanıyor...")
if os.path.exists(model_file):
    # Var ise modeli yükle
    model = joblib.load(model_file)
    print(Fore.GREEN, "Eğitimli model başarıyla yüklendi !")

    while True:
        print("")
        print(Fore.RESET, '#################################################')
        input_mail = input('E-posta mesajını yazın : ')
        input_data_features = feature_extraction.transform([input_mail])
        prediction = model.predict(input_data_features)

        if (prediction[0] == 1):
            print(Fore.RED, 'Bu bir kimlik avı e-postası olabilir.')

        else:
            print(Fore.GREEN, 'Bu güvenli bir e-postadır.')

        confidence = model.predict_proba(input_data_features)[0][prediction[0]]
        print(Fore.WHITE, 'Doğruluk puanı : ', confidence)

else:
    print(Fore.GREEN, 'Model dosyası eğitiliyor !')
    time.sleep(2)

    print(Fore.WHITE, 'raw_mail_data')
    print(Fore.RESET, raw_mail_data)

    print(Fore.WHITE, 'X.shape')
    print(Fore.RESET, X.shape)
    print(Fore.WHITE, 'X_train.shape')
    print(Fore.RESET, X_train.shape)
    print(Fore.WHITE, 'X_test.shape')
    print(Fore.RESET, X_test.shape)

    print(Fore.WHITE, 'X_train')
    print(Fore.RESET, X_train)
    print(Fore.WHITE, 'X_train_features')
    print(Fore.RESET, X_train_features)

    model = LogisticRegression()
    model.fit(X_train_features, Y_train)

    # eğitim verilerine ilişkin tahmin
    prediction_on_training_data = model.predict(X_train_features)
    accuracy_on_training_data = accuracy_score(Y_train, prediction_on_training_data)
    print(Fore.RESET, "")
    print('Eğitim verilerinin doğruluğu : ', accuracy_on_training_data)


    # test verilerine ilişkin tahmin
    prediction_on_test_data = model.predict(X_test_features)
    accuracy_on_test_data = accuracy_score(Y_test, prediction_on_test_data)
    print('Test verilerinin doğruluğu : ', accuracy_on_test_data)

    # klasör yoksa oluştur
    if not os.path.exists('model'):
        os.makedirs('model')

    joblib.dump(model, model_file)
    print(Fore.GREEN, "Model dosyası eğitildi.")







