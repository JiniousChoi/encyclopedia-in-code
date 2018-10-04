package week5

object Lecture0502_PairsAndTuples {
  def msort(xs: List[Int]) : List[Int] = xs match {
    case Nil => xs
    case List(_) => xs
    case _ => {
      val (ys,zs) = xs.splitAt(xs.size/2)
      merge(msort(ys), msort(zs))
    }
  }

  def merge(xs: List[Int], ys: List[Int]) : List[Int] = (xs,ys) match {
    case (Nil, ys) => ys
    case (xs, Nil) => xs
    case(x::xs1, y::ys1) => if (x <= y) x::merge(xs1,ys)
                            else y::merge(xs,ys1)
  }
}
