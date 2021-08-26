from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from matplotlib import rc
rc('font', family='Arial Unicode Ms')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import math
import warnings
warnings.filterwarnings(action='ignore')

class Split:
    def __init__(self, data):
        self.data = data

    def get_split(self, column, new):
        ls1 = self.data[column]
        ls2 = []
        for i in range(0,len(self.data)):
            ls2.append(ls1[i].split(' ')[0])
            
        self.data[new] = ls2
        return(self.data)

    def get_split2(self, column, new):

        ls1 = self.data[column]
        ls2 = []
        for i in range(0,len(self.data)):
            ls2.append(ls1.str.split(' ', n=1)[i][1])
            
        self.data[new] = ls2
        return(self.data)


class Results:
    def get_results_lr(self, X, y):
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=13)
        
        reg = LinearRegression()
        reg.fit(X_train, y_train)

        pred_test = reg.predict(X_test)

        print('explained_variance_score: {}'.format(explained_variance_score(y_test, pred_test)))
        print('mean_squared_errors: {}'.format(mean_squared_error(y_test, pred_test)))
        print('r2_score: {}'.format(r2_score(y_test, pred_test)))

    def get_results_rf(self, X, y):

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=13)

        rf = RandomForestRegressor()
        rf.fit(X_train, y_train)

        pred_test = rf.predict(X_test)

        print('explained_variance_score: {}'.format(explained_variance_score(y_test, pred_test)))
        print('mean_squared_errors: {}'.format(mean_squared_error(y_test, pred_test)))
        print('r2_score: {}'.format(r2_score(y_test, pred_test)))

    def inverse_log(self, log):
        return(math.pow(10,log))


class Brand:
    def __init__(self, data):
        self.data = data

    def ready(self):
        car = self.data.drop([4446, 4904])
        car.drop(['Unnamed: 0'], axis=1, inplace=True)
        car = car[(car['Fuel_Type'] == 'Diesel') | (car['Fuel_Type'] == 'Petrol')]
        car.reset_index(drop=True, inplace=True)

        ls1 = car['Name']
        ls2 = []
        for i in range(0,len(car)):
            ls2.append(ls1[i].split(' ')[0])
            
        car['Brand'] = ls2

        ls1 = car['Mileage']
        ls2 = []
        for i in range(0,len(car)):
            ls2.append(ls1[i].split(' ')[0])
            
        car['Mile'] = ls2

        ls1 = car['Engine']
        ls2 = []
        for i in range(0,len(car)):
            ls2.append(ls1[i].split(' ')[0])
            
        car['Eng'] = ls2

        ls1 = car['Power']
        ls2 = []
        for i in range(0,len(car)):
            ls2.append(ls1[i].split(' ')[0])
            
        car['Pow'] = ls2

        return(car)
    
    def get_Brand_df(self, data, Brand):
        car = data[data['Brand'] == Brand]

        car.reset_index(drop=True, inplace=True)

        car['Owner'] = range(0,len(car))

        for i in range(0,len(car)):
            if car['Owner_Type'][i] == 'First':
                car['Owner'][i] = 1

            elif car['Owner_Type'][i] == 'Second':
                car['Owner'][i] = 2

            elif car['Owner_Type'][i] == 'Third':
                car['Owner'][i] = 3

            elif car['Owner_Type'][i] == 'Fourth & Above':
                car['Owner'][i] = 4

        car = pd.get_dummies(car, columns=['Location','Fuel_Type', 'Transmission'])

        car = car.drop(['Name', 'Owner_Type', 'Mileage', 'Engine', 'Power', 'Seats', 'New_Price'], axis=1)

        return(car)

class Graph:
    def get_graph_lr(self, X ,y ,x_axis ,y_axis, title):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=13)
        reg = LinearRegression()
        reg.fit(X_train, y_train)

        predicted = reg.predict(X_test)

        actual = y_test

        act_df = pd.DataFrame(actual)
        pred_df = pd.DataFrame(predicted)

        act_df.reset_index(inplace=True)

        act_pred_df = pd.concat([act_df, pred_df], axis=1)

        act_pred_df.columns = ['index','actual', 'predicted']

        plt.figure(figsize=(15,10))
        plt.plot(act_pred_df['predicted'],act_pred_df['actual'], 'o')

        plt.xlabel('predicted', fontsize=14)

        plt.ylabel('actual', fontsize=14)
        plt.title(title, fontsize=20, y=1.05)
        plt.axis([0, x_axis, 0, y_axis])  
        line = plt.plot([0,x_axis], [0,y_axis])
        plt.setp(line, color='r', linewidth=3.0)

        return(plt.show())

    def get_graph_rf(self, X, y, x_axis, y_axis, title):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=13)
        rf_reg = RandomForestRegressor()
        rf_reg.fit(X_train, y_train)

        predicted = rf_reg.predict(X_test)

        actual = y_test

        act_df = pd.DataFrame(actual)
        pred_df = pd.DataFrame(predicted)

        act_df.reset_index(inplace=True)

        act_pred_df = pd.concat([act_df, pred_df], axis=1)

        act_pred_df.columns = ['index','actual', 'predicted']

        plt.figure(figsize=(15,10))
        plt.plot(act_pred_df['predicted'],act_pred_df['actual'], 'o')

        plt.xlabel('predicted', fontsize=14)

        plt.ylabel('actual', fontsize=14)
        plt.title(title, fontsize=20, y=1.05)
        plt.axis([0, x_axis, 0, y_axis])  
        line = plt.plot([0,x_axis], [0,y_axis])
        plt.setp(line, color='r', linewidth=3.0)

        return(plt.show())

class PredictPrice:
    def get_car_price_lr(self, X, y, car):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=13)

        reg = LinearRegression()
        reg.fit(X_train, y_train)

        pred = reg.predict(car)
        return(pred)

    def get_car_price_rf(self, X, y, car):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=13)

        rf_reg = RandomForestRegressor()
        rf_reg.fit(X_train, y_train)

        pred = rf_reg.predict(car)
        return(pred)

    def inverse_log(self, log):
        return(math.pow(10,log))

    def where_we_should_sell(self, X, y, brand):

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=13)

        rf = RandomForestRegressor()
        rf.fit(X_train, y_train)

        value = rf.feature_importances_
        value_s = pd.Series(value, index=X_train.columns)

        print('\033[91m' + '\033[1m' + brand  + '\033[0m' + '  you should sell your car at :' , value_s[6:15].sort_values(ascending=False).index[0])
        