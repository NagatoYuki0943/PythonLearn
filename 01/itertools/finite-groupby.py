# 有限迭代器（Iterators Terminating on the Shortest Input Sequence）
# groupby(iterable,key=None) 可以把相邻元素按照 key 函数分组，并返回相应的 key 和 groupby，如果 key 函数为 None，则只有相同的元素才能放在一组


from itertools import groupby


def count_vowels(word: str) -> int:
    vowel_count: int = 0

    for letter in word:
        if letter in "aeiouAEIOU":
            vowel_count += 1

    return vowel_count


words: list[str] = ["cat", "dog", "mood", "banana", "red", "hood", "mate"]
# 先要进行排序
sorted_words: list[str] = sorted(words, key=count_vowels)

grouped: groupby = groupby(sorted_words, key=count_vowels)

for vowels, group in grouped:
    print(f"{vowels = }, {list(group)}")
# vowels = 1, ['cat', 'dog', 'red']
# vowels = 2, ['mood', 'hood', 'mate']
# vowels = 3, ['banana']
