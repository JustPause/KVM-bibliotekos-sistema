from concurrent.futures import ThreadPoolExecutor
from time import sleep


class Thunrd:
    def print(self):
        sleep(5)
        return [1, 2, 3]


class Second:
    def __init__(self):
        self.thunrd = Thunrd()
        self.executor = ThreadPoolExecutor()

    def call_print_async(self):
        future = self.executor.submit(self.thunrd.print)
        return future


class First:
    second = Second()
    future = second.call_print_async()
    for count in range(3):
        print(count)
        sleep(1)

    result = future.result()  # waits when needed
    print(result)


First()
