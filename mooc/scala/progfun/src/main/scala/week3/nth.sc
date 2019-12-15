import week3._

def nth[T](n: Int, xs: List[T]): T = {
  if (xs.isEmpty) throw new IndexOutOfBoundsException
  if (n==0) xs.head
  else nth(n-1, xs.tail)
}

val nil = new Nil[Int]
val ls = new Cons(1, new Cons(2, nil))
ls.head
ls.tail.head
nth(0, ls)
nth(1, ls)
nth(11, ls)