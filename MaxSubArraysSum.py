import os


def MaxSubArrayForce(array):
    _max  = 0
    _temp = int()
    for i in range(0,len(array)):
        for j in range(i,len(array)):
            _temp = 0
            for k in range(i,j):
                _temp += array[k]
            if _temp > _max:
                _max = _temp    
    return _max

def MaxSubArrayDivid(array,_from,_to):
    if (_to == _from):
        return array[_from]
    
    middle = (_from+_to)/2
    m1 = MaxSubArrayDivid(array,_from,middle)
    m2 = MaxSubArrayDivid(array,middle+1, _to)
    
    left = array[middle]
    now = array[middle]
    for i in reversed(range(_from,middle-1)): #issues
        for j in reversed(range(_from,middle-1)):
            now += array[i]
            left = max(now,left)
    right = array[middle+1]
    now = array[middle+1]
    for i in range(middle+2,_to):
        now += array[i]
        right = max(now,right)
    m3 = left+right
    return max(m1,m2,m3)
    
def MaxSubArrayDp(array):
    result = _sum = array[0]
    for i in range(1,len(array)-1):
        if array[i] > 0:
            _sum+= array[i]
        else:
            _sum = array[i]
        
        if _sum > result:
            result = _sum
    return result        


MaxSubArray= [1,-2,3,10,-4,7,2,-5]

def main():
    print MaxSubArrayForce(MaxSubArray)
    print MaxSubArrayDivid(MaxSubArray,0,len(MaxSubArray)-1)
    print MaxSubArrayDp(MaxSubArray)
    pass




if __name__ == '__main__':
    main()