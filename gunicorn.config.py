from hyperdx.opentelemetry import configure_opentelemetry


def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)
    configure_opentelemetry()
