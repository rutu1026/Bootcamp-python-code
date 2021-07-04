import hashlib
  
s = input("Enter your string : ")
hashed = hashlib.md5(s.encode())
  

print("\nThe md5 hashed byte string is :")
print(hashed.digest())
