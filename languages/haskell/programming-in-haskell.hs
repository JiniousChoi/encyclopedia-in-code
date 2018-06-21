-- Chapter 01

main = do
    --putStrLn $ "double 3 = " ++ (show $ double 3)
    --putStrLn $ "sum [1,2,3] = " ++ (show $ sum [1,2,3])
    showStmt "double 3" (double 3)
    showStmt "sum [1,2,3]" (sum [1,2,3])

showStmt :: Show a => [Char] -> a -> IO ()
showStmt s a = do putStrLn $ s ++ " = " ++ (show a)

double x = x + x
