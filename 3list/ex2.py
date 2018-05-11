def prList(arr):
    for idx,el in enumerate(arr):
        if(idx!=len(arr)-1):
            print(el,end=',')
        else:
            print(el)

a = [10,20,30,40,50]
prList(a)

def enumlist(arr):
    for idx,el in enumerate(arr):
        #print(idx+1,',',el)
        print('{}. {}'.format(idx+1,el))
enumList=['apple','banana','orange']
enumlist(enumList)