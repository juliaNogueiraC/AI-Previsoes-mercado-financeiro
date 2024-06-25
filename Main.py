import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error

# Carregar os dados do arquivo CSV (Dataset)
data = pd.read_csv('AAPL 3.csv')
# Estamos usando esse:
# https://finance.yahoo.com/quote/AAPL/history/?period1=1686960000&period2=1718582400

# Garantir que a coluna Date esteja no formato datetime
data['Date'] = pd.to_datetime(data['Date'])

# Definir a coluna Date como índice
data.set_index('Date', inplace=True)

# Usar a coluna 'Close' para o preço de fechamento
data = data[['Close']]

# Visualizar os dados
plt.figure(figsize=(10, 6))
plt.plot(data['Close'])
plt.title('Preço de Fechamento ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
plt.show()