#!/ccnc_bin/venv/bin/python

import re
import os
import argparse
import sys
import textwrap

def nameChange(directoryLocation):
    directoryList = os.listdir(directoryLocation)

    # pattern compile
    t1 = re.compile(r'tfl|[^s]t1|^t1|208',re.IGNORECASE)
    dti = re.compile(r'dti\S*\(.\)_\d+\S*|^dti64D_65$',re.IGNORECASE)
    dti_AP = re.compile(r'dti_[0-9]*D_.*AP.*',re.IGNORECASE)
    dti_PA = re.compile(r'dti_[0-9]*D_.*PA.*',re.IGNORECASE)
    dtiFA = re.compile(r'dti.*[^l]fa',re.IGNORECASE)
    dtiEXP = re.compile(r'dti.*exp',re.IGNORECASE)
    dtiCOLFA = re.compile(r'dti.*colfa',re.IGNORECASE)
    dki = re.compile(r'dki\S*\(.\)_\d+\S*|^DKI30D_151$|^DKI_151$|^DKI_30D_151$',re.IGNORECASE)
    dkiFA = re.compile(r'dki.*[^l]fa',re.IGNORECASE)
    dkiEXP = re.compile(r'dki.*exp',re.IGNORECASE)
    dkiCOLFA = re.compile(r'dki.*colfa',re.IGNORECASE)
    rest = re.compile(r'rest|rest\S*4060',re.IGNORECASE)
    t2flair = re.compile(r'flair',re.IGNORECASE)
    t2tse = re.compile(r'tse',re.IGNORECASE)
    epi = re.compile(r'epi',re.IGNORECASE)


    foundDict={}

    modality = [(t1,'T1'),(rest,'REST'),(dki,"DKI"),(dti,'DTI'),
                (dti_AP, 'DTI_AP'), (dti_PA, 'DTI_PA'),
                (t2flair,'T2FLAIR'),(t2tse,'T2TSE'),
                (dtiFA,'DTI_FA'),(dtiEXP,'DTI_EXP'),(dtiCOLFA,'DTI_COLFA'),
                (dkiFA,'DKI_FA'),(dkiEXP,'DKI_EXP'),(dkiCOLFA,'DKI_COLFA')]

    for directory in directoryList:
        matchingStandard = [x[1] for x in modality if x[0].search(directory)]
        if matchingStandard != []: 
            if len(matchingStandard) < 2:
                #print directory, ''.join(matchingStandard)
                foundDict[directory] = ''.join(matchingStandard)
            else:
                print directory, matchingStandard
                sys.exit('Confusing directory names. Please change them manually')

    
    #test
    print "Location : directoryLocation"
    print "============================"
    for source,target in foundDict.iteritems():

        print "\tmv '{0}' {1}".format(os.path.basename(source),
                                      target)

    ##confirm
    if raw_input('Execute the name change ? [y/n] : ') == 'y':
        for source,target in foundDict.iteritems():

            print source, os.path.join(directoryLocation,target)
            os.system("mv '{0}' {1}".format(
                            os.path.join(directoryLocation,source),
                            os.path.join(directoryLocation,target)))
            print "mv '{0}' {1}".format(
                            os.path.join(directoryLocation,source),
                            os.path.join(directoryLocation,target))



if __name__=='__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
            description = textwrap.dedent('''\
                    {codeName}
                    ====================
                        eg) {codeName} 
                        eg) {codeName} -dir /Users/kevin/NOR04_CKI
                    '''.format(codeName=os.path.basename(__file__))))


            #epilog="By Kevin, 26th May 2014")
    parser.add_argument('-dir',help='run name change')
    args = parser.parse_args()


    #if both options are on
    if args.dir:
        nameChange(directoryLocation = args.dir)
    else:
        nameChange(directoryLocation = os.getcwd())
