import sys, pygame, data.components.ow_main, OpenGL, data.states.startMenu, data.states.intro
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


data.states.intro.runIntro()
gm = data.states.startMenu.gameMenu(data.states.startMenu.startFunctions)
gm.run()
data.components.ow_main.scriptHandler("act_i_scene_i","test_script.txt")