import os
import threading

import flask

from .environment import SERVER_UUID, WORKER_UUID
from .modules import import_as_new


def get_app():
    flaskapp = flask.Flask(__name__)

    @flaskapp.get("/consume")
    def consume():
        import_as_new("consume.py")
        return {"ok": True}

    @flaskapp.get("/oom")
    def oom():
        huge_list = []
        while True:
            huge_list.extend([1] * 1000000)

    @flaskapp.get("/")
    def index():
        pid = os.getpid()
        worker = WORKER_UUID()
        server = SERVER_UUID()

        print(f"[{pid = }] [{worker = }] [{server = }]")
        return {
            "pid": pid,
            "worker": worker,
            "server": server,
            "threads": [str(th) for th in threading.enumerate()],
        }

    return flaskapp
