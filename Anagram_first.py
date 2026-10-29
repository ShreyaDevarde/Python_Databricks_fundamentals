import time
from collections import Counter

start = time.perf_counter()
def is_anagram_check(word1,word2):
    return sorted(word1) == sorted(word2)

print(is_anagram_check("listen", "silent"))
print(is_anagram_check("Hello", "world"))

def anagram_check(word3,word4):
    return Counter(word3) == Counter(word4)

print(anagram_check("heart", "earth"))
print(anagram_check("triangle", "integral"))

end = time.perf_counter()

print(f"Execution Time: {end - start:.6f} seconds")