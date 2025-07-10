# Print elements of a list one by one recursively.
def print_list_recursive(lis, index=0):
    if index == len(lis):
        return
    print(lis[index])
    print_list_recursive(lis, index + 1)


# Take user input and split it into list
lis = input("Enter your list: ").split()
print_list_recursive(lis)
