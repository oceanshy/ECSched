from element import Machine
from parameter import Parameter

class MacGenerator(object):
    def __init__(self, pa):
        # type: (Parameter) -> object
        self.mac_sequence = []
        res_vec = []
        for i in xrange(pa.res_num):
            res_vec.append(pa.res_slot)
        for i in xrange(pa.mac_num):
            self.mac_sequence.append(Machine(pa.res_num, pa.res_slot, res_vec))
