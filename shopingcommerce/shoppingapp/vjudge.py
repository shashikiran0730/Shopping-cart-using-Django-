from num2words import num2words
while True:
    try:
        n=(input())
        a=[]
        for i in str(n):
            a.append(num2words(i))
        s=" ".join(a)
        print(s.upper())
    except:
        break