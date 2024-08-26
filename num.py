l=[]
while(True):
    try:
        n=int(input("Enter any number:"))
        l.append(n)
    except ValueError:
        print("I said an integer ya fool")
        continue
    except EOFError:
        break
print(l)
