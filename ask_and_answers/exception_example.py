class ExampleOnLection(Exception):
    pass


def some_useful_function():
    raise ExampleOnLection


if __name__ == "__main__":
    try:
        # my code
        some_useful_function()
    except ValueError:
        print("We catch value error")
    except ExampleOnLection:
        print("Yes look on me")
    except Exception:
        print("We catch some exception")
    else:
        print("No exceptions raised")

