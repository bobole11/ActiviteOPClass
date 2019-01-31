#!/usr/bin/python3.5
import classPerso as perso

print("Hello World")

p = perso.Personne("Golo", "Bala", 55)

#print(p)
p.affichage()

p1 = perso.Personne("Nokhe", "Dinho", 23)
p2  = p.add(p1)
p2.affichage()
