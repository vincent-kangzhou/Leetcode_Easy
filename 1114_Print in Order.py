import threading
class Foo(object):
    def __init__(self):
        self.l2=threading.Lock()
        self.l2.acquire()
        self.l3=threading.Lock()
        self.l3.acquire()

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.l2.release()


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        self.l2.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.l3.release()
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        self.l3.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        
        
        
        

class Foo(object):
    def __init__(self):
        self.flag2=False
        self.flag3=False
        
        
    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.flag2=True


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        while self.flag2==False:
            time.sleep(0.01)
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.flag3=True
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        while self.flag3==False:
            time.sleep(0.01)
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        
