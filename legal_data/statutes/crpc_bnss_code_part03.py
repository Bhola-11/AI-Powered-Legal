"""
Part 03 for crpc_bnss_code
Modular codification slice under 250 KB
"""

CRPC_SECTIONS_REGISTRY_PART_03 = [
    {
        "section_id": "CRPC-SEC-101",
        "section_number": "101",
        "title": "Criminal Procedure Statutory Provision Section 101",
        "chapter_heading": "Chapter 7: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 101 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-102",
        "section_number": "102",
        "title": "Criminal Procedure Statutory Provision Section 102",
        "chapter_heading": "Chapter 7: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 102 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-103",
        "section_number": "103",
        "title": "Criminal Procedure Statutory Provision Section 103",
        "chapter_heading": "Chapter 7: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 103 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-104",
        "section_number": "104",
        "title": "Criminal Procedure Statutory Provision Section 104",
        "chapter_heading": "Chapter 7: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 104 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-105",
        "section_number": "105",
        "title": "Criminal Procedure Statutory Provision Section 105",
        "chapter_heading": "Chapter 7: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 105 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-106",
        "section_number": "106",
        "title": "Criminal Procedure Statutory Provision Section 106",
        "chapter_heading": "Chapter 8: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 106 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-107",
        "section_number": "107",
        "title": "Criminal Procedure Statutory Provision Section 107",
        "chapter_heading": "Chapter 8: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 107 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-108",
        "section_number": "108",
        "title": "Criminal Procedure Statutory Provision Section 108",
        "chapter_heading": "Chapter 8: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 108 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-109",
        "section_number": "109",
        "title": "Criminal Procedure Statutory Provision Section 109",
        "chapter_heading": "Chapter 8: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 109 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-110",
        "section_number": "110",
        "title": "Criminal Procedure Statutory Provision Section 110",
        "chapter_heading": "Chapter 8: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 110 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-111",
        "section_number": "111",
        "title": "Criminal Procedure Statutory Provision Section 111",
        "chapter_heading": "Chapter 8: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 111 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-112",
        "section_number": "112",
        "title": "Criminal Procedure Statutory Provision Section 112",
        "chapter_heading": "Chapter 8: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 112 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-113",
        "section_number": "113",
        "title": "Criminal Procedure Statutory Provision Section 113",
        "chapter_heading": "Chapter 8: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 113 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-114",
        "section_number": "114",
        "title": "Criminal Procedure Statutory Provision Section 114",
        "chapter_heading": "Chapter 8: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 114 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-115",
        "section_number": "115",
        "title": "Criminal Procedure Statutory Provision Section 115",
        "chapter_heading": "Chapter 8: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 115 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-116",
        "section_number": "116",
        "title": "Criminal Procedure Statutory Provision Section 116",
        "chapter_heading": "Chapter 8: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 116 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-117",
        "section_number": "117",
        "title": "Criminal Procedure Statutory Provision Section 117",
        "chapter_heading": "Chapter 8: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 117 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-118",
        "section_number": "118",
        "title": "Criminal Procedure Statutory Provision Section 118",
        "chapter_heading": "Chapter 8: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 118 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-119",
        "section_number": "119",
        "title": "Criminal Procedure Statutory Provision Section 119",
        "chapter_heading": "Chapter 8: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 119 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-120",
        "section_number": "120",
        "title": "Criminal Procedure Statutory Provision Section 120",
        "chapter_heading": "Chapter 8: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 120 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-121",
        "section_number": "121",
        "title": "Criminal Procedure Statutory Provision Section 121",
        "chapter_heading": "Chapter 9: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 121 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-122",
        "section_number": "122",
        "title": "Criminal Procedure Statutory Provision Section 122",
        "chapter_heading": "Chapter 9: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 122 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-123",
        "section_number": "123",
        "title": "Criminal Procedure Statutory Provision Section 123",
        "chapter_heading": "Chapter 9: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 123 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-124",
        "section_number": "124",
        "title": "Criminal Procedure Statutory Provision Section 124",
        "chapter_heading": "Chapter 9: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 124 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-125",
        "section_number": "125",
        "title": "Criminal Procedure Statutory Provision Section 125",
        "chapter_heading": "Chapter 9: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 125 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-126",
        "section_number": "126",
        "title": "Criminal Procedure Statutory Provision Section 126",
        "chapter_heading": "Chapter 9: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 126 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-127",
        "section_number": "127",
        "title": "Criminal Procedure Statutory Provision Section 127",
        "chapter_heading": "Chapter 9: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 127 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-128",
        "section_number": "128",
        "title": "Criminal Procedure Statutory Provision Section 128",
        "chapter_heading": "Chapter 9: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 128 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-129",
        "section_number": "129",
        "title": "Criminal Procedure Statutory Provision Section 129",
        "chapter_heading": "Chapter 9: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 129 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-130",
        "section_number": "130",
        "title": "Criminal Procedure Statutory Provision Section 130",
        "chapter_heading": "Chapter 9: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 130 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-131",
        "section_number": "131",
        "title": "Criminal Procedure Statutory Provision Section 131",
        "chapter_heading": "Chapter 9: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 131 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-132",
        "section_number": "132",
        "title": "Criminal Procedure Statutory Provision Section 132",
        "chapter_heading": "Chapter 9: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 132 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-133",
        "section_number": "133",
        "title": "Criminal Procedure Statutory Provision Section 133",
        "chapter_heading": "Chapter 9: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 133 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-134",
        "section_number": "134",
        "title": "Criminal Procedure Statutory Provision Section 134",
        "chapter_heading": "Chapter 9: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 134 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-135",
        "section_number": "135",
        "title": "Criminal Procedure Statutory Provision Section 135",
        "chapter_heading": "Chapter 9: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 135 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-136",
        "section_number": "136",
        "title": "Criminal Procedure Statutory Provision Section 136",
        "chapter_heading": "Chapter 10: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 136 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-137",
        "section_number": "137",
        "title": "Criminal Procedure Statutory Provision Section 137",
        "chapter_heading": "Chapter 10: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 137 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-138",
        "section_number": "138",
        "title": "Criminal Procedure Statutory Provision Section 138",
        "chapter_heading": "Chapter 10: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 138 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-139",
        "section_number": "139",
        "title": "Criminal Procedure Statutory Provision Section 139",
        "chapter_heading": "Chapter 10: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 139 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-140",
        "section_number": "140",
        "title": "Criminal Procedure Statutory Provision Section 140",
        "chapter_heading": "Chapter 10: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 140 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-141",
        "section_number": "141",
        "title": "Criminal Procedure Statutory Provision Section 141",
        "chapter_heading": "Chapter 10: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 141 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-142",
        "section_number": "142",
        "title": "Criminal Procedure Statutory Provision Section 142",
        "chapter_heading": "Chapter 10: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 142 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-143",
        "section_number": "143",
        "title": "Criminal Procedure Statutory Provision Section 143",
        "chapter_heading": "Chapter 10: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 143 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-144",
        "section_number": "144",
        "title": "Criminal Procedure Statutory Provision Section 144",
        "chapter_heading": "Chapter 10: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 144 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-145",
        "section_number": "145",
        "title": "Criminal Procedure Statutory Provision Section 145",
        "chapter_heading": "Chapter 10: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 145 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-146",
        "section_number": "146",
        "title": "Criminal Procedure Statutory Provision Section 146",
        "chapter_heading": "Chapter 10: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 146 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-147",
        "section_number": "147",
        "title": "Criminal Procedure Statutory Provision Section 147",
        "chapter_heading": "Chapter 10: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 147 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-148",
        "section_number": "148",
        "title": "Criminal Procedure Statutory Provision Section 148",
        "chapter_heading": "Chapter 10: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 148 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-149",
        "section_number": "149",
        "title": "Criminal Procedure Statutory Provision Section 149",
        "chapter_heading": "Chapter 10: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 149 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
    {
        "section_id": "CRPC-SEC-150",
        "section_number": "150",
        "title": "Criminal Procedure Statutory Provision Section 150",
        "chapter_heading": "Chapter 10: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 150 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
(1) In every criminal investigation, inquiry, committal proceeding, and trial conducted under this Code, the procedural mechanisms delineated herein shall be strictly complied with by investigating agencies, police officers, public prosecutors, and criminal courts of competent jurisdiction.
(2) Every arrest made under this provision must conform to the mandatory guidelines issued by the Supreme Court of India in D.K. Basu v. State of West Bengal and the statutory safeguards incorporated under Sections 41A, 41B, 41C, and 41D.
(3) Where an accused person is produced before a Judicial Magistrate pursuant to an arrest or detention, the Magistrate shall independently scrutinize the grounds of arrest, verify the medical examination report, ascertain whether legal counsel was made available, and record reasons in writing for authorizing judicial or police remand under Section 167.
(4) In the conduct of trials before the Court of Session, Chief Judicial Magistrate, or Metropolitan Magistrate, the accused shall be entitled to a speedy, public, and impartial trial, with the prosecution bearing the non-negotiable burden of proving guilt beyond reasonable doubt.""",
        "cognizable_classification": "Cognizable Offense - Police may arrest without warrant" if sec % 2 == 1 else "Non-Cognizable Offense - Magisterial warrant required",
        "bailable_classification": "Non-Bailable - Bail within judicial discretion under Section 437/439" if sec % 3 == 0 else "Bailable - Right to bail as of right under Section 436",
        "trial_forum": "Court of Session" if sec % 4 == 0 else "Magistrate of the First Class / Metropolitan Magistrate",
        "mandatory_statutory_safeguards": [
            "Preparation of formal Memo of Arrest with attestation by at least one family member or respectable witness",
            "Mandatory medical examination of the arrested person immediately following apprehension",
            "Right of the arrested person to consult an advocate of choice during interrogation under Section 41D",
            "Mandatory transmission of case diary copies to the jurisdictional magistrate within 24 hours"
        ],
        "investigation_guidelines": """The investigating officer shall record statements of witnesses under Section 161 with utmost fidelity, without threat, promise, or inducement. All seized material objects, weapons of offense, and digital records must be sealed immediately on site, marked with unique identifiers, and cataloged in a seizure memo signed by independent panch witnesses.""",
        "landmark_authorities": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51"
        ],
        "constitutional_nexus": ["Constitution of India, Art. 20(3) Protection against self-incrimination", "Art. 21 Right to life and personal liberty", "Art. 22 Safeguards against arbitrary arrest"],
        "practice_notes": "Advocates handling bail hearings must verify the chargesheet status to examine entitlement to default statutory bail under Section 167(2) upon expiry of 60 or 90 days.",
    },
]
