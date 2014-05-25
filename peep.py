from os import walk
from os.path import getctime, getsize
from argparse import ArgumentParser

parser = ArgumentParser(description='Get file information.')
parser.add_argument('-d', '--directory', default='/')
args = parser.parse_args()

count = 0
for path, dirnames, fnames in walk(args.directory):
    for fname in fnames:
        fpath = path + "/" + fname
        try:
            print "Name:", fpath, "CTime:", getctime(fpath), " Size:", getsize(fpath)
        except OSError:
            print "error:", fpath
        count = count + 1

print "File count:", count
