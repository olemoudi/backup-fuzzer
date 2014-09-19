#!/usr/bin/pyhon

import time
from itertools import product
import argparse

'''
wp-config.php generates

wp-config.php.1
wp-config.php.bak
wp-config.php.20140909
wp-config.php_08082014
.wp-config.php
.wp-config.php.swp
wp-config.txt
'''

preffixes = set(['', '.', '_', '~'])
date_seps = set(['', '.', '-', '_'])
extensions = set(['', '.swp', '.tmp', '~', '.zip', '.tar.gz', '.tgz', '.tar.bz2', '.rar', '.7z', '.bak', '.0', '.1', '.2', '.old'])


if __name__ ==  '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-nd', '--no-dates', help='Disable YYYYMMDD and YYYYDDMM dates as file suffixes (default False)', default=False, action='store_true')
    parser.add_argument('-bd', '--basic-dates', help='Use basic dates variation only', default=False, action='store_true')
    parser.add_argument('-cs', '--case-sensitive', help='Enable case sensitiveness (default False)', default=False, action='store_true')
    parser.add_argument('-y', '--years', help='Past years to include in dates (default 1)', default=1, type=int)
    parser.add_argument('word') 
    args = parser.parse_args()

    original = args.word.strip()
    splitted = original.split('.')
    if len(splitted) > 1:
        original_name = '.'.join(splitted[:-1])
        original_ext = '.' + splitted[-1]
    else:
        original_name = splitted[0]
        original_ext = ''

    dates = set([''])
    if not args.no_dates:
        current = time.localtime()
        for d in product(range(current.tm_year-args.years, current.tm_year), [str(i).zfill(2) for i in range(1,13)], [str(i).zfill(2) for i in range(1,31)]):
            dates.add('%s%s%s' % d)
            if not args.basic_dates:
                dates.add('%s%s%s' % (d[0],d[2],d[1]))
                dates.add('%s%s' % (d[2],d[1]))
                dates.add('%s%s' % (d[1],d[2]))
                dates.add('%s%s%s' % tuple(reversed(d)))
                dates.add('%s%s%s' % tuple(reversed((d[0],d[2],d[1]))))
        for d in product([str(i).zfill(2) for i in range(1,current.tm_mon+1)], [str(i).zfill(2) for i in range(1,31)]):
            dates.add('%s%s%s' % (current.tm_year, d[0], d[1]))
            if not args.basic_dates:
                dates.add('%s%s%s' % (current.tm_year, d[1], d[0]))
                dates.add('%s%s' % (d[0], d[1]))
                dates.add('%s%s' % (d[1], d[0]))
                dates.add('%s%s%s' % tuple(reversed((current.tm_year, d[0], d[1]))))
                dates.add('%s%s%s' % tuple(reversed((current.tm_year, d[1], d[0]))))

    filenames = set([original_name])
    if args.case_sensitive:
        filenames.add(original_name.upper())
        filenames.add(original_name.lower())
        filenames.add(original_name[0].upper() + original_name[1:])

    duplicates = set()
    for result in product(preffixes, filenames, ('', original_ext), date_seps, dates, extensions):
        if result[4] == '':
            string = '%s%s%s%s%s' % tuple([result[i] for i in [0,1,2,4,5]])
        else:
            string = '%s%s%s%s%s%s' % result

        if string not in duplicates:
            print string
            duplicates.add(string)




