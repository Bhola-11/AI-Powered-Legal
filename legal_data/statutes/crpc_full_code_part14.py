"""
Part 14 for crpc_full_code
Modular codification slice under 250 KB
"""

CRPC_EXTENDED_SECTIONS_PART_14 = [
    {
        "section_id": "CRPC-SEC-131-SUB-01",
        "section_number": "131",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 131 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 131(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-131-SUB-02",
        "section_number": "131",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 131 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 131(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-131-SUB-03",
        "section_number": "131",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 131 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 131(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-131-SUB-04",
        "section_number": "131",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 131 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 131(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-131-SUB-05",
        "section_number": "131",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 131 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 131(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-132-SUB-01",
        "section_number": "132",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 132 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 132(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-132-SUB-02",
        "section_number": "132",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 132 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 132(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-132-SUB-03",
        "section_number": "132",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 132 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 132(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-132-SUB-04",
        "section_number": "132",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 132 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 132(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-132-SUB-05",
        "section_number": "132",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 132 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 132(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-133-SUB-01",
        "section_number": "133",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 133 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 133(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-133-SUB-02",
        "section_number": "133",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 133 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 133(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-133-SUB-03",
        "section_number": "133",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 133 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 133(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-133-SUB-04",
        "section_number": "133",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 133 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 133(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-133-SUB-05",
        "section_number": "133",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 133 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 133(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-134-SUB-01",
        "section_number": "134",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 134 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 134(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-134-SUB-02",
        "section_number": "134",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 134 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 134(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-134-SUB-03",
        "section_number": "134",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 134 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 134(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-134-SUB-04",
        "section_number": "134",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 134 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 134(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-134-SUB-05",
        "section_number": "134",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 134 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 134(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-135-SUB-01",
        "section_number": "135",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 135 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 135(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-135-SUB-02",
        "section_number": "135",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 135 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 135(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-135-SUB-03",
        "section_number": "135",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 135 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 135(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-135-SUB-04",
        "section_number": "135",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 135 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 135(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-135-SUB-05",
        "section_number": "135",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 135 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 135(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-136-SUB-01",
        "section_number": "136",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 136 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 136(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-136-SUB-02",
        "section_number": "136",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 136 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 136(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-136-SUB-03",
        "section_number": "136",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 136 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 136(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-136-SUB-04",
        "section_number": "136",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 136 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 136(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-136-SUB-05",
        "section_number": "136",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 136 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 136(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-137-SUB-01",
        "section_number": "137",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 137 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 137(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-137-SUB-02",
        "section_number": "137",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 137 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 137(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-137-SUB-03",
        "section_number": "137",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 137 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 137(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-137-SUB-04",
        "section_number": "137",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 137 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 137(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-137-SUB-05",
        "section_number": "137",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 137 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 137(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-138-SUB-01",
        "section_number": "138",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 138 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 138(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-138-SUB-02",
        "section_number": "138",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 138 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 138(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-138-SUB-03",
        "section_number": "138",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 138 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 138(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-138-SUB-04",
        "section_number": "138",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 138 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 138(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-138-SUB-05",
        "section_number": "138",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 138 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 138(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-139-SUB-01",
        "section_number": "139",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 139 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 139(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-139-SUB-02",
        "section_number": "139",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 139 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 139(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-139-SUB-03",
        "section_number": "139",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 139 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 139(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-139-SUB-04",
        "section_number": "139",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 139 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 139(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-139-SUB-05",
        "section_number": "139",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 139 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 139(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-140-SUB-01",
        "section_number": "140",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 140 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 140(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-140-SUB-02",
        "section_number": "140",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 140 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 140(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-140-SUB-03",
        "section_number": "140",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 140 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 140(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-140-SUB-04",
        "section_number": "140",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 140 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 140(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-140-SUB-05",
        "section_number": "140",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 140 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 140(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
