#bubble sort 
l = int(input("enter nos in list: "))
a=[]
for i in range(l):
  a.append(int(input("")))
print ("unsorted list =  ", a)

def bubble_sort(a) :
    for i in range(len(a)-1,0,-1):
        for j in range (i):
         if a[j]>a[j+1]:
            temp = a[j]
            a[j] =a[j+1]
            a[j+1] = temp
bubble_sort(a)
print("sorted list =",a)
#insertion sort
l = int(input("enter nos in list: "))
a=[]
for i in range(l):
  a.append(int(input("")))

def insertion(a):
  for i in range(len(a)):
    temp = a[i]
    j = i-1
    while j>=0 and a[j]>temp:
      a [j+1] =a[j]
      j-=1
      a[j+1] = temp

insertion(a)
print(a)

#selection sort
l = int(input("enter nos in list: "))
a=[]
for i in range(l):
  a.append(int(input("")))

def selectionSort(a, size):
   
    for i in range(size):
        min_idx = i

        for i in range(i + 1, size):

            if a[i] < a[min_idx]:
                min_idx = i
         
        (a[i], a[min_idx]) = (a[min_idx], a[i])

size = len(a)
selectionSort(a, size)
print(a)
