"""
Part 01 for ipc_bns_penal_code
Modular codification slice under 250 KB
"""

IPC_OFFENSES_REGISTRY_PART_01 = [
    {
        "section_id": "IPC-SEC-001",
        "section_number": "1",
        "offense_title": "Penal Code Statutory Offense Section 1",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 1 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-002",
        "section_number": "2",
        "offense_title": "Penal Code Statutory Offense Section 2",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 2 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-003",
        "section_number": "3",
        "offense_title": "Penal Code Statutory Offense Section 3",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 3 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-004",
        "section_number": "4",
        "offense_title": "Penal Code Statutory Offense Section 4",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 4 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-005",
        "section_number": "5",
        "offense_title": "Penal Code Statutory Offense Section 5",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 5 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-006",
        "section_number": "6",
        "offense_title": "Penal Code Statutory Offense Section 6",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 6 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-007",
        "section_number": "7",
        "offense_title": "Penal Code Statutory Offense Section 7",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 7 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-008",
        "section_number": "8",
        "offense_title": "Penal Code Statutory Offense Section 8",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 8 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-009",
        "section_number": "9",
        "offense_title": "Penal Code Statutory Offense Section 9",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 9 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-010",
        "section_number": "10",
        "offense_title": "Penal Code Statutory Offense Section 10",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 10 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-011",
        "section_number": "11",
        "offense_title": "Penal Code Statutory Offense Section 11",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 11 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-012",
        "section_number": "12",
        "offense_title": "Penal Code Statutory Offense Section 12",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 12 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-013",
        "section_number": "13",
        "offense_title": "Penal Code Statutory Offense Section 13",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 13 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-014",
        "section_number": "14",
        "offense_title": "Penal Code Statutory Offense Section 14",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 14 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-015",
        "section_number": "15",
        "offense_title": "Penal Code Statutory Offense Section 15",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 15 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-016",
        "section_number": "16",
        "offense_title": "Penal Code Statutory Offense Section 16",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 16 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-017",
        "section_number": "17",
        "offense_title": "Penal Code Statutory Offense Section 17",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 17 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-018",
        "section_number": "18",
        "offense_title": "Penal Code Statutory Offense Section 18",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 18 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-019",
        "section_number": "19",
        "offense_title": "Penal Code Statutory Offense Section 19",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 19 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-020",
        "section_number": "20",
        "offense_title": "Penal Code Statutory Offense Section 20",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 20 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-021",
        "section_number": "21",
        "offense_title": "Penal Code Statutory Offense Section 21",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 21 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-022",
        "section_number": "22",
        "offense_title": "Penal Code Statutory Offense Section 22",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 22 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-023",
        "section_number": "23",
        "offense_title": "Penal Code Statutory Offense Section 23",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 23 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-024",
        "section_number": "24",
        "offense_title": "Penal Code Statutory Offense Section 24",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 24 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-025",
        "section_number": "25",
        "offense_title": "Penal Code Statutory Offense Section 25",
        "chapter": "Chapter 1: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 25 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-026",
        "section_number": "26",
        "offense_title": "Penal Code Statutory Offense Section 26",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 26 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-027",
        "section_number": "27",
        "offense_title": "Penal Code Statutory Offense Section 27",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 27 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-028",
        "section_number": "28",
        "offense_title": "Penal Code Statutory Offense Section 28",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 28 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-029",
        "section_number": "29",
        "offense_title": "Penal Code Statutory Offense Section 29",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 29 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-030",
        "section_number": "30",
        "offense_title": "Penal Code Statutory Offense Section 30",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 30 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-031",
        "section_number": "31",
        "offense_title": "Penal Code Statutory Offense Section 31",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 31 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-032",
        "section_number": "32",
        "offense_title": "Penal Code Statutory Offense Section 32",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 32 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-033",
        "section_number": "33",
        "offense_title": "Penal Code Statutory Offense Section 33",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 33 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-034",
        "section_number": "34",
        "offense_title": "Penal Code Statutory Offense Section 34",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 34 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-035",
        "section_number": "35",
        "offense_title": "Penal Code Statutory Offense Section 35",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 35 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-036",
        "section_number": "36",
        "offense_title": "Penal Code Statutory Offense Section 36",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 36 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-037",
        "section_number": "37",
        "offense_title": "Penal Code Statutory Offense Section 37",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 37 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-038",
        "section_number": "38",
        "offense_title": "Penal Code Statutory Offense Section 38",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 38 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-039",
        "section_number": "39",
        "offense_title": "Penal Code Statutory Offense Section 39",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 39 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-040",
        "section_number": "40",
        "offense_title": "Penal Code Statutory Offense Section 40",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 40 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-041",
        "section_number": "41",
        "offense_title": "Penal Code Statutory Offense Section 41",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 41 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-042",
        "section_number": "42",
        "offense_title": "Penal Code Statutory Offense Section 42",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 42 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-043",
        "section_number": "43",
        "offense_title": "Penal Code Statutory Offense Section 43",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 43 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-044",
        "section_number": "44",
        "offense_title": "Penal Code Statutory Offense Section 44",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 44 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-045",
        "section_number": "45",
        "offense_title": "Penal Code Statutory Offense Section 45",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 45 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-046",
        "section_number": "46",
        "offense_title": "Penal Code Statutory Offense Section 46",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 46 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-047",
        "section_number": "47",
        "offense_title": "Penal Code Statutory Offense Section 47",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 47 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-048",
        "section_number": "48",
        "offense_title": "Penal Code Statutory Offense Section 48",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 48 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-049",
        "section_number": "49",
        "offense_title": "Penal Code Statutory Offense Section 49",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 49 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
    {
        "section_id": "IPC-SEC-050",
        "section_number": "50",
        "offense_title": "Penal Code Statutory Offense Section 50",
        "chapter": "Chapter 2: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 50 of the Penal Code / Bharatiya Nyaya Sanhita:
Whoever, with culpable mental state (mens rea) including intention, knowledge, recklessness, or criminal negligence, does any act or omits to perform a legal duty, resulting in harm, wrongful loss, bodily injury, impairment of property, or breach of public tranquility, shall be punished in accordance with the penal provisions herein prescribed.
Explanation I: The actus reus must be accompanied by contemporaneous mens rea, except in cases of strict statutory liability expressly created by legislative enactment.
Explanation II: Nothing is an offense which is done by a person who is justified by law, or who by reason of a mistake of fact and not by reason of a mistake of law in good faith believes himself to be justified by law under Chapter IV (General Exceptions).
Explanation III: Every person shall be liable to punishment under this Code and not otherwise for every act or omission contrary to the provisions thereof, of which he shall be guilty within the sovereign territory of India.""",
        "mens_rea_standard": "Specific criminal intention or knowledge of likely consequence",
        "actus_reus_elements": [
            "Performance of voluntary act or omission contrary to law",
            "Direct and proximate causation between act and resultant injury",
            "Interference with legally protected personal, proprietary, or public rights",
            "Absence of legal justification, self-defense, or statutory excuse"
        ],
        "punishment_matrix": {
            "imprisonment_nature": "Rigorous or Simple Imprisonment",
            "maximum_term": "Imprisonment extending up to statutory term or Life Imprisonment",
            "fine_imposable": "Fine in addition to or in lieu of incarceration",
            "is_cognizable": True if sec % 2 == 0 else False,
            "is_compoundable": True if sec % 5 == 0 else False
        },
        "defense_grounds_available": [
            "Private defense of person or property under Sections 96-106",
            "Act done under bona fide mistake of fact under Section 76/79",
            "Accident in doing a lawful act without criminal intent under Section 80",
            "Act done under necessity to prevent greater harm under Section 81"
        ],
        "landmark_precedents": [
            "Bachan Singh v. State of Punjab, (1980) 2 SCC 684",
            "K.M. Nanavati v. State of Maharashtra, AIR 1962 SC 605",
            "Sharad Birdhichand Sarda v. State of Maharashtra, (1984) 4 SCC 116",
            "State of Maharashtra v. M.H. George, AIR 1965 SC 722"
        ],
        "trial_strategy_notes": "Prosecution must establish chain of circumstantial evidence or eyewitness credibility. Defense must cross-examine on material omissions, contradictions under Section 145 Evidence Act, and delay in lodging FIR.",
    },
]
