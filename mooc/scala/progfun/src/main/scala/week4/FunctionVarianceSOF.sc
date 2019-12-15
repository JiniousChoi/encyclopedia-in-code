abstract class Animal {
  def name: String
}
class Dog(val name: String) extends Animal {
  def bark = println("wow")
}

class Husky(override val name: String) extends Dog(name)

val fn1: Dog => Dog = {d => println(d.name); new Dog("baby dog")}
val fn2: Animal => Husky = {a => println(a.name); new Husky("new husky")}
val fn3: Husky => Dog = {h => println(h.name); new Dog("new baby dog")}
def needsDog(f: Dog => Dog)(d: Dog) = f(d)

needsDog(fn1)(new Dog("jin")).bark
needsDog(fn2)(new Dog("jang")).bark
// needsDog(fn3)(new Husky("pj")).bark // compile error

// Covariance, Invariance, Contra-variance 에 대해 이해
// Variance란, 클래스 파라미터의 속성이다.
// e.g. Queue[+T]라 써있으면 제네릭 큐는 (파라미터 T에 대해) 공변성을 띈다고 한다.
// (단, 제네릭 큐의 경우 파라미터가 하나 뿐이므로, 그냥 공변적이라고 해도 됨.
// e.g. Function1[-T, +U] 인 제네릭 함수의 경우, T에 대해서는 반공변적이고 U에 대해서는 공변적이라고 표현한다.
// 공변성은 함수에 따로, 클래스에 따로 있는것이 아니다. (모든 함수도 결국은 제네릭 함수로 귀결된다는 사실을 기억하자)
// 함수의 경우 인수에 대해서는 반공변적이고 결과값에 대해서는 공변적이다. 이 경우엔 꽤나 직관적이다.
// 왜냐하면, 리턴타입에 맞춰, 그 타입 또는 하위 타입이라고 가정하고 리턴값을 다룰 수 없다면, 할 수 있는게 아무것도 없기 때문이다.
// 다른 말로, 슈퍼함수의 리턴타입이 해석타입이 되고, 서브함수의 리턴타입이 실제타입이 되는 것이다.
// 반면, 함수의 인자가 반공변성을 띄는 이유는 조금 헷갈리지만, 이 또한 꼼꼼히 따져보면 공변/무공변의 경우엔 모순임을 알 수 있다.
// 슈퍼함수의 인자타입이 실제타입(사실은 해석타입일 수 있다.)이고, 서브함수의 인자타입이 해석타입이어야 한다.
// 왜냐하면, Function[Dog, Dog]라는 함수에는 분명 사람들이 Dog 또는 허스키 등의 섭서브 타입을 넘길테니
// SubFunction[Animal, Dog]도 문제없이 성립합을 알 수 있다. Dog를 Animal로 해석하겠다는데 문제가 없는게 당연
// 반면 SubFunction[Husky, Dog]로 해석한다면, Chiwawa가 넘어왔을때 문제가 생김.
// 결론, Function[-X, +Y]는 당연한 귀결이다. -,+도 사실 관점의 뱡향의 차이일분, 해석타입이 항상
// 상위 클래스여만 한다는 LSP를 그대로 따르고 있다.

// 키워드: LSP(Liskov Substitution Principle)
// 상위 클래스에 대해 참인 것은, 하위 클래스에 대해서도 항상 참이어야만 한다. 그 반대는 거짓이다.