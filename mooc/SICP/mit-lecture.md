## Lecture 2B

See, in general, as systems designers, you are forced with the necessity to make decisions about how you're going to do things, and in general, the way you'd like to retain flexibility is to never make up your mind about anything, until you are forced to do it. 

이를 위해 고안된 powerful design technique 이 있다.
노골적인 미루기와 결정을 유보하는 것은 사실 미묘하다.

진전을 이루고 싶지만 동시에 그 결정의 결과에 속박되고 싶지는 않다. Data Abstraction 이 그렇게 하는 방법 중 하나다. 
우리는 이걸 Wishful Thinking으로 사용했다. use와 representation 으로부터 분리해 생각한 것이다.
이름을 주고 (decision 이) 있다 가정하고 쓴것이 use, 실제 구현(decision)을 나중의 내가 하든 George에게 넘기든 그것이 실제 representation (decision) 이 될것이다.
따라서 이림이 가리키는 내용을 바꾸면 representation을 유연하게 바꿔칠 수가 있다. use 레벨을 건들이지 않은채로.
(단, use 레벨을 건들인 다는 것은 그 이름, api를 바꾸는 것이므로 많은 혼란스런 변화를 초래한다)
