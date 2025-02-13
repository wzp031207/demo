from scipy.optimize import linprog
# 目标函数的系数
c = [-2, -3]  # 由于 linprog 默认执行的是最小化，因此我们对系数取反
# 不等式约束的系数
A = [
    [2, 2],
    [1, 2],
    [4, 0],
    [0, 4]
]
# 不等式约束的右侧常数
b = [12, 8, 16, 12]
# 决策变量的范围
x_bounds = (0, None)
y_bounds = (0, None)
# 解决线性规划问题
res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
# 提取结果
x1 = res.x[0]
x2 = res.x[1]
max_z = -res.fun  # 取反得到最大值
# 显示结果
print("目标函数最大值：", max_z)
print("甲产品：", x1)
print("乙产品：", x2)
