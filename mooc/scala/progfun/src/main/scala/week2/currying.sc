object currying {
  def id(a: Int): Int = a

  def mapReduce(f: Int=>Int, combine: (Int, Int) => Int, zero: Int)(a: Int, b:Int): Int =
    if (a > b) zero
    else combine(f(a), mapReduce(f, combine, zero)(a+1, b))
  def product(f: Int=>Int, a: Int, b: Int): Int =
    mapReduce(f, (_ * _), 1)(a, b)
  def fact(n: Int): Int = product(id, 1, n)

  product(id, 1, 5)
  fact(10)
}