import numpy
import typing
import Colors
import Renderer

def first_non_checked(array: numpy.ndarray) -> typing.Tuple[int, int] | None:
    for y, row in enumerate(array):
        for x, is_checked in enumerate(row):
            if not is_checked:
                return y, x

    return None

def count(character: str) -> int:
    checked = Renderer.render(character) == Colors.black
    rows, columns = checked.shape

    total = 0

    while (index := first_non_checked(checked)) is not None:
        is_hole = True

        queue = [index]
        checked[index] = True

        while len(queue) != 0:
            (y, x) = index = queue.pop()

            if x == 0:
                is_hole = False
            elif not checked[y, x - 1]:
                checked[y, x - 1] = True
                queue.append((y, x - 1))

            if x == columns - 1:
                is_hole = False
            elif not checked[y, x + 1]:
                checked[y, x + 1] = True
                queue.append((y, x + 1))

            if y == 0:
                is_hole = False
            elif not checked[y - 1, x]:
                checked[y - 1, x] = True
                queue.append((y - 1, x))

            if y == rows - 1:
                is_hole = False
            elif not checked[y + 1, x]:
                checked[y + 1, x] = True
                queue.append((y + 1, x))

        if is_hole:
            total += 1

    return total