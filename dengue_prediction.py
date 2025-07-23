import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load data
dengue_features = pd.read_csv('dengue_features_train.csv')
dengue_labels = pd.read_csv('dengue_labels_train.csv')

# Merge datasets on city, year, weekofyear
data = pd.merge(dengue_features, dengue_labels, on=['city', 'year', 'weekofyear'])

# Check for missing values
print(data.isnull().sum())

# Fill missing values with median (simple approach)
data.fillna(data.median(), inplace=True)

# Select features and target
features = ['reanalysis_air_temp_k', 'reanalysis_relative_humidity_percent',
            'reanalysis_precip_amt_kg_per_m2', 'station_avg_temp_c',
            'station_precip_mm']
X = data[features]
y = data['total_cases']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
