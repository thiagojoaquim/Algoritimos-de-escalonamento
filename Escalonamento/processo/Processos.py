class Processos():
    def __init__(self, id_process, submission_time, priority, time_execution, blocked_time):
        self._id_process = id_process
        self._submission_time = submission_time
        self._priority = priority
        self._time_execution = time_execution
        self._blocked_time = blocked_time

    @property
    def id_process(self):
        return self._id_process

    @id_process.setter
    def id_process(self, id_process):
        self._id_process = id_process

    @property
    def submission_time(self):
        return self._submission_time

    @submission_time.setter
    def submission_time(self, submission_time):
        self._submission_time = submission_time


    @property
    def blocked_time(self):
        return self._blocked_time

    @blocked_time.setter
    def blocked_time(self, blocked_time):
        self._blocked_time = blocked_time

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, priority):
        self._priority = priority

    @property
    def time_execution(self):
        return self._time_execution

    @time_execution.setter
    def time_execution(self, time_execution):
        self._time_execution = time_execution