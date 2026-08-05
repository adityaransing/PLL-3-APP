class Fibonacci:

    def __init__(self, n):
        self.n = n

    def recursive(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.recursive(n - 1) + self.recursive(n - 2)


    def dynamic(self):
        if self.n == 0:
            return [0]

        fib = [0] * (self.n + 1)
        fib[0] = 0

        if self.n >= 1:
            fib[1] = 1

        for i in range(2, self.n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]

        return fib

    
    def display_recursive(self):
        print("\nFibonacci Series using Recursion")
        for i in range(self.n):
            print(self.recursive(i), end=" ")
        print()

    def display_dynamic(self):
        print("\nFibonacci Series using Dynamic Programming")
        series = self.dynamic()
        for i in range(self.n):
            print(series[i], end=" ")
        print()



def main():
    n = int(input("Enter number of terms: "))

    obj = Fibonacci(n)

    obj.display_recursive()
    obj.display_dynamic()


if __name__ == "__main__":
    main()