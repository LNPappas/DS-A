counter = 0
def inception():
    global counter
    print(counter)
    #base case to prevent stack overflow
    if counter > 3:
        return "done" #<- 1
    counter +=1
    #recursive case
    return inception() # <- 2 returns (base case and return from recursion)
    
if __name__ == "__main__":
    print(inception())