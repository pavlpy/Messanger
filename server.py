import Pyro4,hashlib
@Pyro4.expose()
class Server:
    def check(self):
        return True

daemon = Pyro4.Daemon()
uri = daemon.register(Server)
print("uri=",uri)
daemon.requestLoop()