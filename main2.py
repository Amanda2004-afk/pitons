import os
if os.path.exists('aste.txt'):
    os.remove('aste.txt')
else:
    print('fails neekiste')
os.rmdir('bildes')