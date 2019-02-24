# Explicitly casts chars to ints

import get_string

s = get_string("String: ")
for c in s:
    print(f"{c} {ord(c)}")
