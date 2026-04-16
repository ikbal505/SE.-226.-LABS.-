

import geometry_utils

print("Available shapes: circle, rectangle, triangle")
print("Available calculations: _area, _perimeter (e.g., circle_area)")

operation=input("Enter the operation you want to perform: ")

match operation:
    case "circle_area":
        radius= float(input("Enter the radius of the circle"))
        result= geometry_utils.circle_area(radius)
    case "circle_perimeter":
          radius = float(input("enter the radius of the circle"))
          result=geometry_utils.circle_perimeter(radius)

    case "rectangle_area":
          height=float(input("Enter the height of rectangle"))
          width = float(input("Enter the width of rectangle"))
          result=geometry_utils.rectangle_area(height, width)
    case "triangle_area":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        result = geometry_utils.triangle_area(base, height)
    case _:
        result = None
        print("input error: Unknown operation.")

if result is None:
    print("Input Error: Dimensions must be strictly positive.")
else:
    print(f"\nResult: {result}")








