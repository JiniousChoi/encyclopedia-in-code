import java.lang.System;

public class p040_SimUDuck {
    public static void main(String[] argv) {
        Duck duck = new MallardDuck();
        duck.quack();
        duck.swim();
        duck.display();

        duck = new RedheadDuck();
        duck.quack();
        duck.swim();
        duck.display();
    }
}

abstract class Duck {
    public void quack() {
        System.out.println("quack quack!");
    }

    public void swim() {
        System.out.println("swim swim!");
    }

    abstract public void display();
}

class MallardDuck extends Duck {
    public void display() {
        System.out.println("I'm MallardDuck");
    }
}

class RedheadDuck extends Duck {
    public void display() {
        System.out.println("I'm RedheadDuck");
    }
}
