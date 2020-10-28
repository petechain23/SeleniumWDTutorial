def detectsAnagrams(textA, textB):
    if (len(textA) != len(textB)):
        return False
    if (len(textA) == len(textB)):
        if (sorted(textA) == sorted(textB)):
            return True
    else:
        return False


def sum(numbers):
    total = 0
    for num in numbers:
        total+=num
    print("Sum of the numbers: ", total)

def string_reverse(str1):
    rev_str = ' '
    index = len(str1) #defining index as length of string.
    while(index>0):
       rev_str = rev_str + str1[index-1]
       index = index-1
    return(rev_str)

def numInRange(n=0):
    if n in range(1,101):
        print ("so nay nam trong range",n)
    else:
        print("Number not in range")

def string_test(s):
    a = { 'Lower_Case':0 , 'Upper_Case':0} #intiail count of lower and upper
    for ch in s: #for loop
       if(ch.islower()): #if-elif-else condition
          a['Lower_Case'] = a['Lower_Case'] + 1
       elif(ch.isupper()):
          a['Upper_Case'] = a ['Upper_Case'] + 1
       else:
          pass

print ("=" *50)
txt1 = ["love", "I", "you"]
txt2 = ["you", "I", "love"]
print (detectsAnagrams(txt1,txt2))

print ("=" *50)
sum((100, 200, 300, 400, 0, 500))

print ("=" *50)
print (string_reverse('1tniop'))

print ("=" *50)
numInRange(101)

print ("=" *50)
import random
x = ['1','5','3','7','9']
print (random.randrange(10))
'njnjnjnjnjnj'
'''
fefefefeef
'''
primeList = []
for possiblePrime in range(2, 100):
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False

    if isPrime:
        primeList.append(possiblePrime)

print(primeList)

x = [[]]*3
x[1].append(1)
print(x)

for i in range (1,10):
    if i == 2:
        continue
    else:
        print(i)