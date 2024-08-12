import os, pathlib


class makeDir(object):
    def __init__(self, dir = None):
        if dir is None:
            dir = os.getcwd()
        self.dir = dir
    
    def make(self,name_dir='test'):
        path=os.path.join(self.dir,name_dir)
        pathlib.Path(path).mkdir(parents=True,exist_ok=True)
        return path
    
        

        