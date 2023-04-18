from typing import TypeVar, Protocol, List
from dataclasses import dataclass

T = TypeVar('T')
class Repeatable(Protocol):
    def repeat(self: T, repeat_count: int) -> List[T]: ...

# Every type that (at least) implements `Repeatable`
RT = TypeVar('RT', bound=Repeatable)
def double(x: RT) -> List[RT]:
    return x.repeat(2)

# "implicit" Repeatable 
@dataclass
class Person:
    def repeat(self, repeat_count: int):
        return [self] * repeat_count
    name: str
    age: int
    
p = Person("Jane", 30)

def main():
    print(double(p))

if __name__ == "__main__":
    main()

