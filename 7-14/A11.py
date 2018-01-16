# Write a function, called reverse, that is given a list and it returns the list in reverse order. (Using reverse from the standard library is not allowed) Hint: pop
#
# print reverse([1,2,3,4]) # prints [4,3,2,1]
# print reverse(["aa", "bb", "cc"]) # prints ["cc", "bb", "aa"]

def reverse(li):
    new = []
    for item in li:
        last = li.pop()
        li.insert(0, last)
        new.append(last)
    return new

# Test
test = ["aa", "bb", "cc", "dd"]
print reverse(test)
