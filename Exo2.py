class fibo1 :
    
    def _init_(run, n):
        run.a = 1
        run.b = 1
        run.somme = 0
        run.n = n
    
    def fibo_1(run):
    
        for n in range(1,run.n):
            run.a,run.b = run.b,run.a + run.b
            run.somme = run.somme + run.a
        
        print(run.somme)
        
#def timereps(reps, func):
    #from time import time
    #start = time()
    #for i in range(0, reps):
        #func()
    #end = time()
    #return (end - start) / reps
