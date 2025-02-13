import tkinter as tk
import analysis   # 导入自己写的analysis模块
window = tk.Tk()  # 创建主窗口
window.title("电影数据分析系统")  # 设置窗口标题
window.geometry("600x400")  # 设置窗口大小
label = tk.Label(window, text="IMDB电影数据分析系统",font='Consolas 20') # 创建标签
label.pack()
def hanshu():
    print('执行对应的函数','欢迎学习GUI')
    label.config(text='欢迎学习GUI、标签、按钮')
button1=tk.Button(window,text='电影数量前10位国家地区',font='Consolas 15',command=analysis.top10area)
button1.place(x=20, y=50)
button2=tk.Button(window,text='每年的电影数量',font='Consolas 15',command=analysis.year_count)
button2.place(x=320, y=50)
button1=tk.Button(window,text='不同类型的电影数量',font='Consolas 15',command=hanshu)
button1.place(x=20, y=110)
button2=tk.Button(window,text='电影类型的分布比例',font='Consolas 15',command=hanshu)
button2.place(x=320, y=110)
# 运行主循环
window.mainloop()