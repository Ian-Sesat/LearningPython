integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]

#z=zip(integer,binary)
#binary_dict={integ:bina for integ,bina in z}
#print(binary_dict)
integer = [1, -1, 2, 3, 5, 0, -7]
print(integer)
additive_inverse=[-i for i in integer]
print(additive_inverse)

integer = [1, -1, 2, -2, 3, -3]
sq_set=set(i*i for i in integer)
print(sq_set)