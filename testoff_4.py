
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def set_coord(self,a,b):
        self.x=a
        self.y=b
        
    def get_coord(self):
        return self.x,self.y 

    def get_distance(self, p):
        if isinstance(p, Point):
            return ((p.x - self.x) ** 2 + (p.y - self.y) ** 2) ** 0.5



