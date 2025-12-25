import geometry

print("1.area_circle")
print("2.area_rectangle")

choice = int(input("Enter your choice:"))
if(choice==1):
        radius = float(input("Enter radius of the circle:"))
        print(f"Area of circle={geometry.area_circle(radius)}")
else: 
    length=float(input("Enter length of the rectangle: "))
    breadth=float(input("Enter breadth of the rectangle: "))
    print(f"Area of rectangle={geometry.area_rectangle(length,breadth)}")