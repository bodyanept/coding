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
        if str(packet.dst) in self.devices:
            self.devices[str(packet.dst)].receive(packet)
            
router = Router()

pc1 = Computer('1',router)
pc2 = Computer('2',router)
pc3 = Computer('3',router)
pc4 = Computer('4',router)

router.connect(pc1)
router.connect(pc2)
router.connect(pc3)
router.connect(pc4)

pc1.send(3, 'Привет от PC1!')
pc1.send(1, 'Ответ от PC3!')
pc1.send(4, 'PC2 здесь')
pc1.send(2, 'Принято')
