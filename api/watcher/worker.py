import threading
import re
import time
from datetime import datetime, timedelta

import requests

from database import get_closed_session
from hosts.services import get_hosts


class Worker:
    _instance = None
    _lock = threading.Lock()
    _last_host_update = None
    _hosts = None

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                cls._instance = super().__new__(cls)
                cls._instance.thread = None
                cls._instance.running = False
        return cls._instance

    def _run(self):
        while self.running:
            # log do worker
            print("[Worker] Verificando hosts...")

            if not self._last_host_update or self._update_time <= datetime.now():
                Session = get_closed_session()

                with Session() as session:
                    self._hosts = get_hosts(session)

                self._update_time = datetime.now() + timedelta(minutes=30)

            for host in self._hosts:
                req = requests.get(host.endpoint)

                if not req.ok:
                    print('error in req!')
                    # add to queue + log in db
                    continue

            time.sleep(30)

    def start(self):
        if self.thread and self.thread.is_alive():
            return "Worker já está rodando."

        self.running = True
        self.thread = threading.Thread(target=self._run, daemon=True)
        self.thread.start()
        return "Worker iniciado."

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join(timeout=3)
        return "Worker parado."

    def get_status(self):
        if self.thread and self.thread.is_alive():
            return "Rodando"
        return "Parado"
