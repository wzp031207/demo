import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimSun']
rcParams['axes.unicode_minus'] = False
file_path = "C:/Users/文/Desktop/score.xls"
df = pd.read_excel(file_path)
my_info = pd.DataFrame([{
    "stu_id": 2102160102020,
    "name": "文曾培",
    "Chinese": 99,
    "math": 99,
    "physics": 99,
    "chemistry": 99
}])
df = pd.concat([df, my_info], ignore_index=True)
plt.figure(figsize=(8, 6))
plt.boxplot(df["Chinese"], labels=["语文"])
plt.title("语文成绩箱线图")
plt.ylabel("成绩")
chinese_scores = df["Chinese"]
plt.text(1.1, chinese_scores.max(), f"最大值: {chinese_scores.max()}", fontsize=10, color="red")
plt.text(1.1, chinese_scores.min(), f"最小值: {chinese_scores.min()}", fontsize=10, color="blue")
plt.text(1.1, chinese_scores.median(), f"中位数: {chinese_scores.median()}", fontsize=10, color="green")
plt.savefig("语文成绩箱线图.png")
plt.show()
def categorize_math(score):
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 60:
        return "中等"
    else:
        return "不及格"
df["math_category"] = df["math"].apply(categorize_math)
grouped = df.groupby("math_category").agg(
    人数=("math", "count"),
    物理平均分=("physics", "mean"),
    物理最高分=("physics", "max"),
    物理最低分=("physics", "min")
)
print("按数学成绩分组统计：")
print(grouped)