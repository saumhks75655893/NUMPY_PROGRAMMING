import timeit

m = []
def test():
    """Stupid test function"""
    L = [i**4 for i in range(100)]
    m.append(L)
test()
print(m)
if __name__ == '__main__':
    print(timeit.timeit("test()", setup="from __main__ import test"))
    
    

    

