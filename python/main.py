from typing import TypeVar, Protocol
from dataclasses import dataclass

T = TypeVar('T')
class Repeatable(Protocol):
    def repeat(self: T, repeat_count: int) -> T: ...

# Every type that (at least) implements `Repeatable`
RT = TypeVar('RT', bound=Repeatable)
def double(x: RT) -> RT:
    return x.repeat(2)

@dataclass
# "implicit" Repeatable 
class Person:
    def repeat(self, repeat_count: int):
        return Person(self.name * repeat_count, self.age * repeat_count)
    name: str
    age: int
    
p = Person("Jack", 30)

def main():
    print(double(p))

if __name__ == "__main__":
    main()