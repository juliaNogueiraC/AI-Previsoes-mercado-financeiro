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

# Criar uma coluna de previsão com o preço de fechamento deslocado (por exemplo, 30 dias à frente)
data['Prediction'] = data['Close'].shift(-30)

# Excluir as últimas 30 linhas, onde os valores de 'Prediction' são NaN
data = data[:-30]

# Definir as features (X) e o target (y)
X = data[['Close']]
y = data['Prediction']

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo de Regressão Linear
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
lr_predictions = lr_model.predict(X_test)

# Avaliar o modelo de Regressão Linear
lr_mse = mean_squared_error(y_test, lr_predictions)
print(f'Erro Quadrático Médio da Regressão Linear: {lr_mse}')

# Treinar o modelo de SVR
svr_model = SVR(kernel='rbf')
svr_model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
svr_predictions = svr_model.predict(X_test)

# Avaliar o modelo de SVR
svr_mse = mean_squared_error(y_test, svr_predictions)
print(f'Erro Quadrático Médio do SVR: {svr_mse}')

# Visualizar as previsões do modelo de Regressão Linear
plt.figure(figsize=(10, 6))
plt.plot(y_test.values, label='Valores Reais')
plt.plot(lr_predictions, label='Previsões da Regressão Linear')
plt.legend()
plt.title('Previsões da Regressão Linear vs Valores Reais')
plt.xlabel('Amostras')
plt.ylabel('Preço de Fechamento')
plt.show()

# Visualizar as previsões do modelo de SVR
plt.figure(figsize=(10, 6))
plt.plot(y_test.values, label='Valores Reais')
plt.plot(svr_predictions, label='Previsões do SVR')
plt.legend()
plt.title('Previsões do SVR vs Valores Reais')
plt.xlabel('Amostras')
plt.ylabel('Preço de Fechamento')
plt.show()

# Pegar os últimos 30 dias do dataset original para prever os próximos 30 dias
X_future = data[['Close']].tail(30)

# Fazer previsões para os próximos 30 dias com o modelo de Regressão Linear
lr_future_predictions = lr_model.predict(X_future)

# Exibir as previsões futuras do modelo de Regressão Linear
print("Previsões para os próximos 30 dias (Regressão Linear):")
print(lr_future_predictions)

# Fazer previsões para os próximos 30 dias com o modelo de SVR
svr_future_predictions = svr_model.predict(X_future)

# Exibir as previsões futuras do modelo de SVR
print("Previsões para os próximos 30 dias (SVR):")
print(svr_future_predictions)