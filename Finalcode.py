import matplotlib.pyplot as plt
from operator import itemgetter



L1 = []
L = []
lx = []
ly = []
rx = []
ry = []
mx = []
my = []
m = []
g = []
h = []
e = []
f = []
mybox = [[3, 1.5], [5.5, 1.5], [3, 3], [5.5, 3], [2.5, 4.5], [5, 4.5], [2, 6], [4.5, 6], [1.5, 7.5], [4, 7.5], [1, 9],
         [3.5, 9], [1, 10.5], [3.5, 10.5], [1, 12], [3.5, 12], [1.5, 13.5], [4, 13.5], [2, 15], [4.5, 15]]


sorted(mybox, key=itemgetter(0, 1))
D = 0
# A = len(mybox)

# start writing here computation
for i in range(len(mybox)-1):
    # for j in range(1, 15):
        # print("mybox[j][1]=", mybox[j][1])
    #for left
    if (mybox[i][0] == mybox[i+1][0] - 2.5 and mybox[i][1] == mybox[i+1][1]):
        #print("mybox[i][0]=", mybox[i][0])
        g.append(mybox[i])
        h.append(mybox[i+1])
    elif (mybox[i][0] != mybox[i+1][0] - 2.5 and mybox[i][1] == mybox[i+1][1]):
        e = mybox[i+1][0] - 2.5
        f = mybox[i+1][1]
        g.append([e, f])
        h.append(mybox[i+1]) 
    elif (mybox[i][0] == mybox[i+1][0] + 0.5 and mybox[i][1] != mybox[i+1][1] and mybox[i][0] < mybox[i-1][0]):
        m = mybox[i][0] + 2.5
        n = mybox[i][1]
        h.append([m,n])
        g.append(mybox[i])
    elif (mybox[i][0] == mybox[i+1][0] + 0.5 and mybox[i][1] != mybox[i+1][1] and mybox[i][0] > mybox[i-1][0]):
        m = mybox[i+1][0] - 2.5
        n = mybox[i+1][1]
        h.append([m,n])
        g.append(mybox[i])
    #for straight 
    elif (mybox[i][0] == mybox[i+1][0] and mybox[i][1] == mybox[i+1][1] - 1.5 and mybox[i][0] < mybox[i-1][0]):
        m = mybox[i][0] + 2.5
        n = mybox[i][1]
        h.append([m,n])
        g.append(mybox[i])
    elif (mybox[i][0] == mybox[i+1][0] and mybox[i][1] == mybox[i+1][1] - 1.5 and mybox[i][0] > mybox[i-1][0]):
        m = mybox[i+1][0] - 2.5
        n = mybox[i+1][1]
        h.append([m,n])
        g.append(mybox[i])
     #for Right turn
    elif (mybox[i][0] == mybox[i+1][0] - 0.5 and mybox[i][1] != mybox[i+1][1] and mybox[i][0] < mybox[i-1][0]):
        m = mybox[i][0] + 2.5
        n = mybox[i][1]
        h.append([m,n])
        g.append(mybox[i])
    elif (mybox[i][0] == mybox[i+1][0] - 0.5 and mybox[i][1] != mybox[i+1][1] and mybox[i][0] > mybox[i-1][0]):
        m = mybox[i+1][0] - 2.5
        n = mybox[i+1][1]
        h.append([m,n])
        g.append(mybox[i]) 

    for i in g :
        plt.scatter(float(i[0]), float(i[1]), label="stars", color="red", marker="1", s=30)
    for i in h :
        plt.scatter(float(i[0]), float(i[1]), label="stars", color="green", marker="1", s=30)
for i in g :
    lx.append(i[0])
    ly.append(i[1])
for j in h :
    rx.append(j[0])
    ry.append(j[1])
for i in range(0, len(lx)) :
    mx.append((lx[i]+rx[i])/2)
    my.append((ly[i]+ry[i])/2)
    plt.scatter(float((lx[i]+rx[i])/2), float((ly[i]+ry[i])/2), label="stars", color="blue", marker="1", s=30)
print("rx=", rx)
print("ry=", ry) 
print("lx=", lx)
print("ly=", ly)
print("g=", g)
print("h=", h)
print("mx=", mx)
print("my=", my)
plt.xlim(0, 17)
plt.ylim(0, 17)
plt.show()
