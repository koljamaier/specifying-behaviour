pub trait Repeatable {
    fn repeat(&self, repeat_count: usize) -> Self;
}

pub fn double<T: Repeatable>(x: &T) -> T {
    x.repeat(2)
}

#[derive(Debug)]
struct Person {
    name: String,
    age: usize,
}

impl Repeatable for Person {
    fn repeat(&self, repeat_count: usize) -> Self {
        Self {
            name: self.name.repeat(repeat_count),
            age: self.age * repeat_count
        }
    }
}

fn main() {
    let p = Person {
        name: String::from("Jack"),
        age: 30
    };
    println!("{:?}", double(&p));
}