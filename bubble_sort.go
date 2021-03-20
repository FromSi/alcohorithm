package main

import "fmt"

func main() {
   numbers := []int {123, 12, 34, 111, 5}
   fmt.Println(handler(numbers))
}

func handler(numbers []int) []int {
   N := len(numbers)

   for i := 0; i < N - 1; i++ {
      for j := 0; j < N - i - 1; j++ {
         if numbers[j] > numbers[j + 1] {
            lowValue := numbers[j + 1]
            numbers[j + 1] = numbers[j]
            numbers[j] = lowValue
         }
      }
   }

   return numbers
}
