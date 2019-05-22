"""
   汇率转换器
   输入美元，输出人民币
"""

# 1.获取数据
str_usd = input("请输入人民币")
float_usd = float(str_usd)

# 2逻辑处理
rmb = float_usd * 6.708

# 3.显示结果
print(rmb)

