glob = 'A'

def funky1():
    funkyO = 'B'
    print(glob)
    
    def funky2():
        funkyI = 'C'
        print(glob)
        print(funkyO)
        
funky1()