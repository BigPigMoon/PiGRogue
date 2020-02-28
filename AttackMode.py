from bearlibterminal import terminal

from ViewMode import ViewMode


class AttackMode(ViewMode):
    def __init__(self):
        super().__init__()
        self.color = "orange"
