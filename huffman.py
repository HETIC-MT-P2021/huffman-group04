# ----------------------< Class handling letter occurrence in a text >-------------------------------------------
# constructor parameters :                  None
#
# public methods :
#
#   push()                Push a new letter
# ----------------------------------------------------------------------------------------------------------------------


class Occurrence:
    def __init__(self):
        self._occurrence_dict = {}

    def __str__(self):
        output = 'Tableau des occurences : \n'
        output += 'Lettre' + '          ' + 'Occurence \n'
        for occurrence in self._occurrence_dict:
            output += occurrence + '               '
            output += str(self._occurrence_dict[occurrence])
            output += '\n'
        return output

    def push(self, value):
        if value in self._occurrence_dict:
            self._occurrence_dict[value] += 1
        else:
            self._occurrence_dict[value] = 1


text_occurrence = Occurrence()

with open("text.txt") as f:
    for line in f:
        for ch in line:
            text_occurrence.push(ch.lower())

print(text_occurrence)
f.close()
