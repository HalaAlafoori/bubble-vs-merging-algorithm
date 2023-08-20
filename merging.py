def mergesort(list1):

    if len(list1)>1:

        mid = len(list1)//2

        left = list1[:mid]

        right = list1[mid:]

        mergesort(left)

        mergesort(right)

        i=0

        j=0

        k=0

        while i<len(left) and j<len(right):

            if left[i]<right[j]:

                list1[k] = left[i]

                i=i+1

                k=k+1

            else:

                list1[k] = right[j]

                j = j+1

                k = k+1

        while i<len(left):  #if there is element left out in the left list

            list1[k] = left[i]

            i = i+1

            k = k+1

        while j<len(right): #if there is element left out in the right list

            list1[k] = right[j]

            j = j+1

            k = k+1

           

list1 = input('enter the list of values to be sorted: ').split()

list1 = [int(x) for x in list1] #for every element in list1 we will call merge sort

mergesort(list1)

print(list1)
