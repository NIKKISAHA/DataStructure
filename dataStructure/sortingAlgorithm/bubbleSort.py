#bubble sort
class Ri():
    def ri(self,x:list[int])->list[int]:
        for i in range(len(x)):
            for j in range(len(x)-1):
                if x[j]>x[j+1]:
                    x[j],x[j+1]=x[j+1],x[j]
                    print(x)
        #     print(x)
        return x
riki=Ri()
print(riki.ri([3,1])) 