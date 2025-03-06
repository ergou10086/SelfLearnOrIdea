import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 生成 2024 年 1 月 1 日至 6 月 30 日的日期序列。
# 设置随机种子，确保结果可重复
np.random.seed(52)

# 生成 2024 年 1 月 1 日至 6 月 30 日的日期序列。
dates = pd.date_range(start='2024-01-01', end='2024-06-30')
num_days = len(dates)   # 获取天数


# 生成每天的销量（80 到 120 之间的随机整数）和价格（50 到 70 之间的随机小数）。
sales = np.random.randint(80, 121, size=num_days)   # size=num_days 表示生成与日期序列长度相同的随机数。
prices = np.random.uniform(50,71, size=num_days)


# 检查长度并创建 DataFrame
print(f"日期长度: {len(dates)}, 销量长度: {len(sales)}, 价格长度: {len(prices)}")
# 创建 DataFrame
df = pd.DataFrame({'Date': dates, 'Sales': sales, 'Price': prices})
# 计算总收入
df['Revenue'] = df['Sales'] * df['Price']


# 检查销量为0的行
zero_sales = df[df['Sales'] == 0]
print(f"销量为0的天数: {len(zero_sales)}")

# 输出前5行
print(df.head())


# 数据汇总和可视化
# 提取月份
df['Month'] = df['Date'].dt.to_period('M')

# 按月份分组，并计算每组的平均销量
monthly_summary = df.groupby('Month')['Sales'].mean()

# 找出销量最高的前5天
top_5days = df.sort_values(by='Sales', ascending=False).head(5)

# 找出最高销量月份
max_sales_month = monthly_summary.idxmax()
print(f"销量最高的月份: {max_sales_month}")
print("\n销量最高的前5天：")
print(top_5days[['Date', 'Sales']])



# 绘制折线图并标注最高点
plt.figure(figsize=(12, 6))    # 创建一个新的绘图窗口的函数,宽度为 12 英寸，高度为 6 英寸
plt.plot(df['Date'], df['Sales'], color='blue', linestyle='-', label='Daily Sales')

# 标注最高点
# df.loc[] 是 pandas 库中用于通过标签选择数据的方法
max_sales_day = df.loc[df['Sales'].idxmax()]   # df['Sales'].idxmax() 是 pandas 库中 Series 对象的一个方法，用于返回 df['Sales'] 列中最大值所在的索引。

# plt.annotate()用于在绘图中添加注释的函数。
plt.annotate(f'Max Sales: {max_sales_day["Sales"]}',     # 注释的文本内容,将最高销量的值插入到文本中
             xy=(max_sales_day['Date'], max_sales_day['Sales']),   # 是注释箭头指向的点的坐标，即销量最高的那一天的日期和销量。
             xytext=(max_sales_day['Date'] + pd.Timedelta(days=5), max_sales_day['Sales'] + 10),   # 是注释文本的坐标，这里将注释文本的位置设置为在最高点的日期基础上往后推 5 天，销量基础上增加 10。
             arrowprops=dict(facecolor='red', shrink=0.05))     # 注释箭头的属性设置，facecolor='red' 表示箭头的颜色为红色，shrink=0.05 表示箭头的两端会向内收缩 5%

plt.title('Daily Sales in 2024 (Jan-Jun)')   # 设置图表的标题。
plt.xlabel('Date')      # 设置 x 轴的标签。
plt.ylabel('Sales')    # 设置 y 轴的标签。
plt.legend()    # 显示图例



# 绘制条形图
plt.figure(figsize=(10, 6))
colors = ['red', 'green', 'blue', 'orange', 'purple', 'brown']     # 柱状图颜色列表
plt.bar(monthly_summary.index.astype(str), monthly_summary, color=colors)    # 绘制柱状图的函数。

plt.title('Average Monthly Sales in 2024 (Jan-Jun)')
plt.xlabel('Month')
plt.ylabel('Average Sales')
plt.show()