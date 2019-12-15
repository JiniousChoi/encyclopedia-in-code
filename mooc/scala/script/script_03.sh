#!/bin/sh
exec scala "$0" "$@"
!#

object Hello {
    def main(args: Array[String]) {
        println("Hello, world")
        // if you want to access the command line args:
        args.foreach(println)
    }
}
