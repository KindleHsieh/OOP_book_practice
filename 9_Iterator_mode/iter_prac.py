class CapitalIterator:
    def __init__(self, string):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()

        word = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):
        return self


class CapitalIterable:
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return CapitalIterator(self.string)


if __name__ == '__main__':
    # %% First way.
    iterable = CapitalIterable('The quick bROwn fox jumps over the lazy girl.')
    iterator = iter(iterable)

    while True:
        try:
            print(
                next(iterator)
            )
        except StopIteration:
            break

    # %% Second way.
    print(f"{'-'*5} Second {'-'*5}")
    for word in iterable:
        print(word)

    print(f"{'-' * 5} Thrid {'-' * 5}")
    iterable = CapitalIterable('The quick bROwn fox jumps over the lazy girl.')
    for word in iterable:
        print(word)