from yattag import Doc
from yattag import indent
import os


def saveXML(question, filename):
	doc, tag, text = Doc().tagtext();
	question.correct_answer = 'A' + question.correct_answer.__str__()
	doc.asis('<?xml version="1.0" encoding="UTF-8"?>'\
		'<assessmentItem xmlns="http://www.imsglobal.org/xsd/imsqti_v2p0"'\
		' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'\
		' xsi:schemaLocation="http://www.imsglobal.org/xsd/imsqti_v2p0 http://www.imsglobal.org/xsd/imsqti_v2p0.xsd"' \
		' identifier="' + question.title_id + '"' \
		' title="' + question.title + '"' \
		' adaptive="false"' \
		' timeDependent="false">'
		)

	with tag('responseDeclaration', identifier='RESPONSE', cardinality='single', baseType='identifier'):
		with tag('correctResponse'):
			with tag('value'):
				text(question.correct_answer)
	with tag('outcomeDeclaration', identifier='SCORE', cardinality='single', baseType='integer'):
		with tag('defaultValue'):
			with tag('value'):
				text(0)
	with tag('itemBody'):
		with tag('choiceInteraction', responseIdentifier='RESPONSE', shuffle='true', maxChoices='1'):
			with tag('prompt'):
				text(question.question)
			for i in range(0, len(question.answers)):
				code = 'A' + (i+1).__str__()
				answer = question.answers[i]
				with tag('simpleChoice', identifier=code):
					text(answer)
	with tag('responseProcessing', template="http://www.imsglobal.org/question/qti_v2p0/rptemplates/match_correct"):
		pass

	doc.asis('</assessmentItem>')
	xmlfile = open(filename, 'w')
	xmlfile.write(indent(doc.getvalue()))
	xmlfile.close()

def generateManifest(item_dir, manifest_name):
	doc, tag, text = Doc().tagtext();
	files = os.listdir(item_dir + '/' + item_dir)
	doc.asis('<?xml version="1.0" encoding="UTF-8"?>' \
		'<manifest xmlns="http://www.imsglobal.org/xsd/imscp_v1p1" '\
		'xmlns:imsmd="http://www.imsglobal.org/xsd/imsmd_v1p2" '\
		'xmlns:imsqti="http://www.imsglobal.org/xsd/imsqti_v2p1" '\
		'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '\
		'xsi:schemaLocation="http://www.imsglobal.org/xsd/imscp_v1p1 '\
		'http://www.imsglobal.org/xsd/imscp_v1p1.xsd '\
		'http://www.imsglobal.org/xsd/imsmd_v1p2 imsmd_v1p2p4.xsd '\
		'http://www.imsglobal.org/xsd/imsqti_v2p1 http://www.imsglobal.org/xsd/imsqti_v2p1.xsd" '\
		'identifier="' + manifest_name + '">')
	with tag('organizations'):
		pass
	with tag('resources'):
		for file in files:
			filename = os.path.splitext(file)[0]
			with tag('resource', href=item_dir + '/' + file, identifier=filename.lower(), type="imsqti_item_xmlv2p1"):
				with tag('file', href=item_dir + '/' + file):
					pass
	doc.asis('</manifest>')
	xmlfile = open(item_dir + '/imsmanifest.xml', 'w')
	xmlfile.write(indent(doc.getvalue()))
	xmlfile.close()
