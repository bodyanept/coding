class Packet:
    
    def __init__(self,src,dst,data):
        self.src = src
        self.dst = dst
        self.data = data
        
class Computer:
    
    def __init__(self,name_comp,router_link):
        self.name_comp = name_comp
        self.router_link = router_link

    def send(self,dst,data):
        packet = Packet(self.name_comp,dst,data)
        self.router_link.route(packet)
    
    def receive(self,packet):
        print(packet.data)

class Router:
    
    def __init__(self):
        self.devices = {}
    
    def connect(self,device):
        self.devices[device.name_comp] = device

    
    def route(self,packet):
        if packet.dst in self.devices:
            self.devices[packet.dst].receive(packet)
            
router = Router()

pc1 = Computer('pc1',1)
pc2 = Computer('pc2',2)
pc3 = Computer('pc3',3)
pc4 = Computer('pc4',4)

router.connect(pc1)
router.connect(pc2)
router.connect(pc3)
router.connect(pc4)
