def greet_user(name):
    print(f'Welcome {name} at Codezilla Python Course\nEnjoy your Learning Journey')
input_user = input("Please enter your name: ").title()
greet_user(input_user)
# -------method---------
def reverse_word(word):
    reverse = word[::-1]
    print(reverse)
input_word = input("Enter your text: ")
reverse_word(input_word)
# -----another method------
def reverse_word_2(word_2):
    reverse_now = ''.join(reversed(word_2)) # type(reversed(word_2)): class<reversed>
    print(reverse_now)
input_word_2 = input("Enter your text: ")
reverse_word_2(input_word_2)
# -----another method------
def reverse_word_3(word_3):
    reverse_char = ""
    for char in word_3:
        reverse_char = char + reverse_char
    print(reverse_char)    
input_word_3 = input("Enter your text: ")
reverse_word_3(input_word_3)
# -----another method------
def reverse_word_4(word_4):
    reverse_chr = [word_4[i] for i in range(len(word_4)-1, -1, -1)]
    use_join = "".join(reverse_chr)
    print(use_join)    
input_word_4 = input("Enter your text: ")
reverse_word_4(input_word_4)