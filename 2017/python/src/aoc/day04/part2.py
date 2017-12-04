#!/usr/bin/env python

from . import BaseProcessor, get_file_name


class ProcessorP2(BaseProcessor):
    def is_passphrase_valid(self, passphrase):
        words = passphrase.split()
        anagrams = set()
        for word in words:
            if word in anagrams:
                return False

            anagrams.update(self.generate_anagrams(word))

        return True

    def generate_anagrams(self, word):
        return {''.join(p) for p in self.permute(list(word))}

    # Thanks stackoverflow, didn't feel like thinking this through
    def permute(self, xs, low=0):
        if low + 1 >= len(xs):
            yield xs
        else:
            for p in self.permute(xs, low + 1):
                yield p
            for i in range(low + 1, len(xs)):
                xs[low], xs[i] = xs[i], xs[low]
                for p in self.permute(xs, low + 1):
                    yield p
                xs[low], xs[i] = xs[i], xs[low]


def main():
    processor = ProcessorP2(get_file_name())
    print(processor.process())


if __name__ == '__main__':
    main()
