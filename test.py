import matplotlib.pyplot as plt
from operator import itemgetter



g = []
mybox = [[3, 1.5], [5.5, 1.5], [3, 3], [5.5, 3], [2.5, 4.5], [5, 4.5], [4.5, 6], [1.5, 7.5], [4, 7.5], [1, 9],
         [3.5, 9], [1, 10.5], [3.5, 10.5], [2, 12], [4.5, 12], [2, 13.5], [4.5, 13.5]]


sorted(mybox, key=itemgetter(0, 1))
D = 0
# A = len(mybox)

# start writing here computation
for i in range(len(mybox)-1):
    # for j in range(1, 15):
        # print("mybox[j][1]=", mybox[j][1])
    if (mybox[i][0] == mybox[i+1][0] - 2.5 and mybox[i+1][1] == mybox[i+1][1]):
        print("mybox[i][0]=", mybox[i][0])
        g.append(mybox[i])
    elif (mybox[i][0] != mybox[i+1][0] - 2.5 and mybox[i][1] == mybox[i+1][1]):
        mybox[i][0] = mybox[i+1][0] - 2.5
        mybox[i][1] = mybox[i+1][1]
        g.append(mybox[i])
print("g=", g)
plt.plot(g)
plt.show()
