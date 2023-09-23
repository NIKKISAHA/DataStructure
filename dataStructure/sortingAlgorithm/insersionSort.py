#insersion sort
class Ri():
    def ri(self,x:list[int])->list[int]:
        for j in range(len(x)):
            i=j
            while i > 0 and x[i-1]>x[i]:
                x[i-1],x[i]=x[i],x[i-1]
                i-=1
                # print(x)
        return x
riki=Ri()
print(riki.ri([0,9,5,1]))