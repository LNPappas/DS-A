class Factorial():

    def __init__(self):
        self.total = 0

    def recursive(self, data=0):
        if data == 0:
            x = self.total
            self.total = 0
            return x

        if self.total == 0:
            self.total = data
        else:
            self.total = self.total*data

        data -= 1
        return self.recursive(data)

    def iterative(self, info=0):

        if self.total == 0:
            self.total = info

        while info > 1:
            info -= 1
            self.total = self.total*info

        x = self.total
        self.total = 0
        return x
        
            

        
if __name__ == "__main__":
    f = Factorial()
    print(f.recursive(5))
    print(f.iterative(5))


