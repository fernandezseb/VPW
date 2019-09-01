import Control.Monad (replicateM_)

main :: IO ()
main = do
    count <- getInt
    replicateM_ count processLine

getInt = read <$> getLine

processLine :: IO ()
processLine = do
    n <- getInt
    putStrLn $ show $ transform n

transform n = sum [k ^ 3 | k <- [1..n]]