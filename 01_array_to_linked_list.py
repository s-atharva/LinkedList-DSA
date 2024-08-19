# arr_ll(lis): Converts a list to a linked list (O(n)).
# length_ll(head): Calculates the length of the linked list (O(n)).
# display(head): Prints the elements of the linked list (O(n)).
# check_if_present(head, data): Checks if a specific value is present in the linked list (O(n)).

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def arr_ll(lis: list):
    head = Node(lis[0])
    mover = head
    for i in range(1, len(lis)):
        temp = Node(lis[i])
        mover.next = temp
        mover = mover.next
    return head


def length_ll(head):
    count = 0
    temp = head
    while temp:
        temp = temp.next
        count += 1
    return count


def display(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next


def check_if_present(head, data):
    temp = head
    while temp:
        if temp.data == data:
            return 1
        else:
            temp = temp.next
    return 0


arr = [2, 1, 3, 8]
first_elem = arr_ll(lis=arr)
print(length_ll(first_elem))
print(display(first_elem))
print(check_if_present(first_elem, data=3))
