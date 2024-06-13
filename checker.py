
class Checker():
    def __init__(self):
        self.length_similarity = 0

    def get_length_similarity(self):
        return self.length_similarity
    def update_length_similarity(self, str1, str2):
        if str1 == str2:
            self.length_similarity = 60