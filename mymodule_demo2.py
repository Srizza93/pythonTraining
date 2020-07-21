#Same output as mymodule_demo.py
#NOTE: IT'S BETTER USE import AS mymodule_demo.py
from mymodule import say_hi, __version__


say_hi()
print('Version', __version__)

#Explanation why it's better simple then complex or explicit then implicit
print("\n")
import this
