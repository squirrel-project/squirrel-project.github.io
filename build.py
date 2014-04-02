#!/usr/bin/env python
import sys, subprocess, os

with file( 'templates/header.tpl' ) as f:
    header=f.read()
with file( 'templates/footer.tpl' ) as f:
    footer=f.read()

def getHeader( classname ):
    return header.replace( 'BODYCLASSNAME', classname )

def notInstalled( program ):
    return not isInstalled( program )

def isInstalled( program ):
    cmd = 'type %s > /dev/null 2>&1' % program
    p = subprocess.Popen( cmd, shell=True )
    return p.wait() == 0

def warning( text ):
    # http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    print '%sWARNING: %s%s' % ( WARNING, text, ENDC )

def buildJs():
    if notInstalled( 'r.js' ):
        warning( 'r.js not installed. Not building javascript files' )
        return

    cmds = [ 'rm -rf build/*', 'r.js -o build.js' ]
    for cmd in cmds:
        p = subprocess.Popen( cmd.split( ' ' ))
        p.wait()

def buildScss():
    if notInstalled( 'scss' ):
        warning( 'scss not installed. Not building scss styles' )
        return
    cmd = 'scss style/style.scss:style/style.css'
    p = subprocess.Popen( cmd.split( ' ' ))
    p.wait()


def compactCss():
    if notInstalled( 'r.js' ):
        warning( 'r.js not installed. Not compressing/coying css files' )
        return
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
        'cd build; tar cvzf packed.tar.gz * >/dev/null; mv packed.tar.gz ..',
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
    if len( sys.argv ) <= 2 or sys.argv[ 1 ] != 'tpl':
        buildJs()
        buildScss()
        compactCss()
    buildPages()
    copyImages()
    pack()
