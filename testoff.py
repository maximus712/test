

#два варианта 
def uniq(arr):
    return list(set(arr))

def uniq_2(arr):
    arr_2=[]
    for i in arr:
        if i not in arr_2:
            arr_2.append(i)
    return arr_2



