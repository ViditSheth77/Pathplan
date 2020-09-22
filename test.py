
import matplotlib.pyplot as plt
from operator import itemgetter


g = []
mybox = [[3, 1.5], [5.5, 1.5], [3, 3], [5.5, 3], [2.5, 4.5], [5, 4.5], [4.5, 6], [1.5, 7.5], [4, 7.5], [1, 9],
         [3.5, 9], [1, 10.5], [3.5, 10.5], [2, 12], [4.5, 12], [2, 13.5], [4.5, 13.5]]

while True:
    """data = file.readlines(x)
    if not data :
        break
    for s in range(len(data)):
        if '\n' in data[s] :
            L.append(data[s][:-1])
        else :
            L.append(data[s])"""
    # print(L)
    """for i in mybox :
        #L1.append(("" + i).split(" "))
        mybox.sort(key=lambda k: [k[1], k[0]])"""
    sorted(mybox, key=itemgetter(0, 1))
    D = 0
    #A = len(mybox)

    # start writing here computation
    for i in range(0, 16):
        for j in range(1, 16):
            # print("mybox[j][1]=", mybox[j][1])
            if (mybox[i][0] == mybox[j][0] - 2.5 and mybox[i][1] == mybox[j][1]) :
                print("mybox[i][0]=", mybox[i][0])
                g.append(mybox[i])
            elif(mybox[i][0] != mybox[j][0] - 2.5 and mybox[i][1] == mybox[j][1]) :
                mybox[i][0] = mybox[j][0] -2.5
                mybox[i][1] = mybox[j][1]
                g.append(mybox[i])
            print("g=", g)
            plt.plot(g)
            break 