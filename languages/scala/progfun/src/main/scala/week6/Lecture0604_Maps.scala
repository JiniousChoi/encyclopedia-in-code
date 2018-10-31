package week6

/**
  * Another fundamental collection type in Scala is the Map.
  * Maps are special in Scala in the sense that
  * they are both Iterables and Functions
  *
  * Map[Key, Value] extends the function type Key => Value,
  * so maps can be used everywhere functions can.
  */
object Lecture0604_Maps {
  trait Poly {
    val terms: Map[Int, Double]
    override def toString: String = {
      val ss = for ((exp, coef) <- terms.toList.sorted.reverse) yield coef + "x^" + exp
      ss mkString " + "
    }
  }

  class Poly_1st(val terms: Map[Int, Double]) extends Poly {
    def this(bindings: (Int, Double)*) = this(bindings.toMap)
    def +(that: Poly_1st): Poly_1st = new Poly_1st(terms ++ (that.terms map adjust))
    def adjust(term: (Int, Double)): (Int, Double) = {
      val (exp, coef) = term
      this.terms get exp match {
        case Some(coef1) => exp -> (coef+coef1)
        case None => exp -> coef
      }
    }
  }

  class Poly_2nd(val terms: Map[Int, Double]) extends Poly {
    def +(that: Poly_2nd): Poly_2nd = new Poly_2nd(terms ++ (that.terms map adjust))
    def adjust(term: (Int, Double)): (Int, Double) = {
      val terms0 = terms withDefaultValue 0.0
      val (exp, coef) = term
      exp -> (coef + terms0(exp))
    }
  }

  class Poly_foldleft(val terms: Map[Int, Double]) extends Poly {
    def +(other: Poly_foldleft): Poly_foldleft = new Poly_foldleft(terms.foldLeft(other.terms)(addTerm))
    def addTerm(terms: Map[Int,Double], term: (Int, Double)): Map[Int,Double] = {
      val terms0 = terms withDefaultValue 0.0
      val (exp, coef) = term
      val new_coef = coef + terms0(exp)
      terms + (exp -> new_coef)
    }
  }
}

