class FooBar:
    def __init__(self, n):
        self.n = n
        self.event1 = threading.Event()
        self.event2 = threading.Event()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            if i > 0:
                self.event2.wait()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            if i > 0:
                self.event2.clear()
            self.event1.set()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.event1.wait()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.event1.clear()
            self.event2.set()