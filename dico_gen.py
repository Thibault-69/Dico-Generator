#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import sys
#import os

from write_dico import *


letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
hexadecimal = 'ABCDEF0123456789'

key_done = 0

#######################################################################

print('\n')
	
dico_type = input('[+] Quel type de dictionnaire voulez vous créer ?\n\n\t- simple (lettres minuscules & majuscules)\n\t- alphanum. (lettres minus & majs + chiffres)\n\t- hexa. (hexadécimale)\n\n[+] Votre choix : ')

if dico_type != 'simple' and dico_type != 'alphanum' and dico_type != 'hexa':

	sys.exit('Tête de con !')

nombre = int(input('[+] Combien de clés voulez vous créer : '))

length = int(input('[+] Définnissez ici le nombre de caractères des mots du dictionnaire : '))

i = 0

#######################################################################

if dico_type == 'simple':

	fichier_letters = open('dico/dico_letters.txt', 'w')

	while key_done < nombre:

		simple_dico(fichier_letters, letters, length)
		key_done += 1
		fichier_letters.write('\n')

	supp_doublons(fichier_letters)

	fichier_letters.close()


#######################################################################

if dico_type == 'alphanum':

	fichier_alphanum = open('dico/dico_alphanumerique.txt', 'w')

	while key_done < nombre:
		
		alphanumerique_dico(fichier_alphanum, letters, length)
		key_done += 1
		fichier_alphanum.write('\n')

	supp_doublons(fichier_alphanum)

	fichier_alphanum.close()

#######################################################################

if dico_type == 'hexa':

	fichier_hexadecimal = open('dico/dico_hexadecimal.txt', 'w')

	while key_done < nombre:
		
		hexadecimal_dico(fichier_hexadecimal, hexadecimal, length)
		key_done += 1
		fichier_hexadecimal.write('\n')

	supp_doublons(fichier_hexadecimal)

	fichier_hexadecimal.close()

#######################################################################