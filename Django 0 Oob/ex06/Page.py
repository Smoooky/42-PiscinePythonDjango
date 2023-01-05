#!/usr/bin/env python3

from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Elem, Text


class Page:
    def __init__(self, elem: Elem()) -> None:
        if not isinstance(elem, Elem):
            raise Elem.ValidationError()
        self.elem = elem

    def __str__(self) -> str:
        result = ""
        if isinstance(self.elem, Html):
            result += "<!DOCTYPE html>\n"
        result += str(self.elem)
        return result

    def write_to_file(self, path: str) -> None:
        f = open(path, "w")
        f.write(self.__str__())

    def is_valid(self) -> bool:
        return self.__recursive_check(self.elem)

    def __recursive_check(self, elem: Elem()) -> bool:
        if not (isinstance(elem, (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li,
                                  H1, H2, P, Div, Span, Hr, Br)) or type(elem) == Text):
            return False
        if type(elem) == Text or isinstance(elem, Meta):
            return True
        if isinstance(elem, Html) and len(elem.content) == 2 \
                and type(elem.content[0]) == Head and type(elem.content[1]) == Body:
            if (all(self.__recursive_check(el) for el in elem.content)):
                return True
        elif isinstance(elem, Head) and [isinstance(el, Title) for el in elem.content].count(True) == 1:
            if (all(self.__recursive_check(el) for el in elem.content)):
                return True
        elif isinstance(elem, (Body, Div)) and \
                all([isinstance(el, (H1, H2, Div, Table, Ul, Ol, Span)) or
                    type(el) == Text for el in elem.content]):
            if (all(self.__recursive_check(el) for el in elem.content)):
                return True
        elif isinstance(elem, (Title, H1, H2, Li, Th, Td)) and \
                len(elem.content) == 1 and type(elem.content[0]) == Text:
            return True
        elif isinstance(elem, P) and \
                all([isinstance(el, Text) for el in elem.content]):
            return True
        elif isinstance(elem, Span) and \
                all([isinstance(el, (Text, P)) for el in elem.content]):
            if (all(self.__recursive_check(el) for el in elem.content)):
                return True
        elif isinstance(elem, (Ul, Ol)) and len(elem.content) > 0 and \
                all([isinstance(el, Li) for el in elem.content]):
            if (all(self.__recursive_check(el) for el in elem.content)):
                return True
        elif isinstance(elem, Tr) and len(elem.content) > 0 and\
                all([isinstance(el, (Th, Td)) for el in elem.content]) and \
                all([type(el) == type(elem.content[0]) for el in elem.content]):
            return True
        elif isinstance(elem, Table) and \
                all([isinstance(el, Tr) for el in elem.content]):
            return True
        return False


def __print_test(target: Page, toBe: bool):
    print("-----------Test----------")
    print(str(target))
    assert target.is_valid() == toBe
    print("{:^10s}".format(str(target.is_valid())))


def __test_write_to_file(target: Page, path: str):
    print("-----------Begin----------")
    print(str(target))
    print("--------Output_file-------")
    target.write_to_file(path)
    print("{:^10s}".format(path))


def __test():

    __test_write_to_file(
        Page(Html([Head(Title(Text("hello world!"))),
             Body(H1(Text("HELLO WORLD!")))])),
        "__test_write_to_file.html")


if __name__ == '__main__':
    __test()
