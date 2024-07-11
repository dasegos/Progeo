from typing import Any

if __name__ == '__main__':
    from figure import Figure 
else:
    from app.figure import Figure


class SideDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = f'_{name}'

    def __get__(self, instance: 'Triangle', owner: type['Triangle']):
        return getattr(instance, self.private_name)
    
    def __set__(self, instance: 'Triangle', value: Any):
        if not isinstance(value, (int, float)):
            raise ValueError('Side value must be integer or float instance!')
        if value < 0:
            raise ValueError('Side value can not negative!')
        if value == 0:
            raise ValueError('Side value can not be zero!')

        sides = instance.__dict__
        sides[self.private_name] = value
        ready_sides = len(sides)
        if ready_sides == 3:
            if sides['_a'] + sides['_b'] <= sides['_c'] or sides['_b'] + sides['_c'] <= sides['_a'] or sides['_a'] + sides['_c'] <= sides['_b']:
                raise NonexistentTriangleException()
        setattr(instance, self.private_name, value)

class Triangle(Figure):
    a = SideDescriptor()
    b = SideDescriptor()
    c = SideDescriptor()

    def __init__(self, a: int | float, b: int | float, c: int | float) -> None:
        self.a = a
        self.b = b
        self.c = c

    @property
    def area(self) -> float:
        semiperimeter = self.perimeter / 2
        return (semiperimeter * (semiperimeter - self.a) * (semiperimeter - self.b) * (semiperimeter - self.c)) ** 0.5

    @property 
    def perimeter(self) -> int | float:
        return self.a + self.b + self.c
    

class NonexistentTriangleException(Exception):
    def __str__(self):
        return 'The Triangle object contradicts the Triangle inequality theorem!'
    
if __name__ == '__main__':
    triangle = Triangle(5, 2, 5)
    print(triangle.a)
    triangle.c = 6
    print(triangle.__dict__)
    print(triangle.area)
    print(triangle.perimeter)
    # triangle.c = 'd' -> Side value must be integer or float instance!
    # triangle.c = -6 -> ValueError: Side value can not negative!
    # triangle.c = 0 -> ValueError: Side value can not be zero!
    # triangle.c = 1 -> NonexistentTriangleException: The Triangle object contradicts the Triangle inequality theorem!
