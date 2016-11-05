class Somme :

    def _intit_(run) :

        run.entier = 1
        run.somme = 0
        run.last_nb = 0
        run.Somme = 0
 
        while entier != 0
        {
            somme += entier % 10
            entier /= 10
        }
    
        div_3 = [0, 1, 3, 6, 9, 12, 15, 18, 21, 27, 30]
    
        if somme in div_3 :
            run.Somme += run.Somme + somme
            entier++
        
        last_nb = (entier)%10 
    
        div_5 = [0, 5]
    
        if last_nb in div_5
            run.Somme += run.Somme + last_nb
            entier++