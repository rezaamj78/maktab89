import re


# 1
# x = re.findall(r'exercises', 'python exercises, PHP exercises, C# exercises')
# for i in x:
#     print(i)


# 2

# res = re.search(r'exercises', 'python exercises, PHP exercises, C# exercises')
# print(res.group())
# print(res.span())

# 3

# def convert_case(match_obj):
#     if match_obj.group(1) is not None:
#         return "_"
#     if match_obj.group(2) is not None:
#         return " "
#
#
# str1 = " "
# str = "regex_is Fucking me"
# print(re.sub(r"( )|(_)", convert_case, str))

# 4
# res = re.match(r'^([1-9]|0[1-9]|1[012])[/]([1-9]|0[1-9]|[12][0-9]|3[01])[/]\d{2}(\d{2})?$', "04/18/2022")
# print(res)

# 5
# res = re.split(r'-', 'yyyy-mm-dd')
# res.reverse()
# print("-".join(res))

# 6
# lst = ['Pazzell', 'Pizza', 'Nima', 'farhad']
# flag = 0
# for i in lst:
#     if re.findall(r'^P', i):
#         flag += 1
#
# if flag == 2:
#     print("match")


# 7

# res = re.findall(r'\d+', '51648dver846')
# print(res)

# 8
# res = re.findall(r'\b[a|e]\w+', "egg is an expensive")
# print(res)


# 9
# res = re.finditer(r'\d+', '48516dver846')
# for i in res:
#     print(i)


# 10
# res = re.sub(r'\b([A-Z])[a-z]*([a-z])\b', r'\1\2.', 'Mohammad Hossein Nima')
# print(res)


class User:
    users = dict()

    def __init__(self, name, email, phone, username, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.username = username
        self.password = password

    @staticmethod
    def validate_email(email):
        if re.match(r'^[\w\.]+@\w+\.\w+', email):
            return email

    @staticmethod
    def validate_phone(phone):
        if re.match(r'^\+98\d{10}$', phone):
            return phone

    @staticmethod
    def validate_password(password):
        if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$', password):
            return password

    @classmethod
    def validate_username(cls, username):
        if username not in cls.users:
            return username

    @classmethod
    def register(cls, name, email, phone, username, password):
        new_user = User(name, email, phone, username, password)
        cls.users[username] = new_user
        return new_user

    @classmethod
    def login(cls, username, password):
        try:
            assert username in cls.users.keys() and cls.users[
                username].password == password
            return cls.users[username]
        except AssertionError:
            print("Invalid username or password!!!")


class Main:
    def __init__(self):
        pass

    while True:
        order = input("Enter 1 register, 2 login, 3 exit: ")
        if order == "1":
            name = input("Enter your name: ")

            email = input("Enter your email: ")
            while not User.validate_email(email):
                email = input("valid format for email is: abc12edf@abc.abc: ")

            phone = input("Enter your phone number: ")
            while not User.validate_phone(phone):
                phone = input("Enter a valid phone: ")

            username = input("Enter your username: ")
            while not User.validate_username(username):
                username = input("Enter another username")

            password = input("Enter password: ")
            while not User.validate_password(password):
                password = input("Enter a valid password: ")

            User.register(name, email, phone, username, password)

        elif order == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            logged_user = User.login(username, password)
            if logged_user:
                print(f"Welcome {logged_user.name} with phone {logged_user.phone}")
            else:
                print("")

        elif order == "3":
            break


Main()
