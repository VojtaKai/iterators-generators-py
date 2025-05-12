# Generators
- simple implementation of iterator and iterable - uses "yield"

# Custom iterator
- class needs to have defined the `__next__` method - contrary to JS where iterator's next method returns `{ value: unknown; done: boolean }`, Python only returns the `value or raise StopIteration (represents done: True)`. For iteration you have to define the `__iter__` method - it should return an iterator => an object with defined next method. The simpliest way is to return the object itself because the `__next__` method is already defined there. No need to create another class with next method just to return a "unique" object.