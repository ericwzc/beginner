if __name__ == '__main__':
    a=[ ]
    for x in range (1,10):
        for y in range (1,10):
            if 15-x-y >0 and 20-2*x-y >0 and x+y-5 >0 and 2*x+y-10 >0 and x!=y and x!=5 and y!=5 and 15-x-y!=5 and 20-2*x-y!=5 and x+y-5!=10-x and 15-x-y!=y and (15-x-y)!=(20-2*x-y) and (15-x-y)!=(2*x+y-10) and x!=(20-x*2-y):
                a.append(x)
                a.append(y)
                a.append(15-x-y)
                a.append(20-2*x-y,)
                a.append(5)
                a.append(2*x+y-10)
                a.append(x+y-5)
                a.append(10-x)
                a.append(10-y)
            if len(a)>0:
                print(a)
            a=[]





