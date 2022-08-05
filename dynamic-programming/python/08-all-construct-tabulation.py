### Tabulation

def allConstruct(target, wordBank):
    table = [None] * (len(target) + 1)
    table[0] = [[]]
    for i in range(1, len(target) + 1):
        table[i] = []
    for i in range(0, len(target) + 1):
        for word in wordBank:
            if target[i : i + len(word)] == word:
                currentCombinations = table[i + len(word)]
                newCombinations = []
                for current in table[i]:
                    tmp = current.copy()
                    tmp.append(word)
                    newCombinations.append(tmp)
                if table[i + len(word)] is None:
                    table[i + len(word)] = newCombinations
                else:
                    entry = table[i + len(word)]
                    for c in newCombinations:
                       entry.append(c) 
    return table[len(target)]

print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
    # purp, le
    # p, ur, p, le
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
    # ab, cd, ef
    # ab, c, def
    # abc, def
    # abcd, ef
print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # []
print(allConstruct("aaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"])) # []