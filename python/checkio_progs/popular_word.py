import re
def popular_words(text, words):
    # your code here
    
   # print(text);print(words)
    #lp = text.lower()

    list1 = {}

    for word in words:

        list1[word] = text.lower().count(word)
        #print(list1)
    return list1


    #return {w:text.lower().count(w) for w in words}
   

if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']) == {
        'i': 4,
        'was': 3,
        'three': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")

