import os, sys

lib_path = os.path.abspath('../classFolder')
print(lib_path)
sys.path.append(lib_path)

from classFile import ClassName
from echo import echo_x

A = ClassName("Hello", "World!")
A.display()
A.value1 = "Yo"
A.display()

echo_x('SubAlgo')