class fibo1 :
    
    def _init_(self, n):
        self.a = 1
        self.b = 1
        self.somme = 0
        self.n = n
    
    def run(self):
    
        for n in range(1, self.n):
            self.a,self.b = self.b,self.a + self.b
            self.somme = self.somme + self.a
        
        print(self.somme)
        

class fibo2 :

    def _init_(self, n) :
        self.arr = [1, 1]
        self.somme = 0
        self.n = n
        i=0

    def run(self) :

        while i != self.n:
            print(arr[-1])
            self.somme = sum(arr)
            arr.append(self.somme)
            i++


class fibo3 :

    def _init_(self, n):
        self.n = n
        self.somme = 0

    def run(self) :
        if self.n > 1 :
            self.somme = self.n * run(self.n -1)
        else :
            return 1



#def timereps(reps, func):
    #from time import time
    #start = time()
    #for i in range(0, reps):
        #func()
    #end = time()
    #return (end - start) / reps
