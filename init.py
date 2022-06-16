import os, time
import zipfile
import datetime

pathZip = 'C:\\Publicaciones\\publicar.zip'
pathFiles = ['C:\Publicaciones\Backoffice', 'C:\Publicaciones\Frontoffice']
pathComprimet = 'C:\\Publicaciones'
now = datetime.datetime.now()
now = now - datetime.timedelta(days=2)
formatDate = now.strftime('%Y-%m-%d %H:%M%S')
fantasy_zip = zipfile.ZipFile(pathZip, 'w')
 
def ArchivoZip(pathFiles):
    for folder, subfolders, files in os.walk(pathFiles): 
        for file in files:
            path = (os.path.join(folder,file))
            #print(path)
            modTimesinceEpoc = os.path.getmtime(path)
            modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
            date_file_obj = datetime.datetime.strptime(modificationTime, "%Y-%m-%d %H:%M:%S")
            
            if(date_file_obj > now):
                #print(path + ' Paso del archivo fecha modificacion: '+ modificationTime)
                print(path)
                #print('Pal zip: '+ modificationTime)
                fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), pathComprimet), compress_type = zipfile.ZIP_DEFLATED)
    
for path in pathFiles:
    ArchivoZip(path)
