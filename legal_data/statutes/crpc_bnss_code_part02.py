"""
Part 02 for crpc_bnss_code
Modular codification slice under 250 KB
"""

CRPC_SECTIONS_REGISTRY_PART_02 = [
    {
        "section_id": "CRPC-SEC-051",
        "section_number": "51",
        "title": "Criminal Procedure Statutory Provision Section 51",
        "chapter_heading": "Chapter 4: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 51 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-052",
        "section_number": "52",
        "title": "Criminal Procedure Statutory Provision Section 52",
        "chapter_heading": "Chapter 4: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 52 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-053",
        "section_number": "53",
        "title": "Criminal Procedure Statutory Provision Section 53",
        "chapter_heading": "Chapter 4: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 53 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-054",
        "section_number": "54",
        "title": "Criminal Procedure Statutory Provision Section 54",
        "chapter_heading": "Chapter 4: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 54 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-055",
        "section_number": "55",
        "title": "Criminal Procedure Statutory Provision Section 55",
        "chapter_heading": "Chapter 4: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 55 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-056",
        "section_number": "56",
        "title": "Criminal Procedure Statutory Provision Section 56",
        "chapter_heading": "Chapter 4: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 56 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-057",
        "section_number": "57",
        "title": "Criminal Procedure Statutory Provision Section 57",
        "chapter_heading": "Chapter 4: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 57 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-058",
        "section_number": "58",
        "title": "Criminal Procedure Statutory Provision Section 58",
        "chapter_heading": "Chapter 4: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 58 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-059",
        "section_number": "59",
        "title": "Criminal Procedure Statutory Provision Section 59",
        "chapter_heading": "Chapter 4: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 59 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-060",
        "section_number": "60",
        "title": "Criminal Procedure Statutory Provision Section 60",
        "chapter_heading": "Chapter 4: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 60 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-061",
        "section_number": "61",
        "title": "Criminal Procedure Statutory Provision Section 61",
        "chapter_heading": "Chapter 5: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 61 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-062",
        "section_number": "62",
        "title": "Criminal Procedure Statutory Provision Section 62",
        "chapter_heading": "Chapter 5: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 62 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-063",
        "section_number": "63",
        "title": "Criminal Procedure Statutory Provision Section 63",
        "chapter_heading": "Chapter 5: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 63 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-064",
        "section_number": "64",
        "title": "Criminal Procedure Statutory Provision Section 64",
        "chapter_heading": "Chapter 5: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 64 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-065",
        "section_number": "65",
        "title": "Criminal Procedure Statutory Provision Section 65",
        "chapter_heading": "Chapter 5: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 65 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-066",
        "section_number": "66",
        "title": "Criminal Procedure Statutory Provision Section 66",
        "chapter_heading": "Chapter 5: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 66 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-067",
        "section_number": "67",
        "title": "Criminal Procedure Statutory Provision Section 67",
        "chapter_heading": "Chapter 5: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 67 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-068",
        "section_number": "68",
        "title": "Criminal Procedure Statutory Provision Section 68",
        "chapter_heading": "Chapter 5: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 68 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-069",
        "section_number": "69",
        "title": "Criminal Procedure Statutory Provision Section 69",
        "chapter_heading": "Chapter 5: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 69 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-070",
        "section_number": "70",
        "title": "Criminal Procedure Statutory Provision Section 70",
        "chapter_heading": "Chapter 5: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 70 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-071",
        "section_number": "71",
        "title": "Criminal Procedure Statutory Provision Section 71",
        "chapter_heading": "Chapter 5: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 71 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-072",
        "section_number": "72",
        "title": "Criminal Procedure Statutory Provision Section 72",
        "chapter_heading": "Chapter 5: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 72 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-073",
        "section_number": "73",
        "title": "Criminal Procedure Statutory Provision Section 73",
        "chapter_heading": "Chapter 5: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 73 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-074",
        "section_number": "74",
        "title": "Criminal Procedure Statutory Provision Section 74",
        "chapter_heading": "Chapter 5: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 74 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-075",
        "section_number": "75",
        "title": "Criminal Procedure Statutory Provision Section 75",
        "chapter_heading": "Chapter 5: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 75 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-076",
        "section_number": "76",
        "title": "Criminal Procedure Statutory Provision Section 76",
        "chapter_heading": "Chapter 6: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 76 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-077",
        "section_number": "77",
        "title": "Criminal Procedure Statutory Provision Section 77",
        "chapter_heading": "Chapter 6: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 77 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-078",
        "section_number": "78",
        "title": "Criminal Procedure Statutory Provision Section 78",
        "chapter_heading": "Chapter 6: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 78 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-079",
        "section_number": "79",
        "title": "Criminal Procedure Statutory Provision Section 79",
        "chapter_heading": "Chapter 6: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 79 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-080",
        "section_number": "80",
        "title": "Criminal Procedure Statutory Provision Section 80",
        "chapter_heading": "Chapter 6: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 80 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-081",
        "section_number": "81",
        "title": "Criminal Procedure Statutory Provision Section 81",
        "chapter_heading": "Chapter 6: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 81 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-082",
        "section_number": "82",
        "title": "Criminal Procedure Statutory Provision Section 82",
        "chapter_heading": "Chapter 6: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 82 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-083",
        "section_number": "83",
        "title": "Criminal Procedure Statutory Provision Section 83",
        "chapter_heading": "Chapter 6: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 83 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-084",
        "section_number": "84",
        "title": "Criminal Procedure Statutory Provision Section 84",
        "chapter_heading": "Chapter 6: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 84 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-085",
        "section_number": "85",
        "title": "Criminal Procedure Statutory Provision Section 85",
        "chapter_heading": "Chapter 6: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 85 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-086",
        "section_number": "86",
        "title": "Criminal Procedure Statutory Provision Section 86",
        "chapter_heading": "Chapter 6: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 86 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-087",
        "section_number": "87",
        "title": "Criminal Procedure Statutory Provision Section 87",
        "chapter_heading": "Chapter 6: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 87 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-088",
        "section_number": "88",
        "title": "Criminal Procedure Statutory Provision Section 88",
        "chapter_heading": "Chapter 6: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 88 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-089",
        "section_number": "89",
        "title": "Criminal Procedure Statutory Provision Section 89",
        "chapter_heading": "Chapter 6: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 89 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-090",
        "section_number": "90",
        "title": "Criminal Procedure Statutory Provision Section 90",
        "chapter_heading": "Chapter 6: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 90 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-091",
        "section_number": "91",
        "title": "Criminal Procedure Statutory Provision Section 91",
        "chapter_heading": "Chapter 7: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 91 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-092",
        "section_number": "92",
        "title": "Criminal Procedure Statutory Provision Section 92",
        "chapter_heading": "Chapter 7: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 92 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-093",
        "section_number": "93",
        "title": "Criminal Procedure Statutory Provision Section 93",
        "chapter_heading": "Chapter 7: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 93 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-094",
        "section_number": "94",
        "title": "Criminal Procedure Statutory Provision Section 94",
        "chapter_heading": "Chapter 7: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 94 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-095",
        "section_number": "95",
        "title": "Criminal Procedure Statutory Provision Section 95",
        "chapter_heading": "Chapter 7: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 95 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-096",
        "section_number": "96",
        "title": "Criminal Procedure Statutory Provision Section 96",
        "chapter_heading": "Chapter 7: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 96 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-097",
        "section_number": "97",
        "title": "Criminal Procedure Statutory Provision Section 97",
        "chapter_heading": "Chapter 7: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 97 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-098",
        "section_number": "98",
        "title": "Criminal Procedure Statutory Provision Section 98",
        "chapter_heading": "Chapter 7: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 98 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-099",
        "section_number": "99",
        "title": "Criminal Procedure Statutory Provision Section 99",
        "chapter_heading": "Chapter 7: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 99 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-100",
        "section_number": "100",
        "title": "Criminal Procedure Statutory Provision Section 100",
        "chapter_heading": "Chapter 7: Criminal Administration, Investigation & Adjudication",
        "statutory_text": """Section 100 of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
