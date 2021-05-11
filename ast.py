import argparse


class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

class mult(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()

class divide(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()

class Boolean():
    parser = argparse.ArgumentParser()
    parser.add_argument('--my_variable', default=False, action='store_true')
    parser.add_argument('--other_variable', default=True, action='store_false')
    args = parser.parse_args()
    print(args)

class Access():
    parser = argparse.ArgumentParser()
    parser.add_argument('--my_variable', default=False, action='store_true')
    parser.add_argument('--other_variable', default=True, action='store_false')
    args = parser.parse_args()
    print(args)

class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())