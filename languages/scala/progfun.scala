//Created by Jin

object runnable {
  def main(args: Array[String]) {
    horizontal_line
    println("fractorial1(10) = " + exer1.factorial1(10))
    println("fractorial2(10) = " + exer1.factorial2(10))

    horizontal_line
    println("abs(-3) = " + exer2.abs(-3))
    println("sqrt(2) = " + exer2.sqrt(2))
    println("sqrt(4) = " + exer2.sqrt(4))
    println("sqrt(1e-6) = " + exer2.sqrt(1e-6))
    println("sqrt(1e60) = " + exer2.sqrt(1e60))

    horizontal_line
    println("sum(id, 1, 10) = " + exer3.sum(exer3.id, 1, 10))
    println("sum(sq, 1, 10) = " + exer3.sum(exer3.sq, 1, 10))
    println("sum((x=> 3*x), 3, 5) = " + exer3.sum((x=> 3*x), 3, 5))

    horizontal_line
    println("product(id, 1, 5) = " + exer4.product(exer4.id, 1, 5))
    println("fact(10) with currying = " + exer4.fact(10))

    horizontal_line
    val aOne = new exer5.Rational(1)
    val aThird = new exer5.Rational(1, 3)
    val aHalf = new exer5.Rational(1, 2)
    val aSixth = new exer5.Rational(1, 6)
    println("new Rational(1) = " + aOne)
    println("aHalf + aHalf = " + (aHalf + aHalf))
    println("aHalf - aHalf = " + (aHalf - aHalf))
    println("aHalf + aThird = " + (aHalf + aThird))
    println("aThird - aHalf = " + (aThird - aHalf))
    println("aOne - aSixth = " + (aOne - aSixth))
    println("aHalf / aHalf = " + (aHalf / aHalf))
    println("aHalf * aHalf = " + (aHalf * aHalf))
    println("aHalf < aOne = " + (aHalf < aOne))
    println("aHalf max aOne = " + (aHalf max aOne))
    println("aSixth max aHalf = " + (aSixth max aHalf))
    println("aHalf max aSixth = " + (aHalf max aSixth))
    println("-aHalf = " + -aHalf)

    horizontal_line
    println("1 + aHalf = " + (1 + aHalf) + " (implicit conversion)")

    horizontal_line
    println("todo week2/find_fixed_points")

    horizontal_line
    val nil = new exer7.JNil[Int]
    val ls = new exer7.JCons(1, new exer7.JCons(2, nil))
    println("val ls = new JCons(1, new JCons(2, new JNil[Int]))")
    println("ls.head = " + ls.head)
    println("ls.tail.head = " + ls.tail.head)
    println("nth(0, ls) = " + exer7.nth(0, ls))
    println("nth(1, ls) = " + exer7.nth(1, ls))
    try {
      exer7.nth(11, ls)
    } catch {
      case e : Exception => println("nth(11, ls) => " + e)
    }

    horizontal_line
    println("IntSet is binary search tree for int")
    val tree1 = new exer8.NonEmpty(3, new exer8.NonEmpty(2), new exer8.NonEmpty(5))
    val tree2 = new exer8.NonEmpty(4, new exer8.NonEmpty(1), new exer8.NonEmpty(8))
    println("val tree1 = new NonEmpty(3, new NonEmpty(2), new NonEmpty(5))")
    println("val tree2 = new NonEmpty(4, new NonEmpty(1), new NonEmpty(8))")
    println("tree1 => " + tree1)
    println("tree1 => " + tree2)
    println("tree1 union tree2 => " + (tree1 union tree2))

    horizontal_line
    println("""assert (MTrue === MTrue)
              ^assert (MFalse === MFalse)
              ^assert (MTrue !== MFalse)
              ^assert (!MTrue === MFalse)
              ^assert (!MFalse === MTrue)
              ^assert ((MTrue == MTrue) === MTrue)
              ^assert ((MTrue == MFalse) === MFalse)
              ^assert ((MFalse == MTrue) === MFalse)
              ^assert ((MFalse == MFalse) === MTrue)
              ^assert ((MTrue != MTrue) === MFalse)
              ^assert ((MTrue != MFalse) === MTrue)
              ^assert ((MFalse != MTrue) === MTrue)
              ^assert ((MFalse != MFalse) === MFalse)
              ^assert ((MTrue && MTrue) === MTrue)
              ^assert ((MTrue && MFalse) === MFalse)
              ^assert ((MFalse && MTrue) === MFalse)
              ^assert ((MFalse && MFalse) === MFalse)
              ^assert ((MTrue || MTrue) === MTrue)
              ^assert ((MTrue || MFalse) === MTrue)
              ^assert ((MFalse || MTrue) === MTrue)
              ^assert ((MFalse || MFalse) === MFalse)
              ^assert ((MTrue < MTrue) === MFalse)
              ^assert ((MTrue < MFalse) === MFalse)
              ^assert ((MFalse < MTrue) === MTrue)
              ^assert ((MFalse < MFalse) === MFalse)""".stripMargin('^'))

    horizontal_line
    println("""assert (JTrue === JTrue)
              ^assert (JFalse === JFalse)
              ^assert (JTrue !== JFalse)
              ^assert (!JTrue === JFalse)
              ^assert (!JFalse === JTrue)
              ^assert ((JTrue == JTrue) === JTrue)
              ^assert ((JTrue == JFalse) === JFalse)
              ^assert ((JFalse == JTrue) === JFalse)
              ^assert ((JFalse == JFalse) === JTrue)
              ^assert ((JTrue != JTrue) === JFalse)
              ^assert ((JTrue != JFalse) === JTrue)
              ^assert ((JFalse != JTrue) === JTrue)
              ^assert ((JFalse != JFalse) === JFalse)
              ^assert ((JTrue && JTrue) === JTrue)
              ^assert ((JTrue && JFalse) === JFalse)
              ^assert ((JFalse && JTrue) === JFalse)
              ^assert ((JFalse && JFalse) === JFalse)
              ^assert ((JTrue || JTrue) === JTrue)
              ^assert ((JTrue || JFalse) === JTrue)
              ^assert ((JFalse || JTrue) === JTrue)
              ^assert ((JFalse || JFalse) === JFalse)
              ^assert ((JTrue < JTrue) === JFalse)
              ^assert ((JTrue < JFalse) === JFalse)
              ^assert ((JFalse < JTrue) === JTrue)
              ^assert ((JFalse < JFalse) === JFalse)""".stripMargin('^'))

    println("")
  }

  def horizontal_line = println("-" * 30)
}

object exer1 {
  def factorial1(x: Int) : Int =
    if (x==1) 1
    else x * factorial1(x-1)

  def factorial2(x: Int): Int = {
    def loop(a: Int, b: Int, acc: Int) : Int =
      if (a > b) acc
      else loop(a+1, b, a*acc)
    loop(1, x, 1)
  }
}

object exer2 {
  def abs(x:Double) : Double = if (x<0) -x else x

  def sqrt(x: Double) : Double = {
    def sqrtIter(guess: Double): Double =
      if (isGoodEnough(guess)) guess
      else sqrtIter(improve(guess))
    def isGoodEnough(guess: Double) =
      abs(guess * guess - x) / x < 0.001
    def improve(guess: Double): Double =
      (guess + x / guess) / 2
    sqrtIter(1.0)
  }
}

object exer3 {
  // higher order functions
  def id(x: Int): Int = x
  def sq(x: Int): Int = x*x
  def sum(f: Int => Int, a: Int, b: Int): Int = {
    def loop(a: Int, acc: Int): Int = {
      if (a > b) acc
      else loop(a+1, acc + f(a))
    }

    loop(a, 0)
  }
}

object exer4 {
  // currying
  def id(a: Int): Int = a
  def mapReduce(f: Int=>Int, combine: (Int, Int) => Int, zero: Int)(a: Int, b:Int): Int =
    if (a > b) zero
    else combine(f(a), mapReduce(f, combine, zero)(a+1, b))
  def product(f: Int=>Int, a: Int, b: Int): Int =
    mapReduce(f, (_ * _), 1)(a, b)
  def fact(n: Int): Int = product(id, 1, n)
}

object exer5 {
  implicit def int2rational(i:Int) = new Rational(i)
  class Rational(x: Int, y: Int) {
    require(y != 0, "denominator should be non-zero!")
    val g = gcd(x, y).abs
    val numer = x / g
    val denom = y / g

    def this(a: Int) = this(a, 1)
    def + (other: Rational): Rational =
      new Rational(
        numer * other.denom + denom * other.numer,
        denom * other.denom)
    def - (other: Rational): Rational =
      new Rational(
        numer * other.denom - denom * other.numer,
        denom * other.denom)
    def * (other: Rational): Rational =
      new Rational(numer * other.numer, denom * other.denom)
    def / (other: Rational): Rational =
      new Rational(numer * other.denom, denom * other.numer)
    def unary_- = new Rational(-numer, denom)
    def < (other:Rational) =
      numer * other.denom < other.numer * denom
    def max (other: Rational) =
      if (this < other) other else this
    override def toString(): String =
      if (denom == 1) numer + "" else numer + "/" + denom
    def gcd(a: Int, b: Int): Int = if (b==0) a else gcd(b, a%b)
  }
}

object exer6 {
  //todo week2/find_fixed_points
}

object exer7 {
  trait JList[T] {
    def head: T
    def tail: JList[T]
    def isEmpty: Boolean
  }

  class JNil[T] extends JList[T] {
    def head: Nothing = throw new NoSuchElementException("JNil.head")
    def tail: Nothing = throw new NoSuchElementException("JNil.tail")
    def isEmpty: Boolean = true
  }

  class JCons[T](val head: T, val tail: JList[T]) extends JList[T] {
    def isEmpty: Boolean = false
  }

  def nth[T](n: Int, xs: JList[T]): T = {
    if (xs.isEmpty) throw new IndexOutOfBoundsException
    if (n==0) xs.head
    else nth(n-1, xs.tail)
  }
}

object exer8 {
  // binary search tree for int
  abstract class IntSet {
    def contains(x: Int): Boolean
    def incl(x: Int): IntSet
    def union(other: IntSet): IntSet
  }

  object Empty extends IntSet {
    override def contains(x: Int): Boolean = false
    override def incl(x: Int): IntSet =
      new NonEmpty(x, Empty, Empty)
    override def union(other: IntSet): IntSet = other
    override def toString(): String = ""
  }

  class NonEmpty(elem: Int, left: IntSet = Empty, right: IntSet = Empty) extends IntSet {
    override def contains(x: Int): Boolean =
      if (elem == x) true
      else if (x < elem) left contains x
      else right contains x
    override def incl(x: Int): IntSet =
      if (elem == x) this
      else if (x < elem) new NonEmpty(elem, left incl x, right)
      else new NonEmpty(elem, left, right incl x)
    override def union(other: IntSet): IntSet =
      //elegant yet inefficient implementation
      ((left union right) union other) incl elem
    override def toString(): String =
      "{" + left + " , " + elem + " , " + right + "}"
  }
}

// week4
object exer9 {
  // This is how an OOP(Polymorphism, to be specific) would eliminate if-else parts
  abstract class MBoolean {
    // Below is the original one by Martin Odersky.
    // Why does he use generic type here? non-generic seems alright.
    // def ifThenElse[T] (t: => T, e: => T): T
    def ifThenElse(t: => MBoolean, e: => MBoolean): MBoolean
    def && (x: MBoolean): MBoolean = ifThenElse(x, MFalse)
    def || (x: MBoolean): MBoolean = ifThenElse(MTrue, x)
    def unary_! : MBoolean = ifThenElse(MFalse, MTrue)
    def == (x: MBoolean): MBoolean = ifThenElse(x, !x)
    def != (x: MBoolean): MBoolean = !(this == x)
    def < (x: MBoolean): MBoolean = ifThenElse(MFalse, x)
  }
  object MTrue extends MBoolean {
    override def ifThenElse(t: => MBoolean, e: => MBoolean): MBoolean = t
    //override def ifThenElse[T](t: => T, e: => T): T = t
  }
  object MFalse extends MBoolean {
    override def ifThenElse(t: => MBoolean, e: => MBoolean): MBoolean = e
    //override def ifThenElse[T](t: => T, e: => T): T = e
  }

  // My version of Boolean Implementation
  trait JBoolean {
    def && (that: JBoolean): JBoolean
    def || (that: JBoolean): JBoolean
    def unary_! : JBoolean
    // def == (x: MBoolean): MBoolean = ifThenElse(MTrue, !x) // Impossible to implement without ifThenElse method
    // def != (x: MBoolean): MBoolean = !(this == x) // However, JTrue and JFalse are singleton object, hence ==, != works anyways
    def < (that: JBoolean): JBoolean
  }
  object JTrue extends JBoolean {
    override def unary_! : JBoolean = JFalse
    override def &&(that: JBoolean): JBoolean = that
    override def ||(that: JBoolean): JBoolean = this
    override def <(that: JBoolean): JBoolean = JFalse
  }
  object JFalse extends JBoolean {
    override def unary_! : JBoolean = JTrue
    override def &&(that: JBoolean): JBoolean = this
    override def ||(that: JBoolean): JBoolean = that
    override def <(that: JBoolean): JBoolean = that
  }
}
