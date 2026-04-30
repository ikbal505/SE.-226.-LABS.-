from vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, vid, model, year, engine_cc, type_):
        super().__init__(vid, model, year)
        self.engine_cc = engine_cc
        self.type = type_

    def __str__(self):
        return f"[Motorcycle] VID: {self.vid} | {self.model} ({self.year}) | Eng: {self.engine_cc}cc | Type: {self.type}"