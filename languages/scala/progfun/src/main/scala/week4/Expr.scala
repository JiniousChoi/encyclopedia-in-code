package week4


trait Expr1 {
 // classification functions
 def isNumber: Boolean
 def isSum: Boolean

 // accessor functions
 def numValue: Int
 def leftOp: Expr1
 def rightOp: Expr1
}

class Number1(val n: Int) extends Expr1 {
 override def isNumber: Boolean = true
 override def isSum: Boolean = false
 override def numValue: Int = n
 override def leftOp: Nothing = throw new Error("num.leftOp")
 override def rightOp: Nothing = throw new Error("num.rightOp")
}

class Sum1(val l: Expr1, val r: Expr1) extends Expr1 {
 override def isNumber: Boolean = false
 override def isSum: Boolean = true
 override def numValue: Int = throw new Error("Sum.numValue")
 override def leftOp: Expr1 = l
 override def rightOp: Expr1 = r
}

object Expr1 {
 // Writing and using classification / accessor functions become tedious quickly,
 // especially when adding more subslasses of Expr1, e.g., Var, Prod, etc.
 // quadratic increase of methods
 def eval(e: Expr1): Int = {
  if (e.isNumber) e.numValue
  else if (e.isSum) eval(e.leftOp) - eval(e.rightOp)
  else throw new Error("Unknown Expression " + e)
 }
}


/////////////
// Expr2 //
/////////////

// I could remove classification functions by migrating recursive logic such as eval from object Expr1, into trait Expr2,
// thanks to polymorphism, but could NOT manage to do so with accessor functions.
trait Expr2

class Number2(val n: Int) extends Expr2

class Sum2(val leftOp: Expr2, val rightOp: Expr2) extends Expr2

object Expr2 {
 // Type tests and casts: hacky, unsafe, low-level
 def eval(e: Expr2): Int = {
  if (e.isInstanceOf[Number2]) e.asInstanceOf[Number2].n
  else if (e.isInstanceOf[Sum2]) eval(e.asInstanceOf[Sum2].leftOp ) + eval(e.asInstanceOf[Sum2].rightOp)
  else throw new Error("Unknown Expressions " + e)
 }
}


/////////////
// Expr3 //
/////////////

// I could remove classification functions by migrating recursive logic such as eval from object Expr1, into trait Expr2,
// thanks to polymorphism, but could NOT manage to do so with accessor functions.
trait Expr3 {
 def eval: Int
 def leftOp: Expr3
 def rightOp: Expr3
}

class Number3(val n: Int) extends Expr3 {
 override def eval: Int = n
 override def leftOp: Expr3 = throw new Error("num.leftOp")
 override def rightOp: Expr3 = throw new Error("num.rightOp")
}

class Sum3(val l: Expr3, val r: Expr3) extends Expr3 {
 override def eval: Int = l.eval + r.eval
 override def leftOp: Expr3 = l
 override def rightOp: Expr3 = r
}


///////////
// Expr4 //
///////////

// No classification / accessor functions needed thanks to pattern matching !!
// pattern matching in functional languages including scala is so beautiful as to abstract all those tedious work from OOP
// pattern matching is strong with extending features from existing classes
// whereas OOP is strong with adding more subclasses without touching existing api
trait Expr4 {
 def eval: Int = this match {
  case Number4(n) => n
  case Sum4(l, r) => l.eval + r.eval
 }

 def show: String = this match {
  case Number4(n) => n.toString
  case Sum4(l, r) => l.show + " + " + r.show
 }
}

case class Number4(val n: Int) extends Expr4
case class Sum4(val l: Expr4, val r: Expr4) extends Expr4
case class Prod(val l: Expr4, val r: Expr4) extends Expr4
case object Var extends Expr4 // does case object work??

object Expr4 {
 //todo: show ( Prod( Sum(2, Var), 4 ) == "(2 + x) * 4"
 //todo: show ( compress ( Sum(Sum(Sum(Var, Var), Var), 3) )  == " 3 * x + 3"
 def compress(e: Expr4): Expr4 = ???
}