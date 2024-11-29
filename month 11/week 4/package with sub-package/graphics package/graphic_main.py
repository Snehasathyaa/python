from Graphic_package.Graphics import circle
from Graphic_package.Graphics import rectangle
from Graphic_package._3D_Graphics import cuboid
from Graphic_package._3D_Graphics import sphere


print("Circle")
print("\nCircle(radius=7) area : ",circle.area_circle(7))
print("\nCircle(radius=7) perimeter : ",circle.peri_circle(7))

print("\n\nRectangle")
print("\nRectangle(length=5,width=3) area : ",rectangle.rectangle_area(5,3))
print("\nRectangle(length=5,width=3) perimeter : ",rectangle.peri_rectangle(5,3))

print("\n\nCuboid")
print("\nCuboid area (length=5,width=4,height=8): ",cuboid.cuboid_area(5,4,8))
print("\nCuboid perimeter (length=5,width=4,height=8): ",cuboid.peri_cuboid(5,4,8))

print("\n\nsphere")
print("\nsphere area (radius=6): ",sphere.sphere_area(6))
print("\nsphere perimeter (radius=6): ",sphere.peri_sphere(6))

