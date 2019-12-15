--computerphile 에서 모나드 예제 보고 한걸로 기억.

data Expr = Val Int | Div Expr Expr deriving Show

safeDiv :: Int -> Int -> Maybe Int
safeDiv x y = if y==0 then Nothing else return (div x y)
--safeDiv x y = if y==0 then Nothing else Just (div x y)

--eval :: Expr -> Maybe Int
--eval (Val n) = return n
--eval (Div x y) = do eval x >>= \n -> ( eval y >>= \m -> ( safeDiv n m ))

eval :: Expr -> Maybe Int
eval (Val n) = return n
eval (Div x y) = do n <- eval x
                    m <- eval y
                    safeDiv n m

main = do let e = Div (Val 4) (Val 2)
          let f = Div (Val 8) e
          let g = Div f (Val 0)
          print $ eval e
          print $ eval f
          print $ eval g

--Prelude> let e = Div (Val 4) (Val 2)
--Prelude> eval e
--Just 2

--Prelude> let f = Div (Val 8) e
--Prelude> eval f
--Just 4

--Prelude> let g = Div f (Val 0)
--Prelude> eval g
--Nothing
