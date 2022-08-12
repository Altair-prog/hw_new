class Candidate:
    def __init__(self, pk, name, position, skills, picture):
        self.pk = pk
        self.name = name
        self.position = position
        self.skills = skills
        self.picture = picture

    def __repr__(self):
        return f'{self.name} \n {self.position} \n {self.skills}'