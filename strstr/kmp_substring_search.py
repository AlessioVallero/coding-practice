def compute_kmp_prefix(substr_to_search):
    """
    Given the substring to search, compute the KMP prefix.
    Complexity O(substr_to_search)
    """
    kmp_prefix = [0] * len(substr_to_search)

    j = 0
    i = 1
    while i < len(substr_to_search):
        # If the char match, we move both pointers and set KMP to j + 1
        if substr_to_search[i] == substr_to_search[j]:
            kmp_prefix[i] = j + 1
            j += 1
            i += 1
        else:
            # If the char doesn't match, if we are at the beginning we move i
            # Otherwise we set j with the value of the previous element
            if j == 0:
                i += 1
            else:
                j = kmp_prefix[j-1]

    return kmp_prefix


def strstr(s, x):
    """
    Given a string s and a pattern x to search, return the index of the first match.
    Return -1 Otherwise
    Complexity O(s + x)
    """

    # If the length of one of the inputs is null, we return -1
    if not s or not x:
        return -1

    # If the pattern is longer than s, we know there is no match already
    if len(s) < len(x):
        return - 1

    # Compute the KMP prefix for the pattern string x in O(x)
    kmp_prefix = compute_kmp_prefix(x)

    i = 0
    x_pos = 0
    # Traverse the string, complexity O(s)
    while i < len(s):
        # If the char match...
        if s[i] == x[x_pos]:
            # If we are at the end of x, we can return the index of the beginning of the match
            if x_pos == len(x) - 1:
                return i - x_pos
            # Otherwise we increment both pointers in s and x
            x_pos += 1
            i += 1
        else:
            # If we are at the beginning of x, we only need to increment i
            if x_pos == 0:
                i += 1
            else:
                # Otherwise, the next x_pos is going to be the value in the char before
                # This is to avoid to check a prefix that we know being valid already
                # And where KMP algorithm saves time compared to brute force
                x_pos = kmp_prefix[x_pos-1]

    # Total complexity O(s + x)
    return -1


print(strstr("abxabcabcaby", "abcaby"))
print(strstr("abcxabcdabxabcdabcdabcy", "abcdabcy"))
