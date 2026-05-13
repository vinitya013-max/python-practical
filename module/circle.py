class Circle:
    def area(self, radius):
        area = 3.14 * radius * radius
        print("Circle Area =", area)

a = int(input("Enter radius: "))

c = Circle()
c.area(a)