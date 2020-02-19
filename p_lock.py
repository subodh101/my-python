import time
from multiprocessing import Process, Lock, Value


def add_monthly_salary(money_left, lock):
    for i in range(30):
        time.sleep(0.05)
        lock.acquire()
        money_left.value += 20000
        lock.release()


def sub_daily_food(money_left, lock):
    for i in range(30):
        time.sleep(0.05)
        lock.acquire()
        money_left.value -= 3500
        lock.release()


def sub_bus_fares(money_left, lock):
    for i in range(30):
        time.sleep(0.05)
        lock.acquire()
        money_left.value -= 400
        lock.release()


def sub_taxi_fares(money_left, lock):
    for i in range(30):
        time.sleep(0.05)
        lock.acquire()
        money_left.value += 400
        lock.release()


def sub_train_fares(money_left, lock):
    for i in range(30):
        time.sleep(0.05)
        lock.acquire()
        money_left.value -= 550
        lock.release()


if __name__ == '__main__':
    money_left = Value('i', 0)
    lock = Lock()
    salary_process = Process(target=add_monthly_salary, args=(money_left, lock,))
    bus_process = Process(target=sub_bus_fares, args=(money_left, lock,))
    taxi_process = Process(target=sub_taxi_fares, args=(money_left, lock,))
    flight_process = Process(target=sub_train_fares, args=(money_left, lock,))
    food_process = Process(target=sub_daily_food, args=(money_left, lock,))

    salary_process.start()
    bus_process.start()
    taxi_process.start()
    flight_process.start()
    food_process.start()

    salary_process.join()
    bus_process.join()
    taxi_process.join()
    flight_process.join()
    food_process.join()

    print("money_left:", money_left.value)
    if money_left.value < 500000:
        print("Spending too much!")
    else:
        print("You are doing good!")
