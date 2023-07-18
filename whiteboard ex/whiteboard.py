# Given a string of letters, write a function to see if the word  (case insensitive) is a palindrome (the same word spelled forward and backwards).
# The given string will contain only letters 
# Examples:
# is_palindrome("RaceCar") \\ => True
# is_palindrome("mom")  \\ => True
# is_palindrome("Shoha") \\ => False

def solution(word):
    word= word.lower()
    reverse_word=word[::-1]
    if reverse_word== word:
        return True
    else:
        return False
    # word = word.lower()
    # first_half = ""
    # second_half = ""
    # for i in range(len(word)//2):
    #     first_half+=word[i]
    #     second_half+=word[-(i+1)]
    # if first_half == second_half:
    #     return True
    # else:
    #     return False
    

    

    