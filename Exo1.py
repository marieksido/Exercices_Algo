class Somme :

    def _intit_(self,n) :
        self.entier = n
        self.a = 3
        self.b = 5
        self.somme = 0

    def run(self) :
        for n in range (1, self.entier):
            if self.entier % self.a == 0:
                self.somme = self.somme + self.entier
            elif self.entier % self.b == 0:
                self.somme = self.somme + self.entier
            elif :
                print "Non divisible par %i ou %i" %(self.a,self.b)

                
