def decode_string_internal(s, i, multiplier):
    """
    Takes a string and decode it
    :param s: String to decode
    :param i: Current index of the string from which start the decoding
    :param multiplier: Multiplies the ret value by this number
    :return: The decoded string
    """

    if len(s) < 1:
        return s

    ret = []

    number_detected = False
    number_str = ""
    while i < len(s):
        # We've detected a number, start "number mode"
        if '0' <= s[i] <= '9':
            number_detected = True
            number_str += s[i]
        elif number_detected:
            # We didn't detect a number but we were in "number mode"
            number_detected = False
            # Convert the number we were parsing
            counter = int(number_str)
            number_str = ""
            # Recursively decode the following part of the string
            # until ']' is found and return the string duplicated by the multiplier
            decoded_str, i = decode_string_internal(s, i + 1, counter)
            # Concat the recursive call the result
            ret += decoded_str
        elif s[i] == ']':
            # We've got here recursively, we shall multiply and return what we've parsed
            return multiplier * ret, i
        else:
            # Standard char and no specific mode going on, just concat the value
            ret.append(s[i])

        i += 1

    # Convert result to string
    return ''.join(ret)


def decodeString(s):
    return decode_string_internal(s, 0, 0)


print(decodeString("z1[y]zzz2[abc]"))
