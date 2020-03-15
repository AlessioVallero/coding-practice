class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def reverse_list(l):
    """
    Given head of LinkedList, reverse list and return new head.
    O(n) complexity, where n is the list size
    """

    prev_e = None
    curr_e = l
    next_e = None
    while curr_e is not None:
        next_e = curr_e.next
        curr_e.next = prev_e
        prev_e = curr_e
        curr_e = next_e

    return prev_e


def addTwoHugeNumbers(a, b):
    sum_ret = []

    # Reverse both lists to sum each element in right order. O(a) and O(b)
    a = reverse_list(a)
    b = reverse_list(b)

    curr_a = a
    curr_b = b
    carry = 0
    # Until we have element in both lists at the same time
    # we sum up each pair, trim to 4 digits and take into an account a carriage, if any
    # Complexity: O( min(len(a), len(b)) )
    while curr_a is not None and curr_b is not None:
        curr_sum = curr_a.value + curr_b.value + carry

        if curr_sum > 9999:
            carry = 1
            curr_sum = curr_sum % 10000
        else:
            carry = 0

        sum_ret.insert(0, curr_sum)

        curr_a = curr_a.next
        curr_b = curr_b.next

    # Sum remaining elements from list a, if any
    # Complexity: O(a)
    while curr_a is not None:
        curr_sum = curr_a.value + carry

        if curr_sum > 9999:
            carry = 1
            curr_sum = curr_sum % 10000
        else:
            carry = 0

        sum_ret.insert(0, curr_sum)
        curr_a = curr_a.next

    # Sum remaining elements from list b, if any
    # Complexity: O(b)
    while curr_b is not None:
        curr_sum = curr_b.value + carry

        if curr_sum > 9999:
            carry = 1
            curr_sum = curr_sum % 10000
        else:
            carry = 0

        sum_ret.insert(0, curr_sum)
        curr_b = curr_b.next

    if carry == 1:
        sum_ret.insert(0, 1)

    # Reverse lists again to reset them. O(a) and O(b)
    a = reverse_list(a)
    b = reverse_list(b)

    return sum_ret


lis1 = ListNode(1)

lis2 = ListNode(9998)
lis2.next = ListNode(9999)
lis2.next.next = ListNode(9999)
lis2.next.next.next = ListNode(9999)
lis2.next.next.next.next = ListNode(9999)
lis2.next.next.next.next.next = ListNode(9999)

# 8001 + 1999 = 10000 -> 0
# 1 + 5432 + 1 = 5434
# 9876
# 987654340

print(addTwoHugeNumbers(lis1, lis2))
