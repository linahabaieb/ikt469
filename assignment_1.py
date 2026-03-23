import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
import torch
from torch import nn, optim

url_red = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
url_white = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"

df_red = pd.read_csv(url_red, sep=';')
df_white = pd.read_csv(url_white, sep=';')

df = pd.concat([df_red, df_white], ignore_index=True)

# Split data into training, validation, and test sets
train_df, temp_df = train_test_split(df, test_size=0.3, random_state=42)
val_df, test_df = train_test_split(temp_df, test_size=0.5, random_state=42)
#test_df.to_csv('test.csv', index=False)
#val_df.to_csv('validation.csv', index=False)

# Standardization
scaler = StandardScaler()
features = df.columns[:-1]
train_df[features] = scaler.fit_transform(train_df[features])
val_df[features] = scaler.transform(val_df[features])
test_df[features] = scaler.transform(test_df[features])
#train_df.to_csv('train.csv', index=False)

#Train using shallow neural network
class WineQualityNN(nn.Module):
    def __init__(self):
        super(WineQualityNN, self).__init__()
        self.fc1 = nn.Linear(11, 64) 
        self.fc2 = nn.Linear(32, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x