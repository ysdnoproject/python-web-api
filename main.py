import ctypes
import os
import threading
import time

from fastapi import FastAPI

app = FastAPI()
thread_count_max_limit = min(32, (os.cpu_count() or 1) + 4)


@app.get("/")
@app.get("/threads")
def threads_index():
    thread_list = []
    for t in threading.enumerate():
        thread_list.append({"name": t.name, "ident": t.ident, "daemon": t.daemon})
    return {"list": thread_list, "count": thread_count(), 'limit': thread_count_max_limit}


@app.get("/thread/create")
@app.post("/thread/create")
def thread_create():
    if thread_count() >= thread_count_max_limit:
        return {"error": "Thread count is over limit.Please delete some"}
    else:
        # set daemon=True to let child thread exist when main thread(server) exist
        t = threading.Thread(target=read_file, args=(os.path.abspath('.') + '/test.png',),
                             daemon=True)
        t.start()
        return {"success": True, "taskId": t.ident}


@app.get("/thread/{ident}/delete")
@app.delete("/thread/{ident}/delete")
def thread_delete(ident: int):
    t = find_thread(ident)
    if isinstance(t, threading.Thread):
        # todo not stop immediately.Maybe take a long time to stop thread.
        t.do_run = False
        return {"success": True}
    else:
        return {"error": "Thread(ident: {0}) is not found".format(ident)}


def read_file(path: str):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        so_file_path = os.path.abspath('.') + '/lib/readFile.so'
        c_read_file = ctypes.CDLL(so_file_path)
        # todo handle binary
        file = c_read_file.readFile(ctypes.c_char_p(path.encode('utf-8')))
        print("Thread: {0}, path: ({1})!".format(t.ident, path))
        print(file)
        time.sleep(5)


def find_thread(ident: int):
    for t in threading.enumerate():
        if t.ident == ident:
            return t


def thread_count():
    return threading.active_count()
