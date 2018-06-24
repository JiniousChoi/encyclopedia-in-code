#!/usr/bin/env runhaskell
-- usage 1 (as script) : ./script.hs
-- usage 2 (as script) : runhaskell script.hs
-- usage 3 (compile) : ghc -o hello script.hs && ./hello
-- uwage 4 (in repl) : ghci script.hs
-- usage 5 (in repl) : guci
--                     Prelude> :load script.hs
--                  or Prelude> :reload

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

printTitle title = do putStrLn $ replicate 50 '-'
                      putStrLn $ left ++ " "  ++ title ++ " " ++ right
                      putStrLn $ replicate 50 '-'
                      where len_hiphens = 50 - 2 - length title
                            hiphens = replicate len_hiphens '-'
                            (left, right) = splitAt (div len_hiphens 2) hiphens

printEq :: Show a => [Char] -> a -> IO ()
printEq s a = putStrLn $ s ++ " = " ++ (show a)

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
