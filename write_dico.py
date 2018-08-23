#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import os


def simple_dico(fichier_letters, letters, length):

	i = j = k = l = 0
	password = []
	random_index = []

#######################################################################

	while i < length:
		r = random.randint(0,25)
		random_index.append(r)
		#print(random_index[i])
		i+=1

#######################################################################

	while j < len(letters):

		if j == random_index[k]:

#######################################################################

			if random_index[k] % 2 == 0:
				password.append(letters[j].upper())
				#print(password[k])

				fichier_letters.write(str(password[k]))

				j = -1
				k+=1

				if k == length:
					break

#######################################################################

			else :
				password.append(letters[j])
				#print(password[k])
	
				fichier_letters.write(str(password[k]))

				j = -1
				k+=1

				if k == length:
					break

		j+=1

#######################################################################ù

def alphanumerique_dico(fichier_alphanum, letters, length):

	i = j = k = l = 0
	password = []
	random_index = []
	number_index = []

#######################################################################

	while i < length:
		r = random.randint(0,25)
		random_index.append(r)
		#print(random_index[i])

		r = random.randint(0,9)
		number_index.append(r)
		#print(number_index[i])

		i+=1

#######################################################################

	while j < len(letters):

		if j == random_index[k]:

			if random_index[k] % 2 == 0:
				password.append(letters[j].upper())
				#print(password[k])

#######################################################################		

		if j == number_index[k]:
			if number_index[k] % 2 != 0:
				password.append(number_index[k])
				#print(password[k])

				fichier_alphanum.write(str(password[k]))

				j = -1
				k+=1

				if k == length:
					break

#######################################################################

			else :
				password.append(letters[j])
				#print(password[k])
	
				fichier_alphanum.write(str(password[k]))

				j = -1
				k+=1

				if k == length:
					break

		j+=1



def hexadecimal_dico(fichier_hexadecimal, hexadecimal, length):

	i = j = k = l = 0
	password = []
	hexa_index = []
	number_index = []

#######################################################################

	while i < length:
		r = random.randint(0,15)
		hexa_index.append(r)
		#print(hexa_index[i])

		i+=1

#######################################################################

	while j < len(hexadecimal):

		if j == hexa_index[k]:

			if hexa_index[k] % 2 == 0:
				password.append(hexadecimal[j])
				#print(password[k])	

				fichier_hexadecimal.write(str(password[k]))

				j = -1
				k+=1

				if k == length:
					break

#######################################################################

			else :
				password.append(hexadecimal[j])
				#print(password[k])
	
				fichier_hexadecimal.write(str(password[k]))

				j = -1
				k+=1

				if k == length:
					break

		j+=1


def supp_doublons(fichier_letters):

	ret = os.popen("uniq dico/dico_letters.txt")

	print('[+] Suppression ds doublons\n')

def supp_doublons(fichier_alphanum):

	ret = os.popen("uniq dico/dico_alphanumerique.txt")

	print('[+] Suppression ds doublons\n')

def supp_doublons(fichier_hexadecimal):

	ret = os.popen("uniq dico/dico_hexadecimal.txt")

	print('[+] Suppression ds doublons\n')