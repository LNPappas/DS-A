class Node(object):

    def __init__(self,data=None,nex=None):
        self.data = data
        self.nex = nex

    
    def get_data(self):
        return self.data


    def get_nex(self):
        return self.nex


    def set_nex(self,new):
        self.nex = new
        