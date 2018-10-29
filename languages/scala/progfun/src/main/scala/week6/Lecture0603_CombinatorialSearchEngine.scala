package week6

object Lecture0603_CombinatorialSearchEngine {
  object NQueen {
    def placeable(qs: List[Int], i: Int, j: Int): Boolean = {
      if (qs.isEmpty) return true
      val safes = for ((j2,i2) <- qs.reverse.zipWithIndex) yield safe(i,j,i2,j2)
      safes.forall(s => s)
    }

    def safe(i: Int, j: Int, i2: Int, j2: Int): Boolean = {
      if (Math.abs(i-i2) == Math.abs(j-j2) || i == i2 || j == j2) false
      else true
    }

    def solution_mutable(n: Int): Set[List[Int]] = {
       def run(i: Int, qs: List[Int]): Set[List[Int]] = {
         if (i >= n) Set(qs)
         else {
           var res = Set[List[Int]]()
           for (j <- 0 until n) {
             if (placeable(qs, i, j)) {
               val subres = run(i + 1, j :: qs)
               res ++= subres
             }
           }
           res
         }
       }
      run(0, List())
    }

    def solution_immutable(n: Int): Set[List[Int]] = {
      def run(i: Int, qs: List[Int]): Set[List[Int]] = {
        if (i >= n) Set[List[Int]](qs)
        else {
          val sets = for {
            j <- 0 until n
            if placeable(qs, i, j)
        } yield run(i+1, j::qs)
          sets.foldLeft(Set[List[Int]]())(_++_)
        }
      }
      run(0, List())
    }

    def solution_martin(n: Int): Set[List[Int]] = {
      def safe(qs: List[Int], col: Int): Boolean = {
        val row = qs.length
        val qs_with_index = (row-1 to 0 by -1) zip qs
        qs_with_index.forall{
          case (r,c) => c != col && math.abs(c-col) != row-r
        }
      }

      /**
        *
        * @param k: add a queen at kth row, being not in check with placeQueens(k-1)
        * @return [k-1th col, ... 0th col]
        *    0  1  2  3
        * 0  *  X  *  *
        * 1  *  *  *  X
        * 2  X  *  *  *
        * 3  *  *  X  *
        */
      def placeQueens(k: Int): Set[List[Int]] = {
        if (k<=0) Set(List()) // IMPORTANT: it must NOT be Set()
        else {
          for {
            queens <- placeQueens(k-1)
            col <- 0 until n
            if safe(queens, col)
          } yield col :: queens
        }
      }

      placeQueens(n)
    }
  }

  def showOne(qs: List[Int]): String = {
    val lines =
      for (c <- qs.reverse)
      yield Vector.fill(qs.length)("* ").updated(c, "X ").mkString
    "\n" + (lines mkString "\n")
  }

  def showAll(qss: Set[List[Int]]): String = {
    (qss map showOne) mkString "\n"
  }
}

