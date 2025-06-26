class Motherboard:
    def __init__(self, typesize, socket, socket_CP):
        self.typesize = typesize
        self.socket = socket
        self.socket_CP = socket_CP
    
    def data_transfer(self,sender, receiver, data):
        if receiver == 'ram':
            ram.save(data)
        elif receiver == 'storage':
            storage.save(data)
        elif receiver == 'cpu':
            cpu.save(data)
        elif receiver == 'gpu':
            gpu.save(data)
            
    
    
mb = Motherboard()
class RAM:
    def __init__(self, socket, speed, manyfactory, cache):
        self.socket = socket
        self.speed = speed
        self.manyfactory = manyfactory
        self.cache = cache
    
    def read(self):
        pass
    
    def rec(self):
        pass
        
class CP:
    def __init__(self, core, speed, GP, size):
        self.core = core
        self.speed = speed
        self.GP = GP
        self.manyfactory = size
        
    def calc(self):
        pass
        
class GP:
    def __init__(self, core, speed, energy, GP, memory, price):
        self.core = core
        self.speed = speed
        self.energy = energy
        self.GP = GP
        self.memory = memory
        self.price = price
        
        
    def calc(self):
        pass
        
        
class SSD:
    def __init__(self, volume, socket):
        self.volume = volume
        self.speed = speed
        self.socket = socket
        
        
    def calc(self):
        pass
    
    
    
