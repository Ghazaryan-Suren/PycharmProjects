def create_a(n):
    a = [list(range(n*(i),n*(i+1))) for i in range(n)]
    a = [[str(j) for j in i] for i in a]
    for i in a:
        for j in i:
            if len(j)<len(str(n**2-1)):
               i[i.index(j)] = "0"*(len(str(n**2-1))-len(j)) + j
    a = [["💜"+j for j in i] for i in a]
    return a
def show(a):
    print("")
    [print(i) for i in a]
    print("")
def change(x):
    if "💜" in x:
       return x.replace("💜", "💛")
    else:
       return x.replace("💛", "💜")
def check(a):
    for i in a:
        for j in i:
            if "💜" in j:
               return False
    return True
def play(a):
    while True:
      show(a)
      print("Choose a number")
      try:
         m = int(input("_"))
         if m not in list(range(n**2)):
            print("Number not found\n")
            break
      except:
            print("Not a number\n")
            break
      a[m//n][m%n]=change(a[m//n][m%n])
      if m//n>0:
         a[m//n-1][m%n]=change(a[m//n-1][m%n])
      if m//n<n-1:
         a[m//n+1][m%n]=change(a[m//n+1][m%n])
      if m%n>0:
         a[m//n][m%n-1]=change(a[m//n][m%n-1])
      if m%n<n-1:
         a[m//n][m%n+1]=change(a[m//n][m%n+1])
      if check(a):
         show(a)
         print("\n       YOU WON!!!!!\n")
         break

k ="play"
while k in ["play", "Play", "\"Play\""]:
      print("Enter the number between 2 and 7")
      try:
          n = int(input("_"))
          if n not in list(range(2,8)):
             continue
      except:
          continue
      a = create_a(n)
      play(a)
      print("Enter \"Play\" to play")
      k = input("_")
      print("\n")
print("Goodbye 👋👋👋")