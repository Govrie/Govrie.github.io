class Polynom:
    def __init__(self, *args):
        self.coefficients = []
        for arg in args:
            self.coefficients.append(arg)

    def __len__(self):
        return len(self.coefficients)

    def __repr__(self):
        _len = len(self.coefficients)
        result = " + ".join(["{}x^{}".format(x, _len-i-1) for i, x in enumerate(self.coefficients)])
        return result.replace("x^0", "")

    def __add__(self, right_polynom):
        coef_left = self.coefficients[::-1].copy()
        coef_right = right_polynom.coefficients[::-1].copy()

        coef_result = None
        if len(coef_left) > len(coef_right):
            coef_result = coef_left
        else:
            coef_result = coef_right

        for i, (a, b) in enumerate(zip(coef_left, coef_right)):
            coef_result[i] = a+b
        coef_result = coef_result[::-1]
        return Polynom(*coef_result)

    def _negative(self):
        return Polynom(*[-x for x in self.coefficients])

    def __sub__(self, right_polynom):
        return self.__add__(right_polynom._negative())

    def __mul__(self, right_polynom):
        coef_left = self.coefficients[::-1].copy()
        coef_right = right_polynom.coefficients[::-1].copy()
        coef_result = [0]*(len(coef_right)+len(coef_left)-1)

        for i, a in enumerate(coef_left):
            for j, b in enumerate(coef_right):
                coef_result[i+j] += a*b
        coef_result = coef_result[::-1]
        return Polynom(*coef_result)

if __name__ == '__main__':
    x = Polynom(1, 2, 3)
    y = Polynom(2, 4, 6, 5)
    print(x)
    print(y)
    print(x+y)
    print(x-y)
    print(x*y)
