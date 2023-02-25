class A:
    def __init__(self,name):
        self.name = name
        self.age = 15
        self.massa = 12
        print('создаём нового ученика')

    def Name(self):
        print(f'name {self.name} age {self.age} massa {self.massa}')

    #def hello(self,a):
        #print(a)
Yara = A('Yara')
Uri = A('U')
Uri.age = -29
Uri.massa = 96
Yara.massa = 50
Yara.Name()
Uri.Name()
#a = A(input())
#a.Name()