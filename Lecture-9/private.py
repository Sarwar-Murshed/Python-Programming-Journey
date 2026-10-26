# making account password as private attribute

class Account:
    def __init__(self,accNo,accPass):
        self.accNo = accNo
        self.__accPass = accPass   # two double underline defines the attribute as private

    def reset_Pass(self):
        print(self.__accPass)

acc1 = Account(12345,"asdf1234")       
acc1.reset_Pass()     

# print(acc1.__accPass) outside the class

print(acc1.reset_Pass())  # reset_Pass() is inside the class