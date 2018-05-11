#list1內容是[0,1,2,3,4]
list1 = list(range(0,5,1))  #最後的1可以不寫，預設就是加一
print(list1)
list2 = list(range(2,7,1))
print(list2)
list3 = list(range(1,10,2))
print(list3)
list4 = list(range(5,0,-1))
print(list4)

print(list(range(2)))       #零開始屬兩個數
print(list(range(2,10)))    #頭跟尾的數字
print(list(range(2,10,2)))  #頭跟尾數字加上遞增