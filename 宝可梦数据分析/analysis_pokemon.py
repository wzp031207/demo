import pandas as pd
def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    print("数据集预览：")
    print(df.head())
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    df['Type 1'].fillna('Unknown', inplace=True)
    df['Type 2'].fillna('Unknown', inplace=True)
    df['Legendary'].fillna(False, inplace=True)
    print("\n数据清洗后预览：")
    print(df.head())
    return df
def perform_data_analysis(df):
    print("\n数据集信息：")
    print(df.info())
    print("\n描述性统计：")
    print(df.describe())
    print("\n缺失值检查：")
    print(df.isnull().sum())
    print("\nLegendary 宝可梦统计：")
    print(df['Legendary'].value_counts())
    print("\n各类型宝可梦数量：")
    print(df['Type 1'].value_counts())
    print("\n不同世代宝可梦数量：")
    print(df['Generation'].value_counts())
    type_relation = df.groupby(['Type 1', 'Type 2']).size().reset_index(name='Count')
    print("\nType 1 与 Type 2 组合的数量：")
    print(type_relation)
if __name__ == "__main__":
    file_path = "pokemon.csv"
    df = load_and_clean_data(file_path)
    perform_data_analysis(df)
