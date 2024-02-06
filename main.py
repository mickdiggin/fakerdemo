from faker import Faker

fake = Faker()

def getTenNames():
    fake = Faker()
    mynames = []
    for i in range(0,10):
        mynames.append(fake.name())
    return mynames

theNames = getTenNames()
print(theNames)