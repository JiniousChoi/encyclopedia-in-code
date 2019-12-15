#!/bin/sh
exec scala -classpath "libs/jutil.jar:libs/building-scala-libraries.jar" "$0" "$@"
!#

import jinchoi.util.JMath

object Exercise {
  def main(args: Array[String]) {
    if (args.size < 2) {
        println("usage: ./script_04.sh <Int> <Int>")
        return
    }
    val ns: Array[Int] = for(a <- args) yield a.toInt
    val a = ns(0)
    val b = ns(1)
    println("args[0] + args[1] = " + JMath.add(a, b))

    println("new Library().someLibraryMethod = " + new Library().someLibraryMethod)
  }
}
