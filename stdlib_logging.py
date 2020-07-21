import os
import platform
import logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),
                                'test.log')

print("Logging to", logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")

#Output:

#$ python stdlib_logging.py
#Logging to /Users/swa/test.log

#$ cat /Users/swa/test.log
#2014-03-29 09:27:36,660 : DEBUG : Start of the program
#2014-03-29 09:27:36,660 : INFO : Doing something
#2014-03-29 09:27:36,660 : WARNING : Dying now
#The cat command is used in the command line to read the 'test.log' file.
#If the cat command is not available, you can open the test.log file in a text editor instead.
