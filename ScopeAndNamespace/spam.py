def spam1():

    def spam2():

        def spam3():
            z = " even"
            z += y  # using variable from outer scope (not changing them)
            print(f"In spam3, locals are {locals()}")
            return z

        y = " more " + x  # y must exist before spam3 is called
        y += spam3()  # do not combine these assignments
        print(f"In spam2, locals are {locals()}")
        return y

    x = "spam"  # + spam2(), error as x doesn't have a value so free variable referenced before assignment
    x += spam2()  # x must exist before spam2 is called, do not combine these assignments
    print(f"In spam1, locals are {locals()}")
    return x


print(spam1())
print(locals())
print(globals())  # both are identical, in module scope, local and global are same
