import os,sys
folder = 'C:/Users/pohsa/Desktop/test folder/images'
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace(filename,filename[:3] + '.jpeg')
       output = os.rename(infilename, newname)
       if WindowsError:
           results = []
           results += [each for each in os.listdir(folder) if each.endswith('.bmp')] 
           os.remove(results[0])
