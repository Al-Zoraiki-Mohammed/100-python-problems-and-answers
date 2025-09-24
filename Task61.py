"""Task61"""
import random 


def random_number(start, end):
    """Generate random number without using the built-in random module"""
    lake = set()
    for i in range(start, end):
        lake.add(str(i))
    return lake.pop()


def random_builtin(start, end):
    """Generate a random number using built in radom module"""
    return random.randint(start,end)
  
    
if __name__ =="__main__":
    start = int(input('Type a start of the range: '))
    end = int(input('Type end of the range: '))
    print(random_number(start,end))
    print(random_builtin(start,end))
