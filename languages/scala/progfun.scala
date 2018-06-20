//Created by Jin

object exercise1 {
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

object exercise2 {
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

object runnable {
  def horizontal_line = println("-" * 30)
  def main(args: Array[String]) {
    horizontal_line
    println("fractorial1(10) = " + exercise1.factorial1(10))
    println("fractorial2(10) = " + exercise1.factorial2(10))
    println

    horizontal_line
    println("abs(-3) = " + exercise2.abs(-3))
    println("sqrt(2) = " + exercise2.sqrt(2))
    println("sqrt(4) = " + exercise2.sqrt(4))
    println("sqrt(1e-6) = " + exercise2.sqrt(1e-6))
    println("sqrt(1e60) = " + exercise2.sqrt(1e60))
  }
}
