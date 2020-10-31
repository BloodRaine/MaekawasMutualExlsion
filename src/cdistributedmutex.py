import vectorclock as vc
from enum import Enum
import time

class STATE(Enum):
    INIT = 0
    REQUEST = 1
    LOCKED = 3
    RELEASED = 4

    def to_str(self):
        if self == 0:
            return 'INIT'
        elif self == 1:
            return 'REQUEST'
        elif self == 3:
            return 'LOCKED'
        elif self == 4:
            return 'RELEASE'
        else:
            return None


class CDistributedMutex:
    def GlobalInitialize(self, thisHost, hosts):
        self.clock = vc.VectorClock().generate(len(hosts))
        self.host = thisHost
        self.hosts = hosts
        

    def QuitAndCleanup(self):
        pass

    #Maekawa
    def MInit(self, votingGroupHosts):
        self.state = STATE.INIT
        pass

    def MLockMutex(self):
        self.state = STATE.LOCKED
        self.clock = self.clock.increment(self.clock, self.host)
        time.sleep(5)
        self.MReleaseMutex()

    def MReleaseMutex(self):
        self.state = STATE.RELEASED
        pass

    def MCleanup(self):
        pass


CDistributedMutex.GlobalInitialize(CDistributedMutex, 1, [0, 1, 2, 3])
