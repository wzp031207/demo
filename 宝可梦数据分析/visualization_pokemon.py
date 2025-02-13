import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    df['Type 1'].fillna('Unknown', inplace=True)
    df['Type 2'].fillna('Unknown', inplace=True)
    df['Legendary'].fillna(False, inplace=True)
    return df
def plot_type_distribution(df):
    plt.figure(figsize=(10, 6))
    type_counts = df['Type 1'].value_counts()
    sns.barplot(x=type_counts.index, y=type_counts.values, palette='viridis')
    plt.title("宝可梦类型分布")
    plt.xlabel('宝可梦类型')
    plt.ylabel('数量')
    plt.xticks(rotation=45)
    plt.show()
def plot_legendary_distribution(df):
    plt.figure(figsize=(6, 4))
    sns.countplot(x='Legendary', data=df, palette='coolwarm')
    plt.title("传说宝可梦分布")
    plt.xlabel('是否为传说宝可梦')
    plt.ylabel('数量')
    plt.show()
def plot_generation_analysis(df):
    plt.figure(figsize=(8, 5))
    generation_counts = df['Generation'].value_counts()
    sns.barplot(x=generation_counts.index, y=generation_counts.values, palette='coolwarm')
    plt.title("宝可梦各世代分布")
    plt.xlabel('世代')
    plt.ylabel('数量')
    plt.show()
def plot_attack_defense_relation(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='Attack', y='Defense', data=df, hue='Type 1', palette='tab20', s=100)
    plt.title("攻击与防御关系")
    plt.xlabel('攻击')
    plt.ylabel('防御')
    plt.show()
def visualize_data(df):
    plot_type_distribution(df)
    plot_legendary_distribution(df)
    plot_generation_analysis(df)
    plot_attack_defense_relation(df)
if __name__ == "__main__":
    file_path = "pokemon.csv"
    df = load_and_clean_data(file_path)
    visualize_data(df)
