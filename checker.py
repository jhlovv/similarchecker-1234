
class Checker():
    def __init__(self):
        self.length_similarity = 0

    def get_length_similarity(self):
        return self.length_similarity
    def update_length_similarity(self, str1, str2):
        if len(str1) == len(str2):
            self.length_similarity = 60
        elif len(str1) >= len(str2)*2 or len(str1)*2 <= len(str2):
            self.length_similarity = 0
        else:
            if len(str1) > len(str2):
                large_len = len(str1)
                gap = len(str1) - len(str2)
            else:
                large_len = len(str2)
                gap = len(str2) - len(str1)
            self.length_similarity = (1 - gap/large_len) * 60
