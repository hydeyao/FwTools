class FwGuide:
    def __init__(self, num, model, pid, pcb, file_path, burn_way):
        self.num = num
        self.model = model
        self.pid = pid
        self.pcb = pcb
        self.file_path = file_path
        self.burn_way = burn_way


class PID:
    def __init__(self, major, first, second):
        self.major = major
        self.first = first
        self.second = second


class PCB:
    def __init__(self, fw1, fw2, fw3):
        self.fw1 = fw1
        self.fw2 = fw2
        self.fw3 = fw3


class FilePath:
    def __init__(self, name1, name2, name3):
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3


class BurnWay:
    def __init__(self, way1, way2, way3):
        self.way1 = way1
        self.way2 = way2
        self.way3 = way3
