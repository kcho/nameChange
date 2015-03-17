#!/ccnc_bin/venv/bin/python

import re
import os
import argparse
import sys
import textwrap

def nameChange(directoryLocation):
    directoryList = os.listdir(directoryLocation)

    #pattern compile
    t1 = re.compile(r'tfl|[^s]t1|^t1|208',re.IGNORECASE)

    dti = re.compile(r'dti\S*\(.\)_\d+\S*|^dti64D_65$',re.IGNORECASE)
    dti_AP = re.compile(r'dti_72D_.*AP',re.IGNORECASE)
    dti_PA = re.compile(r'dti_72D_.*PA',re.IGNORECASE)
    dtiFA = re.compile(r'dti.*[^l]fa',re.IGNORECASE)
    dtiEXP = re.compile(r'dti.*exp',re.IGNORECASE)
    dtiCOLFA = re.compile(r'dti.*colfa',re.IGNORECASE)

    dki = re.compile(r'dki\S*\(.\)_\d+\S*|^DKI30D_151$',re.IGNORECASE)
    dkiFA = re.compile(r'dki.*[^l]fa',re.IGNORECASE)
    dkiEXP = re.compile(r'dki.*exp',re.IGNORECASE)
    dkiCOLFA = re.compile(r'dki.*colfa',re.IGNORECASE)

    rest = re.compile(r'rest|rest\S*4060',re.IGNORECASE)

    t2flair = re.compile(r'flair',re.IGNORECASE)
    t2tse = re.compile(r'tse',re.IGNORECASE)

    epi = re.compile(r'epi',re.IGNORECASE)

    foundDict={}

    #Search for modality in (t1,'T1'),(rest,'REST'),(dki,"DKI"),(dti,'DTI'),(t2flair,'T2FLAIR'),(t2tse,'T2TSE'),(dtiFA,'DTI_FA'),(dtiEXP,'DTI_EXP'),(dtiCOLFA,'DTI_COLFA'),(dkiFA,'DKI_FA'),(dkiEXP,'DKI_EXP'),(dkiCOLFA,'DKI_COLFA'):
        #print modality[0].search(' '.join(directoryLocation)).group()
        foundDict[os.path.join(directoryLocation,modality[1])] = ''.join([os.path.join(directoryLocation,x) for x in directoryList if modality[0].search(x)])


    #test
    print "Location : directoryLocation"
    print "============================"
    for target,source in foundDict.iteritems():

        print "\tmv '{0}' {1}".format(os.path.basename(source),
                os.path.basename(target))

    #confirm
    if raw_input('Execute the name change ? [Y/N] : ') == 'Y':
        for target,source in foundDict.iteritems():
            os.system("mv '{0}' {1}".format(source,target))



#if __name__=='__main__':
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
        description = textwrap.dedent('''\
                {codeName}
                ====================
                    eg) {codeName} --here
                    eg) {codeName} --dir /Users/kevin/NOR04_CKI
                '''.format(codeName=os.path.basename(__file__))))


        #epilog="By Kevin, 26th May 2014")
parser.add_argument('--here',action='store_true',help='run name change')
parser.add_argument('--dir',help='run name change')
args = parser.parse_args()


#if both options are on
if args.dir and args.here:
    sys.exit('Please choose one option')
else:
    if args.here:
        nameChange(directoryLocation = os.getcwd())
    if args.dir:
        nameChange(directoryLocation = args.dir)
