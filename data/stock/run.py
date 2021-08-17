from stockyWockie import stockies
from multiprocessing import Process
if __name__=='__main__':
    try:

        args=[("GME", .1, True), ("AMC", 1, True)]
        for arg in args:
            process = Process(target = stockies, args=arg)
            process.start()
    except KeyboardInterrupt:
        pass