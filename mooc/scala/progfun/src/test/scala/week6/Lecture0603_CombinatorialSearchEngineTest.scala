package week6

import org.scalatest.FunSuite

class Lecture0603_CombinatorialSearchEngineTest extends FunSuite {
  test("safe") {
    def assertSafe(pair1: (Int,Int), pair2: (Int,Int)) = {
      val (i1, j1 )= (pair1._1, pair1._2)
      val (i2, j2) = (pair2._1, pair2._2)
      assert(Lecture0603_CombinatorialSearchEngine.NQueen.safe(i1,j1,i2,j2))
      assert(Lecture0603_CombinatorialSearchEngine.NQueen.safe(i2,j2,i1,j1))
    }
    def assertNotSafe(pair1: (Int,Int), pair2: (Int,Int)) = {
      val (i1, j1 )= (pair1._1, pair1._2)
      val (i2, j2) = (pair2._1, pair2._2)
      assert(!Lecture0603_CombinatorialSearchEngine.NQueen.safe(i1,j1,i2,j2))
      assert(!Lecture0603_CombinatorialSearchEngine.NQueen.safe(i2,j2,i1,j1))
    }
    val q00 = (0,0)
    val q01 = (0,1)
    val q10 = (1,0)
    val q11 = (1,1)
    val q12 = (1,2)
    val q21 = (2,1)
    val q22 = (2,2)

    assertNotSafe(q00, q01)
    assertNotSafe(q00, q10)
    assertNotSafe(q00, q11)
    assertNotSafe(q00, q22)
    assertNotSafe(q11, q22)
    assertNotSafe(q01, q21)

    assertSafe(q00, q12)
    assertSafe(q00, q21)
    assertSafe(q01, q22)
    assertSafe(q10, q22)
  }

  test("nqueen") {
    val expected: Set[List[Int]] = Set(List(2,0,3,1), List(1,3,0,2))
    val actual1: Set[List[Int]] = Lecture0603_CombinatorialSearchEngine.NQueen.solution_mutable(4)
    val actual2: Set[List[Int]] = Lecture0603_CombinatorialSearchEngine.NQueen.solution_immutable(4)
    val actual3: Set[List[Int]] = Lecture0603_CombinatorialSearchEngine.NQueen.solution_martin(4)
    assert (actual1 === expected)
    assert (actual2 === expected)
    assert (actual3 === expected)
  }

  test("print nqueen(4)") {
    val qss: Set[List[Int]] = Lecture0603_CombinatorialSearchEngine.NQueen.solution_immutable(4)
    println(Lecture0603_CombinatorialSearchEngine.showAll(qss))
  }
}
