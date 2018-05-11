nums = list(range(5,0,-1))
print(nums)
nums[2] = 100
print(nums)
#range是一個類別(class)，藍圖，給參數就做出這個類別的物件。沒有定義中括號，所以拿不到東西。
#List也是一種類別，把range放在nums裡面，就是建立一個新List把Range的質放在心的list，就是nums裡面。
a=[1,2,3,4,5]
total = 0
for el in a:
    total+=el
total2=sum(a)
print(total,total2)

b = range(5,0,-1)
print(sum(b))

strA = 'Stone'
strA = list(strA) #沒有轉換成list無法做改變。
strA[0] = 'Y' 
print(strA)       #印出來是['Y', 't', 'o', 'n', 'e']
strA = ''.join(strA)  #再將strA轉換成字串str
print(strA)       #印出來是Ytone