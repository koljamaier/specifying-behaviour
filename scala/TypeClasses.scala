//> using scala "3.nightly"

trait Repeatable[T]:
  def repeat(x: T, repeatCount: Int): List[T]

  extension (x: T)(using r: Repeatable[T])
    def repeat(repeatCount: Int): List[T] =  
      r.repeat(x, repeatCount)

def double[T: Repeatable](x: T) =
  x.repeat(2)

case class Person(name: String, age: Int)

given Repeatable[Person] with
  override def repeat(x: Person, repeatCount: Int): List[Person] = 
    List.fill(repeatCount)(x)

@main def main = 
    val p = Person("Jane", 30)
    println(double(p))
