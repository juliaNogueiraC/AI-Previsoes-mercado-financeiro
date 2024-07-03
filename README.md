# Análise e Previsão de Tendências em Dados de Mercado Financeiro

## Sobre
O dataset AAPL.csv é um conjunto de dados históricos de preços de ações da empresa Apple Inc. (símbolo de ticker AAPL) extraído do Yahoo Finance. Este conjunto de dados inclui informações diárias de preços de fechamento das ações da Apple em um intervalo de tempo específico. Vamos dar uma olhada nos detalhes:

* Date (Data): Esta coluna representa a data em que o preço de fechamento das ações foi registrado.

* Open (Abertura): Este é o preço da ação no momento da abertura do mercado naquela data.

* High (Máximo): É o preço mais alto alcançado pela ação durante o dia de negociação.

* Low (Mínimo): Representa o preço mais baixo que a ação alcançou durante o dia de negociação.

* Close (Fechamento): É o preço da ação no momento do fechamento do mercado naquela data. Este é o preço que é mais comumente usado para análise técnica e outras análises de mercado.

* Adj Close (Fechamento Ajustado): Este é o preço de fechamento ajustado por eventos corporativos, como divisões de ações, dividendos, etc. É útil para análises de longo prazo.

* Volume: Representa o volume de negociação, ou seja, o número total de ações negociadas naquele dia.

 > Para uma melhor vizualização:
 > - Baixe o dataset ou desse github ou do própio Yahoo Finances (de onde os dados vieram) conforme o link:
  https://finance.yahoo.com/quote/AAPL/history/
 > - Faça uma cópia desde programa no Google Colab: https://colab.research.google.com/drive/1a78x7wgR-gxFN17VHYw4jsVXbNLVkwvb?usp=sharing
 > - Coloque o Dataset nos arquivos e Altere o valor de `data` de acordo com o nome do arquivo.

## Dependências

Para o funcionamento do software, se faz nescessário a instalação das bibliotecas pandas, numpy, matplotlib e scikit-learn, para isso use o comando:

    !pip install pandas numpy matplotlib scikit-learn
  > Para mais detalhes com mais comentários, confira o Colab.
