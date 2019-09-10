def function_test(arg1=0, arg2=1, *param):
    print(type(param))
    print(arg1, arg2, param)


if __name__ == '__main__':
    function_test(1, 2, "asd", 2)
