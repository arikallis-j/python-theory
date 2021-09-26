def listTest(li, x):
    length = len(li)
    for i in li:
        if i<length and x != li[i]:
            i+=1
        else:
            break
    if i<length:
        return True
    else:
        return False

class Concept:
    objects = []
    type = ""
    def __init__(self,type):
        self.type = type
    def new(self,object):
        self.objects.append(object)
    def isIt(self,object):
        return listTest(self.objects,object)
    def isWhere(self,object):
        return objects.index(object)


def new(type,object):
    type.new(object)

def isIt(type,object):
    return type.isIt(object)

def what(type):
    return type.objects
def isWhere(type,object):
    return type.isWhere(object)


list = Concept("list")

new(list,3)
text = what(list)
print(text)
text = isIt(list,3)
print(text)

class Judgment:
    type = ""
    description = type == 0
    def __init__(self,type,description):
        self.type = type
        self.description = description
    description_bool = description
    def isTrue(description_bool):
        return description_bool
man = Concept("man")
woman = Concept("woman")
new(man,"Slava")
new(woman,"Liza")
new(man,"Vadim")
def got_married_descrip(object_1,object_2):
    if isIt(object_1,"man") and isIt(object_2,"woman"):
        return True
    else:
        return False
object_1 = man.objects[isWhere(man,"Slava")]
object_2 = man.objects[isWhere(wooman,"Liza")]
got_married = Judgment("got_married",got_married_descrip(object_1,object_2))
