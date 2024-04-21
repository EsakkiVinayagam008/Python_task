value = "raju008"
digit=0
letter=0
for ch in value:
   if ch.isdigit():
      digit=digit+1
   elif ch.isalpha():
      letter=letter+1
   else:
      pass
print("Letters:", letter)
print("Digits:", digit)