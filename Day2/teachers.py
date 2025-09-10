list1=[]

def assignSubject(id,sub):
    global list1
    list1.append(id,sub)
    return list1

def viewTeachersInfo():
    global list1
    return list1