from reader.compressed import bzipped
from reader.compressed import gzipped
import os

extension_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener,
}

class Reader:
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        opener = extension_map.get(extension, open) # just like map.getOrDefault in java
        self.filename = filename
        self.f = opener(filename, 'rt')
        
    def close(self):
        self.f.close()
        
    def read(self):
       return self.f.read()