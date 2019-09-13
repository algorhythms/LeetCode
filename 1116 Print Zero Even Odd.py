#!/usr/bin/python3
"""
uppose you are given the following code:

class ZeroEvenOdd {
  public ZeroEvenOdd(int n) { ... }      // constructor
  public void zero(printNumber) { ... }  // only output 0's
  public void even(printNumber) { ... }  // only output even numbers
  public void odd(printNumber) { ... }   // only output odd numbers
}
The same instance of ZeroEvenOdd will be passed to three different threads:

Thread A will call zero() which should only output 0's.
Thread B will call even() which should only ouput even numbers.
Thread C will call odd() which should only output odd numbers.
Each of the threads is given a printNumber method to output an integer. Modify
the given program to output the series 010203040506... where the length of the
series must be 2n.


Example 1:

Input: n = 2
Output: "0102"
Explanation: There are three threads being fired asynchronously. One of them
calls zero(), the other calls even(), and the last one calls odd(). "0102" is
the correct output.
Example 2:

Input: n = 5
Output: "0102030405"
"""
from typing import Callable
from threading import Lock


class ZeroEvenOdd:
    def __init__(self, n):
        """
        only use 3 locks, and zero() knows and commonds which lock to release,
        determing whether even() or odd() will run.
        """
        self.n = n
        self.locks = [Lock() for _ in range(3)]
        self.locks[1].acquire()
        self.locks[2].acquire()

	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: Callable[[int], None]) -> None:
        for i in range(self.n):
            self.locks[0].acquire()
            printNumber(0)
            if (i + 1) % 2 == 1:
                self.locks[1].release()
            else:
                self.locks[2].release()

    def odd(self, printNumber: Callable[[int], None]) -> None:
        for i in range((self.n + 1) // 2):
            self.locks[1].acquire()
            printNumber(i * 2 + 1)
            self.locks[0].release()

    def even(self, printNumber: Callable[[int], None]) -> None:
        for i in range(self.n // 2):
            self.locks[2].acquire()
            printNumber(i * 2 + 2)
            self.locks[0].release()


class ZeroEvenOddError:
    def __init__(self, n):
        """
        Like 1115, two layer of locks can do: zero and non-zero alternating,
        odd and even alternating. 4 locks required.

        Using only 3 locks?
        """
        self.n = n
        self.locks = [Lock(), Lock(), Lock(), Lock()]
        for i in range(1, len(self.locks)):
            self.locks[i].acquire()

	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        with self.locks[0]:
            printNumber(0)

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        # cannot lock self.locks[1] from both "even" and "odd"
        pass


    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        pass
