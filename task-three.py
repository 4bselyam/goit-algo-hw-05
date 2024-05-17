import timeit

def boyer_moore(text, pattern):
    def create_bad_match_table(pattern):
        table = {}
        length = len(pattern)
        for i in range(length - 1):
            table[pattern[i]] = length - i - 1
        return table

    bad_match_table = create_bad_match_table(pattern)
    i = 0
    comparisons = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
            comparisons += 1
        comparisons += 1
        if j < 0:
            return i, comparisons
        else:
            i += bad_match_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1, comparisons


def kmp_search(text, pattern):
    def create_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = create_lps(pattern)
    i = j = 0
    comparisons = 0
    while i < len(text):
        comparisons += 1
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j, comparisons
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1, comparisons


def rabin_karp(text, pattern):
    def hash_func(s):
        return sum(ord(c) for c in s)

    m, n = len(pattern), len(text)
    pattern_hash = hash_func(pattern)
    text_hash = hash_func(text[:m])
    comparisons = 0

    for i in range(n - m + 1):
        comparisons += 1
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                return i, comparisons
        if i < n - m:
            text_hash = text_hash - ord(text[i]) + ord(text[i + m])
    return -1, comparisons


def run_tests(text, pattern):
    bm_time = timeit.timeit(lambda: boyer_moore(text, pattern), number=100)
    kmp_time = timeit.timeit(lambda: kmp_search(text, pattern), number=100)
    rk_time = timeit.timeit(lambda: rabin_karp(text, pattern), number=100)

    print(f"Boyer-Moore: {bm_time:.6f} seconds")
    print(f"KMP: {kmp_time:.6f} seconds")
    print(f"Rabin-Karp: {rk_time:.6f} seconds")

with open('article-1.txt', 'r', encoding='utf-8') as file1, open('article-2.txt', 'r', encoding='utf-8') as file2:
    text1 = file1.read()
    text2 = file2.read()

# Підрядки для тестування
existing_substring1 = "алгоритмів"  # існуючий підрядок
non_existing_substring1 = "неіснуючийпідрядок"  # вигаданий підрядок

existing_substring2 = "системи"  # існуючий підрядок
non_existing_substring2 = "неіснуючийпідрядок"  # вигаданий підрядок

print("Тестування на статті 1:")
run_tests(text1, existing_substring1)
run_tests(text1, non_existing_substring1)

print("\nТестування на статті 2:")
run_tests(text2, existing_substring2)
run_tests(text2, non_existing_substring2)
