n="c"
history=[]
while (n!="q"):
    a=float(input("enter your first num : "))
    c=input("enter your operation (ex : +,-,*,/,etc..) : ")
    b=float(input("enter your second num : "))
    if c=="+":
        ans=a+b
        print(a,"+",b,"=",ans)
    elif c=="-":
        ans=a-b
        print(a,"-",b,"=",ans)
    elif c=="*":
        ans=a*b
        print(a,"*",b,"=",ans)
    elif c=="/":
        ans=a/b
        if b==0:
            print("answer undefined")
        print(a,"/",b,"=",ans)
    elif c=="**":
        ans=a**b
        print(a,"^",b,"=",ans)      
    elif c=="%":
        ans=a%b
        print(a,"%",b,"=",ans)
    else :
        print("invalid")
        ans = None
    if ans is not None :
        history.append(f"{a}{c}{b}")
    n=input("press any key to continue : \n press q for quit or exit : ")
    if n=="h":
        print("--------------------- \n Calculaton History \n ---------------------")
        if len(history)==0:
            print("---Empty---")
        else:
            for cal in history:
                print(cal)
if n=="q":
    print("Thanks for your calculation")