if __name__ == '__main__':
    from figure import Figure 
else:
    from app.figure import Figure


class RadiusDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = f'_{name}'

    def __get__(self, instance: 'Circle', owner: type['Circle']):
        return getattr(instance, self.private_name)

    def __set__(self, instance, radius) -> None:
        if not isinstance(radius, (int, float)):
            raise ValueError('Radius value must be integer or float instance!')
        if radius < 0:
            raise ValueError('Radius value can not negative!')
        setattr(instance, self.private_name, radius)

class Circle(Figure):
    PI = 3.14

    radius = RadiusDescriptor()

    def __init__(self, radius: int | float) -> None:
        self.radius = radius

    @property
    def area(self) -> int | float:
        return Circle.PI * self.radius ** 2
    
    @property
    def perimeter(self) -> int | float:
        return Circle.PI * self.radius * 2
    
if __name__ == '__main__':
    circle = Circle(3)
    print(circle.radius)
    print(circle.area)
    circle.radius = 4
    print(circle.radius)
    print(circle.area)
    # circle.radius = -8 -> ValueError: Radius can not negative!
    # circle.radius = '7' -> ValueError: Radius must be integer or float instance!