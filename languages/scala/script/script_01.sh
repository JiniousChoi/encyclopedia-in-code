#!/bin/sh
exec scala "$0" "$@"
!#

println("Hello, world")

args.foreach { println }

//using class
class Person(var firstName: String, var lastName: String) {
    override def toString = firstName + " " + lastName
}

println(new Person("Nacho", "Libre"))
