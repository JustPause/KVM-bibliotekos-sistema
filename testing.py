from concurrent.futures import ThreadPoolExecutor
from time import sleep

values = [3,4,5,6]

def cube(x):
    sleep(5)
    return 3232133


if __name__ == '__main__':
    resul = []
    with ThreadPoolExecutor(max_workers=1) as thread:
        future = thread.submit(cube, 2)
        result = future.result() 
        result.append(resul)
    
    for r in resul:
        print(r)