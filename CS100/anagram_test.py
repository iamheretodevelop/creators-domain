
def anagram(word, match):
    """
    The function should return true if the word is an anagram of the match word.
    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
    For instance,

    "evil" : "vile",
    "a gentleman" : "elegant man"
    "William Shakespeare" : "I am a weakish speller"

    Input: word = "evil", match = "vile"
    Output: anagram(word, match) -> True

    Input: word = "eyes ", match = "yess"
    Output: anagram(word, match) -> False

    Input: word = "Eleven Plus Two", match = "twelve plus one"
    Output: anagram(word, match) -> True

    """
    # write your code here
    word = word.lower()
    match = match.lower()
    wordlist = []
    matchlist = []
    word = word.replace(" ", "")
    match = match.replace(" ", "")
    for i in word:
        wordlist.append(i)
    for j in match:
        matchlist.append(j)
    if sorted(matchlist) == sorted(wordlist):
        return True 
    return False
    
