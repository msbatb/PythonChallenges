#two sum
# nums = [2,7,11,15]
# target = 9
# result=[]
# left=0
# right=len(nums)-1
# while left<=right:
#     if (nums[left]+nums[right])==target:
#         result.append(left)
#         result.append(right)
#         break
#     elif (nums[left]+nums[right])>target:
#         right-=1
#     elif (nums[left]+nums[right])<target:
#         left+=1
# print(result)

# nums1=[1,2]
# nums2=[3,4]
#
# nums = nums1 + nums2
# nums.sort()
#
# n = len(nums)
#
#
# if n % 2 == 0:
#     median = (nums[n//2 - 1] + nums[n//2]) / 2
# else:
#     median = nums[n//2]
#
# print(median)

#min and max nuber find
# arr=[3,5,1,9]
# min_number=999
# max_number=-999
#
# for i in arr:
#     if max_number < i:
#         max_number=i
#     if min_number>i:
#         min_number=i
# print(min_number,max_number)

#reverse arr
# arr=[1,2,3,4]
# l=len(arr)
# left=0
# right=l-1
# mid=l//2
# while left<right:
#     arr[left],arr[right]=arr[right],arr[left]
#     left+=1
#     right-=1
# print(arr)

#move all zero to end
# arr=[0,1,0,3,12]
# j=0
# for i in range(0, len(arr)):
#     if arr[i]!=0:
#         arr[i],arr[j]=arr[j],arr[i]
#         j+=1
# print(arr)

#two sum
# arr = [2,7,11,15]
# target = 9
# result=[]
# left=0
# right=len(arr)-1
# while left<right:
#     if arr[left]+arr[right]==target:
#         result.append(arr[left])
#         result.append(arr[right])
#         break
#     elif arr[left]+arr[right]<target:
#         left+=1
#     elif arr[left]+arr[right]>target:
#         right-=1
# print(result)

#Kadane's Algorithm
# arr=[-2,1,-3,4,-1,2,1,-5,4]
# max_sum=arr[0]
# current_sum=arr[0]
# for i in range(1,len(arr)):
#     current_sum=max(arr[i],current_sum+arr[i])
#     if current_sum>max_sum:
#         max_sum=current_sum
# print(max_sum)

#Best time to buy and sell stock
# arr=[7,1,5,3,6,4]
# min_price=float('inf')
# profit=0
# for price in arr:
#     min_price=min(min_price,price)
#     profit=max(profit,price-min_price)
# print(profit)

#remove duplicate from sorted array
# arr=[1,1,2,2,3]
# result=[]
# for i in arr:
#     if i not in result:
#         result.append(i)
# print(result)

#majority element
# arr=[1,1,2,2,4,1,3,4,1]
# maxi=0
# number=0
# for i in arr:
#     num=arr.count(i)
#     if num>maxi:
#         maxi=num
#         number=i
# print(number)

#marge two sorted array
# arr1=[1,3,5]
# arr2=[2,4,6]
# result=[]
# for i in range(0,len(arr1)):
#     result.append(arr1[i])
#     result.append(arr2[i])
# print(result)








