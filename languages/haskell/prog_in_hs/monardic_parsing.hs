import Control.Applicative
import Data.Char

newtype Parser a = P (String -> [(a,String)])

parse :: Parser a -> String -> [(a,String)]

parse (P p) inp = p inp

item :: Parser Char
item = P (\inp -> case inp of
                    []     -> []
                    (x:xs) -> [(x,xs)])

--parse item "jin"
-- [('j',"in")]

instance Functor Parser where
    -- fmap :: (a -> b) -> Parser a -> Parser b
    fmap g p = P (\inp -> case parse p inp of
                            [] -> []
                            [(v,out)] -> [(g v, out)])

-- parse (fmap toUpper item) "jin"
-- [('J',"in")]

instance Applicative Parser where
    -- pure :: a -> Parser a
    pure v = P (\inp -> [(v,inp)])
    
    -- <*> :: Parser (a -> b) -> Parser a -> Parser b
    pg <*> px = P (\inp -> case parse pg inp of
                            [] -> []
                            [(g,out)] -> parse (fmap g px) out)

-- parse (pure toUpper <*> item) "jin"
-- [('J',"in")]
-- parse (pure (\x y z -> (x,z)) <*> item <*> item <*> item) "jinchoi"
-- [(('j','n'),"choi")]

instance Monad Parser where
    -- >>= :: Parser a -> (a -> Parser b) -> Parser b
    pa >>= f = P (\inp -> case parse pa inp of
                            [] -> []
                            [(a,out)] -> parse (f a) out)

three :: Parser (Char,Char)
three = do x <- item
           item
           z <- item
           return (x,z)

-- parse three "jinsung"
-- [(('j','n'),"sung")]
