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
    val aOne = new Rational(1)
    val aThird = new Rational(1, 3)
    val aHalf = new Rational(1, 2)
    val aSixth = new Rational(1, 6)
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

object exer6 {
  //todo week2/find_fixed_points
}

