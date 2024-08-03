print("Road Map Provider Project")

status= int(input("enter 1 for fresher/2 for experienced ="))

if status==1:
    interest=int(input("Enter your interested field 1-web 2 -App 3-Data Science"))
    if interest==1:
        print("Learn HTML, JS, CS ")
    elif interest==2:
        print("Learn JAVA,C++,C")
    elif interest==3:
        print("Master Python")
    else:
        print("Invalid Output")

if status==2:
    interest=int(input("Enter your interested field 1-Data Analysis 2 -Cloud Computing 3-Front End"))
    if interest==1:
        print("Learn Python,Excel,Power Bi")
    elif interest==2:
        print("Learn DevOps,and Python for Automation")
    elif interest==3:
        print("Learn Python 1and Django for Backend")
    else:
        print("Invalid Output")