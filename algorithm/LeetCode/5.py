# Longest Palindrome Substring
def longestPalindrome(s: str) -> str:
    if len(s) < 2 or s == s[::-1]:
        return s

    current_index = 0
    longest_palindrome = ""

    while current_index < len(s):
        palindrome_start_index, palindrome_end_index = current_index, current_index

        while (
            palindrome_start_index > 0
            and s[palindrome_start_index] == s[palindrome_start_index - 1]
        ):
            palindrome_start_index -= 1
        while (
            palindrome_end_index < len(s) - 1
            and s[palindrome_end_index] == s[palindrome_end_index + 1]
        ):
            palindrome_end_index += 1

        current_index = palindrome_end_index + 1

        while (
            palindrome_start_index >= 0
            and palindrome_end_index < len(s)
            and s[palindrome_start_index] == s[palindrome_end_index]
        ):
            palindrome = s[palindrome_start_index : palindrome_end_index + 1]
            palindrome_start_index -= 1
            palindrome_end_index += 1

        longest_palindrome = (
            palindrome
            if len(palindrome) > len(longest_palindrome)
            else longest_palindrome
        )

    return longest_palindrome


print(longestPalindrome("aacabdkacaa"))
