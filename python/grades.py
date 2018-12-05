from compute import *

studentData={}
fo=open("class.txt")
for line in fo:
    string=line.split('|')
    st=student(string[0],string[1],string[2])
    studentData[st.id]=st
fo.close()

fo=open("a1.txt")
a1Max=fo.readline()
for line in fo:
    string=line.split('|')
    st=studentData.get(string[0])
    st.a1=string[1]
fo.close()

fo=open("a2.txt")
a2Max=fo.readline()
for line in fo:
    string=line.split('|')
    st=studentData.get(string[0])
    st.a2=string[1]
fo.close()

fo=open("project.txt")
projectMax=fo.readline()
for line in fo:
    string=line.split('|')
    st=studentData.get(string[0])
    st.project=string[1]
fo.close()

fo=open("test1.txt")
test1Max=fo.readline()
for line in fo:
    string=line.split('|')
    st=studentData.get(string[0])
    st.test1=string[1]
fo.close()

fo=open("test2.txt")
test2Max=fo.readline()
for line in fo:
    string=line.split('|')
    st=studentData.get(string[0])
    st.test2=string[1]
    st.setTotal()
    st.setGrade()
fo.close()



terminate=0
while(terminate!=6):
    print("1> Display individual component") 
    print("2> Display component average")
    print("3> Display Standard Report")
    print("4> Sort by alternate column")
    print("5> Change Pass/Fail point")
    print("6> Exit ")

    option=input("Please enter an option number : ")
    print()
    if(str(option)=='1'):
        displayIndividualComponent(studentData,option)
        
    elif(str(option)=='2'):
        displayIndividualComponent(studentData,option)

    elif(str(option)=='3'):
        displayStandardReport(studentData)

    elif(str(option)=='4'):
        displayAccTwoSortOrders(studentData)
        print()

    elif(str(option)=='5'):
        changeFailPoint(studentData)
            
    elif(str(option)=='6'):
        print("Good Bye")
        terminate=6
        
    else:
        print("You have entered an invalid option")
        print("Please enter again")
        print()




    
