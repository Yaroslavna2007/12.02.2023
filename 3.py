class A:
    def __init__(self,name):
        self.__name = name
        self.__age = 15
        print('создаём нового ученика')

    def Name(self):
        print(f'name {self.__name} age {self.__age}')

    def set_age(self,age):
        if age>=0:
            self.__age = age
        else:
            print('недопустимо')

    #def hello(self,a):
        #print(a)
Yara = A('Yara')
Uri = A('U')
Uri.__age = -29
Yara.Name()
Uri.Name()
Uri.set_age(-29)
#a = A(input())
#a.Name()