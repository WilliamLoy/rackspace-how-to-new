import os
count = 0


for (dirname, dirs, files) in os.walk('.'):
   for filename in files:
       if filename.endswith('.md') :
           count = count + 1
print ('Files:'), count
