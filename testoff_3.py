
def sort_list(arr):   
    di = {i:len(i) for i in arr }
    return sorted(di,key=lambda i:len(i)),sorted(di,key=lambda i:len(i),reverse=True)
