import pandas as pd

# Dataset of papers' information per app
df = pd.read_csv(r'C:/Users/Gilles FACCIN/PycharmProjects/e-HealthProject/Outputs/dataset_papers.csv', sep =",")
df2 = pd.read_csv(r'C:/Users/Gilles FACCIN/PycharmProjects/e-HealthProject/Outputs/dataset_papers2.csv', sep =",")
print(df2)

# # Let's take the 4th app which has 2 associated papers --> 2 dictionaries containing information for each paper
# papers = df.iloc[4,1]
# print(type(papers)) # it's a str so we can't write papers[0] to have the first dictionary
# print(papers)
#
# # Let's remove the '[' and ']' at the beginning/end of the str
# papers = papers[1:len(papers)-1]
#
# # Let's extract manually the first paper paper_1 = {'pubmed_id':
# # '32712376\n32378132\n32480303\n31917142\n32228363\n27407704\n31781527\n29936301\n32361677\n32329045\n29127858
# # \n32364125\n25617692\n29755887\n32270358\n31801829\n11045434\n30562653\n18076644\n25191650\n32388156',
# # 'title': 'Feasibility and effectiveness of teleconsultation in children with epilepsy amidst the ongoing COVID-19
# # pandemic in a resource-limited country.', 'abstract': 'The ongoing COVID-19 pandemic and the lockdown measures
# # employed by the government have forced neurologists across the world to look upon telemedicine as the only feasible
# # and practical option to continue providing health care towards children with epilepsy in home isolation. Children
# # with epilepsy are challenging for teleconsultation as direct information from the patient is missing,
# # regarding seizures and adverse effects, especially behavioral and psychological side effects.\nClinical and
# # epilepsy-related details of telephonic consultations for children 1 month-18 years, performed between 26th March
# # and 17th May 2020 in a tertiary care teaching hospital in Uttarakhand (a state of India known for hilly terrains
# # with low per capita income) were recorded. Suitable changes in the dose/commercial brand of antiepileptic drug (
# # AED) regimen were performed, along with the addition of new AED and referral to local practitioners for immediate
# # hospitalization, when urgent health care issues were detected. Voice call, text message, picture/video message,
# # and all other possible measures were employed to accumulate maximum clinical information in real-time.\nA total of
# # 153 children(95 males [62 %], 9.45\u202f±\u202f3.24 years, 140 lower/middle socioeconomic status) were enrolled
# # after screening 237 children with various neurological disorders, whose caregivers contacted for teleconsultation.
# # A total of 278 telephone consultations performed for these 153 children (1-5 telephone calls per patient).
# # Hundred-thirteen children were identified to have a total of 152 significant clinical events (breakthrough
# # seizure/uncontrolled epilepsy (108), AED related (13), and unrelated systemic adverse effects (24), worsening of
# # associated co-morbidities (7). In rest of the patients, the query of the caregiver included unavailability of
# # AED/prescribed commercial brand in the locality, query related to the dose of drugs, proxy for a scheduled routine
# # visit (no active issues), and concern regarding COVID-19 related symptoms and effect of COVID-19 and lockdown in
# # children with epilepsy. Ninety-three (60 %) patients required hiking up of AED dose, whereas 29 (17 %) patients
# # required the addition of a new AED/commercial brand. Five children were advised immediate admission to a nearby
# # hospital. Overall, 147 (96 %) caregivers were satisfied with the quality of medical advice.\nTeleconsultation is
# # one of the few feasible options with good effectiveness for providing medical advice to children with epilepsy
# # during pandemic times.', 'keywords': ['Antiepileptic drugs', 'COVID-19', 'Child neurology', 'Epilepsy',
# # 'Teleconsultation'], 'journal': 'Seizure', 'publication_date': datetime.date(2020, 7, 28), 'authors': [{'lastname':
# # 'Panda', 'firstname': 'Prateek Kumar', 'initials': 'PK', 'affiliation': 'Pediatric Neurology Division, Department
# # of Pediatrics, All India Institute of Medical Sciences, Rishikesh, Uttarakhand, 249203, India.'}, {'lastname':
# # 'Dawman', 'firstname': 'Lesa', 'initials': 'L', 'affiliation': 'Department of Pediatrics, Post Graduate Institute
# # of Medical Education and Research, Chandigarh, 160012, India.'}, {'lastname': 'Panda', 'firstname': 'Pragnya',
# # 'initials': 'P', 'affiliation': 'Department of Medicine, SCB Medical College, Cuttack, Odisha, India.'},
# # {'lastname': 'Sharawat', 'firstname': 'Indar Kumar', 'initials': 'IK', 'affiliation': 'Pediatric Neurology
# # Division, Department of Pediatrics, All India Institute of Medical Sciences, Rishikesh, Uttarakhand, 249203,
# # India. Electronic address: sherawatdrindar@gmail.com.'}], 'methods': None, 'conclusions': 'Teleconsultation is one
# # of the few feasible options with good effectiveness for providing medical advice to children with epilepsy during
# # pandemic times.', 'results': 'A total of 153 children(95 males [62 %], 9.45\u202f±\u202f3.24 years,
# # 140 lower/middle socioeconomic status) were enrolled after screening 237 children with various neurological
# # disorders, whose caregivers contacted for teleconsultation. A total of 278 telephone consultations performed for
# # these 153 children (1-5 telephone calls per patient). Hundred-thirteen children were identified to have a total of
# # 152 significant clinical events (breakthrough seizure/uncontrolled epilepsy (108), AED related (13), and unrelated
# # systemic adverse effects (24), worsening of associated co-morbidities (7). In rest of the patients, the query of
# # the caregiver included unavailability of AED/prescribed commercial brand in the locality, query related to the dose
# # of drugs, proxy for a scheduled routine visit (no active issues), and concern regarding COVID-19 related symptoms
# # and effect of COVID-19 and lockdown in children with epilepsy. Ninety-three (60 %) patients required hiking up of
# # AED dose, whereas 29 (17 %) patients required the addition of a new AED/commercial brand. Five children were
# # advised immediate admission to a nearby hospital. Overall, 147 (96 %) caregivers were satisfied with the quality of
# # medical advice.', 'copyrights': 'Copyright © 2020 British Epilepsy Association. Published by Elsevier Ltd. All
# # rights reserved.', 'doi': '10.1016/j.seizure.2020.07.013', 'xml': <Element 'PubmedArticle' at 0x0A50B1B8>} paper_1
# # = {'pubmed_id': '32712376\n32378132\n32480303\n31917142\n32228363\n27407704\n31781527\n29936301\n32361677\n32329045
# # \n29127858\n32364125\n25617692\n29755887\n32270358\n31801829\n11045434\n30562653\n18076644\n25191650\n32388156',
# # 'title': 'Feasibility and effectiveness of teleconsultation in children with epilepsy amidst the ongoing COVID-19
# # pandemic in a resource-limited country.', 'abstract': 'The ongoing COVID-19 pandemic and the lockdown measures
# # employed by the government have forced neurologists across the world to look upon telemedicine as the only feasible
# # and practical option to continue providing health care towards children with epilepsy in home isolation. Children
# # with epilepsy are challenging for teleconsultation as direct information from the patient is missing,
# # regarding seizures and adverse effects, especially behavioral and psychological side effects.\nClinical and
# # epilepsy-related details of telephonic consultations for children 1 month-18 years, performed between 26th March
# # and 17th May 2020 in a tertiary care teaching hospital in Uttarakhand (a state of India known for hilly terrains
# # with low per capita income) were recorded. Suitable changes in the dose/commercial brand of antiepileptic drug (
# # AED) regimen were performed, along with the addition of new AED and referral to local practitioners for immediate
# # hospitalization, when urgent health care issues were detected. Voice call, text message, picture/video message,
# # and all other possible measures were employed to accumulate maximum clinical information in real-time.\nA total of
# # 153 children(95 males [62 %], 9.45\u202f±\u202f3.24 years, 140 lower/middle socioeconomic status) were enrolled
# # after screening 237 children with various neurological disorders, whose caregivers contacted for teleconsultation.
# # A total of 278 telephone consultations performed for these 153 children (1-5 telephone calls per patient).
# # Hundred-thirteen children were identified to have a total of 152 significant clinical events (breakthrough
# # seizure/uncontrolled epilepsy (108), AED related (13), and unrelated systemic adverse effects (24), worsening of
# # associated co-morbidities (7). In rest of the patients, the query of the caregiver included unavailability of
# # AED/prescribed commercial brand in the locality, query related to the dose of drugs, proxy for a scheduled routine
# # visit (no active issues), and concern regarding COVID-19 related symptoms and effect of COVID-19 and lockdown in
# # children with epilepsy. Ninety-three (60 %) patients required hiking up of AED dose, whereas 29 (17 %) patients
# # required the addition of a new AED/commercial brand. Five children were advised immediate admission to a nearby
# # hospital. Overall, 147 (96 %) caregivers were satisfied with the quality of medical advice.\nTeleconsultation is
# # one of the few feasible options with good effectiveness for providing medical advice to children with epilepsy
# # during pandemic times.', 'keywords': ['Antiepileptic drugs', 'COVID-19', 'Child neurology', 'Epilepsy',
# # 'Teleconsultation'], 'journal': 'Seizure', 'publication_date': datetime.date(2020, 7, 28), 'authors': [{'lastname':
# # 'Panda', 'firstname': 'Prateek Kumar', 'initials': 'PK', 'affiliation': 'Pediatric Neurology Division, Department
# # of Pediatrics, All India Institute of Medical Sciences, Rishikesh, Uttarakhand, 249203, India.'}, {'lastname':
# # 'Dawman', 'firstname': 'Lesa', 'initials': 'L', 'affiliation': 'Department of Pediatrics, Post Graduate Institute
# # of Medical Education and Research, Chandigarh, 160012, India.'}, {'lastname': 'Panda', 'firstname': 'Pragnya',
# # 'initials': 'P', 'affiliation': 'Department of Medicine, SCB Medical College, Cuttack, Odisha, India.'},
# # {'lastname': 'Sharawat', 'firstname': 'Indar Kumar', 'initials': 'IK', 'affiliation': 'Pediatric Neurology
# # Division, Department of Pediatrics, All India Institute of Medical Sciences, Rishikesh, Uttarakhand, 249203,
# # India. Electronic address: sherawatdrindar@gmail.com.'}], 'methods': None, 'conclusions': 'Teleconsultation is one
# # of the few feasible options with good effectiveness for providing medical advice to children with epilepsy during
# # pandemic times.', 'results': 'A total of 153 children(95 males [62 %], 9.45\u202f±\u202f3.24 years,
# # 140 lower/middle socioeconomic status) were enrolled after screening 237 children with various neurological
# # disorders, whose caregivers contacted for teleconsultation. A total of 278 telephone consultations performed for
# # these 153 children (1-5 telephone calls per patient). Hundred-thirteen children were identified to have a total of
# # 152 significant clinical events (breakthrough seizure/uncontrolled epilepsy (108), AED related (13), and unrelated
# # systemic adverse effects (24), worsening of associated co-morbidities (7). In rest of the patients, the query of
# # the caregiver included unavailability of AED/prescribed commercial brand in the locality, query related to the dose
# # of drugs, proxy for a scheduled routine visit (no active issues), and concern regarding COVID-19 related symptoms
# # and effect of COVID-19 and lockdown in children with epilepsy. Ninety-three (60 %) patients required hiking up of
# # AED dose, whereas 29 (17 %) patients required the addition of a new AED/commercial brand. Five children were
# # advised immediate admission to a nearby hospital. Overall, 147 (96 %) caregivers were satisfied with the quality of
# # medical advice.', 'copyrights': 'Copyright © 2020 British Epilepsy Association. Published by Elsevier Ltd. All
# # rights reserved.', 'doi': '10.1016/j.seizure.2020.07.013'}
#
# # From the expression of paper_1 we need to remove the last element 'xml':<...> and comment 'datetime' otherwise --> mistakes
# paper_1 = {'pubmed_id': '32712376\n32378132\n32480303\n31917142\n32228363\n27407704\n31781527\n29936301\n32361677\n32329045\n29127858\n32364125\n25617692\n29755887\n32270358\n31801829\n11045434\n30562653\n18076644\n25191650\n32388156', 'title': 'Feasibility and effectiveness of teleconsultation in children with epilepsy amidst the ongoing COVID-19 pandemic in a resource-limited country.', 'abstract': 'The ongoing COVID-19 pandemic and the lockdown measures employed by the government have forced neurologists across the world to look upon telemedicine as the only feasible and practical option to continue providing health care towards children with epilepsy in home isolation. Children with epilepsy are challenging for teleconsultation as direct information from the patient is missing, regarding seizures and adverse effects, especially behavioral and psychological side effects.\nClinical and epilepsy-related details of telephonic consultations for children 1 month-18 years, performed between 26th March and 17th May 2020 in a tertiary care teaching hospital in Uttarakhand (a state of India known for hilly terrains with low per capita income) were recorded. Suitable changes in the dose/commercial brand of antiepileptic drug (AED) regimen were performed, along with the addition of new AED and referral to local practitioners for immediate hospitalization, when urgent health care issues were detected. Voice call, text message, picture/video message, and all other possible measures were employed to accumulate maximum clinical information in real-time.\nA total of 153 children(95 males [62 %], 9.45\u202f±\u202f3.24 years, 140 lower/middle socioeconomic status) were enrolled after screening 237 children with various neurological disorders, whose caregivers contacted for teleconsultation. A total of 278 telephone consultations performed for these 153 children (1-5 telephone calls per patient). Hundred-thirteen children were identified to have a total of 152 significant clinical events (breakthrough seizure/uncontrolled epilepsy (108), AED related (13), and unrelated systemic adverse effects (24), worsening of associated co-morbidities (7). In rest of the patients, the query of the caregiver included unavailability of AED/prescribed commercial brand in the locality, query related to the dose of drugs, proxy for a scheduled routine visit (no active issues), and concern regarding COVID-19 related symptoms and effect of COVID-19 and lockdown in children with epilepsy. Ninety-three (60 %) patients required hiking up of AED dose, whereas 29 (17 %) patients required the addition of a new AED/commercial brand. Five children were advised immediate admission to a nearby hospital. Overall, 147 (96 %) caregivers were satisfied with the quality of medical advice.\nTeleconsultation is one of the few feasible options with good effectiveness for providing medical advice to children with epilepsy during pandemic times.', 'keywords': ['Antiepileptic drugs', 'COVID-19', 'Child neurology', 'Epilepsy', 'Teleconsultation'], 'journal': 'Seizure', 'publication_date': 'datetime.date(2020, 7, 28)', 'authors': [{'lastname': 'Panda', 'firstname': 'Prateek Kumar', 'initials': 'PK', 'affiliation': 'Pediatric Neurology Division, Department of Pediatrics, All India Institute of Medical Sciences, Rishikesh, Uttarakhand, 249203, India.'}, {'lastname': 'Dawman', 'firstname': 'Lesa', 'initials': 'L', 'affiliation': 'Department of Pediatrics, Post Graduate Institute of Medical Education and Research, Chandigarh, 160012, India.'}, {'lastname': 'Panda', 'firstname': 'Pragnya', 'initials': 'P', 'affiliation': 'Department of Medicine, SCB Medical College, Cuttack, Odisha, India.'}, {'lastname': 'Sharawat', 'firstname': 'Indar Kumar', 'initials': 'IK', 'affiliation': 'Pediatric Neurology Division, Department of Pediatrics, All India Institute of Medical Sciences, Rishikesh, Uttarakhand, 249203, India. Electronic address: sherawatdrindar@gmail.com.'}], 'methods': None, 'conclusions': 'Teleconsultation is one of the few feasible options with good effectiveness for providing medical advice to children with epilepsy during pandemic times.', 'results': 'A total of 153 children(95 males [62 %], 9.45\u202f±\u202f3.24 years, 140 lower/middle socioeconomic status) were enrolled after screening 237 children with various neurological disorders, whose caregivers contacted for teleconsultation. A total of 278 telephone consultations performed for these 153 children (1-5 telephone calls per patient). Hundred-thirteen children were identified to have a total of 152 significant clinical events (breakthrough seizure/uncontrolled epilepsy (108), AED related (13), and unrelated systemic adverse effects (24), worsening of associated co-morbidities (7). In rest of the patients, the query of the caregiver included unavailability of AED/prescribed commercial brand in the locality, query related to the dose of drugs, proxy for a scheduled routine visit (no active issues), and concern regarding COVID-19 related symptoms and effect of COVID-19 and lockdown in children with epilepsy. Ninety-three (60 %) patients required hiking up of AED dose, whereas 29 (17 %) patients required the addition of a new AED/commercial brand. Five children were advised immediate admission to a nearby hospital. Overall, 147 (96 %) caregivers were satisfied with the quality of medical advice.', 'copyrights': 'Copyright © 2020 British Epilepsy Association. Published by Elsevier Ltd. All rights reserved.', 'doi': '10.1016/j.seizure.2020.07.013'}
# print(type(paper_1))
# print(paper_1)
# print(paper_1['pubmed_id'])
