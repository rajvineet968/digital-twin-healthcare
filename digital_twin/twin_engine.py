class DigitalTwin:
    def __init__(self):
        self.history = []

    def update(self, data):
        self.history.append(data)

    def get_latest(self):
        return self.history[-1] if self.history else {}

    def simulate_future(self):
        if not self.history:
            return "No data"

        latest = self.history[-1]

        if latest.get("Glucose", 0) > 150:
            return "Future diabetes risk increasing"

        if latest.get("chol", 0) > 250:
            return "Heart risk increasing"

        return "Stable condition"