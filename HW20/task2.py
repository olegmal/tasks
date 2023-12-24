
	# Given a string, find the length of the longest substring without repeating characters.
	# Examples:
	# Given "abcabcbb", the answer is "abc", which the length is 3.
	# Given "bbbbb", the answer is "b", with the length of 1.
	# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
    # "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(mystr: str)-> int:

    myset = {}
    start, result = 0, 0

    for i in range(len(mystr)):
        if mystr[i] in myset:
            start = max(myset[mystr[i]], start)
        result = max(result, i - start + 1)
        myset[mystr[i]] = i +1

    return result

mystr = "abcabcbb"
print(lengthOfLongestSubstring(mystr))