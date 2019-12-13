class AffineTransformation:
    def __init__(self, M, v):
        self.M = M
        self.v = v

    def transform(self, x):
        x_1 = x[0]
        x_2 = x[1]
        tr_x1 = x_1 * self.M[0][0] + x_2 * self.M[0][1] + self.v[0]
        tr_x2 = x_1 * self.M[1][0] + x_2 * self.M[1][1] + self.v[1]
        return tr_x1, tr_x2

    def __add__(self, right_afftr):
        M1 = [[right_afftr.M[0][0] * self.M[0][0] + right_afftr.M[1][0] * self.M[0][1],
               right_afftr.M[0][1] * self.M[0][0] + right_afftr.M[1][1] * self.M[0][1]],
              [right_afftr.M[0][0] * self.M[1][0] + right_afftr.M[1][0] * self.M[1][1],
               right_afftr.M[0][1] * self.M[1][0] + right_afftr.M[1][1] * self.M[1][1]]]
        v1 = [right_afftr.v[0] * self.M[0][0] + right_afftr.v[1] * self.M[0][1] + self.v[0],
              right_afftr.v[0] * self.M[1][0] + right_afftr.v[1] * self.M[1][1] + self.v[1]]
        return AffineTransformation(M1, v1)

if __name__ == '__main__':
    transformation_1 = AffineTransformation([[3, 1], [-1, 4]], [-12, 7])
    x1 = (33, 47)
    x2 = transformation_1.transform(x1)
    transformation_2 = AffineTransformation([[-2, -3], [1, 5]], [13, -5])
    x3 = transformation_2.transform(x2)
    transformation_3 = transformation_2 + transformation_1
    x4 = transformation_3.transform(x1)

    print(x1)
    print(x2)
    print(x3)
    print(x4)
