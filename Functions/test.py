def random_password(lenth=8, complex=False):
    import string
    import random
    password_user = ''
    num_lower = 0
    num_upper = 0
    num_digits = 0
    if lenth < 8:
        print('The number of password content will be very low')
    elif complex :
        while num_lower<((lenth/2) // 3):
            password_user+=random.choice(string.ascii_lowercase)
            num_lower+=1
        while num_upper<((lenth/2) // 3):
            password_user+=random.choice(string.ascii_uppercase)
            num_upper+=1
        while num_digits<((lenth/2) // 3):
            password_user+=random.choice(string.digits)
            num_digits+=1
        while len(password_user)<lenth:
            password_user+=random.choice(string.punctuation)
        password_list = list(password_user)
        random.shuffle(password_list)
        password_user = ''.join(password_list)
        return password_user
    elif complex==False :
        while num_lower<(lenth // 4):
            password_user+=random.choice(string.ascii_lowercase)
            num_lower+=1
        while num_upper<(lenth // 4):
            password_user+=random.choice(string.ascii_uppercase)
            num_upper+=1
        while num_digits<(lenth // 4):
            password_user+=random.choice(string.digits)
            num_digits+=1
        while len(password_user)<lenth:
            password_user+=random.choice(string.punctuation)
        password_list = list(password_user)
        random.shuffle(password_list)
        password_user = ''.join(password_list)
        return password_user


print(random_password(20, complex=True))
