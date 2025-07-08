class Test:
    def factorial(self,chis):
        if chis == 0:
            return 1
        else:
            return chis * factorial(n-1)


    def stepan(self,chis , step):
        return chis ** step


    def formula(self,a,b):
        return (a ** 2) + (b ** 2)
test = Test()


print(test.stepan(6,2))
