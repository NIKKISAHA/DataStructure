def merge(x:list[int])->list[int]:
     if len(x)>1:
        mid=len(x)//2
        left=x[:mid]
        right=x[mid:]

        merge(left)
        merge(right)

        k,i,j=0,0,0
        while((i<len(left))and (j<len(right))):
             if (left[i]<=right[j]):
                x[k]=left[i]
                i+=1
             else:
                x[k]=right[j]
                j+=1
             k+=1
        while(i<len(left)):
            x[k]=left[i]
            i+=1
            k+=1
        while(j<len(right)):
            x[k]=right[j]
            j+=1
            k+=1
        return x
print(merge([19,8,6,0,1]))
