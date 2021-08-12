user_entry = input('Enter a word: ')

if len(user_entry) > 5: 
    print(user_entry, ' is longer than 5 characters')



num_entry = int(input('Enter a number larger than 100: '))

if num_entry > 100:
    print('Valid Entry!')
else: 
    print('Number too small')


lowercase_letter_entry = input('Enter a lowercase letter: ').lower()

if lowercase_letter_entry in 'aeiou':
    print('Letter is a vowel')
else:
    print('Letter is Not a vowel')



#Part B
num = 10

if (num % 2 == 0) and ((num / 5) % 1 == 0):
    print('Number is even and is divisible by 5')
else:
    print('Number is not even and/or divisible by 5')


word = 'Encyclopedia'

if len(word) > 9 and not(' ' in word):
    print(word, ' is a really long word')
else:
    print(word,' is either short or it contains multiple words')



letter = 'A'
cap_consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
vowels = 'aeiou'

if not(letter in cap_consonants) or not(letter in vowels):
   print("'" + letter + "'", "is either a lowercase vowel OR a capital consonant.")
else:
   print("Pick a capital consonant or a lowercase vowel.")
#Using not will refactor if statement to check for inverse statements. 

num = 5
num >= 0 and num*2 <= 50 and num%2 == 0 #False
num >= 0 or num*2 <= 50 or num%2 == 0 #True
num >= 0 and num*2 <= 50 or num%2 == 0 #True
num >= 0 or num*2 <= 50 and num%2 == 0 #True
not num < 0 and num%3 != 0 #True
not (num%3 == 0 or num*4 >= 20) #False



#Part C
#PA
num = 7 # Try the values 10, 15, and 7 as well.

if num%2 == 0 and num%3 == 0:
    print(num, "is divisible by 2 and 3.")  
elif num%3 == 0:
   print(num, "is divisible by 3.")
elif num%2 == 0:
   print(num, "is divisible by 2.")
else:
   print(num, "is NOT divisible by 2 or 3.")

#Pb
exam_score = 89
 
if exam_score >= 90 and exam_score<= 100:
    print(str(exam_score),'% = A' )
elif exam_score <= 89 and exam_score >= 80:
    print(str(exam_score),'% = B' )
elif exam_score <=79 and exam_score >= 70:
    print(str(exam_score),'% = C' )
elif exam_score <= 69 and exam_score >=65:
    print(str(exam_score),'% = D' )
else:
    print(str(exam_score),'% = F' )
    

#PC
temperature = 'hot'
wetness = 'rainy'

if temperature == 'hot' and wetness == 'rainy':
    print("Go watch netflix")
elif temperature == 'cold' and wetness == 'rainy':
    print("Stay home and read")
elif temperature == 'cold' and wetness == 'dry':
    print("Go see your friend")
elif temperature == 'hot' and wetness == 'dry':
    print("Hit the pool")


lunch_selection = input('What do you want for lunch')
topping = None

burger = 4.99
cheese = 0.49
salad = 2.99
ranch_dressing = 0.10
italian_dressing = 0.20

total_order = None

if lunch_selection == 'burger':
    topping = input('Do you want cheese').lower()
    if topping == "yes":
        total_order = burger + cheese
    else:
        total_order = burger
    print('Your meal order is ', "{:.2f}".format(total_order), ' plus Tax')
elif lunch_selection == 'salad':
    topping = input("Would you like some Ranch or Italian Dressing").lower()
    if topping == 'ranch':
        total_order = salad + ranch_dressing
    elif topping == 'italian':
        total_order = salad + italian_dressing
    else:
        total_order = salad
    print('Your meal order is ', "{:.2f}".format(total_order), ' plus Tax')
else:
    print('Sorry we do not have that item')

#Best place to place the drink question is outside separately from the conditional statement because it is the best method to keep the code DRY.


