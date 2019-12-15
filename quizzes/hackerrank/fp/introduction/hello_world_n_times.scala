#!/usr/bin/env scala
// author: jinchoiseoul@gmail.com

object Solution {
    def f(n : Int) {
        for (i <- 1 to n)
            println("Hello World");
    }

    def main(args: Array[String]) {
        val n = scala.io.StdIn.readInt;
        f(n);
    }
}
