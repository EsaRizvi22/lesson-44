#Operations on Sets

set1={1,1,1,4,4,4,2,2,3,9,7,7,7,7}
print("Set1 is ",set1)

set1.add(5)
print("Updated Set1 is ",set1)

set2={2,3,3,3,4,7,9,9,9,11,24}
print("Set2 is ",set2)

print("Difference betwwen set1 and set2 is ",set1.difference(set2))
print("Difference between set2 and set1 is ",set2.difference(set1))

print("Symmetric Difference between set1 and set2 is ",set1.symmetric_difference(set2))
print("Symmetric Difference between set2 and set1 is ",set2.symmetric_difference(set1))
