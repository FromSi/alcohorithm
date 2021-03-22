package main

import "fmt"

func main() {
   numbers := []int{1, 9, 2, 8, 3, 7, 4, 6, 5, 10}
   fmt.Println(handler(numbers))
}

func handler(numbers []int) []int {
   if len(numbers) < 2 {
      return numbers
   } else {
      pivot := numbers[0]
     
      var less []int

      for _, value := range numbers[1:] {
         if value <= pivot {
            less = append(less, value)
         }
      }

      var greater []int

      for _, value := range numbers[1:] {
         if value > pivot {
            greater = append(greater, value)
         }
      }

      return append(append(handler(less), pivot), handler(greater)...)
   }
}
