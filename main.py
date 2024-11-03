import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns


class DataMining:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)

    def apply_clustering(self, n_clusters=3):
        data = self.df[['Age', 'Salary']]

        kmeans = KMeans(n_clusters=n_clusters, random_state=0)
        self.df['Cluster'] = kmeans.fit_predict(data)

    def plot_clusters(self):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='Age', y='Salary', hue='Cluster', data=self.df, palette='viridis', s=100)
        plt.title('K-Means Clustering of Age and Salary')
        plt.xlabel('Age')
        plt.ylabel('Salary')
        plt.legend(title='Cluster')
        plt.grid(True)
        plt.show()

    def plot_avg_salary_by_cluster(self):
        avg_salary = self.df.groupby('Cluster')['Salary'].mean()
        avg_salary.plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title('Average Salary by Cluster')
        plt.xlabel('Cluster')
        plt.ylabel('Average Salary')
        plt.xticks(rotation=0)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()



csv_path = r'C:\Users\Baldez\PycharmProjects\pythonProject1\dataset_example.csv'  # Altere o caminho conforme necessário
data_mining = DataMining(csv_path)
data_mining.apply_clustering()
data_mining.plot_clusters()
data_mining.plot_avg_salary_by_cluster()
