#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Developed By: Sanduuz
# Instagram: @sanduuz
# E-mail: 19jdmz5js@protonmail.com

import zipfile, optparse, time, sys, platform

# ### Experimental [Check README.md]
# if platform.system() != "Linux":
#    exit("ZPC is currently only available for Linux systems!")

class Linux:
    class colors:
        blue = "\033[94m"
        red = "\033[91m"
        green = "\033[92m"
        bold = "\033[1m"
        underl = "\033[4m"
        reset = "\033[0m"
        default = "\033[39m"
        magenta = "\033[95m"
        white = "\033[97m"

    def extractFile(self, zFile, password):
        try:
            zFile.extractall(pwd=password)
            return password
        except:
            if verbosity == True:
                if dynamicLineUpdate == True:
                    sys.stdout.write(linuxZPC.colors.blue+'\r[*] Trying Password Number'+linuxZPC.colors.magenta+' '+str(passNum)+' '+linuxZPC.colors.blue+'Out Of'+linuxZPC.colors.magenta+' '+str(listLength)+' '+linuxZPC.colors.blue+'Possibilities | Trying Password:'+linuxZPC.colors.magenta+' '+str(password)+linuxZPC.colors.default+'										')
                    sys.stdout.flush()
                else:
                    print linuxZPC.colors.blue+'[*] Trying Password Number'+linuxZPC.colors.magenta+' '+str(passNum)+' '+linuxZPC.colors.blue+'Out Of'+linuxZPC.colors.magenta+' '+str(listLength)+' '+linuxZPC.colors.blue+'Possibilities | Trying Password:'+linuxZPC.colors.magenta+' '+str(password)+''+linuxZPC.colors.default
            elif verbosity == False and dynamicLineUpdate == True:
                exit(linuxZPC.colors.bold+linuxZPC.colors.red+'[!] '+linuxZPC.colors.underl+'Dynamic line updates can\'t be True if verbosity is False'+linuxZPC.colors.reset+linuxZPC.colors.red+'!'+linuxZPC.colors.default)

    def main(self):
        global passNum
        passNum = 0

        startTime = time.time()

        parser = optparse.OptionParser("Usage: "+ "python ZPC.py -f <ZipFile> -w <Wordlist> | See -h/--help for more info.")
        parser.add_option('-f', dest='zname', type='string', help="Specify ZipFile")
        parser.add_option('-w', dest='dname', type='string', help="Specify Wordlist")
        parser.add_option('--dv', dest='verbose', default=True, action="store_false", help="Disable Verbosity")
        parser.add_option('--dl', dest='DynamicLine', default=False, action="store_true", help="Enable Dynamic line updates.")

        (options, args) = parser.parse_args()

        if (options.zname == None) | (options.dname == None):
            print parser.usage
            exit()
        else:
            zname = options.zname
            dname = options.dname
            global verbosity
            verbosity = options.verbose
            global dynamicLineUpdate
            dynamicLineUpdate = options.DynamicLine

        zFile = zipfile.ZipFile(zname)
        with open(dname, 'r') as passFile:
            getListLength(dname)
            for line in passFile.readlines():
                password = line.strip('\n')
                passNum += 1
                guess = linuxZPC.extractFile(zFile, password)
                if guess:
                    print linuxZPC.colors.bold+linuxZPC.colors.green+'\n[+] '+linuxZPC.colors.underl+'Password Found'+linuxZPC.colors.reset+linuxZPC.colors.bold+linuxZPC.colors.green+': '+linuxZPC.colors.white+password+linuxZPC.colors.green+' | Password Number '+linuxZPC.colors.white+str(passNum)+linuxZPC.colors.green+' Out Of '+linuxZPC.colors.white+str(listLength)+linuxZPC.colors.green+' Possibilities.\n'
                    print linuxZPC.colors.white+"Time Elapsed: "+str(time.time()-startTime)
                    exit(0)
                elif passNum >= listLength:
                    print linuxZPC.colors.bold+linuxZPC.colors.red+'\n[!] '+linuxZPC.colors.underl+'No Correct Password Found'+linuxZPC.colors.reset+linuxZPC.colors.red+'!'+linuxZPC.colors.default
                    print linuxZPC.colors.white+"\nTime Elapsed: "+str(time.time()-startTime)

class Windows:
    def extractFile(self, zFile, password):
        try:
            zFile.extractall(pwd=password)
            return password
        except:
            if verbosity == True:
                if dynamicLineUpdate == True:
                    sys.stdout.write('\r[*] Trying Password Number '+str(passNum)+' Out Of '+str(listLength)+' Possibilities | Trying Password: '+str(password)+'						')
                    sys.stdout.flush()
                else:
                    print '[*] Trying Password Number '+str(passNum)+' Out Of '+str(listLength)+' Possibilities | Trying Password: '+str(password)
            elif verbosity == False and dynamicLineUpdate == True:
                exit('[!] Dynamic line updates can\'t be True if verbosity is False!')

    def main(self):
        global passNum
        passNum = 0

        startTime = time.time()

        parser = optparse.OptionParser("Usage: "+ "python ZPC.py -f <ZipFile> -w <Wordlist> | See -h/--help for more info.")
        parser.add_option('-f', dest='zname', type='string', help="Specify Zip file")
        parser.add_option('-w', dest='dname', type='string', help="Specify Wordlist")
        parser.add_option('--dv', dest='verbose', default=True, action="store_false", help="Disable Verbosity")
        parser.add_option('--dl', dest='DynamicLine', default=False, action="store_true", help="Enable Dynamic line updates.")

        (options, args) = parser.parse_args()

        if (options.zname == None) | (options.dname == None):
            print parser.usage
            exit()
        else:
            zname = options.zname
            dname = options.dname
            global verbosity
            verbosity = options.verbose
            global dynamicLineUpdate
            dynamicLineUpdate = options.DynamicLine

        zFile = zipfile.ZipFile(zname)
        with open(dname, 'r') as passFile:
            getListLength(dname)
            for line in passFile.readlines():
                password = line.strip('\n')
                passNum += 1
                guess = windowsZPC.extractFile(zFile, password)
                if guess:
                    print '\n[+] Password Found: '+password+' | Password Number '+str(passNum)+' Out Of '+str(listLength)+' Possibilities.\n'
                    print "Time Elapsed: "+str(time.time()-startTime)
                    exit(0)
                elif passNum >= listLength:
                    print '\n[!] No Correct Password Found!'
                    print "\nTime Elapsed: "+str(time.time()-startTime)

def getListLength(dname):
    global listLength
    with open(dname, 'r') as listLength:
        listLength = len(listLength.readlines())

linuxZPC = Linux()
windowsZPC = Windows()

if __name__ == '__main__':
    if platform.system() == "Linux":
        linuxZPC.main()
    elif platform.system() == "Windows":
        windowsZPC.main()
    else:
        print "[!] Unsupported OS!"
