from matplotlib import pyplot as plt
import matplotlib

font = {'family':'MicroSoft YaHei',
        'weight':'bold',
        'size':12}
matplotlib.rc("font",**font)
matplotlib.rc("font",family='MicroSoft YaHei',weight="bold",size=8)

y_1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_2 = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]

x = range(11,31)

# 绘制时指定：color,linestyle,linewidth,alpha
# color='r';r红色；g绿色；b蓝色；w白色；c青色；y黄色；k黑色；
# linesytle='--'; 线条风格
# linewidth=5; 线条粗细
# alpha=0.5； 线条透明度

plt.figure(figsize=(15,7),dpi=80)

plt.plot(x,y_1,label="小红",color='k',linestyle='--',linewidth=6)
plt.plot(x,y_2,label="小兰",color='y')

_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x,_xtick_labels)
plt.yticks(range(0,8))

# 绘制网格,设置网格透明度（0-1）
plt.grid(alpha=0.5)

# 添加图例,以及图例的位置
plt.legend(loc="upper left")

plt.show()