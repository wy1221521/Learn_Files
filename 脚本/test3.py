
nums= [213,123,12435,5654,67567,768,678,768,34534,24234]
a= [213,123,12435,5654,67567,768,678,768,34534,24234]

# for i in range(0, len(nums)):  # 这个循环负责设置冒泡排序进行的次数
#     print("第",i,'次排序')
#     for j in range(i+1, len(nums)):
#         print("下标是", j)
#         # ｊ为列表下标
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
for i in range(len(a)-1):
       print("第",i,'次排序')
       for j in range(len(a)-1-i):
         print("下标是", j)
         print("比较", a[j],a[j+1],"中")
         if a[j] > a[j+1]:
           print("交换",a[j], a[j+1],"的值")
           a[j], a[j+1] = a[j+1], a[j]

print(a)





