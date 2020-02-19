import time

from multiprocessing import Pool


def sum_square(numbers: int):
    s = 0
    for i in range(numbers):
        s += i * i
    return s


def sum_sq_with_mp(numbers: list):
    """
    Finds sum of squares using multiprocessing.
    By default Pool uses maximum processes available.
    Args:
        numbers: the list of number to find sum of squares

    """
    start = time.time()
    pool = Pool()
    result = pool.map(sum_square, numbers)
    pool.close()
    # wait for the processes to complete
    pool.join()
    end = time.time() - start
    print(f"Processing {len(numbers)} numbers took {end} time using multiprocessing.")


def sum_sq_without_mp(numbers: list):
    """
    Finds sum of squares without using multiprocessing.
    Args:
        numbers: the list of number to find sum of squares

    """
    start = time.time()
    result = []
    for i in numbers:
        result.append(sum_square(i))

    end = time.time() - start
    print(
        f"Processing {len(numbers)} numbers took {end} time without using multiprocessing."
    )


if __name__ == "__main__":
    numbers = range(10000)
    # Sum of squares with multiprocessing
    sum_sq_with_mp(numbers)
    # Sum of squares without multiprocessing
    sum_sq_without_mp(numbers)
