import urllib.request as req
from pathlib import Path
import os
import patoolib
# .exe fixes
import patoolib.programs.rar
import patoolib.programs.p7zip
#
from shutil import rmtree
from logs import log


def installGD():

    if not Path(r'./Geometry.Dash/').exists():
        if not Path('GD2113.rar').exists():
            log('downloading GD2113.rar by url "https://download2389.mediafire.com/ifz4oeqrcpqg/6sptj6gxc37rx6t/Geometry.Dash.rar"')
            req.urlretrieve('https://download2389.mediafire.com/ifz4oeqrcpqg/6sptj6gxc37rx6t/Geometry.Dash.rar', r'./GD2113.rar')
            log('success download')

        log('creating /Geometry.Dash/ dir')

        patoolib.extract_archive('GD2113.rar', outdir='.')
    
        #removing not gd files
        rmtree(r'Geometry.Dash/_CommonRedist', ignore_errors=True)
        os.remove(r'Geometry.Dash/HOW TO RUN GAME!!.txt')
        os.remove(r'Geometry.Dash/STEAMUNLOCKED.COM.url')
        os.remove('GD2113.rar')

        log('GD 2.113 installed')
    else:
        log('dir /Geometry.Dash/ already created (warning)')

