#!/usr/bin/python3
"""
There are two kinds of threads, oxygen and hydrogen. Your goal is to group these
threads to form water molecules. There is a barrier where each thread has to
wait until a complete molecule can be formed. Hydrogen and oxygen threads will
be given releaseHydrogen and releaseOxygen methods respectively, which will
allow them to pass the barrier. These threads should pass the barrier in groups
of three, and they must be able to immediately bond with each other to form a
water molecule. You must guarantee that all the threads from one molecule bond
before any other threads from the next molecule do.

In other words:
If an oxygen thread arrives at the barrier when no hydrogen threads are
present, it has to wait for two hydrogen threads.
If a hydrogen thread arrives at the barrier when no other threads are present,
it has to wait for an oxygen thread and another hydrogen thread.
We don’t have to worry about matching the threads up explicitly; that is, the
threads do not necessarily know which other threads they are paired up with. The
key is just that threads pass the barrier in complete sets; thus, if we examine
the sequence of threads that bond and divide them into groups of three, each
group should contain one oxygen and two hydrogen threads.

Write synchronization code for oxygen and hydrogen molecules that enforces these
constraints.

Example 1:

Input: "HOH"
Output: "HHO"
Explanation: "HOH" and "OHH" are also valid answers.
Example 2:

Input: "OOHHHH"
Output: "HHOHHO"
Explanation: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH",
"HOHOHH" and "OHHOHH" are also valid answers.

Constraints:

Total length of input string will be 3n, where 1 ≤ n ≤ 20.
Total number of H will be 2n in the input string.
Total number of O will be n in the input string.
"""
from typing import Callable
from threading import Semaphore

from collections import deque

class H2O:
    def __init__(self):
        self.hq = deque()
        self.oq = deque()

    def hydrogen(self, releaseHydrogen: Callable[[], None]) -> None:
        self.hq.append(releaseHydrogen)
        self.try_output()

    def oxygen(self, releaseOxygen: Callable[[], None]) -> None:
        self.oq.append(releaseOxygen)
        self.try_output()

    def try_output(self):
        if len(self.hq) >= 2 and len(self.oq) >= 1:
            self.hq.popleft()()
            self.hq.popleft()()
            self.oq.popleft()()


class H2O_TLE2:
    def __init__(self):
        """
        Conditional Variable as counter? - Semaphore
        """
        self.gates = [Semaphore(2), Semaphore(0)]  # inititally allow 2 H, 0 O

    def hydrogen(self, releaseHydrogen: Callable[[], None]) -> None:
        self.gates[0].acquire()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        if self.gates[0].acquire(blocking=False):  # self.gates[0]._value > 0
            # still have available count
            self.gates[0].release()
        else:
            self.gates[1].release()


    def oxygen(self, releaseOxygen: Callable[[], None]) -> None:
        self.gates[1].acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.gates[0].release()
        self.gates[0].release()


class H2O_TLE:
    def __init__(self):
        """
        Conditional Variable as counter?
        Fixed at HHO pattern
        """
        self.h_cnt = 0
        self.locks = [Lock() for _ in range(3)]
        self.locks[1].acquire()


    def hydrogen(self, releaseHydrogen: Callable[[], None]) -> None:
        self.locks[0].acquire()
        self.h_cnt += 1
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        if self.h_cnt < 2:
            self.locks[0].release()
        else:
            self.locks[1].release()


    def oxygen(self, releaseOxygen: Callable[[], None]) -> None:
        self.locks[1].acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.h_cnt = 0
        self.locks[0].release()
