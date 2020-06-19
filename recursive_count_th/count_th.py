'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    
    key = "th"
    var1 = len(word)
    var2 = len(key)
    # Base Case
    # if the word equals 0 or the word is less then the key return 0
    if (var1 == 0 or var1 < var2):
        return 0
    # Recursive Case
    # Checking if the first substring matches
    # if it does then return it
    if (word[0: var2] == key):
        return count_th(word[var2 - 1:]) + 1

    # If not, return the count
    # from remaining index
    # repeats
    return count_th(word[var2 - 1:])
# no loops
