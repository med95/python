def iterativeBinarySearch(alist,val,low,high):
    while low <= high:
        mid = int((low+high)/2)
        if val == alist[mid]:
            return mid
        elif val>alist[mid]:
            low = mid+1
        else:
            high = mid-1
    return False

def multiSearch(alist):
    #sorted list
    #返回重复元素
    n = len(alist)
    multi_elem = []
    #multi_times = []
    for i in range(n):
        #print('i:',i)
        if iterativeBinarySearch(alist[i+1:],alist[i],0,len(alist[i+1:])-1) or str(iterativeBinarySearch(
            alist[i+1:],alist[i],0,len(alist[i+1:])-1))=='0':
            #print('multi:',alist[i])
            multi_elem.append(alist[i])
        #else:
            #print(alist[i+1:],alist[i])
    return multi_elem
    
 def deleteElem(alist,val):
    while iterativeBinarySearch(alist,val,0,len(alist)-1) or str(
        iterativeBinarySearch(alist,val,0,len(alist)-1))=='0':
        pos = iterativeBinarySearch(alist,val,0,len(alist)-1)
        alist = alist[:pos]+alist[pos+1:]
    return alist
    
 if __name__ == '__main__':    
    a = [1,4,4,6,5]
    x = 8
    print(multiSearch(mergeSort.mergeSort(a)))
    print(deleteElem(a,4))
