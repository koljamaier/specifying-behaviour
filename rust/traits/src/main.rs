pub trait Repeatable {
    fn repeat(&self, repeat_count: usize) -> Vec<Self> where Self: Sized;
}

pub fn double<T: Repeatable>(x: &T) -> Vec<T> {
    x.repeat(2)
}

#[derive(Debug, Clone)]
struct Person {
    name: String,
    age: usize,
}

impl Repeatable for Person {
    fn repeat(&self, repeat_count: usize) -> Vec<Self> {
        vec![self.clone(); repeat_count]

    }
}

fn main() {
    let p = Person {
        name: String::from("Jane"),
        age: 30
    };

    let doubled = double(&p);
    
    println!("{:?}", double(&p));
}