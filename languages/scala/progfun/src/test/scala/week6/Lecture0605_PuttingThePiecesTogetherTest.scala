package week6

import org.scalatest.FunSuite

class Lecture0605_PuttingThePiecesTogetherTest extends FunSuite {
  test("read allWords.txt file") {
    val head = Lecture0605_PuttingThePiecesTogether.allWords take 10
    println(head)
  }

  test("decode") {
    val name = "jinchoi"
    val actual = Lecture0605_PuttingThePiecesTogether.decode(name)
    val expected = "5462464"
    assert (actual === expected)
  }

  test("translate") {
    val codes = "7225247386"
    val expected = "SCALA IS FUN"
    val actual = Lecture0605_PuttingThePiecesTogether.translate(codes)
    assert (actual.contains(expected))
  }
}
