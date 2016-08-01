package main

import "fmt"
import "math"

func IsPrime(n int64) bool{
    s := int64(math.Sqrt(float64(n)));

	for i := s; i > 1; i-- {
		if(n%i == 0) {
			return false;
		}
	}

	return true;
}

func MaxPrimeFactor(n int64) int64 {
    s := int64(math.Sqrt(float64(n)));

    for i :=s; i > 1; i-- {
		if(n%i == 0 && IsPrime(i)) {
			return i;
		}
	}

	return 1;
}

func main() {
	fmt.Println("result = ",MaxPrimeFactor(600851475143));
}
