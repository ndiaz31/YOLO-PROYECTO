import os
path = 'revolver'
files = os.listdir(path)
i = 0

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, '{:06}.jpg'.format(i)))
    i += 1
