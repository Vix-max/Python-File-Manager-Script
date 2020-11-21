import os
import glob
import shutil
from os import path
filename=glob.glob("C:/Users/User/Downloads/*")
documents=['.pdf','.docx','.doc','.txt']
videos=['.mp4','.MOV','.WMV','.WebM']
pictures=['.jpeg','.jpg','.svg','.png','.PNG','.gif']
audios=['.mp3','.WAV']
setupFiles=['.exe','.msi']
pythonfiles=['.py']
compressedFiles=['.zip','.rar','.gz','.tgz']
files=['.apk']
camtsiapak=['.campackage']
camtasialocation='C:/Users/User/Downloads/Camtasia pak'
videoslocation='C:/Users/User/Downloads/Videos'
audiolocation='C:/Users/User/Downloads/Audios'
DocumentsLocation='C:/Users/User/Downloads/Documents'
picturesLocation='C:/Users/User/Downloads/Pictures'
setupFilesLocation='C:/Users/User/Downloads/Setup Files'
compressedFilesLocation='C:/Users/User/Downloads/Compressed Files'
pythonfilelocation='C:/Users/User/Downloads/Python programms'
FilesLocation='C:/Users/User/Downloads/Files'
for file in filename:
    if os.path.splitext(file)[1] in documents:
        if(path.exists(DocumentsLocation)):
            shutil.move(file,DocumentsLocation)
        else:
            os.mkdir(picturesLocation)
            shutil.move(file,picturesLocation)
    if os.path.splitext(file)[1] in pictures:
        if(path.exists(picturesLocation)):
            shutil.move(file,picturesLocation)
        else:
            os.mkdir(videoslocation)
            shutil.move(file,videoslocation)
    if os.path.splitext(file)[1] in videos:
        if(path.exists(videoslocation)):
            shutil.move(file,videoslocation)
        else:
            os.mkdir(setupFilesLocation)
            shutil.move(file,setupFilesLocation)
    if os.path.splitext(file)[1] in setupFiles:
        if(path.exists(setupFilesLocation)):
            shutil.move(file,setupFilesLocation)
        else:
            os.mkdir(audiolocation)
            shutil.move(file,audiolocation)
    if os.path.splitext(file)[1] in audios:
        if(path.exists(audiolocation)):
            shutil.move(file,audiolocation)
        else:
            os.mkdir(compressedFilesLocation)
            shutil.move(file,compressedFilesLocation)
    if os.path.splitext(file)[1] in compressedFiles:
        if(path.exists(compressedFilesLocation)):
            shutil.move(file,compressedFilesLocation)
        else:
            os.mkdir(camtasialocation)
            shutil.move(file,camtasialocation)
    if os.path.splitext(file)[1] in camtsiapak:
        if(path.exists(camtasialocation)):
            shutil.move(file,camtasialocation)    
        else:
            os.mkdir(pythonfilelocation)
            shutil.move(file,pythonfilelocation)
    if os.path.splitext(file)[1] in pythonfiles:
        if(path.exists(pythonfilelocation)):
            shutil.move(file,pythonfilelocation)     