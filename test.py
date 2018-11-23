import File


print(File.exists("~/.emacs.d/utils/Build.py"))




class Aminal:

    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.teregol = self.type()

    def type(self):
        return "UROBOROOOSSS!!!!"
        
    def say(self):
        print(self.type() + " " + self.name + " " + str(self.age) + " " + self.teregol) 


class Kec(Aminal):

    def __init__(self, age, name):
       super().__init__(age, name)

    def type(self):
        return "ce je kec!"

kot = Kec(5, "keceren")


kot.say      ()
