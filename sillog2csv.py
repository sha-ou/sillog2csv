#!/usr/bin/python3

###################################################################
#    File name     : sillog2csv.py
#    Author        : sha-ou
#    Date          : 2019年03月28日 星期四 11时08分32秒
#    Description   : 
###################################################################

import re
import sys

def log2csv(inf, outf=None):
    if outf is None:
        outf = str(inf).split('.')[0] + '.csv'
    content = ''
    pattern = re.compile(r'^d\s+(-?\d\.\d+?e[+-]\d+?\s+?)+')
    
    infd = open(inf, 'r')
    for line in infd.readlines():
        matched_title = re.match('^f\s+?\d+?\s+?(\"\w+?\"\s+?)+', line)
        if matched_title:
            titles = matched_title.group().split()
            content = content + \
                    titles[2].replace('"','')+' voltage,' + titles[2].replace('"','')+' current,' +\
                    titles[3].replace('"','')+' voltage,' + titles[3].replace('"','')+' current,' +\
                    titles[4].replace('"','')+' voltage,' + titles[4].replace('"','')+' current,\n'

        matched = re.match(pattern, line)
        if matched:
            datas = matched.group().split()
            content = content + \
                    datas[1] + ',' + datas[3] + ',' +\
                    datas[4] + ',' + datas[6] + ',' +\
                    datas[7] + ',' + datas[9] + ',\n'
    infd.close()

    outfd = open(outf, 'w')
    outfd.write(content)
    outfd.close()
    print('Save to %s...' % outf)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: [python3] sillog2csv.py xxx.log [xxx.log ...]')
    else:
        for item in sys.argv[1:]:
            log2csv(item)
