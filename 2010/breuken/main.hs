import Control.Monad (replicateM_)
import Data.List (sort)

data Breuk = Breuk [Char] [Char]
    deriving (Show)

main :: IO ()
main = do
    count <- getInt
    replicateM_ count processLine

getInt = read <$> getLine

processLine :: IO ()
processLine = do
    n <- getBreuk
    putStrLn $ transform n

transform (Breuk xs ys) = unwords [(emptyTo1 xs'),(emptyTo1 ys')]
    where (xs',ys') = simplify xs ys

getBreuk :: IO Breuk
getBreuk = do
    line <- getLine
    let [p1,p2] = words line
    let s1 = sort p1
        s2 = sort p2
    return $ Breuk s1 s2
    
emptyTo1 [] = "1"
emptyTo1 x  = x
                    
                    
                    
simplify xs [] = (xs, [])
simplify [] ys = ([], ys)
simplify (x:xs) ys = if x `elem` ys
    then simplify xs ys'
    else (x:xss', yss')
    where ys' = deleteFirst x ys
          (xss',yss') = simplify xs ys


deleteFirst _ [] = [] 
deleteFirst a (b:bc) | a == b    = bc 
                     | otherwise = b : deleteFirst a bc