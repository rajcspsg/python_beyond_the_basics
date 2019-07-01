import gzip
import os
import sys

opener = gzip.open

if __name__ == "__main__":
    f = gzip.open(sys.argv[1], 'wt')
    f.write(' '.join(sys.argv[2:]))
    f.close()