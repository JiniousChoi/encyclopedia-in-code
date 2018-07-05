object printer {
  def horizontal_line(len: Int = 50) = println("-" * len)
  def printTitle(title: String) = {
    val dashes = "-" * (50 - 2 - title.length)
    val (left, right) = dashes.splitAt(dashes.length/2) 
    println("")
    horizontal_line()
    println(s"$left $title $right")
    horizontal_line()
  }
  def printEq(left:String, right:Any, paren:Boolean=false) = printAbstract(left, "=", right, paren)
  def printIs(left:String, right:Any, paren:Boolean=false) = printAbstract(left, "is", right, paren)
  def printTo(left:String, right:Any, paren:Boolean=false) = printAbstract(left, "=>", right, paren)
  def printAbstract(left:String, sep:String, right:Any, paren:Boolean=false) = 
    if (paren) println(s"($left) $sep $right")
    else println(s"$left $sep $right")
  def printError(exprInStr: String, expr: => Any, paren:Boolean=false) {
    try { expr }
    catch {
      case t : Throwable =>
        if (paren) println(s"($exprInStr) throws $t")
        else println(s"$exprInStr throws $t")
    }
  }
  def printAssert(exprInStr: String, expr: => Boolean) {
    assert(expr)
    println(s"assert ( $exprInStr )")
  }
}
