while True:
    n = int(input("Qani harcic gushakem? 😃\n"))
    x = 2**n
    print("De hima dzer mtqum minchev " + str(x-1) + "-y tiv paheq\n")
    list = []
    for k in range(n):
        a = []
        for i in range(x):
            if i%2*(k+1) >= 2*(k+1)/2 :
               a.append(i)
        list.append(a)
    num = 0
    for i in range(len(list)):
        print(list[i])
        ans = input("Ka mejy dzer pahats tivy?\n_").lower()
        while True:
           if ans in ["ha","ka", "ayo"]:
              num +=2**i
              break
           elif ans in ["che", "chka"]:
              break
           else:
              ans = input("Chem haskanum😑\n_").lower()
    print("Zder tivn e: " + str(num))
    text = input("Greq \"krkin\" krkin xaxalu hamar\n")
    if text != "krkin":
        break