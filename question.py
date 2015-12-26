class Question:

	def __init__(self):
		self.title = ''
		self.title_id = ''
		self.correct_answer = ''
		self.question = ''
		self.answers = []

	def __str__(self):
		returnString = self.title + " (" + self.title_id + ")" + "\n"
		returnString += self.question + "\n"
		for i in range(0, len(self.answers)):
			answer = self.answers[i]
			if i == self.correct_answer:
				returnString += i.__str__() + ")* " + answer + "\n"
			else:
				returnString += i.__str__() + ") " + answer + "\n"
		return returnString
