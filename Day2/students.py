list1=[]

def addStudents(id,studentName):
    global list1
    list1.append(id,studentName)
    return list1

def viewStudents():
    global list1
    return list1