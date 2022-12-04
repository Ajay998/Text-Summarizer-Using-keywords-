import spacy
import re
import pymysql.cursors

try:
    # db = pymysql.connect('localhost','demomrat_mrstaging',"!DyM*ySI%c#;U8",'demomrat_mrattestai_staging',autocommit=True,cursorclass = pymysql.cursors.DictCursor)

    db = pymysql.connect(host='localhost', user='root', password='',
                         database='demomrat_mrattestai_staging', autocommit=True,
                         cursorclass=pymysql.cursors.DictCursor)

    # db = pymysql.connect(host="localhost", user="root", passwd="",database='brian',autocommit=True,cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
except pymysql.err.OperationalError as e:
    print(e)
nlp=spacy.load("en_core_web_sm")
labels = []

text = "jooknl AIIMS Medical Center Admission Information Attending Provider Admitting Provider Admission Type Admission Date/Time Emergency 11/10/19 1208 Discharge Date/Time HOSPITAL Service Auth/Cert Status Service Area 11/10/19 1446 Emergency Room Incomplete THP Unit Room/Bed Admission Status THP EMERGENCY ED DISCH/ED DISCH Discharged (Confirmed) Diagnosis Discharge Information Destination (none) Discharge Provider (none) Disposition Home or other long-term residential arrangement Date/Time 11/10/19 1446 Patient Demographics Damitra Hood 614-500-2007 (M) Name Patient ID SSN Legal Sex Birth Date Broom, Laronda 2000008125 xxx-xx-2846 Female 05/27/69 (50 yrs) Address Phone Email Employer 14600 MARSH LANE APT 1003 ADDISON TX 75001 972-707-7208 (M) larondabroombailey@gmail.c om OTHER-CONCENTRA HEALTH Reg Status PCP Verified Chandra, Archana972-353- 8616 Marital Status Religion Language Single Christian English Emergency Contact 1 Patient Ethnicity & Race SHIELD - BCBS TX PPO POS Ethnic Group Patient Race NON HISPANIC BLACK Hospital Account Name Acct ID Class Status Primary Coverage Broom, Laronda 21800038201 Emergency Billed BLUE CROSS BLUE Guarantor Account (for Hospital Account #21800038201) 14600 MARSH LANE APT 1003 ADDISON, TX 75001 Name Relation to Pt Service Area Active? Acct Type Broom, Laronda Self TH Yes Personal/Family Address Phone Coverage Information (for Hospital Account #21800038201) F/O Payor/Plan Precert # BLUE CROSS BLUE SHIELD/BCBS TX PPO POS Subscriber Relation to Pt Subscriber # Broom, Laronda Self SBR129353864001 Grp # Address Phone PO BOX 120695 DALLAS, TX 75312-0695 Status 800-451-0287 Page 1 AIIMS HEALTH University Broom, Laronda 6200 WEST PARKER ROAD MRN: 2000008125, DOB: 5/27/1969, Sex: F Adm: 11/10/2019, D/C: 11/10/2019 Printed by BARRL at 1/9/20 9:59 AM "

keywords = ['HOSPITAL','Medical Center','Health Center','University','HEALTH PLANO']
sentence = text.split(".")
for i in sentence:
    doc = nlp(i)
    for j in doc.ents:
        if j.label_ == "ORG":
        	print(j)
        labels.append(str(j))
print(labels)
C = [x for x in labels if any(b in x for b in keywords)]
print(C)
# # regices = [f"(\w+ {keyword})" for keyword in keywords]
# for i in C:
#     a = re.findall("(\w+ Medical Center)",i)
#     print(a)

# for i in C:
#     for keyword in keywords:
#         keyword_index = i.find(keyword)
#         if keyword_index == -1:
#            continue
#         new_text = i[:keyword_index + len(keyword)]
#         print(new_text)

