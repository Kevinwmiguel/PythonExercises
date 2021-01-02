from pathlib import Path

def existarq(c):
    fileName = r"C:\Usuários\kevin\Documentos\python\dados.txt"
    fileObj = Path(fileName)
    fileObj.is_file()
    if fileObj != '':
        return True
    else:
        return False