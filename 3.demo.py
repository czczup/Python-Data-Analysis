import matplotlib.pyplot as plt
plt.subplot(3,2,4)
plt.plot([0,2,4,6,8],[3,1,4,5,2])
plt.ylabel("grade")
plt.savefig('test1',dpi=600)
plt.axis([-1,10,0,6])
plt.show()