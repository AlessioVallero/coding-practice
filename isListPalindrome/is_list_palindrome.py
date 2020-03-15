class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def get_tail_mid_first_half(head):
    """
    Given head of LinkedList, return mid point and elem before mid.
    O(n)/2 complexity (O(n)), where n is the list size
    """
    tail = None
    p = r = head
    while r is not None and r.next is not None:
        tail = p
        p = p.next
        r = r.next.next

    return tail, p


def reverse_list(head):
    """
    Given head of LinkedList, reverse list and return new head.
    O(n) complexity, where n is the list size
    """
    prev_e = None
    curr_e = head
    next_e = None
    while curr_e is not None:
        next_e = curr_e.next
        curr_e.next = prev_e
        prev_e = curr_e
        curr_e = next_e

    return prev_e


def compare_halves(head_fh, head_sh):
    """
    Given two LinkedLists, compare them element by element.
    O(n) complexity, where n is the lists size (same size)
    """
    is_pal = True

    curr_e_fh = head_fh
    curr_e_sh = head_sh
    while curr_e_fh is not None and curr_e_sh is not None:
        if curr_e_fh.value != curr_e_sh.value:
            is_pal = False
            break
        curr_e_fh = curr_e_fh.next
        curr_e_sh = curr_e_sh.next

    return is_pal


def isListPalindrome(l):
    if l is None or l.next is None:
        return True

    # Get middle element and his ancestor
    tail, p = get_tail_mid_first_half(l)
    # Reverse second half of list
    new_head = reverse_list(p)
    # Compare each element of both halves
    is_pal = compare_halves(l, new_head)
    # Reverse  second half of list again to reset it
    new_head = reverse_list(new_head)
    # Link first half with double reversed second half
    tail.next = new_head

    return is_pal


lis = ListNode(1)
lis.next = ListNode(2)
lis.next.next = ListNode(3)
lis.next.next.next = ListNode(2)
lis.next.next.next.next = ListNode(1)

print(isListPalindrome(lis))
