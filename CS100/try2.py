def same_order(original, sample):
    """
    The functions takes two arguments, original and sample, both string type. 
    It returns True if the characters in sample are contained in original 
    in the same order. 
    eg: 
    input: original = 'abCdODzIgNbevG', sample = 'CODING'
    output: same_order(original, sample) -> True 
    
    input: original = 'abCdODzIgNbevG', sample = "HELLO'
    output: same_order(original, sample) -> False
    """
    if sample == original:
        return True
    for i in range(len(sample)):
        if not(sample[i] in original):
            return False
    a = 0
    for char in sample:
        if char in original[a:len(original)]:
            a = sample.index(char)
        else:
            return False
    return True

a = same_order("AHRIKASHA", "KASAH")
print(a)