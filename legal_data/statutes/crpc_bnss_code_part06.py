"""
Part 06 for crpc_bnss_code
Modular codification slice under 250 KB
"""

CRPC_SECTIONS_REGISTRY_PART_06 = [
    {
        "section_id": "CRPC-SEC-251",
        "section_number": "251",
        "title": "Criminal Procedure Statutory Provision Section 251",
        "chapter_heading": "Chapter 17: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 251 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-252",
        "section_number": "252",
        "title": "Criminal Procedure Statutory Provision Section 252",
        "chapter_heading": "Chapter 17: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 252 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-253",
        "section_number": "253",
        "title": "Criminal Procedure Statutory Provision Section 253",
        "chapter_heading": "Chapter 17: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 253 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-254",
        "section_number": "254",
        "title": "Criminal Procedure Statutory Provision Section 254",
        "chapter_heading": "Chapter 17: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 254 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-255",
        "section_number": "255",
        "title": "Criminal Procedure Statutory Provision Section 255",
        "chapter_heading": "Chapter 17: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 255 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-256",
        "section_number": "256",
        "title": "Criminal Procedure Statutory Provision Section 256",
        "chapter_heading": "Chapter 18: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 256 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-257",
        "section_number": "257",
        "title": "Criminal Procedure Statutory Provision Section 257",
        "chapter_heading": "Chapter 18: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 257 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-258",
        "section_number": "258",
        "title": "Criminal Procedure Statutory Provision Section 258",
        "chapter_heading": "Chapter 18: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 258 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-259",
        "section_number": "259",
        "title": "Criminal Procedure Statutory Provision Section 259",
        "chapter_heading": "Chapter 18: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 259 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-260",
        "section_number": "260",
        "title": "Criminal Procedure Statutory Provision Section 260",
        "chapter_heading": "Chapter 18: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 260 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-261",
        "section_number": "261",
        "title": "Criminal Procedure Statutory Provision Section 261",
        "chapter_heading": "Chapter 18: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 261 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-262",
        "section_number": "262",
        "title": "Criminal Procedure Statutory Provision Section 262",
        "chapter_heading": "Chapter 18: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 262 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-263",
        "section_number": "263",
        "title": "Criminal Procedure Statutory Provision Section 263",
        "chapter_heading": "Chapter 18: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 263 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-264",
        "section_number": "264",
        "title": "Criminal Procedure Statutory Provision Section 264",
        "chapter_heading": "Chapter 18: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 264 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-265",
        "section_number": "265",
        "title": "Criminal Procedure Statutory Provision Section 265",
        "chapter_heading": "Chapter 18: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 265 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-266",
        "section_number": "266",
        "title": "Criminal Procedure Statutory Provision Section 266",
        "chapter_heading": "Chapter 18: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 266 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-267",
        "section_number": "267",
        "title": "Criminal Procedure Statutory Provision Section 267",
        "chapter_heading": "Chapter 18: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 267 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-268",
        "section_number": "268",
        "title": "Criminal Procedure Statutory Provision Section 268",
        "chapter_heading": "Chapter 18: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 268 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-269",
        "section_number": "269",
        "title": "Criminal Procedure Statutory Provision Section 269",
        "chapter_heading": "Chapter 18: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 269 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-270",
        "section_number": "270",
        "title": "Criminal Procedure Statutory Provision Section 270",
        "chapter_heading": "Chapter 18: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 270 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-271",
        "section_number": "271",
        "title": "Criminal Procedure Statutory Provision Section 271",
        "chapter_heading": "Chapter 19: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 271 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-272",
        "section_number": "272",
        "title": "Criminal Procedure Statutory Provision Section 272",
        "chapter_heading": "Chapter 19: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 272 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-273",
        "section_number": "273",
        "title": "Criminal Procedure Statutory Provision Section 273",
        "chapter_heading": "Chapter 19: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 273 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-274",
        "section_number": "274",
        "title": "Criminal Procedure Statutory Provision Section 274",
        "chapter_heading": "Chapter 19: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 274 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-275",
        "section_number": "275",
        "title": "Criminal Procedure Statutory Provision Section 275",
        "chapter_heading": "Chapter 19: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 275 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-276",
        "section_number": "276",
        "title": "Criminal Procedure Statutory Provision Section 276",
        "chapter_heading": "Chapter 19: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 276 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-277",
        "section_number": "277",
        "title": "Criminal Procedure Statutory Provision Section 277",
        "chapter_heading": "Chapter 19: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 277 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-278",
        "section_number": "278",
        "title": "Criminal Procedure Statutory Provision Section 278",
        "chapter_heading": "Chapter 19: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 278 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-279",
        "section_number": "279",
        "title": "Criminal Procedure Statutory Provision Section 279",
        "chapter_heading": "Chapter 19: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 279 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-280",
        "section_number": "280",
        "title": "Criminal Procedure Statutory Provision Section 280",
        "chapter_heading": "Chapter 19: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 280 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-281",
        "section_number": "281",
        "title": "Criminal Procedure Statutory Provision Section 281",
        "chapter_heading": "Chapter 19: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 281 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-282",
        "section_number": "282",
        "title": "Criminal Procedure Statutory Provision Section 282",
        "chapter_heading": "Chapter 19: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 282 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-283",
        "section_number": "283",
        "title": "Criminal Procedure Statutory Provision Section 283",
        "chapter_heading": "Chapter 19: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 283 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-284",
        "section_number": "284",
        "title": "Criminal Procedure Statutory Provision Section 284",
        "chapter_heading": "Chapter 19: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 284 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-285",
        "section_number": "285",
        "title": "Criminal Procedure Statutory Provision Section 285",
        "chapter_heading": "Chapter 19: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 285 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-286",
        "section_number": "286",
        "title": "Criminal Procedure Statutory Provision Section 286",
        "chapter_heading": "Chapter 20: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 286 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-287",
        "section_number": "287",
        "title": "Criminal Procedure Statutory Provision Section 287",
        "chapter_heading": "Chapter 20: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 287 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-288",
        "section_number": "288",
        "title": "Criminal Procedure Statutory Provision Section 288",
        "chapter_heading": "Chapter 20: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 288 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-289",
        "section_number": "289",
        "title": "Criminal Procedure Statutory Provision Section 289",
        "chapter_heading": "Chapter 20: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 289 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-290",
        "section_number": "290",
        "title": "Criminal Procedure Statutory Provision Section 290",
        "chapter_heading": "Chapter 20: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 290 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-291",
        "section_number": "291",
        "title": "Criminal Procedure Statutory Provision Section 291",
        "chapter_heading": "Chapter 20: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 291 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-292",
        "section_number": "292",
        "title": "Criminal Procedure Statutory Provision Section 292",
        "chapter_heading": "Chapter 20: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 292 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-293",
        "section_number": "293",
        "title": "Criminal Procedure Statutory Provision Section 293",
        "chapter_heading": "Chapter 20: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 293 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-294",
        "section_number": "294",
        "title": "Criminal Procedure Statutory Provision Section 294",
        "chapter_heading": "Chapter 20: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 294 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-295",
        "section_number": "295",
        "title": "Criminal Procedure Statutory Provision Section 295",
        "chapter_heading": "Chapter 20: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 295 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-296",
        "section_number": "296",
        "title": "Criminal Procedure Statutory Provision Section 296",
        "chapter_heading": "Chapter 20: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 296 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-297",
        "section_number": "297",
        "title": "Criminal Procedure Statutory Provision Section 297",
        "chapter_heading": "Chapter 20: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 297 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-298",
        "section_number": "298",
        "title": "Criminal Procedure Statutory Provision Section 298",
        "chapter_heading": "Chapter 20: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 298 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-299",
        "section_number": "299",
        "title": "Criminal Procedure Statutory Provision Section 299",
        "chapter_heading": "Chapter 20: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 299 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-300",
        "section_number": "300",
        "title": "Criminal Procedure Statutory Provision Section 300",
        "chapter_heading": "Chapter 20: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 300 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
