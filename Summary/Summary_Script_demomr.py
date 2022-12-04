import pymysql.cursors
import re
# import nltk
# import heapq 
# from gensim.summarization import summarize
# from gensim.summarization import keywords
import time
from findKeyword import find_keword as find_keyword 
import spacy
# import scispacy
# import en_core_sci_md  
# from spacy import displacy
# from scispacy.abbreviation import AbbreviationDetector
import Summary_new_approch  as sm

med7 = spacy.load("en_core_med7_lg")
print("MEDS model loaded")


try:					
	# db = pymysql.connect('localhost','demomrat_mrstaging',"!DyM*ySI%c#;U8",'demomrat_mrattestai_staging',autocommit=True,cursorclass = pymysql.cursors.DictCursor)


	db = pymysql.connect(host='localhost',user='demomrat_mrstaging',password='!DyM*ySI%c#;U8',database ='demomrat_mrattestai_staging', autocommit = True,cursorclass=pymysql.cursors.DictCursor)
	
	# db = pymysql.connect(host="localhost", user="root", passwd="",database='brian',autocommit=True,cursorclass=pymysql.cursors.DictCursor)
	cursor = db.cursor()
except pymysql.err.OperationalError as e:
	print(e)

while True:
	cursor.execute("select pk_case_id,report_qc from mt_cases where summary_report=1 and sorting_report =2 and is_empty_report=0 LIMIT 1")
	pending_case = cursor.fetchone()

	if (pending_case is not None):

		case_id=pending_case['pk_case_id']

		if (pending_case['report_qc']==0):
			print(case_id)
			cursor.execute("SELECT pk_report_id,rm_page_date,rm_page_number,rm_bates_number,rm_keyword,rm_provider FROM `mt_sorting_report_master` WHERE fk_case_id=%s and is_summary_gen=0",(case_id))
			Sorted_content = cursor.fetchall()

			for pages in Sorted_content:
				pk_report_id=pages['pk_report_id']
				date=pages['rm_page_date']
				page_number=pages['rm_page_number']
				# bates_number=pages['rm_bates_number']
				heading=pages['rm_keyword']+'\n'+pages['rm_provider']

				if '-' in page_number:
					page_start,page_end=page_number.split('-')
					cursor.execute("SELECT page_number,page_content FROM `mt_page_file_contents` WHERE fk_case_id=%s and page_number BETWEEN %s AND %s  ",(case_id,page_start,page_end))
					page_rage_contents = cursor.fetchall()
					text=[]
					for contents in page_rage_contents :
						text.append(contents['page_content'])
					text=' '.join(map(str, text))
					# print(text)

				else:
					cursor.execute("SELECT page_number,page_content FROM `mt_page_file_contents` WHERE fk_case_id=%s and page_number=%s",(case_id,page_number))
					page_rage_contents = cursor.fetchall()
					for contents in page_rage_contents :
						text=contents['page_content']
					# print(text)

				keyword_list=find_keyword(text)
				print(keyword_list)
				summary=""
				ab_summary="NULL"
				for se in sm.Text_summurization(text):

					se= sm.clean_summary(se)

					print(sm.validate_key(se))
					if sm.validate_key(se):
						# print(split_clean(se)+"\n")
						summary+=sm.split_clean(se)+"\n"
					else:
						print("+++++"+se+"+++++")

				meds= med7(text)
				insert_meds=''
				for med in meds.ents:
					entities_om=str(med.text)
					labels_om=str(med.label_)
					insert_meds+=f'({entities_om},{labels_om})'

				if summary!="":
					is_generated=1
					cursor.execute("update mt_sorting_report_master set is_summary_gen=1 where  fk_case_id=%s and pk_report_id=%s ",(case_id,pk_report_id))
				else:
					is_generated=0
					cursor.execute("update mt_sorting_report_master set is_summary_gen=2 where  fk_case_id=%s and pk_report_id=%s ",(case_id,pk_report_id))



				if len(keyword_list)!=0:
					print(page_number,is_generated)


					cursor.execute("INSERT INTO  mt_summary_report_master"
													"(fk_case_id,fk_report_source_id,fk_report_id,summary_heading,summary_date,source_content,extractive_summary,abstractive_summary,meds,page_range,is_generated)"
													"VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
													   (case_id,1,pk_report_id,heading,date,text,summary,ab_summary,insert_meds,page_number,is_generated))
					try:

						cursor.execute("update nmr_case_details set summary = %s WHERE fk_report_id= %s;",(summary,pk_report_id))

					except:
						print(f"No such {pk_report_id} report id found")
			

			cursor.execute("update mt_cases set summary_report=2 where  pk_case_id=%s",case_id)
				
	 

		elif (pending_case['report_qc']==2):

			cursor.execute("SELECT PK_EID,DATE,PGRANGE,TITLE,PROVIDER FROM `mt_entitiesdata` WHERE fk_case_id=%s",(case_id))
			Sorted_content = cursor.fetchall()

			for pages in Sorted_content:
				
				date=pages['DATE']
				page_number=pages['PGRANGE']
				heading=pages['TITLE']+'\n'+pages['PROVIDER']
				pk_report_id=pages['PK_EID']

				if '-' in page_number:
					page_start,page_end=page_number.split('-')
					cursor.execute("SELECT page_number,page_content FROM `mt_page_file_contents` WHERE fk_case_id=%s and page_number BETWEEN %s AND %s",(case_id,page_start,page_end))
					page_rage_contents = cursor.fetchall()
					text=[]
					for contents in page_rage_contents :
						text.append(contents['page_content'])
					text=' '.join(map(str, text))

				else:
					cursor.execute("SELECT page_number,page_content FROM `mt_page_file_contents` WHERE fk_case_id=%s and page_number=%s",(case_id,page_number))
					page_rage_contents = cursor.fetchall()
					for contents in page_rage_contents :
						text=contents['page_content']
					# print(page_number)

				keyword_list=find_keyword(text)
				summary=""
				ab_summary="NULL"

				for se in sm.Text_summurization(text):

					se= sm.clean_summary(se)

					print(sm.validate_key(se))
					if sm.validate_key(se):
						# print(split_clean(se)+"\n")
						summary+=sm.split_clean(se)+"\n"
					else:
						print("+++++"+se+"+++++")

				meds= med7(text)
				insert_meds=''
				for med in meds.ents:
					entities_om=str(med.text)
					labels_om=str(med.label_)
					insert_meds+=f'({entities_om},{labels_om})'


				if summary!="":
					is_generated=1
				else:
					is_generated=0


				if len(keyword_list)!=0:
					print(page_number,is_generated)
					
					cursor.execute("INSERT INTO  mt_summary_report_master"
									"(fk_case_id,fk_report_source_id,fk_report_id,summary_heading,summary_date,source_content,extractive_summary,abstractive_summary,meds,page_range,is_generated)"
									"VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
									   (case_id,2,pk_report_id,heading,date,text,summary,ab_summary,insert_meds,page_number,is_generated))

					try:

						cursor.execute("update nmr_case_details set summary = %s WHERE fk_report_id= %s;",(summary,pk_report_id))

					except:
						print(f"No such {pk_report_id} report id found")
				
			cursor.execute("update mt_cases set summary_report=2 where  pk_case_id=%s",case_id)

				
		else:
			print("No sorting report generated for this case!!")


	else:
		print("No case pending for generating medical summary!!!")

	time.sleep(15)
	

	
	












