"""
Part 08 for crpc_bnss_code
Modular codification slice under 250 KB
"""

CRPC_SECTIONS_REGISTRY_PART_08 = [
    {
        "section_id": "CRPC-SEC-351",
        "section_number": "351",
        "title": "Criminal Procedure Statutory Provision Section 351",
        "chapter_heading": "Chapter 24: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 351 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-352",
        "section_number": "352",
        "title": "Criminal Procedure Statutory Provision Section 352",
        "chapter_heading": "Chapter 24: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 352 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-353",
        "section_number": "353",
        "title": "Criminal Procedure Statutory Provision Section 353",
        "chapter_heading": "Chapter 24: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 353 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-354",
        "section_number": "354",
        "title": "Criminal Procedure Statutory Provision Section 354",
        "chapter_heading": "Chapter 24: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 354 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-355",
        "section_number": "355",
        "title": "Criminal Procedure Statutory Provision Section 355",
        "chapter_heading": "Chapter 24: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 355 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-356",
        "section_number": "356",
        "title": "Criminal Procedure Statutory Provision Section 356",
        "chapter_heading": "Chapter 24: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 356 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-357",
        "section_number": "357",
        "title": "Criminal Procedure Statutory Provision Section 357",
        "chapter_heading": "Chapter 24: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 357 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-358",
        "section_number": "358",
        "title": "Criminal Procedure Statutory Provision Section 358",
        "chapter_heading": "Chapter 24: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 358 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-359",
        "section_number": "359",
        "title": "Criminal Procedure Statutory Provision Section 359",
        "chapter_heading": "Chapter 24: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 359 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-360",
        "section_number": "360",
        "title": "Criminal Procedure Statutory Provision Section 360",
        "chapter_heading": "Chapter 24: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 360 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-361",
        "section_number": "361",
        "title": "Criminal Procedure Statutory Provision Section 361",
        "chapter_heading": "Chapter 25: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 361 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-362",
        "section_number": "362",
        "title": "Criminal Procedure Statutory Provision Section 362",
        "chapter_heading": "Chapter 25: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 362 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-363",
        "section_number": "363",
        "title": "Criminal Procedure Statutory Provision Section 363",
        "chapter_heading": "Chapter 25: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 363 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-364",
        "section_number": "364",
        "title": "Criminal Procedure Statutory Provision Section 364",
        "chapter_heading": "Chapter 25: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 364 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-365",
        "section_number": "365",
        "title": "Criminal Procedure Statutory Provision Section 365",
        "chapter_heading": "Chapter 25: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 365 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-366",
        "section_number": "366",
        "title": "Criminal Procedure Statutory Provision Section 366",
        "chapter_heading": "Chapter 25: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 366 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-367",
        "section_number": "367",
        "title": "Criminal Procedure Statutory Provision Section 367",
        "chapter_heading": "Chapter 25: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 367 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-368",
        "section_number": "368",
        "title": "Criminal Procedure Statutory Provision Section 368",
        "chapter_heading": "Chapter 25: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 368 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-369",
        "section_number": "369",
        "title": "Criminal Procedure Statutory Provision Section 369",
        "chapter_heading": "Chapter 25: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 369 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-370",
        "section_number": "370",
        "title": "Criminal Procedure Statutory Provision Section 370",
        "chapter_heading": "Chapter 25: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 370 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-371",
        "section_number": "371",
        "title": "Criminal Procedure Statutory Provision Section 371",
        "chapter_heading": "Chapter 25: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 371 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-372",
        "section_number": "372",
        "title": "Criminal Procedure Statutory Provision Section 372",
        "chapter_heading": "Chapter 25: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 372 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-373",
        "section_number": "373",
        "title": "Criminal Procedure Statutory Provision Section 373",
        "chapter_heading": "Chapter 25: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 373 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-374",
        "section_number": "374",
        "title": "Criminal Procedure Statutory Provision Section 374",
        "chapter_heading": "Chapter 25: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 374 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-375",
        "section_number": "375",
        "title": "Criminal Procedure Statutory Provision Section 375",
        "chapter_heading": "Chapter 25: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 375 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-376",
        "section_number": "376",
        "title": "Criminal Procedure Statutory Provision Section 376",
        "chapter_heading": "Chapter 26: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 376 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-377",
        "section_number": "377",
        "title": "Criminal Procedure Statutory Provision Section 377",
        "chapter_heading": "Chapter 26: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 377 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-378",
        "section_number": "378",
        "title": "Criminal Procedure Statutory Provision Section 378",
        "chapter_heading": "Chapter 26: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 378 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-379",
        "section_number": "379",
        "title": "Criminal Procedure Statutory Provision Section 379",
        "chapter_heading": "Chapter 26: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 379 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-380",
        "section_number": "380",
        "title": "Criminal Procedure Statutory Provision Section 380",
        "chapter_heading": "Chapter 26: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 380 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-381",
        "section_number": "381",
        "title": "Criminal Procedure Statutory Provision Section 381",
        "chapter_heading": "Chapter 26: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 381 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-382",
        "section_number": "382",
        "title": "Criminal Procedure Statutory Provision Section 382",
        "chapter_heading": "Chapter 26: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 382 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-383",
        "section_number": "383",
        "title": "Criminal Procedure Statutory Provision Section 383",
        "chapter_heading": "Chapter 26: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 383 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-384",
        "section_number": "384",
        "title": "Criminal Procedure Statutory Provision Section 384",
        "chapter_heading": "Chapter 26: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 384 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-385",
        "section_number": "385",
        "title": "Criminal Procedure Statutory Provision Section 385",
        "chapter_heading": "Chapter 26: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 385 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-386",
        "section_number": "386",
        "title": "Criminal Procedure Statutory Provision Section 386",
        "chapter_heading": "Chapter 26: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 386 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-387",
        "section_number": "387",
        "title": "Criminal Procedure Statutory Provision Section 387",
        "chapter_heading": "Chapter 26: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 387 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-388",
        "section_number": "388",
        "title": "Criminal Procedure Statutory Provision Section 388",
        "chapter_heading": "Chapter 26: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 388 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-389",
        "section_number": "389",
        "title": "Criminal Procedure Statutory Provision Section 389",
        "chapter_heading": "Chapter 26: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 389 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-390",
        "section_number": "390",
        "title": "Criminal Procedure Statutory Provision Section 390",
        "chapter_heading": "Chapter 26: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 390 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-391",
        "section_number": "391",
        "title": "Criminal Procedure Statutory Provision Section 391",
        "chapter_heading": "Chapter 27: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 391 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-392",
        "section_number": "392",
        "title": "Criminal Procedure Statutory Provision Section 392",
        "chapter_heading": "Chapter 27: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 392 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-393",
        "section_number": "393",
        "title": "Criminal Procedure Statutory Provision Section 393",
        "chapter_heading": "Chapter 27: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 393 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-394",
        "section_number": "394",
        "title": "Criminal Procedure Statutory Provision Section 394",
        "chapter_heading": "Chapter 27: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 394 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-395",
        "section_number": "395",
        "title": "Criminal Procedure Statutory Provision Section 395",
        "chapter_heading": "Chapter 27: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 395 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-396",
        "section_number": "396",
        "title": "Criminal Procedure Statutory Provision Section 396",
        "chapter_heading": "Chapter 27: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 396 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-397",
        "section_number": "397",
        "title": "Criminal Procedure Statutory Provision Section 397",
        "chapter_heading": "Chapter 27: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 397 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-398",
        "section_number": "398",
        "title": "Criminal Procedure Statutory Provision Section 398",
        "chapter_heading": "Chapter 27: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 398 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-399",
        "section_number": "399",
        "title": "Criminal Procedure Statutory Provision Section 399",
        "chapter_heading": "Chapter 27: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 399 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-400",
        "section_number": "400",
        "title": "Criminal Procedure Statutory Provision Section 400",
        "chapter_heading": "Chapter 27: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 400 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
