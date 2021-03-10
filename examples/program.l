/* This program serves as a 
   demo for the lexer
*/

begin Program1 { 
    func main() -> int { 
        /* Here we begin the assignments */     
        x int := 4; 
        y int := 5; 
        pi float := 3.14 - 5; 
        name string := "Liam Murphy"; 
    }

    func fib(n int) -> int {
        if (n == 0 || n == 1) {
            return n;
        }
        else {
            return fib(n - 1) + fib(n - 2);
        }
    }
}