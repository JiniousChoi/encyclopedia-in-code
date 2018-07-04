import week4._

class Animal {
  def show(name: String) = println(name)
}

class Dog extends Animal
class Person extends Animal
class Man extends Person
class Woman extends Person

val a = new Animal()
val d = new Dog()
val p = new Person()
val m = new Man()
val w = new Woman()

def fnTest(f:Person => Person): Unit = print("")

//되는게 맞는거 같은데...
fnTest(p => p)
fnTest(p => m)
fnTest(a => p)
fnTest(a => w)

//여긴 왜 되는거지...?
fnTest(a => a)
fnTest(m => p)
fnTest(m => m)


// Invariant List

def invariantFn2(ls: InvariantList2[Int]): Unit = print()
invariantFn2(new InvariantNil2[Int])
//invariantFn2(new InvariantNil2[Nothing]) //Compile Error


// Covariant List
def covariantFn(ls: CovariantList3[Int]): Unit = print()
val covariantNil = CovariantNil3
val covariantLs1: CovariantCons3[Int] = new CovariantCons3(3, covariantNil)
val covariantLs2: CovariantCons3[AnyVal] = new CovariantCons3(false, covariantLs1)
covariantFn(covariantNil)
covariantFn(covariantLs1)
//covariantFn(covariantLs2)
