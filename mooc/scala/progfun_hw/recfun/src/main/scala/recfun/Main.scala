package recfun

object Main {
  def main(args: Array[String]) {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
  }

  /**
   * Exercise 1
   */
    def pascal(c: Int, r: Int): Int = {
      if (c==0) 1
      else if (c==r) 1
      else pascal(c-1, r-1) + pascal(c, r-1)
    }
  
  /**
   * Exercise 2
   */
    def balance(chars: List[Char]): Boolean = {
      def logic(chars: List[Char], opened: Int): Boolean = {
        if (opened < 0) false
        else if (chars == List())
          opened == 0
        else if (chars.head == '(')
          logic(chars.tail, opened + 1)
        else if (chars.head == ')')
          logic(chars.tail, opened - 1)
        else
          logic(chars.tail, opened)
      }
      logic(chars, 0)

    }
  
  /**
   * Exercise 3
   */
    def countChange(money: Int, coins: List[Int]) : Int = {
      if (money == 0) 1
      else if (coins.isEmpty) 0
      else (0 to money/coins.head) map (i => countChange(money - i * coins.head, coins.tail)) sum
    }
  }
