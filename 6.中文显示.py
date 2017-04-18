import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family']='SimHei'
plt.plot([0,2,4,6,8])
plt.ylabel("纵轴(值)")
plt.savefig('中文显示',dpi=600)
plt.show()