#!/usr/bin/python3
"""
Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A
will call first(), thread B will call second(), and thread C will call third().
Design a mechanism and modify the program to ensure that second() is executed
after first(), and third() is executed after second().



Example 1:

Input: [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input
[1,2,3] means thread A calls first(), thread B calls second(), and thread C
calls third(). "firstsecondthird" is the correct output.
Example 2:

Input: [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls
third(), and thread C calls second(). "firstsecondthird" is the correct output.
"""
from typing import Callable
from threading import Lock


class Foo:
    def __init__(self):
        """
        Two locks
        """
        self.locks = [Lock(), Lock()]
        self.locks[0].acquire()
        self.locks[1].acquire()


    def first(self, printFirst: Callable[[], None]) -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.locks[0].release()



    def second(self, printSecond: Callable[[], None]) -> None:
        with self.locks[0]:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.locks[1].release()


    def third(self, printThird: Callable[[], None]) -> None:
        with self.locks[1]:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()


class FooError:
    def __init__(self):
        """
        Have a counter, and only the corresponding method can change update the
        counter.

        Error, will miss an input.
        """
        self._value = 1
        self._lock = Lock()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        with self._lock:
            if self._value == 1:
                # printFirst() outputs "first". Do not change or remove this line.
                self._value += 1
                printFirst()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self._lock:
            if self._value == 2:
                # printSecond() outputs "second". Do not change or remove this line.
                self._value += 1
                printSecond()


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self._lock:
            if self._value == 3:
                # printThird() outputs "third". Do not change or remove this line.
                self._value += 1
                printThird()
