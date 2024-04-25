from .application import CustomApplication
from .environment import DEFAULT_PORT, THREADS, WORKER_CLASS, WORKER_TEMP_DIR, WORKERS
from .flaskapp import get_app
from .hooks import child_exit, on_starting, pre_fork


def run():
    options = {
        "bind": f":{DEFAULT_PORT or 8002}",
        "workers": WORKERS,
        "threads": THREADS,
        "worker_class": WORKER_CLASS,
        "worker_tmp_dir": WORKER_TEMP_DIR,
        "on_starting": on_starting,
        "child_exit": child_exit,
        "pre_fork": pre_fork,
    }

    app = get_app()
    CustomApplication(app, options).run()


if __name__ == "__main__":
    run()
