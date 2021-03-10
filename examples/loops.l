/* 
 * loops.l
 * By: Liam M Murphy
 */

begin Loops {
    func main() -> int {
        i int := 0;
        while (i < 10) {
            print("Hello world!\n")
            i := i + 1

            if (i % 2 == 0) {
                i := i + 3
            }
        }

        return 0;
    }
}