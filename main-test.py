# Import the Add function, and assert that it works correctly.
from main import add

def TestAdd():
        assert add(2,3) == 5
        assert add(5,5) == 10
        print("Add Function works correctly")

if __name__ == '__main__':
        TestAdd()