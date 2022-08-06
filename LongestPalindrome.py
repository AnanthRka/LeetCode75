def longestPalindrome(s: str) -> int:
    if len(s) == 1:
        return 1

    hash_table = set()
    
    for i in s:
        if i in hash_table:
            hash_table.remove(i)
        else:
            hash_table.add(i)
    
    return len(s) - len(hash_table) + 1 if len(hash_table) > 0 else len(s)

print(longestPalindrome("abccccdd"))