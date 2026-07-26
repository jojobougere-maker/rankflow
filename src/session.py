class Session:

    def __init__(self):
        self.current_sr = 6875
        self.goal = 7000

        self.session_sr = 0

        self.wins = 0
        self.losses = 0

        self.winstreak = 0

        self.rank = ""