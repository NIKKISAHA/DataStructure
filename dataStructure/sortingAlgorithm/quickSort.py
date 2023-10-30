#quick sort
class Ri():
        def part(self,a:list[int],start:int,end:int)->int:
            parti=start
            pivot=a[end]
            for i in range(start,end):
                if a[i]<=pivot:
                    a[i],a[parti]=a[parti],a[i]
                    parti+=1
            a[parti],a[end]=a[end],a[parti]
            return parti
        def quicksort(self,x:list[int],start:int,end:int)->list[int]:
           if start<end:
               partiIndex=self.part(x,start,end)
               self.quicksort(x,start,partiIndex-1)
               self.quicksort(x,partiIndex+1,end)
           return x
riki=Ri()
print(riki.quicksort([100,6,1,9,0],0,4)) 