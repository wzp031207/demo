import tkinter as tk
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
class PokemonAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("宝可梦数据分析系统")
        self.root.geometry("400x400")
        # 加载并清洗数据
        self.df = load_and_clean_data("pokemon.csv")
        # 创建按钮和标签
        self.label = tk.Label(root, text="宝可梦数据分析系统请选择一个分析选项：", font=("Arial", 14))
        self.label.pack(pady=20)
        self.button1 = tk.Button(root, text="宝可梦类型分布", font=("Arial", 12), command=self.plot_type_distribution)
        self.button1.pack(pady=10)
        self.button2 = tk.Button(root, text="传说宝可梦分布", font=("Arial", 12),
                                 command=self.plot_legendary_distribution)
        self.button2.pack(pady=10)
        self.button3 = tk.Button(root, text="宝可梦各世代分布", font=("Arial", 12),
                                 command=self.plot_generation_analysis)
        self.button3.pack(pady=10)
        self.button4 = tk.Button(root, text="攻击与防御关系", font=("Arial", 12),
                                 command=self.plot_attack_defense_relation)
        self.button4.pack(pady=10)
    def plot_type_distribution(self):
        plot_type_distribution(self.df)
    def plot_legendary_distribution(self):
        plot_legendary_distribution(self.df)
    def plot_generation_analysis(self):
        plot_generation_analysis(self.df)
    def plot_attack_defense_relation(self):
        plot_attack_defense_relation(self.df)
# 运行应用
if __name__ == "__main__":
    root = tk.Tk()
    app = PokemonAnalysisApp(root)
    root.mainloop()
