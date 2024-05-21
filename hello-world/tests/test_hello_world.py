from hello_world import main

def test_function1():
    assert main() == "Hello World"

# or

def test_function2():
    r = main.my_first_function()
    assert r != "Pakistan"