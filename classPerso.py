#!/usr/bin/python3.5

class Personne:
	def __init__(self, *args, **kwargs):
		self.nom = args[0]
		self.prenom = args[1]
		self.age = args[2]

	def __repr__(self):
		print("Nom: {}, Premom: {} et Age: {}".format(self.nom, self.prenom, self.age))

	def affichage(self):
		print("Nom: {}, Premom: {} et Age: {}".format(self.nom, self.prenom, self.age))

	#def add(self, p):
		#tmp = []
		#perso = Personne()
		#for el in self.items():
			#tmp.append(el)
		#for el in p:
		#	tmp.append(el)
		#return tmp
