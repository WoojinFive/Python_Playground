def print_hello():
  print("hello")

def deco_print_hello(original):
  def wrapper():
    print("deco start")
    original()
    print("deco end")

  return wrapper

print_hello()

# deco_print_hello(print_hello()) # -> deco_print_hello("hello")

# deco_print_hello(print_hello)() # -> wrapper()


print("@@@decorator@@@")

def deco_func(original):
  def wrapper():
    print("start")
    original()
  return wrapper

@deco_func
def func1():
  print("func1")

@deco_func
def func2():
  print("func2")

@deco_func
def func3():
  print("func3")


func1()
func2()
func3()