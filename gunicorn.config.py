from gevent import monkey

monkey.patch_all(thread=False, ssl=False)


from hyperdx.opentelemetry import configure_opentelemetry


def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)
    configure_opentelemetry()
