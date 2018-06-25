//Created by Jin

object runnable {
  def main(args: Array[String]) {
    printTitle("week1")
    printEq("fractorial1(10)", week1.factorial1(10))
    printEq("fractorial2(10)", week1.factorial2(10))
    horizontal_line()
    printEq("abs(-3)", week1.abs(-3))
    printEq("sqrt(2)", week1.sqrt(2))
    printEq("sqrt(4)", week1.sqrt(4))
    printEq("sqrt(1e-6)", week1.sqrt(1e-6))
    printEq("sqrt(1e60)", week1.sqrt(1e60))

    printTitle("week2")
    printEq("sum(id, 1, 10)", week2.sum(week2.id, 1, 10))
    printEq("sum(sq, 1, 10)", week2.sum(week2.sq, 1, 10))
    printEq("sum((x=> 3*x), 3, 5)", week2.sum((x=> 3*x), 3, 5))
    horizontal_line()
    printEq("product(id, 1, 5)", week2.product(week2.id, 1, 5))
    printEq("fact(10) with currying", week2.fact(10))
    horizontal_line()
    val aOne = new week2.Rational(1)
    val aThird = new week2.Rational(1, 3)
    val aHalf = new week2.Rational(1, 2)
    val aSixth = new week2.Rational(1, 6)
    printEq("new Rational(1)", aOne)
    printEq("aHalf + aHalf", (aHalf + aHalf))
    printEq("aHalf - aHalf", (aHalf - aHalf))
    printEq("aHalf + aThird", (aHalf + aThird))
    printEq("aThird - aHalf", (aThird - aHalf))
    printEq("aOne - aSixth", (aOne - aSixth))
    printEq("aHalf / aHalf", (aHalf / aHalf))
    printEq("aHalf * aHalf", (aHalf * aHalf))
    printEq("aHalf < aOne", (aHalf < aOne))
    printEq("aHalf max aOne", (aHalf max aOne))
    printEq("aSixth max aHalf", (aSixth max aHalf))
    printEq("aHalf max aSixth", (aHalf max aSixth))
    printEq("-aHalf", -aHalf)
    printEq("1 + aHalf", (1 + aHalf) + " (implicit conversion)")
    horizontal_line()
    println("todo week2/find_fixed_points")

    printTitle("week3")
    val nil = new week3.JNil[Int]
    val ls = new week3.JCons(1, new week3.JCons(2, nil))
    println("val ls = new JCons(1, new JCons(2, new JNil[Int]))")
    printEq("ls.head", ls.head)
    printEq("ls.tail.head", ls.tail.head)
    printEq("nth(0, ls)", week3.nth(0, ls))
    printEq("nth(1, ls)", week3.nth(1, ls))
    printError("nth(11, ls)", week3.nth(11, ls))

    horizontal_line()
    println("IntSet is binary search tree for int")
    val tree1 = new week3.NonEmpty(3, new week3.NonEmpty(2), new week3.NonEmpty(5))
    val tree2 = new week3.NonEmpty(4, new week3.NonEmpty(1), new week3.NonEmpty(8))
    println("val tree1 = new NonEmpty(3, new NonEmpty(2), new NonEmpty(5))")
    println("val tree2 = new NonEmpty(4, new NonEmpty(1), new NonEmpty(8))")
    printTo("tree1", tree1)
    printTo("tree1", tree2)
    printTo("tree1 union tree2", (tree1 union tree2))

    printTitle("week4")
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

    horizontal_line()
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

    horizontal_line()
    printEq("JList()", week4.JList())
    printEq("JList(1,2)", week4.JList(1,2))

    horizontal_line()
    println("Nat class")
    val zero = week4.Zero
    val one = zero.successor
    val two = one.successor
    val three = two.successor
    val four = three.successor
    val five = four.successor
    printAssert("zero == zero", zero == zero)
    printAssert("zero == zero.successor.predecessor", zero == zero.successor.predecessor)
    printAssert("three + one == four", three + one == four)
    printAssert("three - two == one", three - two == one)
    printError("three - four", three - four, paren=true)
    
    println("")
  }

  def horizontal_line(len: Int = 50) = println("-" * len)
  def printTitle(title: String) = {
    val dashes = "-" * (50 - 2 - title.length)
    val (left, right) = dashes.splitAt(dashes.length/2) 
    println("")
    horizontal_line()
    println(s"$left $title $right")
    horizontal_line()
  }
  def printEq(left:String, right:Any, paren:Boolean=false) = printAbstract(left, "=", right, paren)
  def printIs(left:String, right:Any, paren:Boolean=false) = printAbstract(left, "is", right, paren)
  def printTo(left:String, right:Any, paren:Boolean=false) = printAbstract(left, "=>", right, paren)
  def printAbstract(left:String, sep:String, right:Any, paren:Boolean=false) = 
    if (paren) println(s"($left) $sep $right")
    else println(s"$left $sep $right")
  def printError(exprInStr: String, expr: => Any, paren:Boolean=false) {
    try { expr }
    catch {
      case t : Throwable =>
        if (paren) println(s"($exprInStr) throws $t")
        else println(s"$exprInStr throws $t")
    }
  }
  def printAssert(exprInStr: String, expr: => Boolean) {
    assert(expr)
    println(s"assert ( $exprInStr )")
  }
}

object week1 {
  def factorial1(x: Int) : Int =
    if (x==1) 1
    else x * factorial1(x-1)

  def factorial2(x: Int): Int = {
    def loop(a: Int, b: Int, acc: Int) : Int =
      if (a > b) acc
      else loop(a+1, b, a*acc)
    loop(1, x, 1)
  }

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

object week2 {
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

  // currying
  def mapReduce(f: Int=>Int, combine: (Int, Int) => Int, zero: Int)(a: Int, b:Int): Int =
    if (a > b) zero
    else combine(f(a), mapReduce(f, combine, zero)(a+1, b))
  def product(f: Int=>Int, a: Int, b: Int): Int =
    mapReduce(f, (_ * _), 1)(a, b)
  def fact(n: Int): Int = product(id, 1, n)

  // rational class designing
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

  //todo find_fixed_points
}

object week3 {
  trait JList[T] {
    def head: T
    def tail: JList[T]
    def isEmpty: Boolean
    override def toString = "jinsung"
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

object week4 {
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

  // Custom List
  trait JList[T] {
    def head: T
    def tail: JList[T]
    def isEmpty: Boolean
  }
  class JNil[T] extends JList[T] {
    def head: Nothing = throw new NoSuchElementException("JNil.head")
    def tail: Nothing = throw new NoSuchElementException("JNil.tail")
    def isEmpty: Boolean = true
    override def toString = "Nil"
  }
  class JCons[T](val head: T, val tail: JList[T]) extends JList[T] {
    def isEmpty: Boolean = false
    override def toString = head.toString + " -> " + tail.toString
  }
  object JList {
    // todo: only () and (1,2) is appliable. make it variable
    def apply[T](x1: T, x2: T): JList[T] = new JCons(x1, new JCons(x2, new JNil))
    def apply[T]() = new JNil
  }

  // Nat class
  abstract class Nat {
    def isZero: Boolean
    def predecessor: Nat
    // Now, every Nat instances including `object Zero` are singletons.
    lazy val successor: Nat = new Succ(this)
    def +(that: Nat): Nat
    def -(that: Nat): Nat
  }
  object Zero extends Nat {
    override def isZero: Boolean = true
    override def predecessor: Nat = throw new Error("0.predecessor")
    override def +(that: Nat): Nat = that
    override def -(that: Nat): Nat = if (that isZero) this else throw new Error("negative num")
  }
  class Succ (val predecessor: Nat) extends Nat {
    override def isZero: Boolean = false
    override def +(that: Nat): Nat = (this predecessor) + (that successor)
    override def -(that: Nat): Nat = if (that isZero) this else this.predecessor - that.predecessor
  }  
}
