class Switch(object):
    count=0
    def __init__(self,ports):
        self.portcount=ports
        self.macid='0'
        Switch.count+=1
    def __del__(self):
        Switch.count-=1
        print 'I am dying'
    def __len__(self):
        return self.portcount
    def __nonzero__(self):
        if len(self.macid)==48:
            return True
        else:
            return False
    def __add__(self,other):
        if type(other)==int:
            self.portcount+=other
            return Switch(self.portcount)
        else:
            portcount=(self.portcount+other.portcount)-2
            return Switch(portcount)

s6=Switch(48)
s5=Switch(12)
print len(s6)
print bool(s5)
s7=s6+s5 # create a network
s6=s6+20 # upgrade the switch
print len(s7)
print Switch.count




