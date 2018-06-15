object exercise {
  def factorial(x: Int) : Int =
    if (x==1) 1
    else x * factorial(x-1)

  factorial(10)

  def factorial2(x: Int): Int = {
    def loop(a: Int, b: Int, acc: Int) : Int =
      if (a > b) acc
      else loop(a+1, b, a*acc)

    loop(1, x, 1)
  }

  factorial2(10)
}