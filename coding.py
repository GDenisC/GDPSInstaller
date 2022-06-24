
from pathlib import Path
from base64 import urlsafe_b64encode
from shutil import copytree, rmtree
from logs import log
from fileinput import FileInput


def encode(db: str) -> bytes:
    return urlsafe_b64encode(('http://'+db).encode('utf-8'))

gdpath = r'./Geometry.Dash/Geometry Dash/'
gdpspath = r'./GD/'
robtop = 'www.boomlings.com/database'

def checkURL(url) -> bool:
    return len(url) == len(robtop) # bool

def CreateGDPS(url: str) -> bool:
    log('creating gdps')

    if not Path(gdpath+'GeometryDash.exe').exists():
        log('! GeometryDash.exe FILE NOT FOUND (ERROR)')
        return False
    
    if Path(gdpspath).exists():
        rmtree(gdpspath)

    log('coping default GD to GDPS dir')
    copytree(gdpath, gdpspath)

    log('replacing links')

    data = b''
    
    with FileInput(gdpspath+'GeometryDash.exe', inplace=True, mode='rb') as f:
        for line in f:
            line = line.replace(robtop.encode('utf-8'), url.encode('utf-8'))
            line = line.replace(encode(robtop),         encode(url)        )
            with open('test.txt', 'ab') as fw:
                fw.write(line)
            data += line

        log('replacing base64 links')
    
    with open(gdpspath+'GeometryDash.exe', 'wb') as f:
        f.write(data)
    
    log('SUCCESS GDPS CREATING')

    return True
