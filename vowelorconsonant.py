a=input("enter an alphabet")
if a=="a" or a=="e" or a=="i" or a=="o" or a=="u" or a=="A" or a=="E" or a=="I" or a=="O" or a=="U":
    print("vowel")
elif a in ("b","c","d","f","g","h","j","k","l","l","m","n","p","q","r","s","t","x","v","w","y","z","B","C","D","F","G","H","I","J","k","L","M","N","Q","P","R","S","T","V","W","X","Y","Z"):
    print("consonant")
else:
    print("invalid")
