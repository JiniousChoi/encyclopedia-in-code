package week6
import scala.io.Source

/**
  * Convert a given telephone number into sentences
  * Original form of data is phonenumber
  * Secondary, processed form of data is words
  *
  * phonenumber ----( encode )---> words
  * phonenumber <---( decode )---- words
  */
object Lecture0605_PuttingThePiecesTogether {
  val abspath = "/Users/jinchoi/github/encyclopedia-in-number/languages/scala/progfun/src/main/scala/week6/big_words.txt"
  val relpath = "src/main/scala/week6/big_words.txt"
  val relpath2 = "src/main/scala/week6/sample_words.txt"
  val in = Source.fromFile(relpath2)

  val mnemonic = Map(
    '2' -> "ABC", '3' -> "DEF", '4' -> "GHI", '5' -> "JKL",
    '6' -> "MNO", '7' -> "PQRS", '8' -> "TUV", '9' -> "WXYZ"
  )

  val allWords = in.getLines().filter(word => word.forall(c => c.isLetter)).map(word => word.toUpperCase).toList

  /**
    * Invert the mnem map into a map from chars 'A' ... 'Z' to '2' ... '9'
    * e.g. Map('A' -> '2', 'B' -> '2', 'C' -> '2', 'D' -> '3' ... 'Z' -> '9')
    */
  val ltr2Digit: Map[Char, Char] =
    for ((digit, str) <- mnemonic; ltr <- str) yield ltr -> digit

  val code2Words: Map[String, Seq[String]] = allWords groupBy word2Code withDefaultValue Seq()

  def word2Code(word: String): String = word map ltr2Digit

  def decode(words0: String): String = {
    val words = words0.toUpperCase
    words.split(" ").map(W => W map ltr2Digit) mkString (" ")
  }

  /**
    * @param number e.g. 8865123
    * @return e.g. [ ["APPLE", "BYE"], ["SCALA", "IS"], ... ]
    */
  def encode(number: String): Set[List[String]] = {
    if (number.isEmpty) Set(List())
    else {
      for {
        split <- 1 to number.length
        word <- code2Words(number take split)
        rest <- encode(number drop split)
      } yield word :: rest
    }.toSet
  }

  def translate(number: String): Set[String] = {
    for (words <- encode(number)) yield words mkString (" ")
  }
}
