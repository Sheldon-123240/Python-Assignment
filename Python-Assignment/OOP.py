#Assignment 1
class smartphone:
    def __init__( self, OS, pixels,):
        self.OS = OS
        self.pixels = pixels

    def specs(self):
            print(f"This phone has" + self.OS)
            
my_smartphone = smartphone('android', 32)

print(my_smartphone.OS)
print(my_smartphone.pixels)

my_smartphone.specs()

class Huawei(smartphone):
    pass

my_smartphone = smartphone('macos', 46)

my_smartphone.specs()
