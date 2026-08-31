#!/usr/bin/env python3

import subprocess
import multiprocessing
from multiprocessing import Pool
import os

home_path = os.path.expanduser('~')
src = os.path.join(home_path, "data/prod/")
dest = os.path.join(home_path, "data/prod_backup/")

def run(task):
    subprocess.call(["rsync","-arq",os.path.join(src, task),dest])

if __name__ == "__main__":
    root, dirs, files = next(os.walk(src))
    cpu_cores = multiprocessing.cpu_count()
    p = Pool(cpu_cores)
    p.map(run, dirs)
    p.close()
    p.join()