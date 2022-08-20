
import string
import random
 
if __name__ == "__main__":
 str1 = string.ascii_lowercase
 str2 = string.ascii_uppercase
 str3 = string.digits
 str4 = string.punctuation
 pwdlen = int(input("Enter password length\n"))
 s = []
 s.extend(list(str1))
 s.extend(list(str2))
 s.extend(list(str3))
 s.extend(list(str4))
 # random.shuffle(s)
 print("Your password is: ")
 print("".join(random.sample(s, pwdlen)))

 
a = input("")
