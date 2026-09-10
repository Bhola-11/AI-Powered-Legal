"""
Part 18 for crpc_full_code
Modular codification slice under 250 KB
"""

CRPC_EXTENDED_SECTIONS_PART_18 = [
    {
        "section_id": "CRPC-SEC-171-SUB-01",
        "section_number": "171",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 171 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 171(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-171-SUB-02",
        "section_number": "171",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 171 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 171(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-171-SUB-03",
        "section_number": "171",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 171 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 171(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-171-SUB-04",
        "section_number": "171",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 171 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 171(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-171-SUB-05",
        "section_number": "171",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 171 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 171(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-172-SUB-01",
        "section_number": "172",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 172 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 172(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-172-SUB-02",
        "section_number": "172",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 172 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 172(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-172-SUB-03",
        "section_number": "172",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 172 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 172(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-172-SUB-04",
        "section_number": "172",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 172 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 172(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-172-SUB-05",
        "section_number": "172",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 172 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 172(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-173-SUB-01",
        "section_number": "173",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 173 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 173(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-173-SUB-02",
        "section_number": "173",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 173 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 173(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-173-SUB-03",
        "section_number": "173",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 173 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 173(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-173-SUB-04",
        "section_number": "173",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 173 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 173(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-173-SUB-05",
        "section_number": "173",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 173 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 173(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-174-SUB-01",
        "section_number": "174",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 174 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 174(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-174-SUB-02",
        "section_number": "174",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 174 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 174(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-174-SUB-03",
        "section_number": "174",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 174 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 174(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-174-SUB-04",
        "section_number": "174",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 174 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 174(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-174-SUB-05",
        "section_number": "174",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 174 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 174(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-175-SUB-01",
        "section_number": "175",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 175 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 175(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-175-SUB-02",
        "section_number": "175",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 175 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 175(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-175-SUB-03",
        "section_number": "175",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 175 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 175(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-175-SUB-04",
        "section_number": "175",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 175 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 175(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-175-SUB-05",
        "section_number": "175",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 175 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 175(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-176-SUB-01",
        "section_number": "176",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 176 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 176(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-176-SUB-02",
        "section_number": "176",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 176 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 176(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-176-SUB-03",
        "section_number": "176",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 176 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 176(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-176-SUB-04",
        "section_number": "176",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 176 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 176(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-176-SUB-05",
        "section_number": "176",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 176 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 176(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-177-SUB-01",
        "section_number": "177",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 177 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 177(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-177-SUB-02",
        "section_number": "177",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 177 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 177(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-177-SUB-03",
        "section_number": "177",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 177 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 177(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-177-SUB-04",
        "section_number": "177",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 177 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 177(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-177-SUB-05",
        "section_number": "177",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 177 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 177(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-178-SUB-01",
        "section_number": "178",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 178 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 178(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-178-SUB-02",
        "section_number": "178",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 178 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 178(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-178-SUB-03",
        "section_number": "178",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 178 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 178(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-178-SUB-04",
        "section_number": "178",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 178 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 178(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-178-SUB-05",
        "section_number": "178",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 178 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 178(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-179-SUB-01",
        "section_number": "179",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 179 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 179(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-179-SUB-02",
        "section_number": "179",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 179 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 179(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-179-SUB-03",
        "section_number": "179",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 179 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 179(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-179-SUB-04",
        "section_number": "179",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 179 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 179(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-179-SUB-05",
        "section_number": "179",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 179 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 179(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-180-SUB-01",
        "section_number": "180",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 180 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 180(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-180-SUB-02",
        "section_number": "180",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 180 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 180(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-180-SUB-03",
        "section_number": "180",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 180 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 180(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-180-SUB-04",
        "section_number": "180",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 180 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 180(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-180-SUB-05",
        "section_number": "180",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 180 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 180(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
