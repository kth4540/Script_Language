import shutil
import os
import datetime
import zipfile
myzip=zipfile.ZipFile('photo.zip','w')
for (root, subfolder, filenames) in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.jpg'):
            os.rename(os.path.join(root,filename),datetime.datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%Y%m%d')+filename)
            myzip.write(os.path.join(root,filename),compress_type=zipfile.ZIP_DEFLATED)
myzip.close()



