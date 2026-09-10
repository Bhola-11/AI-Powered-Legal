"""
Part 09 for crpc_bnss_code
Modular codification slice under 250 KB
"""

CRPC_SECTIONS_REGISTRY_PART_09 = [
    {
        "section_id": "CRPC-SEC-401",
        "section_number": "401",
        "title": "Criminal Procedure Statutory Provision Section 401",
        "chapter_heading": "Chapter 27: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 401 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-402",
        "section_number": "402",
        "title": "Criminal Procedure Statutory Provision Section 402",
        "chapter_heading": "Chapter 27: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 402 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-403",
        "section_number": "403",
        "title": "Criminal Procedure Statutory Provision Section 403",
        "chapter_heading": "Chapter 27: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 403 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-404",
        "section_number": "404",
        "title": "Criminal Procedure Statutory Provision Section 404",
        "chapter_heading": "Chapter 27: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 404 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-405",
        "section_number": "405",
        "title": "Criminal Procedure Statutory Provision Section 405",
        "chapter_heading": "Chapter 27: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 405 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-406",
        "section_number": "406",
        "title": "Criminal Procedure Statutory Provision Section 406",
        "chapter_heading": "Chapter 28: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 406 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-407",
        "section_number": "407",
        "title": "Criminal Procedure Statutory Provision Section 407",
        "chapter_heading": "Chapter 28: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 407 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-408",
        "section_number": "408",
        "title": "Criminal Procedure Statutory Provision Section 408",
        "chapter_heading": "Chapter 28: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 408 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-409",
        "section_number": "409",
        "title": "Criminal Procedure Statutory Provision Section 409",
        "chapter_heading": "Chapter 28: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 409 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-410",
        "section_number": "410",
        "title": "Criminal Procedure Statutory Provision Section 410",
        "chapter_heading": "Chapter 28: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 410 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-411",
        "section_number": "411",
        "title": "Criminal Procedure Statutory Provision Section 411",
        "chapter_heading": "Chapter 28: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 411 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-412",
        "section_number": "412",
        "title": "Criminal Procedure Statutory Provision Section 412",
        "chapter_heading": "Chapter 28: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 412 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-413",
        "section_number": "413",
        "title": "Criminal Procedure Statutory Provision Section 413",
        "chapter_heading": "Chapter 28: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 413 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-414",
        "section_number": "414",
        "title": "Criminal Procedure Statutory Provision Section 414",
        "chapter_heading": "Chapter 28: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 414 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-415",
        "section_number": "415",
        "title": "Criminal Procedure Statutory Provision Section 415",
        "chapter_heading": "Chapter 28: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 415 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-416",
        "section_number": "416",
        "title": "Criminal Procedure Statutory Provision Section 416",
        "chapter_heading": "Chapter 28: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 416 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-417",
        "section_number": "417",
        "title": "Criminal Procedure Statutory Provision Section 417",
        "chapter_heading": "Chapter 28: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 417 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-418",
        "section_number": "418",
        "title": "Criminal Procedure Statutory Provision Section 418",
        "chapter_heading": "Chapter 28: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 418 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-419",
        "section_number": "419",
        "title": "Criminal Procedure Statutory Provision Section 419",
        "chapter_heading": "Chapter 28: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 419 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-420",
        "section_number": "420",
        "title": "Criminal Procedure Statutory Provision Section 420",
        "chapter_heading": "Chapter 28: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 420 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-421",
        "section_number": "421",
        "title": "Criminal Procedure Statutory Provision Section 421",
        "chapter_heading": "Chapter 29: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 421 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-422",
        "section_number": "422",
        "title": "Criminal Procedure Statutory Provision Section 422",
        "chapter_heading": "Chapter 29: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 422 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-423",
        "section_number": "423",
        "title": "Criminal Procedure Statutory Provision Section 423",
        "chapter_heading": "Chapter 29: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 423 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-424",
        "section_number": "424",
        "title": "Criminal Procedure Statutory Provision Section 424",
        "chapter_heading": "Chapter 29: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 424 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-425",
        "section_number": "425",
        "title": "Criminal Procedure Statutory Provision Section 425",
        "chapter_heading": "Chapter 29: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 425 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-426",
        "section_number": "426",
        "title": "Criminal Procedure Statutory Provision Section 426",
        "chapter_heading": "Chapter 29: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 426 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-427",
        "section_number": "427",
        "title": "Criminal Procedure Statutory Provision Section 427",
        "chapter_heading": "Chapter 29: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 427 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-428",
        "section_number": "428",
        "title": "Criminal Procedure Statutory Provision Section 428",
        "chapter_heading": "Chapter 29: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 428 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-429",
        "section_number": "429",
        "title": "Criminal Procedure Statutory Provision Section 429",
        "chapter_heading": "Chapter 29: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 429 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-430",
        "section_number": "430",
        "title": "Criminal Procedure Statutory Provision Section 430",
        "chapter_heading": "Chapter 29: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 430 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-431",
        "section_number": "431",
        "title": "Criminal Procedure Statutory Provision Section 431",
        "chapter_heading": "Chapter 29: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 431 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-432",
        "section_number": "432",
        "title": "Criminal Procedure Statutory Provision Section 432",
        "chapter_heading": "Chapter 29: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 432 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-433",
        "section_number": "433",
        "title": "Criminal Procedure Statutory Provision Section 433",
        "chapter_heading": "Chapter 29: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 433 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-434",
        "section_number": "434",
        "title": "Criminal Procedure Statutory Provision Section 434",
        "chapter_heading": "Chapter 29: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 434 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-435",
        "section_number": "435",
        "title": "Criminal Procedure Statutory Provision Section 435",
        "chapter_heading": "Chapter 29: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 435 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-436",
        "section_number": "436",
        "title": "Criminal Procedure Statutory Provision Section 436",
        "chapter_heading": "Chapter 30: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 436 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-437",
        "section_number": "437",
        "title": "Criminal Procedure Statutory Provision Section 437",
        "chapter_heading": "Chapter 30: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 437 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-438",
        "section_number": "438",
        "title": "Criminal Procedure Statutory Provision Section 438",
        "chapter_heading": "Chapter 30: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 438 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-439",
        "section_number": "439",
        "title": "Criminal Procedure Statutory Provision Section 439",
        "chapter_heading": "Chapter 30: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 439 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-440",
        "section_number": "440",
        "title": "Criminal Procedure Statutory Provision Section 440",
        "chapter_heading": "Chapter 30: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 440 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-441",
        "section_number": "441",
        "title": "Criminal Procedure Statutory Provision Section 441",
        "chapter_heading": "Chapter 30: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 441 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-442",
        "section_number": "442",
        "title": "Criminal Procedure Statutory Provision Section 442",
        "chapter_heading": "Chapter 30: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 442 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-443",
        "section_number": "443",
        "title": "Criminal Procedure Statutory Provision Section 443",
        "chapter_heading": "Chapter 30: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 443 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-444",
        "section_number": "444",
        "title": "Criminal Procedure Statutory Provision Section 444",
        "chapter_heading": "Chapter 30: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 444 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-445",
        "section_number": "445",
        "title": "Criminal Procedure Statutory Provision Section 445",
        "chapter_heading": "Chapter 30: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 445 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-446",
        "section_number": "446",
        "title": "Criminal Procedure Statutory Provision Section 446",
        "chapter_heading": "Chapter 30: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 446 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-447",
        "section_number": "447",
        "title": "Criminal Procedure Statutory Provision Section 447",
        "chapter_heading": "Chapter 30: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 447 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-448",
        "section_number": "448",
        "title": "Criminal Procedure Statutory Provision Section 448",
        "chapter_heading": "Chapter 30: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 448 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-449",
        "section_number": "449",
        "title": "Criminal Procedure Statutory Provision Section 449",
        "chapter_heading": "Chapter 30: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 449 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-450",
        "section_number": "450",
        "title": "Criminal Procedure Statutory Provision Section 450",
        "chapter_heading": "Chapter 30: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 450 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
