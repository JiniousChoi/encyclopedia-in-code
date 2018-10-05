module ChapterX
(
  -- Chapter 01
  double ,
  sum' ,
  qsort ,
  seqn ,
  -- Chapter 02
  product' ,
  qsort_reverse ,
  average ,
  init' ,
  init'' ,
  last' ,
  last'' ,
  -- Chapter 03
  mult ,
  multBy6 ,
  -- Chapter 04
  even' ,
  splitAt' ,
  recip' ,
  abs' ,
  abs'' ,
  signum' ,
  signum'' ,

) where


----------------
-- Chapter 01 --
----------------

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


----------------
-- Chapter 02 --
----------------

-- product' :: Num a => [a] -> a
product' [] = 1
product' (n:ns) = n * product' ns

qsort_reverse :: (Ord a) => [a] -> [a]
qsort_reverse [] = []
qsort_reverse (x:xs) = qsort_reverse larger ++ [x] ++ qsort_reverse smaller
                       where larger = [a | a <- xs, a >= x]
                             smaller = [b | b <- xs, x > b]

average ns = sum ns `div` length ns 

last' = head . reverse
last'' xs = head $ drop (length xs-1) xs
init' xs = take (length xs - 1) xs
init'' = reverse . drop 1 . reverse


----------------
-- Chapter 03 --
----------------

mult :: Int -> Int -> Int -> Int
mult x y z = x*y*z
multBy6 = mult 2 3


----------------
-- Chapter 04 --
----------------

even' :: Integral a => a -> Bool
even' n = n `mod` 2 == 0

splitAt' :: Int -> [a] -> ([a],[a])
splitAt' n xs = (take n xs, drop n xs)

recip' :: Fractional a => a -> a
recip' n = 1/n

abs' :: Int -> Int
abs' n = if n >= 0 then n else -n

abs'' :: Int -> Int
abs'' n | n >= 0    = n
        | otherwise = -n

signum' :: Int -> Int
signum' n = if n > 0 then 1 else
               if n == 0 then 0 else -1

signum'' :: Int -> Int
signum'' n | n > 0     = 1
           | n == 0    = 0
           | otherwise = -1
