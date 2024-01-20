def fullname(first_name,last_name):
    z=first_name + " " + last_name
    return z
def string_alternative(x):
    return x[::2]

user_name=str(input("enter the first name:"))
user_name2=str(input("enter the last name:"))
user_full_name = fullname(user_name, user_name2)


print(user_full_name)

def main():
    alterstring = string_alternative(user_full_name)
    print(alterstring)

if __name__ == '__main__':
    main()

