import csv
from question import Question

class CSVImporter:

	def __init__(self, delimiter = ',', quotechar='"'):
		self.delimiter = delimiter
		self.quotechar = quotechar

	def getQuestions(self, question_file):
		questions = []
		with open(question_file, 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=self.delimiter, quotechar=self.quotechar)
			for row in reader:
				question = Question()
				question.question = row[0]
				question.correct_answer = row[1]
				for i in range(2, len(row)):
					question.answers.append(row[i]);
					questions.append(question)
					return questions
