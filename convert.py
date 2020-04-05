#!/usr/bin/env python3
#https://github.com/nabeel3133/file-converter-.obj-to-.ply
import os
import d3.model.tools as mt
import functools as fc
from d3.model.basemodel import Vector

def OBJ_to_PLY(objFile, plyFile):
	#fileToMake = plyFile[:len(plyFile)-4]
	#fileToMake = fileToMake+"WithRGB.ply"

	objFileOpened = open(objFile,"r")
	plyFileOpened = open(plyFile,"r")
	#fileToMake = open(fileToMake, "w")
	objFileData = []

	for line in objFileOpened:
		w = []
		w = line[:-1].split(' ')    #Splitting each line by space and putting in list

		if(len(w)==7):  #Checking if there are 7 elements in list
			#Removing the first 4 elements of list 
			w.remove(w[0])   
			w.remove(w[0])
			w.remove(w[0])
			w.remove(w[0])

			#Multiplying the remaining elements of list with 255 and converting to int
			w[0] = int(float(w[0])*255)
			w[1] = int(float(w[1])*255)
			w[2] = int(float(w[2])*255)

			objFileData.append(w)  #Appending list to objFile

		else:
			break

	objFileOpened.close()
	
	vertex_count = 0
	vertCounter = 0
	for line in plyFileOpened:
		vertCounter += 1
		if(vertCounter == 4):
			VertList = []
			VertList = line[:-1].split(' ')    #Splitting each line by space and putting in list
			vertex_count = int(VertList[2])
			break

	plyFileOpened.close()

def create_ply(objFile, plyFile):

	up_conversion = None
	
	result = mt.convert(objFile, plyFile, up_conversion)

	with open(plyFile, 'w') as f:
		f.write(result)

def convert(objFile, plyFile):
	create_ply(objFile,plyFile)
	OBJ_to_PLY(objFile,plyFile)
