from gunicorn.arbiter import Arbiter
from gunicorn.workers.base import Worker

from .environment import set_SERVER_UUID, set_WORKER_UUID
from .threaded import threaded
from .utils import get_internal_id


@threaded
def async_child_exit(server: Arbiter, worker: Worker):
    worker = get_internal_id(worker, ensure=False)
    server = get_internal_id(server, ensure=False)
    print(f"KILLED [{worker = }] [{server = }]")


#### HOOKS


# Called just before the master process is initialized.
def on_starting(server: Arbiter):
    server_uuid = get_internal_id(server)
    set_SERVER_UUID(server_uuid)


# Called just before a worker is forked.
def pre_fork(server: Arbiter, worker: Worker):
    worker_uuid = get_internal_id(worker)
    set_WORKER_UUID(worker_uuid)


# Called just after a worker has been exited, in the master process.
def child_exit(server: Arbiter, worker: Worker):
    async_child_exit(server, worker)
