class Action:
    def __init__(self, action_type, action_amount, target):
        self.action_type = action_type or ""
        self.action_amount = action_amount or 0
        self.target = target or ""