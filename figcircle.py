import fig
class Circle(fig.Fig):
    def __init__(self, radius):
        self.name= "Circle"
        self.data= ["Radius: ", radius]
        #use PI from fig.py by informing python of namespace
        self.circumference = 2.*fig.PI*radius