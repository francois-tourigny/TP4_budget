import os

os.system('git bisect reset')
os.system('git bisect start $badhash $goodhash')
os.system('git bisect run manage.py test')
os.system('git bisect system')
