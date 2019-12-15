package week6

import org.scalatest.FunSuite

class Lecture0604_MapsTest extends FunSuite {
  val romanNumerals = Map("I" -> 1, "V" -> 5, "X" -> 10)
  val capitalOfCountry = Map("US" -> "Washington", "Switzerland" -> "Bern", "South Korea" -> "Seoul")

  test("Map is a function") {
    val capital = capitalOfCountry("South Korea")
    assert (capital === "Seoul")
  }

  test("Map is a partial function") {
    //partial function fails on certain conditions
    assertThrows[NoSuchElementException] {
      capitalOfCountry("N/A")
    }
  }

  test("workaround1 - get method") {
    def use_get(key: String): String = {
      val capital: Option[String] = capitalOfCountry get key
      capital match {
        case Some(capital) => capital
        case None => "N/A"
      }
    }

    assert (use_get("US") === "Washington")
    assert (use_get("Arab") === "N/A")
  }

  test("workaround2 - convert it into a total function") {
    val totalfn = capitalOfCountry withDefaultValue "N/A"

    assert (totalfn("US") == "Washington")
    assert (totalfn("Arab") == "N/A")
  }

  test("Poly_1st repr") {
    val p1 = new Lecture0604_Maps.Poly_1st(Map(2->1.0, 1->2.0, 0->1.0))
    val p2 = new Lecture0604_Maps.Poly_1st(2->1.0, 1->2.0, 0->1.0)
    assert (p1.toString === "1.0x^2 + 2.0x^1 + 1.0x^0")
    assert (p1.toString === p2.toString)
  }

  test("map ++ map") {
    val m1 = Map(1->1, 2->2)
    val m2 = Map(1->4, 2->8)
    val actual = m1 ++ m2
    assert (actual === m2)
  }

  test("Ploy + Ploy") {
    val map1 = Map(4->1.0, 2->1.0, 1->2.0, 0->1.0)
    val map2 = Map(3->1.5, 2->2.0, 1->2.0, 0->2.0)
    val expected = "1.0x^4 + 1.5x^3 + 3.0x^2 + 4.0x^1 + 3.0x^0"

    val p1_1 = new Lecture0604_Maps.Poly_1st(map1)
    val p1_2 = new Lecture0604_Maps.Poly_1st(map2)
    assert ((p1_1 + p1_2).toString === expected)

    val p2_1 = new Lecture0604_Maps.Poly_2nd(map1)
    val p2_2 = new Lecture0604_Maps.Poly_2nd(map2)
    assert ((p2_1 + p2_2).toString === expected)

    val p3_1 = new Lecture0604_Maps.Poly_foldleft(map1)
    val p3_2 = new Lecture0604_Maps.Poly_foldleft(map2)
    assert ((p3_1 + p3_2).toString === expected)
  }
}
