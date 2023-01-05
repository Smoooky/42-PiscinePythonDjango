#!/usr/bin/env python3

class Intern:
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.Name = name

    def __str__(self):
        return self.Name

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return self.Coffee()


def intern():
    print('Create intern1')
    intern1 = Intern()
    print(intern1)
    print('Create intern Mark')
    intern_Mark = Intern("Mark")
    print(intern_Mark)
    print('Ask mark to make you a coffee ...')
    print(intern_Mark.make_coffee())
    print('Ask the other intern to work ...')
    try:
        intern1.work()
    except Exception as exc:
        print(exc)


if __name__ == "__main__":
    intern()

