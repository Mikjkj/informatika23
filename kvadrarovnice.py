a = 1
b = 2
c = -3


d = (b ** 2 - (4 * a * c)) ** 0.5
if d == 0:
    print("1:", -b / (2 * a))
elif d > 0:
    print("1: ", (-b + d) / (2 * a),
          "2: ", (-b - d) / (2 * a))
else:
    print("Oops")
