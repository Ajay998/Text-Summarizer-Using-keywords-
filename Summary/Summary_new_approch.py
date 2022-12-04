import re
# import nltk
# import heapq 
# from gensim.summarization import summarize
# from gensim.summarization import keywords
import time
from findKeyword import find_keword
# import pandas as pd

def summary_content(text):
	key_headings=find_keword(text)
	print(key_headings)
	for key in key_headings:
		i_key=key+":"
		i_key_new="~ "+i_key
				
		if (i_key.lower() in text.lower()):
			insensitive_hippo = re.compile(re.escape(i_key), re.IGNORECASE)
			text=insensitive_hippo.sub(i_key_new, text)

		else:
			continue

	text_formatted=text.split("~")

	return text_formatted

def validate_key(text):
	key_headings=find_keword(text)
	for key in key_headings:
		i_key=key+":"

		if (i_key.lower() in text.lower()):
			return True 
		else:
			continue
	return False

def clean_summary(text):
	L_text=text.split(":")
	if len(L_text)>2:
		N_text=L_text[0]+":"+L_text[1]
		NL_text=N_text.split(".")
		N_text=re.sub(r'(?:^|(?<=\s)){}(?:$|(?=\s))'.format(re.escape(NL_text[-1])),"", N_text)
		return N_text
	else:
		return text

def split_clean(text):
	text_ls=text.split(".")
	
	if len(text_ls)>1:
		text=text.replace(text_ls[-1]," ")
	try:
		text = re.sub(r"[-()\"#/@;:<>{}-=~|.?,]", " ", text)
	except:
		print("skipped \n Key word extraction in progress")
	return text


def Text_summurization(text):
	sent_num=20
	article_text = text
	try:
		article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  
		article_text = re.sub(r'\s+', ' ', article_text)  

		formatted_article_text = re.sub('[^a-zA-Z:./],', ' ', article_text )  
		formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
		final_text=summary_content(formatted_article_text)



		# sentence_list = nltk.sent_tokenize(article_text)  
	except Exception as e:
				print (e)
				final_text="error"
	return final_text

#for testing 
# if __name__=="__main__":

# 	Text1="""
# Dx: THIS ,IS ,A. TEST. FOR, CASE.
# Diagnosis: THIS ,IS ,A. TEST. FOR, CASE.
# Impression: THIS ,IS ,A. TEST. FOR, CASE.
# Clinical Impression: THIS ,IS ,A. TEST. FOR, CASE.
# Final Diagnosis: THIS ,IS ,A. TEST. FOR, CASE.
# Discharge Diagnosis: THIS ,IS ,A. TEST. FOR, CASE.
# Meds: THIS ,IS ,A. TEST. FOR, CASE.
# Discharge Meds: THIS ,IS ,A. TEST. FOR, CASE.
# Treatment: THIS ,IS ,A. TEST. FOR, CASE.
# Further Treatment: THIS ,IS ,A. TEST. FOR, CASE.
# Preoperative Dx: THIS ,IS ,A. TEST. FOR, CASE.
# Pre Operative Diagnosis: THIS ,IS ,A. TEST. FOR, CASE.
# Postoperative Dx: THIS ,IS ,A. TEST. FOR, CASE.
# Post Operative Diagnosis: THIS ,IS ,A. TEST. FOR, CASE.

# """

# 	summary_output=" "
# 	for se in Text_summurization(Text1):

# 		se= clean_summary(se)

# 		print(validate_key(se))
# 		if validate_key(se):
# 			# print(split_clean(se)+"\n")
# 			summary_output+=split_clean(se)+"\n"
# 		else:
# 			print("++++++++++++++++++"+se+"+++++++++++++++++++++")

	

# 	print(summary_output)