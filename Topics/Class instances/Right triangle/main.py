class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here


    def t_area(self):
        return round((self.a * self.b) / 2, 1)

# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
if (input_a ** 2) + (input_b ** 2) == (input_c ** 2):
    tri_info = RightTriangle(input_c, input_a, input_b)
    print(tri_info.t_area())
else:
    print('Not right')
