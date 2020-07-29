package main
import "fmt"

func max(a,b int) int{
	var result int = a
	if b > a {
		result = b
	}
	return result
}
func main(){	
	var a,b int
	a = 50
	b = 7
	r:=max(a,b)
	fmt.Printf("the max is %d\n",r)
}