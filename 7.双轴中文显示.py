import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#matplotlib.rcParams['font.family'] = 'STSong'
#matplotlib.rcParams['font.size'] = 20

a = np.arange(0.0,5.0,0.02)

plt.xlabel('横轴：时间',fontproperties='SimHei',fontsize=20)
plt.ylabel('纵轴：振幅',fontproperties='SimHei',fontsize=20)
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.savefig('双轴中文显示',dpi=600)
plt.show()