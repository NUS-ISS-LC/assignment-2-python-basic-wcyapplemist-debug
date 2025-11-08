def find(s, n):
# write your implementation here
    for i in range(len(s)):
        if s[i]+s[i+1] == n:
            return [i, i+1]
            break
    return None

print(find([2,7,11,15], 9))
print(find([3,2,4], 6))
print(find([3,3], 6))
