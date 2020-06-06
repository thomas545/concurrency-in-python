import time
import requests
import string
import random
from multiprocessing import Pool, cpu_count
import threading
import asyncio

def make_requests(size):
    return ''.join(random.choice(string.ascii_letters + string.digits + "!@#$%^&*()_+=") for _ in range(size))


def Normal_getter():
    make_requests(10000000)

def measure_sync():
    """ 18 sec """
    start = time.perf_counter()
    Normal_getter()
    end = time.perf_counter()
    print(f"Sync -> {end - start :.2f}")


def getter_with_multiprocessing():
    with Pool(cpu_count()) as p:
        p.map(make_requests(10000000), [])

def measure_multiprocessing():
    """ 19 sec """
    start = time.perf_counter()
    getter_with_multiprocessing()
    end = time.perf_counter()
    print(f"Multiprocessing -> {end - start}")


def getter_with_threading():
    return threading.Thread(target=make_requests, args=[1000000,])

def measure_threading():
    """ 5 sec """
    start = time.perf_counter()
    getter_with_threading()
    end = time.perf_counter()
    print(f"Threading -> {end - start}")

measure_sync()
measure_multiprocessing()
measure_threading()