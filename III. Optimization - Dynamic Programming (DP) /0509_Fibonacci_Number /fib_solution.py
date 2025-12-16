class Solution(object):
    # This function is what calculates the Nth Fibonacci number
    def fib(self, n):
        # 1. Handle the simplest starting cases: F(0) is 0, F(1) is 1.
        if n <= 1:
            return n

        # 2. Set up the first two numbers (a = F(0), b = F(1))
        # 'a' and 'b' will be our two "pointers" that slide down the sequence.
        a, b = 0, 1

        # 3. Loop from the 2nd number (i=2) all the way up to the Nth number.
        for i in range(2, n + 1):
            # Calculate the NEXT number: (a + b)
            # Then, "shift" the pointers for the next loop:
            # - The old 'b' (the last number) becomes the new 'a'.
            # - The sum (the new Fibonacci number) becomes the new 'b'.
            a, b = b, a + b
        
        # 4. After the loop finishes, 'b' holds the final answer, F(N).
        return b
