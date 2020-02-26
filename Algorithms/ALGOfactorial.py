class Factorial():

    def __init__(self):
        pass

    def recursive(self, data=0):
        if data == 2:
            return 2
        return data * self.recursive(data-1)

    def iterative(self, info=0):
        i = 2
        answer = 1
        if info == 2:
            return 2
        while i <= info:
            answer = answer*i
            i += 1
        return answer       

        
if __name__ == "__main__":
    f = Factorial()
    print(f.recursive(5))
    print(f.iterative(5))



