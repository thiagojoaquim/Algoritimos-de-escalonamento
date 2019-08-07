class Processos():
    def __init__(self, id_process, submission_time, priority, time_execution, blocked_time: int()):
        self.__id_process = id_process
        self.__submission_time = submission_time
        self.__priority = priority
        self.__time_execution = int(time_execution)
        self.__blocked_time = int(blocked_time)
        self.__current_blocked_time = int()
        self.__waiting_time = 0
        self.prioridadeMultilevel = 0
        self.return_time = int(time_execution)
        self.response_time = 0

    @property
    def waiting_time(self):
        return self.__waiting_time

    @property
    def id_process(self):
        return self.__id_process

    @id_process.setter
    def id_process(self, id_process):
        self.__id_process = id_process

    @property
    def submission_time(self):
        return self.__submission_time

    @submission_time.setter
    def submission_time(self, submission_time):
        self.__submission_time = submission_time

    @property
    def blocked_time(self):
        return self.__blocked_time

    @blocked_time.setter
    def blocked_time(self, blocked_time):
        self.__blocked_time = blocked_time

    @property
    def current_blocked_time(self):
        return int(self.__blocked_time)

    @current_blocked_time.setter
    def blocked_time(self, current_blocked_time):
        self.__current_blocked_time = int(current_blocked_time)

    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority):
        self.__priority = priority

    @property
    def time_execution(self):
        return self.__time_execution

    @time_execution.setter
    def time_execution(self, time_execution):
        self.__time_execution = time_execution

    def __eq__(self, other):
        if (other == None):
            return False
        return int(self.id_process) == int(other.id_process)

    def __ne__(self, other):
        if self == None or other == None:
            return False
        return int(self.id_process) != int(other.id_process)

    def __gt__(self, other):
        return int(self.submission_time) > int(other.submission_time)

    def __ge__(self, other):
        return int(self.submission_time) >= (other.submission_time)

    def __le__(self, other):
        return int(self.submission_time) <= int(other.submission_time)

    def __lt__(self, other):
        return int(self.submission_time) < int(other.submission_time)
    def decrementarTempoBloqueio(self, beta:int()):
        if (self.blocked_time > 0):
            self.__blocked_time -= beta
        return self.blocked_time

    def bloquear(self):
        self.__current_blocked_time = self.__blocked_time

    def executar(self, beta):
        self.time_execution -= beta
        return self.time_execution

    def esperar(self):
        self.__waiting_time += 1
