#!/usr/bin/runhaskell
-- author: jinchoiseoul@gmail.com

import Control.Applicative
import Control.Monad
import System.IO

main :: IO ()
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    --  Print "Hello World" on a new line 'n' times.
    mapM_ putStrLn (getMultipleLines n)
    
getMultipleLines :: Int -> [String]

getMultipleLines n
    | n <= 0 = []
    | otherwise = "Hello World" : getMultipleLines (n-1)
