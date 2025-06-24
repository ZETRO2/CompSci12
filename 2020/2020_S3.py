print("Enter the needle string (N):")
needle = input().strip()
print("Enter the haystack string (H):")
haystack = input().strip()

n = len(needle)
h = len(haystack)

def char_count(s):
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    return count

needle_count = char_count(needle)
found = []

window = haystack[:n]
window_count = char_count(window)

def same_count(a, b):
    if len(a) != len(b):
        return False
    for k in a:
        if a[k] != b.get(k, 0):
            return False
    return True

if same_count(needle_count, window_count):
    found.append(window)

for i in range(1, h - n + 1):
    out_char = haystack[i - 1]
    in_char = haystack[i + n - 1]
    window_count[out_char] -= 1
    if window_count[out_char] == 0:
        del window_count[out_char]
    window_count[in_char] = window_count.get(in_char, 0) + 1
    substring = haystack[i:i + n]
    if same_count(needle_count, window_count):
        if substring not in found:
            found.append(substring)

print(len(found))
