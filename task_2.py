from trie import Trie

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise TypeError("Input must be a list of strings")

        if not strings:
            return ""

            # Вставляємо всі слова в Trie
        for word in strings:
            self.put(word)

            # Знаходимо спільний префікс за першим словом
        prefix = ""
        current = self.root

        while True:
            if len(current.children) != 1 or current.value is not None:
                break  # більше однієї гілки або це кінець слова — спільний префікс закінчився

            char, next_node = next(iter(current.children.items()))
            prefix += char
            current = next_node

        return prefix

# if __name__ == "__main__":
#     # Тести
#     trie = LongestCommonWord()
#     strings = ["flower", "flow", "flight"]
#     assert trie.find_longest_common_word(strings) == "fl"
#
#     trie = LongestCommonWord()
#     strings = ["interspecies", "interstellar", "interstate"]
#     assert trie.find_longest_common_word(strings) == "inters"
#
#     trie = LongestCommonWord()
#     strings = ["dog", "racecar", "car"]
#     assert trie.find_longest_common_word(strings) == ""

def run_test(strings, expected):
    trie = LongestCommonWord()
    result = trie.find_longest_common_word(strings)
    status = "✅ PASSED" if result == expected else f"❌ FAILED (expected: '{expected}', got: '{result}')"
    print(f"Test with input {strings}: {status}")

if __name__ == "__main__":
    run_test(["flower", "flow", "flight"], "fl")
    run_test(["interspecies", "interstellar", "interstate"], "inters")
    run_test(["dog", "racecar", "car"], "")
    run_test([], "")
    run_test(["onlyone"], "onlyone")
