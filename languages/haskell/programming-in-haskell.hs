#!/usr/bin/env runhaskell
-- usage 1 (as script) : ./script.hs
-- usage 2 (as script) : runhaskell script.hs
-- usage 3 (compile) : ghc -o hello script.hs && ./hello
-- uwage 4 (in repl) : ghci script.hs
-- usage 5 (in repl) : guci
--                     Prelude> :load script.hs
--                  or Prelude> :reload

import Control.Exception

main :: IO ()
main = do
    printTitle "Chapter 01"
    chapter01
    printTitle "Chapter 01 Exercise"
    chapter01_exercise
    printTitle "Chapter 02"
    chapter02
    printTitle "Chapter 02 Exercise"
    chapter02_exercise
    printTitle "Chapter 03"
    chapter03

printTitle title = do putStrLn $ replicate 50 '-'
                      putStrLn $ left ++ " "  ++ title ++ " " ++ right
                      putStrLn $ replicate 50 '-'
                      where len_hiphens = 50 - 2 - length title
                            hiphens = replicate len_hiphens '-'
                            (left, right) = splitAt (div len_hiphens 2) hiphens

printEq :: Show a => [Char] -> a -> IO ()
printEq s a = putStrLn $ s ++ " = " ++ (show a)

printError :: String -> String -> IO ()
printError s e = do putStr s
                    putStr " => [error] "
                    putStrLn e

chapter01 :: IO ()
chapter01 = do
    -- Chapter 01
    printEq "double 3" $ double 3
    printEq "sum [1,2,3]" $ sum [1,2,3]
    printEq "sum' [1,2,3]" $ sum' [1,2,3]
    printEq "qsort [2,1,4,1,3]" $ qsort [2,1,4,1,3]
    printEq "qsort \"abracadabra\"" $ qsort "abracadabra"
    -- putStr "input three chars: "
    -- res <- seqn [getChar, getChar, getChar]
    -- putStrLn res

-- Chapter 01
-- double :: Num a => a -> a
double x = x + x

-- sum' :: Num a => [a] -> a
sum' [] = 0
sum' (n:ns) = n + sum'(ns)

qsort :: (Ord a) => [a] -> [a]
qsort [] = []
qsort (x:xs) = qsort smaller ++ [x] ++ qsort larger
               where smaller = [a|a <- xs, a <= x]
                     larger  = [b|b <- xs, b > x ]

-- seqn :: [IO a] -> IO [a]
seqn :: Monad m => [m a] -> m [a]
seqn []         = return []
seqn (act:acts) = do x <- act
                     xs <- seqn acts
                     return (x:xs)

-- chapter01_exercise
chapter01_exercise = do
    printEq "product' [1,2,3]" $ product' [1,2,3]
    printEq "qsort_reverse [2,1,4,3]" $ qsort_reverse [2,1,4,3]

chapter02 = do
    printEq "head [1..6]" $ head [1..6]
    printEq "tail [1..6]" $ tail [1..6]
    printEq "[1..6] !! 2" $ [1..6] !! 2
    printEq "take 3 [1..6]" $ take 3 [1..6]
    printEq "drop 3 [1..6]" $ drop 3 [1..6]
    printEq "length [1..6]" $ length [1..6]
    printEq "sum [1..6]" $ sum [1..6]
    printEq "product [1..6]" $ product [1..6]
    printEq "[1,2,3] ++ [4,5,6]" $ [1,2,3] ++ [4,5,6]
    printEq "reverse [1..6]" $ reverse [1..6]
    printEq "average [1..6]" $ average [1..6]

-- product' :: Num a => [a] -> a
product' [] = 1
product' (n:ns) = n * product' ns

qsort_reverse :: (Ord a) => [a] -> [a]
qsort_reverse [] = []
qsort_reverse (x:xs) = qsort_reverse larger ++ [x] ++ qsort_reverse smaller
                       where larger = [a | a <- xs, a >= x]
                             smaller = [b | b <- xs, x > b]

average ns = sum ns `div` length ns 

chapter02_exercise = do printEq "last' [1..6]" $ last' [1..6]
                        printEq "last'' [1..6]" $ last'' [1..6]
                        printEq "init' [1..6]" $ init' [1..6]
                        printEq "init'' [1..6]" $ init'' [1..6]

last' = head . reverse
last'' xs = head $ drop (length xs-1) xs
init' xs = take (length xs - 1) xs
init'' = reverse . drop 1 . reverse

-- Types and classes
chapter03 :: IO()
chapter03 = do
    -- A type is a collection of related values.
    -- e.g. Bool type contains two logical values False and True
    -- e.g. type Bool -> Bool contains functions like, `not`, a logical notation function
    
    -- Basic types
    -- Bool     e.g. False, True
    -- Char     e.g. 'a', 'A', '3', '_'
    -- String   e.g. "abc", "1+2=3"
    -- Int      e.g. -2^63 ~ 2^63-1
    -- Integer  e.g. -inf ~ inf
    -- Float    e.g. sqrt 2 :: Float = 1.4142135
    -- Double   e.g. sqrt 2 :: Double = 1.4142135623730951

    -- List types
    -- a sequence of elements of the same type
    -- e.g. [False, True, False] :: [Bool]
    -- e.g. ['a','b','c','d'] :: [Char] or String
    -- e.g. ["One","Two","Three"] :: [String]
   
    -- Tuple types
    -- a finite sequence of components of possibly different types
    -- e.g. (False,1) :: (Bool,Int)
    -- i.e. (Bool,Int) type includes (False,1), (True,-99), and such

    -- Function types
    -- a mapping from arguments of one type to results of another type.
    -- e.g. fn1 :: T1 -> T2
    -- e.g. fn2 :: T3 -> T4 -> T5
    -- i.e. type Int -> Bool includes `even`, `odd` and such

    -- Curried functions
    -- functions with multiple arguments can be handled in a new way by
    -- exploiting the fact that functions are free to return functions as results
    -- e.g. mult :: Int -> (Int -> (Int -> Int))
    --      mult x y z = x*y*z
    -- As the function arrow -> in types is assumed to associate to the right,
    -- we can rewrite the definition of the mult function above as follows
    -- e.g. mult :: Int -> Int -> Int -> Int
    --      mult x y z = x*y*z
    putStrLn "mult :: Int -> Int -> Int -> Int"
    putStrLn "mult x y z = x*y*z"
    putStrLn "multBy6 = mult 2 3"
    printEq "multBy6 4" $ multBy6 4

    -- Polymorphic types
    printEq "length [1,3,5,7]" $ length [1,3,5,7]
    printEq "length [sin,cos,tan]" $ length [sin,cos,tan]
    printEq "length [\"Yes\",\"No\"]" $ length ["Yes","No"]
    -- The type of function length is [a] -> Int
    -- `a` is called a type variable. In this case, `a` could be anything such as Int, String, etc.
    -- That's why a type that contains 1+ type variables is called polymorphic (of many forms)
    -- length is a polymorphic function, type [a] -> Int is a polymorphic type.
    -- e.g. fst  :: (a,b) -> a
    --      head :: [a] -> a
    --      take :: Int -> [a] -> [a] 
    --      zip  :: [a] -> [b] -> [(a,b)]
    --      id   :: a -> a
    -- The type of a polymorphic function often gives a strong indication about the
    -- function's behavior.
    
    -- 3.8 Overloaded types
    -- A type that contains 1+ class constraints is called overloaded
    -- e.g. (*) :: Num a => a -> a -> a
    --      abs :: Num a => a -> a
    --      (+) :: Num a => a -> a -> a
    --       ^     ^ ^ ^              ^
    --       |     | | type variable  |
    --       |     | class name       |
    --       |     +~~overloaded type~+ 
    --       overloaded function
    -- e.g. 3 :: Num a => a
    --      ^
    --      an overloaded(numeric) type that can be 3::Int, 3::Double, or 
    --      of any numeric type depending on the context in which it is used.
    printEq "(3::Int) * (5::Num a=>a)" $ (3::Int) * (5::Num a=>a)
    printError "(3::Int) * (5::Float)" "Couldn't match expected type ‘Int’ with actual type ‘Float’"
    -- Question
    -- fn1 :: IO a -> IO b -> IO a 는 되면서
    -- fn2 :: Num a -> Num a -> Num a 는 왜 안되고 Num a => a -> a -> a로 해야만 하나?
    
    -- 3.9 Basic classes
    -- A type is a collection of related values
    -- A class is a collection of types that support certain overloaded operations called `methods`
    -- Some basic classes built-in to the language is as follows:
    --
    -- Eq - equality types, whose values can be compared for (in)equality using the following two methods
    --      (==) :: a -> a -> Bool
    --      (/=) :: a -> a -> Bool
    -- All the basic types (Bool, Char, String, Int, Integer, Float, Double) are instances of the Eq class,
    -- as are list and tuple types, provided that their element are compnent types are instances. For example:
    --      > False == False
    --      True
    --      > 'a' == 'b'
    --      False
    --      "abc" == "abc"
    --      True
    --      [1,2] == [1,2,3]
    --      False
    --      ('a',False) == ('a',False)
    --      True
    -- Note. Function types are not in general instances of the Eq class.
    --
    -- Ord - ordered types, that are instances of the Eq class, but in addition whose values are
    -- totally (linearly) ordered, and as such can be compared and processed using the following 6 methods:
    --      (<) :: a -> a -> Bool
    --      (>) :: a -> a -> Bool
    --      (<=) :: a -> a -> Bool
    --      (>=) :: a -> a -> Bool
    --      min :: a -> a -> Bool
    --      max :: a -> a -> Bool
    -- All the basic types are instances of the Ord class, as are list types and tuple types, provided that
    -- their element and component types are instances. For example:
    --      > False < True
    --      True
    --      > min 'a' 'b'
    --      'a'
    --      > "elegant" < "elephant"
    --      True
    --      > [1,2,3] < [1,2]
    --      False
    --      > ('a',2) < ('b',1)
    --      True
    --      > ('a',2) < ('a',1)
    --      False
    -- 
    -- Show - showable types, whose values can be converted into strings of characters using following method:
    --      show :: a -> String
    -- All the basic types are instances of the Show class, as are the list types and tuple types, provided that
    -- their element and component types are instances. For example:
    --      > show False
    --      "False"
    --      > show 'a'
    --      "'a'"
    --      > show 123
    --      "123"
    --      > show [1,2,3]
    --      "[1,2,3]"
    --      show ('a',False)
    --      "('a',False)"
    --      show "abc"
    --      "\"abc\""
    --
    -- Read - readable types, daul to Show, whose values can be converted from strings of characters
    --        using the following method:
    --      read :: String -> a
    -- All the basic types are instances of the Read class, as are list types and tuple types, provided that
    -- their element and component types are instances. For example:
    --      > read "False" :: Bool
    --      False
    --      > read "'a'" :: Char
    --      'a'
    --      > read "123" :: Int
    --      123
    --      > read "[1,2,3]" :: [Int]
    --      [1,2,3]
    --      > read "('a',False)" :: (Char,Bool)
    --      ('a',False)
    -- The use of :: in these examples resolves the type of the result, which would otherwise not be able
    -- to be inferred by GHCi. However, not (read "False") requires no explicit type information, because
    -- the application of the logical negation function `not` implies that read "False" must have type Bool.
    --
    -- Num - numeric types, whose values are numeric, and as such can be processed using the following 6 methods:
    --      (+) :: a -> a -> a
    --      (-) :: a -> a -> a
    --      (*) :: a -> a -> a
    --      negate :: a -> a
    --      abs :: a -> a
    --      signum :: a -> a
    -- For example:
    --      > 1 + 2
    --      3
    --      > 1.0 + 2.0
    --      3.0
    --      > negate 3.0
    --      -3.0
    --      > abs (-3)
    --      3
    --      > signum (-3)
    --      -1
    -- Note that the Num class does not provide a division method. Division is handled separately
    -- using two special classes, one for integral numbers and one for fractional numbers.
    -- 
    -- Integral - integral types, that are instances of the numeric class Num, but in addtion whose
    --            values are integers, and as such support the mothods of integer division and integer remainder:
    --      div :: a -> a -> a
    --      mod :: a -> a -> a
    -- For example:
    --      > 7 `div` 2
    --      3
    --      > 7 `mod` 2
    --      1
    -- For efficiency reasons, a number of prelude functions that involve both list and integers are
    -- restricted to the type Int of finite-precision integers, rather than being applicable to any
    -- instance of the Integral class. For example,
    --      > take 3 [1..]
    --      [1,2,3]
    --      > take 3.0 [1..]
    --      Could not deduce (Fractional Int) arising from the literal ‘3.0’
    -- If required, however, such generic versions of these functions are provided as part of
    -- an additional library file called Data.List.
    --
    -- Fractional - fractional types, that are instances of the numeric class Mum, but in addition whose values
    -- are non-integral, and as such support the methods of fractional division and fractional reciprocation:
    --      (/) :: a -> a -> a
    --      recip :: a -> a
    -- For example:
    --      > 7.0 / 2.0
    --      3.5
    --      > recip 2.0
    --      0.5

mult :: Int -> Int -> Int -> Int
mult x y z = x*y*z
multBy6 = mult 2 3
