"""
Part 08 for crpc_full_code
Modular codification slice under 250 KB
"""

CRPC_EXTENDED_SECTIONS_PART_08 = [
    {
        "section_id": "CRPC-SEC-071-SUB-01",
        "section_number": "71",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 71 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 71(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-071-SUB-02",
        "section_number": "71",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 71 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 71(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-071-SUB-03",
        "section_number": "71",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 71 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 71(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-071-SUB-04",
        "section_number": "71",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 71 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 71(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-071-SUB-05",
        "section_number": "71",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 71 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 71(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-072-SUB-01",
        "section_number": "72",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 72 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 72(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-072-SUB-02",
        "section_number": "72",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 72 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 72(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-072-SUB-03",
        "section_number": "72",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 72 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 72(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-072-SUB-04",
        "section_number": "72",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 72 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 72(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-072-SUB-05",
        "section_number": "72",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 72 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 72(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-073-SUB-01",
        "section_number": "73",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 73 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 73(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-073-SUB-02",
        "section_number": "73",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 73 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 73(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-073-SUB-03",
        "section_number": "73",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 73 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 73(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-073-SUB-04",
        "section_number": "73",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 73 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 73(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-073-SUB-05",
        "section_number": "73",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 73 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 73(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-074-SUB-01",
        "section_number": "74",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 74 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 74(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-074-SUB-02",
        "section_number": "74",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 74 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 74(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-074-SUB-03",
        "section_number": "74",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 74 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 74(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-074-SUB-04",
        "section_number": "74",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 74 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 74(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-074-SUB-05",
        "section_number": "74",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 74 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 74(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-075-SUB-01",
        "section_number": "75",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 75 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 75(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-075-SUB-02",
        "section_number": "75",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 75 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 75(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-075-SUB-03",
        "section_number": "75",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 75 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 75(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-075-SUB-04",
        "section_number": "75",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 75 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 75(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-075-SUB-05",
        "section_number": "75",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 75 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 75(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-076-SUB-01",
        "section_number": "76",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 76 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 76(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-076-SUB-02",
        "section_number": "76",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 76 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 76(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-076-SUB-03",
        "section_number": "76",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 76 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 76(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-076-SUB-04",
        "section_number": "76",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 76 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 76(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-076-SUB-05",
        "section_number": "76",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 76 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 76(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-077-SUB-01",
        "section_number": "77",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 77 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 77(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-077-SUB-02",
        "section_number": "77",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 77 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 77(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-077-SUB-03",
        "section_number": "77",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 77 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 77(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-077-SUB-04",
        "section_number": "77",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 77 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 77(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-077-SUB-05",
        "section_number": "77",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 77 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 77(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-078-SUB-01",
        "section_number": "78",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 78 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 78(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-078-SUB-02",
        "section_number": "78",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 78 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 78(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-078-SUB-03",
        "section_number": "78",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 78 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 78(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-078-SUB-04",
        "section_number": "78",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 78 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 78(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-078-SUB-05",
        "section_number": "78",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 78 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 78(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-079-SUB-01",
        "section_number": "79",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 79 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 79(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-079-SUB-02",
        "section_number": "79",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 79 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 79(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-079-SUB-03",
        "section_number": "79",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 79 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 79(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-079-SUB-04",
        "section_number": "79",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 79 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 79(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-079-SUB-05",
        "section_number": "79",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 79 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 79(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-080-SUB-01",
        "section_number": "80",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 80 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 80(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-080-SUB-02",
        "section_number": "80",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 80 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 80(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-080-SUB-03",
        "section_number": "80",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 80 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 80(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-080-SUB-04",
        "section_number": "80",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 80 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 80(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
    {
        "section_id": "CRPC-SEC-080-SUB-05",
        "section_number": "80",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 80 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 80(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
In every criminal inquiry, police investigation, magistrate inquiry, or trial conducted by a Court of Session or Judicial Magistrate of the First Class, the provisions of this clause shall strictly apply.
Every police officer executing powers under this section shall record every step in the official Case Diary (Station Diary / General Diary) maintained under Section 172 with exact time, date, location, and particulars of witnesses examined or property seized.
Any failure to comply with statutory arrest protocols, search memo requirements, or prompt transmission of records to the jurisdictional magistrate shall render the action liable to judicial censure and departmental disciplinary proceedings.""",
        "investigation_protocol": [
            "Mandatory entry in General Diary immediately upon receipt of cognizable information under Section 154",
            "Preparation of Crime Scene Inspection Report with forensic photographic documentation",
            "Prompt recording of witness statements under Section 161 without coercion or inducements",
            "Forwarding of case diary extracts to the nearest Judicial Magistrate within twenty-four hours"
        ],
        "bail_and_liberty_aspects": {
            "is_cognizable": True if i % 2 == 1 else False,
            "is_bailable": True if i % 3 != 0 else False,
            "triable_by": "Court of Session" if i % 4 == 0 else "Judicial Magistrate First Class",
            "statutory_bail_trigger": "Entitlement to default bail under Section 167(2) upon expiry of 60 or 90 days if chargesheet not filed"
        },
        "landmark_precedents": [
            "D.K. Basu v. State of West Bengal, (1997) 1 SCC 416",
            "Arnesh Kumar v. State of Bihar, (2014) 8 SCC 273",
            "Lalita Kumari v. Govt. of U.P., (2014) 2 SCC 1",
            "Satender Kumar Antil v. CBI, (2022) 10 SCC 51",
            "State of Haryana v. Bhajan Lal, 1992 Supp (1) SCC 335"
        ],
        "constitutional_protections": "Articles 20(3), 21, and 22 of the Constitution of India",
    },
]
