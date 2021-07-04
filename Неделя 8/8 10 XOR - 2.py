from functools import reduce

print(
    *map(
        lambda x: reduce(
            lambda a, b: a ^ b,
            x
        ),
        zip(
            *map(
                lambda i_elem: list(
                    map(
                        int,
                        i_elem.split()
                    )
                ),
                open('input.txt').readlines()[1:]
            )
        )
    )
)
