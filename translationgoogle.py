from google.cloud import translate
import os
import csv

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "ADD PATH TO YOUR GOOGLE CLOUD SERVICE ACCOUNT API KEY HERE"

# https://cloud.google.com/translate/docs/basic/translating-text
# Pull training questions from input_file_name and call the Google Translation API to return JSON response
# Write translated text from JSON response to new CSV spreadsheet in the same order as the input file training questions
# Will recieve an output of a csv file called translation_results.csv


client = translate.TranslationServiceClient()
source_language = 'tr'
target_language = 'en-CA'
parent = client.location_path('tqtraining', 'global')
input_file_format = 'text/plain'
input_file_name = 'turkish_training_questions.csv'

def translation_api():
	with open(input_file_name) as training_questions:
		translation_file = csv.reader(training_questions)
		for tq in translation_file:
			print("Text being translated: {}".format(tq))
			with open('translation_results.csv', 'a') as f:
				translation_output_file = csv.writer(f)
				translation_output = client.translate_text(mime_type = input_file_format, parent = parent, contents = tq, source_language_code= source_language, target_language_code = target_language)
				for translation in translation_output.translations:
					translated_text = translation.translated_text
					print(u"Translated text: {}".format(translated_text))
					# print(type(translated_text))
					translation_output_file.writerow(([translated_text]))

translation_api()


