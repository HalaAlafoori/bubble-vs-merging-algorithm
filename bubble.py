def bSort(list1):

    n = len(list1)

  

    for i in range(n-1):

 

        # Last i elements are already in place

        for j in range(0, n-i-1):  

           

            if list1[j] > list1[j + 1] :

                list1[j], list1[j + 1] = list1[j + 1], list1[j]

 

list1 = input('enter the list of values to be sorted: ').split()

list1 = [int(x) for x in list1] #for every element in list1 we will call bubble sort

bSort(list1)

print(list1)