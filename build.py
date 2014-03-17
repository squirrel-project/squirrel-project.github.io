#!/usr/bin/env python
import sys, subprocess, os

with file( 'templates/header.tpl' ) as f:
    header=f.read()
with file( 'templates/footer.tpl' ) as f:
    footer=f.read()

def getHeader( classname ):
    return header.replace( 'BODYCLASSNAME', classname )

def buildJs():
    cmds = [ 'rm -rf build/*', 'r.js -o build.js' ]
    for cmd in cmds:
        p = subprocess.Popen( cmd.split( ' ' ))
        p.wait()

def buildCss():
    cmd = 'r.js -o cssIn=style/style.css out=build/style.css'
    p = subprocess.Popen( cmd.split( ' ' ))
    p.wait()

def buildPages():
    files = [ f[:-5] for f in os.listdir( 'pages' ) if f[ -5: ] == '.html' ]
    for file in files:
        buildPage( file )

def buildPage( filename ):
    with file( 'build/%s.html' % filename, 'w' ) as out:
        with file( 'pages/%s.html' % filename, 'r' ) as tpl:
            out.write( getHeader( filename ))
            out.write( tpl.read() )
            out.write( footer )



def pack():
    cmds = [
        'rm packed.tar.gz',
        'cd build; tar cvzf packed.tar.gz *; mv packed.tar.gz ..',
        'tar -tvf packed.tar.gz'
    ]
    for cmd in cmds:
        p = subprocess.Popen( cmd, shell=True )
        p.wait()

def copyImages():
    cmds = [
        'rm -rf build/images',
        'cp -r images/ build/images'
    ]
    for cmd in cmds:
        p = subprocess.Popen( cmd, shell=True )
        p.wait()

if __name__ == '__main__':
    if len( sys.argv ) >= 2 and sys.argv[ 1 ] == 'all':
        buildJs()
        buildCss()
    buildPages()
    copyImages()
    pack()
