//> using scala "3.nightly"

trait Repeatable[T]:
  def repeat(x: T, repeatCount: Int): T

  extension (x: T)(using r: Repeatable[T])
    def repeat(repeatCount: Int): T =  
      r.repeat(x, repeatCount)

def double[T: Repeatable](x: T) =
  x.repeat(2)

case class Person(name: String, age: Int)

given Repeatable[Person] with
  override def repeat(x: Person, repeatCount: Int): Person = 
    Person(x.name * repeatCount, x.age * repeatCount)

@main def main = 
    val p = Person("Jack", 30)
    println(double(p))
