from q import Queue
import pytest

def test_is_empty():
    q = Queue()
    assert q.is_empty() is True
    assert q.size == 0


def test_add1():
    q = Queue()
    q.add("A")

    assert q.is_empty() is False
    assert q.head.data == "A"
    assert q.size == 1


def test_add2():
    q = Queue()
    q.add("A")
    q.add("B")

    assert q.head.data == "A"
    assert q.head.next.data == "B"
    assert q.size == 2


def test_pop_left():
    q = Queue()
    q.add("A")
    q.add("B")

    popped = q.pop_left()
    assert popped.data == "A"
    assert q.head.data == "B"
    assert q.size == 1


def test_pop_empty():
    q = Queue()
    q.add("A")

    q.pop_left()

    assert q.is_empty() is True
    assert q.size == 0

