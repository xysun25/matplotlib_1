from matplotlib import pyplot as plt
import matplotlib

# 中文字体
font = {'family':'MicroSoft YaHei',
        'weight':'bold',
        'size':12}
matplotlib.rc("font",**font)
matplotlib.rc("font",family='MicroSoft YaHei',weight="bold",size=8)

a = ["战狼2","速度与激情9","功夫熊猫","西游降魔篇","变形金刚5：\n最后的战士",]
b_16 = [15652,1256,1456,259,986]
b_15 = [869,4852,14785,567,1125]
b_14 = [24586,2546,598,85,4591]

bar_width = 0.2

# x轴刻度递送
x_14 = list(range(len(a)))
x_15 = [i+bar_width for i in x_14]
x_16 = [i+bar_width*2 for i in x_14]
# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)

# bar绘制条形图，只能接受含数字的可迭代对象
# width表示长条的宽度，默认0.8
plt.bar(range(len(a)),b_14,width=bar_width,label="9月14日")
plt.bar(x_15,b_15,width=bar_width,label="9月15日")
plt.bar(x_16,b_16,width=bar_width,label="9月16日")

# 设置x轴刻度，将字符串传入x轴
plt.xticks(range(len(a)),a,rotation=90)

# 设置图例
plt.legend(loc="best")
# 保存图片
plt.savefig("./movie.png")
plt.show()

