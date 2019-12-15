package example.com;
import example.com.FlyBehavior;
import example.com.QuackBehavior;

abstract class Duck {
    private FlyBehavior flyBehavior;
    private QuackBehavior quackBehavior;

    public void setFlyBehavior(FlyBehavior behavior) {
        this.flyBehavior = behavior;
    }

    public void setQuackBehavior(QuackBehavior behavior) {
        this.quackBehavior = behavior;
    }

    public void performFly() {
        flyBehavior.fly();
    }

    public void performQuack() {
        quackBehavior.quack();
    }

    public void swim() {

    }

    public void display() {

    }

}
