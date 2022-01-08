
def countdown(num):
    output = []
    for i in range(num,-1,-1):
        output.append(i)
    return output
print(countdown(5))

def print_and_return(list1):
    print(list1[0])
    return(list1[1])
    

print(print_and_return([1,2]))

#3
def first_plus_length(list2):
    return (list2[0] + len(list2))

print(first_plus_length([1, 2, 3, 4,])) 

#4
def values(list3):
    if len(list3) < 2:
        return False
    output = []
    for i in range (0, len(list3)):
        if list3[i] > list3[1]:
            output.append(list3[i])
    return output

print(values([5,2,3,2,1,4]))
print(values([3]))

#5

def len_val(size, value):
    output1 = []
    for i in range(0, size):
        output1.append(value)
    return output1

print(len_val(4, 2))

