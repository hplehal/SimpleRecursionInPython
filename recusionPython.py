#factorial
def fact(num):
    if num <= 1:
        return 1      
    else:
        return num * fact(num-1)

print(fact(2))

#explode("hello" -> h e l l o)

def explode(word):
    
    if len(word) <= 1:
        return word
    else: 
        return word[0] + ' ' + explode(word[1:])


print(explode('word'))

#removeDup 

def removeDup(word):
    if len(word) <= 1:
        return word
    elif word[0] == word[1]:
        return removeDup(word[1:])
    else:
        return word[0] + removeDup(word[1:])

print(removeDup('aaabbbccc'))
