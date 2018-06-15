class Rational(x: Int, y: Int) {
  require(y != 0, "denominator should be non-zero!")
  val g = gcd(x, y).abs
  val numer = x / g
  val denom = y / g

  def this(a: Int) = this(a, 1)

  def + (other: Rational): Rational =
    new Rational(
      numer * other.denom + denom * other.numer,
      denom * other.denom)

  def - (other: Rational): Rational =
    new Rational(
      numer * other.denom - denom * other.numer,
      denom * other.denom)

  def * (other: Rational): Rational =
    new Rational(numer * other.numer, denom * other.denom)

  def / (other: Rational): Rational =
    new Rational(numer * other.denom, denom * other.numer)

  def unary_- = new Rational(-numer, denom)

  def < (other:Rational) =
    numer * other.denom < other.numer * denom

  def max (other: Rational) =
    if (this < other) other else this
  override def toString(): String =
    if (denom == 1) numer + "" else numer + "/" + denom

  def gcd(a: Int, b: Int): Int = if (b==0) a else gcd(b, a%b)

}

val aOne = new Rational(1)
val aThird = new Rational(1, 3)
val aHalf = new Rational(1, 2)
val aSixth = new Rational(1, 6)

aOne
aHalf + aHalf
aHalf - aHalf
aHalf + aThird
aThird - aHalf
aOne - aSixth

aHalf / aHalf
aHalf * aHalf

aHalf < aOne
aHalf max aOne
aSixth max aHalf
aHalf max aSixth

-aHalf
