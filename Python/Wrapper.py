def say(f):
    def wrapper():
        print("Test Output")
        f()
        print("Output Successfull")
    return wrapper
@say
def test():
    print("Test Output Successfull")

test()