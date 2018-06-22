#!/usr/bin/env runhaskell
-- usage 1 (as script) : ./script.hs
-- usage 2 (as script) : runhaskell script.hs
-- usage 3 (compile) : ghc -o hello script.hs && ./hello
-- uwage 4 (in repl) : ghci script.hs
-- usage 5 (in repl) : guci
--                     Prelude> :load script.hs


main = do
    -- Chapter 01
    printEq "double 3" $ double 3
    printEq "sum [1,2,3]" $ sum [1,2,3]
    printEq "sum' [1,2,3]" $ sum' [1,2,3]
    printEq "qsort [2,1,4,1,3]" $ qsort [2,1,4,1,3]
    printEq "qsort \"abracadabra\"" $ qsort "abracadabra"
    res <- seqn [getChar, getChar, getChar]
    putStrLn res

-- Chapter 01
printEq :: Show a => [Char] -> a -> IO ()
printEq s a = putStrLn $ s ++ " = " ++ (show a)

double x = x + x

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
