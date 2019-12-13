class FIFO:
    def __init__(self, *args):
        self.queue = []
        for arg in args:
            self.queue.append(arg)

    def __repr__(self):
        return str(self.queue)

    def isEmpty(self):
        if not self.queue:
            return True
        else:
            return False

    def push(self, object):
        return self.queue.append(object)

    def pop(self):
        return self.queue.pop(0)

if __name__ == '__main__':
    x = FIFO()
    print(x.isEmpty())
    x.push('wake up')
    x.push('wash')
    x.push('eat')
    print(x)
    print(x.isEmpty())
    print(x.pop())
    print(x)
    print(x.isEmpty())
    print(x.pop())
    print(x)
    print(x.isEmpty())
    print(x.pop())
    print(x.isEmpty())
