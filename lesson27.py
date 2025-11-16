thislist = ["яблоко", "банан", "вишня"]
print(thislist)
print(len(thislist))
list1 = [13, 26, 39, 52]
list2 = [True, False, True]
list3 = ["Abc", "BDS", "BBS"]
x = 12
dynamiclist = [True, {1, 2, 3, 4, 5}, "Яблоко", 12.32132, False, x]
list_1 = list(("False", False))
print(type(dynamiclist))
print(dynamiclist[1])
print(dynamiclist[-1])
print(dynamiclist[1:-1])
print(dynamiclist[:2])
print(dynamiclist[2:])
if "Яблоко" in dynamiclist:
    print("Yes, very good!")

dynamiclist[1] = "Ананас"
dynamiclist[3:6] = ["Киви", "Клубника"]
print(dynamiclist)
dynamiclist.insert(0, "Виноград")
dynamiclist.append("Арбуз")
dynamiclist.extend(thislist)
dynamiclist.extend({1,2,3,4})
dynamiclist.extend(range(0, 10))
print(dynamiclist)