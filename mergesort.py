def merge(list1, list2):
    #Function to merge two lists into a new list
    newlist =[]
    index1 = 0
    index2 = 0
    #Check each item in each list, then add the smallest item to a new list
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] > list2[index2]:
            newlist.append(list2[index2])
            index2 = index2 + 1
        elif list1[index1] < list2[index2]:
            newlist.append(list1[index1])
            index1 = index1 + 1
        elif list1[index1] == list2[index2]:
            newlist.append(list1[index1])
            newlist.append(list2[index2])
            index1 += 2
    #Add left over items from the remaining list
    if index1 < len(list1):
        for item in range(index1, len(list1)):
            newlist.append(list1[item])
    elif index2 < len(list2):
        for item in range(index2, len(list2)):
            newlist.append(list2[item])
    return newlist

#Main Algortihm
items = ["Florida","Georgia","Delaware","Alabama","California"]
listofitems = []
#every item is put into its own list within a container list
for n in range(len(items)):
    item = [items[n]]
    listofitems.append(item)
        #repeat while there is more than one list
    while len(listofitems) != 1:
        index = 0
        #merge pairs of lists
        while index < len(listofitems) - 1:
            newlist = merge(listofitems[index], listofitems[index + 1])
            #once merged delete
            del listofitems[index + 1 ]

#output 
for index in range(0, len(newlist)):
    print(newlist[index])
