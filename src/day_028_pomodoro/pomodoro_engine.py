########################################################################################################################

class PomodoroEngine:
    _LABEL_KEY = "LABEL"
    _TIME_KEY = "TIME"
    _BEFORE_START_LABEL = "Pomodoro"
    _WORK_PHASE_LABEL = "Work"
    _BREAK_PHASE_LABEL = "Break"
    _WORK_MIN = 25
    _SHORT_BREAK_MIN = 5
    _LONG_BREAK_MIN = 20

    _WORK_PHASE = {
        _LABEL_KEY: _WORK_PHASE_LABEL,
        _TIME_KEY: _WORK_MIN
    }
    _SHORT_BREAK_PHASE = {
        _LABEL_KEY: _BREAK_PHASE_LABEL,
        _TIME_KEY: _SHORT_BREAK_MIN
    }
    _LONG_BREAK_PHASE = {
        _LABEL_KEY: _BREAK_PHASE_LABEL,
        _TIME_KEY: _LONG_BREAK_MIN
    }
    _PHASES = (_WORK_PHASE,
               _SHORT_BREAK_PHASE,
               _WORK_PHASE,
               _SHORT_BREAK_PHASE,
               _WORK_PHASE,
               _SHORT_BREAK_PHASE,
               _WORK_PHASE,
               _LONG_BREAK_PHASE)

########################################################################################################################

    def __init__(self):
        """
        Create the pomodoro routine engine. Phase=None means that the routine is not running yet.
        """

        self._phase = None

########################################################################################################################

    def start(self) -> None:
        """
        Go to the first phase of the pomodoro routine.
        """

        self._phase = 0

########################################################################################################################

    def reset(self) -> None:
        """
        Stop the pomodoro routine.
        """

        self._phase = None

########################################################################################################################

    def next_phase(self) -> None:
        """
        Go to the next phase of the pomodoro routine. If this was the last one, stop the routine.
        """

        self._phase += 1

        if self._phase == len(self._PHASES):
            self._phase = None

########################################################################################################################

    @property
    def phase_label(self) -> str:
        """
        :return: name of the current phase of the pomodoro routine
        """

        try:
            return self._PHASES[self._phase][self._LABEL_KEY]
        except TypeError:
            return self._BEFORE_START_LABEL

########################################################################################################################

    @property
    def phase_duration(self) -> int:
        """
        :return: duration of the current phase of the pomodoro routine in minutes
        """

        try:
            return self._PHASES[self._phase][self._TIME_KEY]
        except TypeError:
            return 0

########################################################################################################################

    @property
    def is_work_phase(self) -> bool:
        """
        :return: True if the current phase of the pomodoro routine is the work one, False otherwise
        """

        return self.phase_label == self._WORK_PHASE_LABEL

########################################################################################################################

    @property
    def is_break_phase(self) -> bool:
        """
        :return: True if the current phase of the pomodoro routine is the break one, False otherwise
        """

        return self.phase_label == self._BREAK_PHASE_LABEL

########################################################################################################################

    @property
    def is_running(self) -> bool:
        """
        :return: True if the pomodoro routine is currently running, False otherwise
        """

        return self.is_work_phase or self.is_break_phase

########################################################################################################################

    @property
    def work_phases_complete(self) -> int:
        """
        :return: number of work phases already done in the current running pomodoro routine (zero if the routine is
        currently not running)
        """

        try:
            return (self._phase + 1) // 2
        except TypeError:
            return 0

########################################################################################################################
