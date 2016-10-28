import pygame, sys, time, random
from pygame.locals import *

endingString = ''

odetteBody = {"leftArm" : "normalLeftArm", 
"leftFace" : "normalLeftFace", 
"leftLeg" : "normalLeftLeg", 
"leftHand" : "normalLeftHand", 
"rightArm" : "normalRightArm",
"rightFace" : "normalRightFace",
"rightLeg" : "normalRightLeg", 
"rightHand" : "normalRightHand", 
"torso" : "normalTorso", 
"gut" : "normalGut", 
"back" : "normalBack"}

pangBody = {"leftArm" : "normalLeftArm", 
"rightArm" : "normalRightArm", 
"back" : "normalBack", 
"leftLeg" : "normalLeftLeg", 
"rightLeg" : "normalRightLeg",
"face" : "normalFace"}