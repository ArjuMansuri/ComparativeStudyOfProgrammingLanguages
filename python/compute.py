from collections import OrderedDict
import copy


a1Max=0
a2Max=0
projectMax=0
test1Max=0
test2Max=0
class student:

    def __init__(self,id,firstName,lastName,a1='',a2='',project='',test1='',test2='',total=0.0,grade="F"):
        self.id=id
        self.firstName=firstName
        self.lastName=lastName
        self.a1=a1
        self.a2=a2
        self.project=project
        self.test1=test1
        self.test2=test2
        self.total=total
        self.grade=grade

    def setTotal(self):
        global a1Max
        fo=open("a1.txt")
        a1Max=int(fo.readline())
        if(str(self.a1)==''):
            self.a1=0
        a1Contri=round(float(self.a1)*7.5/a1Max,2)
        fo.close()

        global a2Max
        fo=open("a2.txt")
        a2Max=int(fo.readline())
        if(str(self.a2)==''):
            self.a2=0
        a2Contri=round(float(self.a2)*7.5/a2Max,2)
        fo.close()

        global projectMax
        fo=open("project.txt")
        projectMax=int(fo.readline())
        if(str(self.project)==''):
            self.project=0
        projectContri=round(int(self.project)*25/projectMax,2)
        fo.close()

        global test1Max
        fo=open("test1.txt")
        test1Max=int(fo.readline())
        if(str(self.test1)==''):
            self.test1=0
        test1Contri=round(int(self.test1)*30/test1Max,2)
        fo.close()

        global test2Max
        fo=open("test2.txt")
        test2Max=int(fo.readline())
        if(str(self.test2)==''):
            self.test2=0
        test2Contri=round(int(self.test2)*30/test2Max,2)
        fo.close()

        self.total=a1Contri+a2Contri+projectContri+test1Contri+test2Contri

    def setGrade(self,passPoint=50):
        pPoint=float(passPoint)
        addPoint=float((100-pPoint)/7)
        totalT=float(self.total)
        
        if(totalT< pPoint):
            self.grade="F"
        elif( pPoint+addPoint > totalT >= pPoint ):
            self.grade="C"
        elif( pPoint+(addPoint*2) > totalT >= pPoint+addPoint ):
            self.grade="B-"
        elif( pPoint+(addPoint*3) > totalT >= pPoint+(addPoint*2) ):
            self.grade="B"
        elif( pPoint+(addPoint*4) > totalT >= pPoint+(addPoint*3) ):
            self.grade="B+"
        elif( pPoint+(addPoint*5) > totalT >= pPoint+(addPoint*4) ):
            self.grade="A-"
        elif( pPoint+(addPoint*6) > totalT >= pPoint+(addPoint*5) ):
            self.grade="A"
        elif(100 >= totalT >= pPoint+(addPoint*6) ):
            self.grade="A+"

def displayIndividualComponent(stuData,option):
    cont=0
    studentData=OrderedDict(sorted(stuData.items()))
    while(cont!=2):
        print("Following are the components : ")
        print("Assignment1 : a1/A1")
        print("Assignment2 : a2/A2")
        print("Project : p/P")
        print("Test1 : t1/T1")
        print("Test2 : t2/T2")
        component=input("Enter your option:")
        print()
    
        if(int(option)==1):
            if(component=='a1' or component=='A1'):
                cont=2
                print("A1 grades ("+str(a1Max)+')')
                for key,value in studentData.items():
                    if(value.a1==0):
                        value.a1=''
                    print ('{0:10s} {1:6s} {2:6s}      {3:4s}'.format(value.id.strip(),value.lastName.strip()+',',value.firstName.strip(),str(value.a1).strip()))
            
            elif(component=='a2' or component=='A2'):
                cont=2
                print("A2 grades ("+str(a2Max)+')')
                for key,value in studentData.items():
                    if(value.a2==0):
                        value.a2=''
                    print ('{0:10s} {1:6s} {2:6s}      {3:4s}'.format(value.id.strip(),value.lastName.strip()+',',value.firstName.strip(),str(value.a2).strip()))

            elif(component=='p' or component=='P'):
                cont=2
                print("Project grades ("+str(projectMax)+')')
                for key,value in studentData.items():
                    if(value.project==0):
                        value.project=''
                    print ('{0:10s} {1:6s} {2:6s}      {3:4s}'.format(value.id.strip(),value.lastName.strip()+',',value.firstName.strip(),str(value.project).strip()))

            elif(component=='t1' or component=='T1'):
                cont=2
                print("Test1 grades ("+str(test1Max)+')')
                for key,value in studentData.items():
                    if(value.test1==0):
                        value.test1=''
                    print ('{0:10s} {1:6s} {2:6s}      {3:4s}'.format(value.id.strip(),value.lastName.strip()+',',value.firstName.strip(),str(value.test1).strip()))    

            elif(component=='t2' or component=='T2'):
                cont=2
                print("Test2 grades ("+str(test2Max)+')')
                for key,value in studentData.items():
                    if(value.test2==0):
                        value.test2=''
                    print ('{0:10s} {1:6s} {2:6s}      {3:4s}'.format(value.id.strip(),value.lastName.strip()+',',value.firstName.strip(),str(value.test2).strip()))

            else:
                cont=1
                print("You have entered an invalid component")
                print()

        if(int(option)==2):
            if(component=='a1' or component=='A1'):
                cont=2
                a1Total=0
                for key,value in studentData.items():
                    if(str(value.a1)==''):
                        value.a1=0
                    a1Total=a1Total+int(value.a1)
                avg=round(a1Total/len(studentData),2)
                print("A1 average:"+str(avg)+"/"+str(a1Max))
            
           
            elif(component=='a2' or component=='A2'):
                cont=2
                a2Total=0
                for key,value in studentData.items():
                    if(str(value.a2)==''):
                        value.a2=0
                    a2Total=a2Total+int(value.a2)
                avg=round(a2Total/len(studentData),2)
                print("A2 average:"+str(avg)+"/"+str(a2Max))
                

            elif(component=='p' or component=='P'):
                cont=2
                projectTotal=0;
                for key,value in studentData.items():
                    if(str(value.project)==''):
                        value.project=0
                    projectTotal=projectTotal+int(value.project)
                avg=round(projectTotal/len(studentData),2)
                print("Project average:"+str(avg)+"/"+str(projectMax))
               

            elif(component=='t1' or component=='T1'):
                cont=2
                test1Total=0
                for key,value in studentData.items():
                    if(str(value.test1)==''):
                        value.test1=0
                    test1Total=test1Total+int(value.test1)
                avg=round(test1Total/len(studentData),2)
                print("Test1 average:"+str(avg)+"/"+str(test1Max))
               

            elif(component=='t2' or component=='T2'):
                cont=2
                test2Total=0
                for key,value in studentData.items():
                    if(str(value.test2)==''):
                        value.test2=0
                    test2Total=test2Total+int(value.test2)
                avg=round(test2Total/len(studentData),2)
                print("Test2 average:"+str(avg)+"/"+str(test2Max))

            else:
                cont=1
                print("You have entered an invalid component")
                print("Please enter a valid component")
                print()
    print()

def displayStandardReport(stuData):
    studentData=OrderedDict(sorted(stuData.items()))
    print('{0:5s} {1:6s} {2:6s} {3:4s} {4:4s} {5:4s} {6:4s} {7:4s} {8:6s} {9:2s}'.format("ID","LN","FN","A1","A2","PR","T1","T2","GR","FL"))
    for key,value in studentData.items():
        if(value.a1==0):
            value.a1=""
        if(value.a2==0):
            value.a2=""
        if(value.project==0):
            value.project=""
        if(value.test1==0):
            value.test1=""
        if(value.test2==0):
            value.test2=""
        totalT=float(value.total)
        if(totalT==0.0 or totalT<10):
            print('{0:5s} {1:6s} {2:6s} {3:4s} {4:4s} {5:4s} {6:4s} {7:4s} {8:.2f}   {9:4s}'.format(value.id,value.lastName.strip(),value.firstName.strip(),str(value.a1).strip(),str(value.a2).strip(),str(value.project).strip(),str(value.test1).strip(),str(value.test2).strip(),totalT,value.grade.strip()))
        else:
            print('{0:5s} {1:6s} {2:6s} {3:4s} {4:4s} {5:4s} {6:4s} {7:4s} {8:.2f}  {9:4s}'.format(value.id,value.lastName.strip(),value.firstName.strip(),str(value.a1).strip(),str(value.a2).strip(),str(value.project).strip(),str(value.test1).strip(),str(value.test2).strip(),totalT,value.grade.strip()))        
    print()
    
def displayAccTwoSortOrders(stuData):
    cont=0
    while(cont!=2):
        print("You can sort data in two ways : ")
        print("1. By Last Name")
        print("2. By Numeric Grade")
        option=input("Enter your option : ")
        print()
        if(str(option)=='1'):
            cont=2
            studentData=sorted(stuData.values(),key=lambda student:student.lastName)
            print('{0:5s} {1:6s} {2:6s} {3:4s} {4:4s} {5:4s} {6:4s} {7:4s} {8:6s} {9:2s}'.format("ID","LN","FN","A1","A2","PR","T1","T2","GR","FL"))
            for value in studentData:
                if(value.a1==0):
                    value.a1=""
                if(value.a2==0):
                    value.a2=""
                if(value.project==0):
                    value.project=""
                if(value.test1==0):
                    value.test1=""
                if(value.test2==0):
                    value.test2=""
                totalT=float(value.total)
                if(totalT==0.0 or totalT<10):
                    print('{0:5s} {1:6s} {2:6s} {3:4s} {4:4s} {5:4s} {6:4s} {7:4s} {8:.2f}   {9:4s}'.format(value.id,value.lastName.strip(),value.firstName.strip(),str(value.a1).strip(),str(value.a2).strip(),str(value.project).strip(),str(value.test1).strip(),str(value.test2).strip(),totalT,value.grade.strip()))
                else:
                   print('{0:5s} {1:6s} {2:6s} {3:4s} {4:4s} {5:4s} {6:4s} {7:4s} {8:.2f}  {9:4s}'.format(value.id,value.lastName.strip(),value.firstName.strip(),str(value.a1).strip(),str(value.a2).strip(),str(value.project).strip(),str(value.test1).strip(),str(value.test2).strip(),totalT,value.grade.strip()))        
                

        elif(str(option)=='2'):
            cont=2
            studentData=sorted(stuData.values(),key=lambda student:student.total,reverse=True)
            print('{0:5s} {1:6s} {2:6s} {3:4s} {4:4s} {5:4s} {6:4s} {7:4s} {8:6s} {9:2s}'.format("ID","LN","FN","A1","A2","PR","T1","T2","GR","FL"))
            for value in studentData:
                if(value.a1==0):
                    value.a1=""
                if(value.a2==0):
                    value.a2=""
                if(value.project==0):
                    value.project=""
                if(value.test1==0):
                    value.test1=""
                if(value.test2==0):
                    value.test2=""
                totalT=float(value.total)
                if(totalT==0.0 or totalT<10):
                    print('{0:5s} {1:6s} {2:6s} {3:4s} {4:4s} {5:4s} {6:4s} {7:4s} {8:.2f}   {9:4s}'.format(value.id,value.lastName.strip(),value.firstName.strip(),str(value.a1).strip(),str(value.a2).strip(),str(value.project).strip(),str(value.test1).strip(),str(value.test2).strip(),totalT,value.grade.strip()))
                else:
                    print('{0:5s} {1:6s} {2:6s} {3:4s} {4:4s} {5:4s} {6:4s} {7:4s} {8:.2f}  {9:4s}'.format(value.id,value.lastName.strip(),value.firstName.strip(),str(value.a1).strip(),str(value.a2).strip(),str(value.project).strip(),str(value.test1).strip(),str(value.test2).strip(),totalT,value.grade.strip()))
        else:
            cont=1
            print("You have entered an invalid option")   
    
def changeFailPoint(studentData):
    stuData=copy.deepcopy(studentData)
    cont=0
    try:
        while(cont!=2):
            failPoint=float(input("Enter new pass/fail point : "))
            if(0 <= failPoint < 100):
                cont=2
                for key,value in stuData.items():
                    st=value;
                    st.setGrade(failPoint)
                displayStandardReport(stuData)
            else:
                cont=1
                print("Please enter a valid value between 0 and 100")
                print()
                
    except:
        print("Please enter a number")
        print()
        changeFailPoint(studentData)
      
        
        


        
        

    
       
        
        
        
