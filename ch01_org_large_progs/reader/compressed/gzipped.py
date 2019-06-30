import gzip
import os
import os

opener = gzip.open

if __name__ == "__main__":
    f = opener(sys.argsv[1], 'wt')
    f.write(' '.join(sys.argsv[2:]))
    f.close()