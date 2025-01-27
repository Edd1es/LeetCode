def areAnagrams(s: list[str], t: list[str]) -> list[str]:
    result = []  # To store the results for each pair
    
    for s_str, t_str in zip(s, t):  # Pair up corresponding strings
        # Step 1: Create frequency arrays
        freq_s = [0] * 26
        freq_t = [0] * 26
        
        # Step 2: Count frequencies of each character in s_str and t_str
        for char in s_str:
            freq_s[ord(char) - ord('a')] += 1
        for char in t_str:
            freq_t[ord(char) - ord('a')] += 1
        
        # Step 3: Compare the frequency arrays
        if freq_s == freq_t:
            result.append("YES")
        else:
            result.append("NO")
    
    # Step 4: Return the final results
    return result
    
s = ["listen", "rat", "hello"]
t = ["silent", "tar", "world"]

print(areAnagrams(s, t))  # Expected output: ["YES", "YES", "NO"]
