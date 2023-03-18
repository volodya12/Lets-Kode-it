# https://docs.python.org/3/library/exceptions.html

def exceptionError():
    try:
        a = 10
        b = "this is string"
        c = 0
        d = (a + b) / c
        print(d)
    #except:        # can be none
        #print("Error")
    except ZeroDivisionError:
        print("Zero")
    except TypeError:
        print("Error has a Typo")  # prints first cuz encounters that error first
        raise Exception("This is RAISED exception, Do Not Ignore")
    finally:
        print("this Finally block, always executes")

exceptionError()