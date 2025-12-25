def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

list1 = input("Enter elements of first list (space separated): ").split()
list2 = input("Enter elements of second list (space separated): ").split()

# Checking overlap
if overlapping(list1, list2):
    print("The lists have at least one common element.")
else:
    print("The lists have no common elements.")