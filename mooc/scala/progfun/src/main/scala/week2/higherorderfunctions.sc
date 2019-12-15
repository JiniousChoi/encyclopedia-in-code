object exercise2 {

  def id(x: Int): Int = x
  def sq(x: Int): Int = x*x
  def sum(f: Int => Int, a: Int, b: Int): Int = {
    def loop(a: Int, acc: Int): Int = {
      if (a > b) acc
      else loop(a+1, acc + f(a))
    }

    loop(a, 0)
  }

  sum(id, 1, 10)
  sum(sq, 1, 10)
  sum((x=> 3*x), 3, 5)


}