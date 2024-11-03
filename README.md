# Data Mining Project - K-Means Clustering

Este projeto aplica o algoritmo de agrupamento K-Means a um dataset para identificar padrões com base em idade e salário. A partir desses clusters, são gerados gráficos para análise visual dos grupos e da média salarial por cluster.

## Pré-requisitos

Este projeto utiliza as seguintes bibliotecas Python:
- `pandas` - para manipulação e análise de dados.
- `matplotlib` e `seaborn` - para visualização de gráficos.
- `scikit-learn` - para a aplicação do algoritmo K-Means.

Instale as bibliotecas com o comando:

```bash
pip install pandas matplotlib seaborn scikit-learn
```

## Estrutura do Código

O código está organizado em uma classe chamada `DataMining`, que possui os seguintes métodos:

- `__init__(csv_path)`: Carrega o dataset a partir de um arquivo CSV especificado pelo caminho `csv_path`.
- `apply_clustering(n_clusters=3)`: Aplica o algoritmo K-Means para dividir o dataset em 3 clusters (ou outro número especificado).
- `plot_clusters()`: Gera um gráfico de dispersão dos clusters com base em idade e salário.
- `plot_avg_salary_by_cluster()`: Gera um gráfico de barras que mostra a média salarial para cada cluster.

## Como Executar

1. Defina o caminho do arquivo CSV que deseja usar como dataset. Por padrão, o código usa o caminho:

   ```python
   csv_path = r'C:\Users\Baldez\PycharmProjects\pythonProject1\dataset_example.csv'
   ```

   Altere o caminho conforme necessário.

2. Inicialize a classe `DataMining` com o caminho do arquivo CSV e execute os métodos para aplicar clustering e visualizar os gráficos:

   ```python
   data_mining = DataMining(csv_path)
   data_mining.apply_clustering()
   data_mining.plot_clusters()
   data_mining.plot_avg_salary_by_cluster()
   ```

## Exemplo de Saída

1. **Gráfico de Dispersão dos Clusters**: Mostra os grupos formados com base na idade e salário.
2. **Gráfico de Barras da Média Salarial por Cluster**: Exibe a média salarial de cada cluster identificado.

## Observações

- Este projeto é uma introdução ao uso de algoritmos de mineração de dados com K-Means e visualização de clusters.
- Pode ser expandido para trabalhar com outros atributos ou algoritmos de clustering, como DBSCAN ou hierárquico.

## Autor

Gabriel Belitz Baldez
