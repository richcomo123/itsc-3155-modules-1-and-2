string=input("Enter a String:")
newstring=string.replace(" ", "")
lower=""
upper=""
for x in newstring:
  if x.islower():
    lower+=x
  elif x.isupper():
    upper+=x
print(lower+upper)





