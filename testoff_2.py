

def uniq_vvalue_list(a,b):
    uniq_list=[]
    for i in range(a,b+1):
        if a>=1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                uniq_list.append(i)
        
    return uniq_list

