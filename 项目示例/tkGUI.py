import tkinter as tk
# 创建主窗口
window = tk.Tk()
# 设置窗口标题
window.title("图形用户界面标题")
# 设置窗口大小
window.geometry("400x300")
# 创建标签
label = tk.Label(window, text="Hello, World!")
label.pack()
def hanshu():
    print('执行对应的函数','欢迎学习GUI')
    label.config(text='欢迎学习GUI、标签、按钮')
button=tk.Button(window,text='执行',command=hanshu)
button.pack()
# 运行主循环
window.mainloop()