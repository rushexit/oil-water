import pygame, OpenGL.GL

class obj():
	def __init__(self, fileName, swapYZ=False):
		self.vertices = []
		self.faces = []
		
		material = None
		for line in open(filename, "r"):