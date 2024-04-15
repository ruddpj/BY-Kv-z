pos_q = [
    'a', 'b', 'c', 'č', 'd', 'ď', 'e', 'f', 'g', 'h', 'ch', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 'š', 't',
    'u', 'v', 'w', 'z', 'ž'
]


class Hexagon:
    def __init__(self, name, state, color, num, normal_q, binary_q):
        self.name = name
        self.state = state
        self.color = color
        self.num = num
        self.normal_q = normal_q
        self.binary_q = binary_q


colors = ("gray90", "orange", "cyan", "red")
