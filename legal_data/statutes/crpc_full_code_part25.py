"""
Part 25 for crpc_full_code
Modular codification slice under 250 KB
"""

CRPC_EXTENDED_SECTIONS_PART_25 = [
    {
        "section_id": "CRPC-SEC-241-SUB-01",
        "section_number": "241",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 241 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 241(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-241-SUB-02",
        "section_number": "241",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 241 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 241(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-241-SUB-03",
        "section_number": "241",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 241 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 241(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-241-SUB-04",
        "section_number": "241",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 241 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 241(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-241-SUB-05",
        "section_number": "241",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 241 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 241(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-242-SUB-01",
        "section_number": "242",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 242 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 242(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-242-SUB-02",
        "section_number": "242",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 242 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 242(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-242-SUB-03",
        "section_number": "242",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 242 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 242(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-242-SUB-04",
        "section_number": "242",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 242 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 242(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-242-SUB-05",
        "section_number": "242",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 242 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 242(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-243-SUB-01",
        "section_number": "243",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 243 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 243(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-243-SUB-02",
        "section_number": "243",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 243 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 243(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-243-SUB-03",
        "section_number": "243",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 243 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 243(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-243-SUB-04",
        "section_number": "243",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 243 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 243(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-243-SUB-05",
        "section_number": "243",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 243 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 243(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-244-SUB-01",
        "section_number": "244",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 244 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 244(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-244-SUB-02",
        "section_number": "244",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 244 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 244(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-244-SUB-03",
        "section_number": "244",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 244 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 244(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-244-SUB-04",
        "section_number": "244",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 244 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 244(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-244-SUB-05",
        "section_number": "244",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 244 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 244(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-245-SUB-01",
        "section_number": "245",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 245 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 245(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-245-SUB-02",
        "section_number": "245",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 245 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 245(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-245-SUB-03",
        "section_number": "245",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 245 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 245(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-245-SUB-04",
        "section_number": "245",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 245 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 245(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-245-SUB-05",
        "section_number": "245",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 245 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 245(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-246-SUB-01",
        "section_number": "246",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 246 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 246(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-246-SUB-02",
        "section_number": "246",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 246 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 246(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-246-SUB-03",
        "section_number": "246",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 246 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 246(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-246-SUB-04",
        "section_number": "246",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 246 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 246(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-246-SUB-05",
        "section_number": "246",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 246 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 246(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-247-SUB-01",
        "section_number": "247",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 247 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 247(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-247-SUB-02",
        "section_number": "247",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 247 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 247(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-247-SUB-03",
        "section_number": "247",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 247 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 247(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-247-SUB-04",
        "section_number": "247",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 247 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 247(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-247-SUB-05",
        "section_number": "247",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 247 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 247(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-248-SUB-01",
        "section_number": "248",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 248 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 248(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-248-SUB-02",
        "section_number": "248",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 248 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 248(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-248-SUB-03",
        "section_number": "248",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 248 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 248(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-248-SUB-04",
        "section_number": "248",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 248 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 248(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-248-SUB-05",
        "section_number": "248",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 248 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 248(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-249-SUB-01",
        "section_number": "249",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 249 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 249(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-249-SUB-02",
        "section_number": "249",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 249 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 249(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-249-SUB-03",
        "section_number": "249",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 249 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 249(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-249-SUB-04",
        "section_number": "249",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 249 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 249(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-249-SUB-05",
        "section_number": "249",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 249 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 249(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-250-SUB-01",
        "section_number": "250",
        "sub_clause": "Clause (1)",
        "title": "Criminal Procedure Code Section 250 - Clause 1: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 250(1) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-250-SUB-02",
        "section_number": "250",
        "sub_clause": "Clause (2)",
        "title": "Criminal Procedure Code Section 250 - Clause 2: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 250(2) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-250-SUB-03",
        "section_number": "250",
        "sub_clause": "Clause (3)",
        "title": "Criminal Procedure Code Section 250 - Clause 3: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 250(3) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-250-SUB-04",
        "section_number": "250",
        "sub_clause": "Clause (4)",
        "title": "Criminal Procedure Code Section 250 - Clause 4: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 250(4) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
        "section_id": "CRPC-SEC-250-SUB-05",
        "section_number": "250",
        "sub_clause": "Clause (5)",
        "title": "Criminal Procedure Code Section 250 - Clause 5: Investigation, Bail & Trial Mandate",
        "statutory_text": """Section 250(5) of the Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita:
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
