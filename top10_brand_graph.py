import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import statsmodels.api as sm
import math
import pandas as pd
from sklearn.metrics import explained_variance_score, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import numpy as np
import warnings
warnings.filterwarnings(action='ignore')


car_t = pd.read_csv('./train_data_r.csv')
car_tr = pd.read_csv('./train_data_n.csv')
car_td = pd.read_csv('./used_car.csv')

from car import Brand
from car import PredictPrice
from car import Graph


bb = Brand(car_t)
PP = PredictPrice()
gg = Graph()

for i in bb.ready()['Brand'].value_counts().index[:10]:

    X = bb.get_Brand_df(bb.ready(), i).drop(['Price', 'Brand'], axis=1)
    y = np.log10(bb.get_Brand_df(bb.ready(), i)['Price'])

    gg.get_graph_rf(X,y,2,2,i)