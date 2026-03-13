#Roman to Integer
# s="III"
# d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
# total = 0
# for i in range(len(s)):
#     if i < len(s) - 1 and d[s[i]] < d[s[i + 1]]:
#         total -= d[s[i]]
#     else:
#         total += d[s[i]]
# print(total)

#Logest Substring without repeating characters 
# s = "abcabcbb"
# ch_set=set()
# left=0
# max_len=0

# for right in range(len(s)):
#     while s[right] in ch_set:
#         ch_set.remove(s[left])
#         left+=1
#     ch_set.add(s[right])
#     max_len=max(max_len,right-left+1)
# print(max_len)
