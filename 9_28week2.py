mylist = ["one", "two", "three"]
another_list = ["four", "five"]

newlist = mylist + another_list

newlist.append("six")

newlist.pop()
popped_item = newlist.pop()
print(popped_item)
print(newlist)