import os

os.system('good_commit=200~e4cfc6f77ebbe2e23550ddab682316ab4ce1c0')
os.system('bad_commit=c1a4be04b972b6c17db242fc37752ad517c29402')
os.system('git bisect reset')
os.system('git bisect start $bad_commit $good_commit')
os.system('git bisect run manage.py test')
os.system('git bisect reset')
