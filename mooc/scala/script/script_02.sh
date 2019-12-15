#!/bin/sh
exec scala "$0" "$@"
!#

object Hello extends App {
    println("Hello, world")
    // if you want to access the command line args:
    args.foreach(println)
}
