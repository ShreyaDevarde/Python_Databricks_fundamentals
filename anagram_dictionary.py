import time

start = time.perf_counter()

def is_anagram(a,b):

    if len(a) != len(b):
        return False

    freq = {}

    for ch in a:
        freq[ch] = freq.get(ch,0)+1

    for ch in b:

        if ch not in freq:
            return False

        freq[ch] -= 1

        if freq[ch] < 0:
            return False
        print(freq)
    return True

print(is_anagram("triangle","integral"))

end = time.perf_counter()

print(f"Execution Time: {end - start:.6f} seconds")