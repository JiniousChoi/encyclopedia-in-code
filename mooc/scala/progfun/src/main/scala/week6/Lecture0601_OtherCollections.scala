package week6

object Lecture0601_OtherCollections {
  /*
   *                          .-> Iterable  <-.
   *                         /       |         \
   *      .---------->   Seq        Set        Map
   *     '      '      /  |  \
   *  Array  String  List | Vector
   *                    Range
   *  Array and String are from Java Universe.
   *  Although scala support almost all methods as any sub type of Seq (if not all),
   *  Keep in mind that Array and String are not of Seq type. (It's just useful hack)
   */

  object exercise {
    // List all combinations numbers, x and y where
    // x is drawn from 1..M and y is drawn from 1..N
    def combi(M: Int, N: Int) = {
      (1 to M) flatMap (x =>
        (1 to N) map (y =>
          (x, y)
        )
      )
    }

    def scalarProduct(xs: Vector[Int], ys: Vector[Int]): Int = {
      (xs zip ys) map (xy => xy._1 * xy._2) sum
    }

    // alternative way to write scalarProduct with a `pattern matching function value`
    // Notice that case clause is embraced with curly brace, not parens
    // Generally the function value `{ case p1 => e1 ... case pn => en }`
    // is equivalent to `x => x match { case p1 => e1 ... case pn => en }`
    def scalarProductWithPatternMatching(xs: Vector[Int], ys: Vector[Int]): Int = {
      (xs zip ys) map { case (x, y) => x * y } sum
      // (xs zip ys) map (x => x match { case (x, y) => x * y }) sum
      // (xs zip ys) map (_ match { case (x, y) => x * y }) sum
    }

    // Write a primality test function of a number in a high-lelvel way
    // For once, value conciseness over efficient
    def isPrime(n: Int): Boolean = if (n > 1) (2 until n) forall (x => n % x != 0) else false
  }
}
