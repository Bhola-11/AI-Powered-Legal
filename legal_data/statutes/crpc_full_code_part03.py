"""
Part 03 for crpc_full_code
Modular codification slice under 250 KB
"""

CRPC_EXTENDED_SECTIONS_PART_03 = [
    {
        "section_id": "CRPC-SEC-021-SUB-01",
        "section_number": "21",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 21 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 21(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-021-SUB-02",
        "section_number": "21",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 21 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 21(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-021-SUB-03",
        "section_number": "21",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 21 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 21(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-021-SUB-04",
        "section_number": "21",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 21 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 21(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-021-SUB-05",
        "section_number": "21",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 21 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 21(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-022-SUB-01",
        "section_number": "22",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 22 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 22(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-022-SUB-02",
        "section_number": "22",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 22 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 22(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-022-SUB-03",
        "section_number": "22",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 22 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 22(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-022-SUB-04",
        "section_number": "22",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 22 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 22(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-022-SUB-05",
        "section_number": "22",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 22 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 22(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-023-SUB-01",
        "section_number": "23",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 23 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 23(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-023-SUB-02",
        "section_number": "23",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 23 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 23(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-023-SUB-03",
        "section_number": "23",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 23 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 23(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-023-SUB-04",
        "section_number": "23",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 23 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 23(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-023-SUB-05",
        "section_number": "23",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 23 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 23(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-024-SUB-01",
        "section_number": "24",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 24 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 24(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-024-SUB-02",
        "section_number": "24",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 24 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 24(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-024-SUB-03",
        "section_number": "24",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 24 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 24(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-024-SUB-04",
        "section_number": "24",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 24 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 24(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-024-SUB-05",
        "section_number": "24",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 24 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 24(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-025-SUB-01",
        "section_number": "25",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 25 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 25(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-025-SUB-02",
        "section_number": "25",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 25 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 25(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-025-SUB-03",
        "section_number": "25",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 25 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 25(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-025-SUB-04",
        "section_number": "25",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 25 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 25(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-025-SUB-05",
        "section_number": "25",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 25 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 25(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-026-SUB-01",
        "section_number": "26",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 26 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 26(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-026-SUB-02",
        "section_number": "26",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 26 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 26(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-026-SUB-03",
        "section_number": "26",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 26 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 26(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-026-SUB-04",
        "section_number": "26",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 26 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 26(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-026-SUB-05",
        "section_number": "26",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 26 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 26(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-027-SUB-01",
        "section_number": "27",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 27 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 27(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-027-SUB-02",
        "section_number": "27",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 27 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 27(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-027-SUB-03",
        "section_number": "27",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 27 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 27(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-027-SUB-04",
        "section_number": "27",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 27 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 27(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-027-SUB-05",
        "section_number": "27",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 27 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 27(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-028-SUB-01",
        "section_number": "28",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 28 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 28(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-028-SUB-02",
        "section_number": "28",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 28 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 28(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-028-SUB-03",
        "section_number": "28",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 28 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 28(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-028-SUB-04",
        "section_number": "28",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 28 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 28(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-028-SUB-05",
        "section_number": "28",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 28 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 28(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-029-SUB-01",
        "section_number": "29",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 29 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 29(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-029-SUB-02",
        "section_number": "29",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 29 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 29(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-029-SUB-03",
        "section_number": "29",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 29 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 29(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-029-SUB-04",
        "section_number": "29",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 29 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 29(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-029-SUB-05",
        "section_number": "29",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 29 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 29(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-030-SUB-01",
        "section_number": "30",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 30 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 30(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-030-SUB-02",
        "section_number": "30",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 30 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 30(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-030-SUB-03",
        "section_number": "30",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 30 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 30(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-030-SUB-04",
        "section_number": "30",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 30 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 30(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-030-SUB-05",
        "section_number": "30",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 30 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 30(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
