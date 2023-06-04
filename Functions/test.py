def reverse_word_4(word_4):
    reverse_chr = [word_4[i] for i in range(len(word_4)-1, -1, -1)]
    use_join = "".join(reverse_chr)
    print(use_join)    
input_word_4 = input("Enter your text: ")
reverse_word_4(input_word_4)