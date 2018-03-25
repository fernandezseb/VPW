package main

import (
	"fmt"
	"math"
)

func main() {
	var amount int
	fmt.Scanf("%d\n", &amount)

	for i := 1; i <= amount; i++ {
		var n int
		fmt.Scanf("%d\n", &n)
		sum := 0
		for c := 1; c < n+1; c++ {
			sum += int(math.Pow(float64(c), 3.0))
		}
		fmt.Println(sum)
	}

}
