sample_list = [1,1,2,3,4,4,5,6,7,8,9]
#converting a list

sample_set = set(sample_list)
print(sample_set)

#show the sets are not indexed
#print(sample_set[2])

#check if an element exusts in the set

if 4 in sample_set:
    print("Yes")
else:
    print("No")

#adding the elements in the set
myset = set([])
myset.add(3)
myset.add(4)
myset.add(7)
print(myset)

#remove element from the set
myset.remove(3)
print(myset)

#does not throw the error if element is not present in the set.
myset.discard(5)
print(myset)

#set operations
#1.) Union
#2.) Intersection
#3.) Difference
#4.) Symmetric Difference

a={1,2,3,4,5}
b={6,7,8,9,10}

#union means addition of sets
print(a.union(b))

#intersection means finding the common element in sets
print(a.intersection(b))

set1 = {1,3,4,6}
set2 = {3,4,6,7,8}
print(set1.intersection(set2))

#Difference means elements that exist in set2 but do not exist in set1
print(set1 - set2)

#Difference means elements that exist in set1 but do not exist in set2
print(set2 - set1)

#symmetric difference in the (union of sets - intersection of the sets.)
print(set1.symmetric_difference(set2))

#union of set1 and set2
union_of_sets = set1.union(set2)
print(union_of_sets)
intersection_of_sets = set1.intersection(set2)
print(intersection_of_sets)
print(union_of_sets.symmetric_difference(intersection_of_sets))


fruit_set = {"apple", "banana", "grapes", "mango"}
fruit_set.add("orange")
fruit_set.remove("grapes")
for loop in fruit_set:
    print (loop)
print(fruit_set)

vowel_set = {"A","E","I","O","U"}

consoset = {"B","C","D","F","G"}
unionL = vowel_set.union(consoset)
print(unionL)

