import os
w = "text_"
n = 0
fr = ".txt"
name = w + str(n) + fr
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), name)
os.remove(path)