import gc

class Demo:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(self.name, "object destroyed")


print("Garbage collection enabled:", gc.isenabled())


obj1 = Demo("Object 1")
obj2 = Demo("Object 2")

obj2.ref = obj1


del obj1
del obj2

print("Garbage collection started")


collected = gc.collect()

print("Garbage collected objects:", collected)


print("Garbage collection counts:", gc.get_count())


gc.disable()
print("Garbage collection enabled:", gc.isenabled())


gc.enable()
print("Garbage collection enabled:", gc.isenabled())