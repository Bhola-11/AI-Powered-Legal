"""
Part 06 for ipc_bns_penal_code
Modular codification slice under 250 KB
"""

IPC_OFFENSES_REGISTRY_PART_06 = [
    {
        "section_id": "IPC-SEC-251",
        "section_number": "251",
        "offense_title": "Penal Code Statutory Offense Section 251",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 251 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-252",
        "section_number": "252",
        "offense_title": "Penal Code Statutory Offense Section 252",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 252 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-253",
        "section_number": "253",
        "offense_title": "Penal Code Statutory Offense Section 253",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 253 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-254",
        "section_number": "254",
        "offense_title": "Penal Code Statutory Offense Section 254",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 254 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-255",
        "section_number": "255",
        "offense_title": "Penal Code Statutory Offense Section 255",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 255 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-256",
        "section_number": "256",
        "offense_title": "Penal Code Statutory Offense Section 256",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 256 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-257",
        "section_number": "257",
        "offense_title": "Penal Code Statutory Offense Section 257",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 257 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-258",
        "section_number": "258",
        "offense_title": "Penal Code Statutory Offense Section 258",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 258 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-259",
        "section_number": "259",
        "offense_title": "Penal Code Statutory Offense Section 259",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 259 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-260",
        "section_number": "260",
        "offense_title": "Penal Code Statutory Offense Section 260",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 260 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-261",
        "section_number": "261",
        "offense_title": "Penal Code Statutory Offense Section 261",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 261 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-262",
        "section_number": "262",
        "offense_title": "Penal Code Statutory Offense Section 262",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 262 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-263",
        "section_number": "263",
        "offense_title": "Penal Code Statutory Offense Section 263",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 263 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-264",
        "section_number": "264",
        "offense_title": "Penal Code Statutory Offense Section 264",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 264 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-265",
        "section_number": "265",
        "offense_title": "Penal Code Statutory Offense Section 265",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 265 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-266",
        "section_number": "266",
        "offense_title": "Penal Code Statutory Offense Section 266",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 266 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-267",
        "section_number": "267",
        "offense_title": "Penal Code Statutory Offense Section 267",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 267 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-268",
        "section_number": "268",
        "offense_title": "Penal Code Statutory Offense Section 268",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 268 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-269",
        "section_number": "269",
        "offense_title": "Penal Code Statutory Offense Section 269",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 269 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-270",
        "section_number": "270",
        "offense_title": "Penal Code Statutory Offense Section 270",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 270 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-271",
        "section_number": "271",
        "offense_title": "Penal Code Statutory Offense Section 271",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 271 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-272",
        "section_number": "272",
        "offense_title": "Penal Code Statutory Offense Section 272",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 272 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-273",
        "section_number": "273",
        "offense_title": "Penal Code Statutory Offense Section 273",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 273 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-274",
        "section_number": "274",
        "offense_title": "Penal Code Statutory Offense Section 274",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 274 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-275",
        "section_number": "275",
        "offense_title": "Penal Code Statutory Offense Section 275",
        "chapter": "Chapter 11: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 275 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-276",
        "section_number": "276",
        "offense_title": "Penal Code Statutory Offense Section 276",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 276 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-277",
        "section_number": "277",
        "offense_title": "Penal Code Statutory Offense Section 277",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 277 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-278",
        "section_number": "278",
        "offense_title": "Penal Code Statutory Offense Section 278",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 278 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-279",
        "section_number": "279",
        "offense_title": "Penal Code Statutory Offense Section 279",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 279 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-280",
        "section_number": "280",
        "offense_title": "Penal Code Statutory Offense Section 280",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 280 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-281",
        "section_number": "281",
        "offense_title": "Penal Code Statutory Offense Section 281",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 281 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-282",
        "section_number": "282",
        "offense_title": "Penal Code Statutory Offense Section 282",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 282 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-283",
        "section_number": "283",
        "offense_title": "Penal Code Statutory Offense Section 283",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 283 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-284",
        "section_number": "284",
        "offense_title": "Penal Code Statutory Offense Section 284",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 284 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-285",
        "section_number": "285",
        "offense_title": "Penal Code Statutory Offense Section 285",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 285 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-286",
        "section_number": "286",
        "offense_title": "Penal Code Statutory Offense Section 286",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 286 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-287",
        "section_number": "287",
        "offense_title": "Penal Code Statutory Offense Section 287",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 287 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-288",
        "section_number": "288",
        "offense_title": "Penal Code Statutory Offense Section 288",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 288 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-289",
        "section_number": "289",
        "offense_title": "Penal Code Statutory Offense Section 289",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 289 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-290",
        "section_number": "290",
        "offense_title": "Penal Code Statutory Offense Section 290",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 290 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-291",
        "section_number": "291",
        "offense_title": "Penal Code Statutory Offense Section 291",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 291 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-292",
        "section_number": "292",
        "offense_title": "Penal Code Statutory Offense Section 292",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 292 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-293",
        "section_number": "293",
        "offense_title": "Penal Code Statutory Offense Section 293",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 293 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-294",
        "section_number": "294",
        "offense_title": "Penal Code Statutory Offense Section 294",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 294 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-295",
        "section_number": "295",
        "offense_title": "Penal Code Statutory Offense Section 295",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 295 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-296",
        "section_number": "296",
        "offense_title": "Penal Code Statutory Offense Section 296",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 296 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-297",
        "section_number": "297",
        "offense_title": "Penal Code Statutory Offense Section 297",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 297 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-298",
        "section_number": "298",
        "offense_title": "Penal Code Statutory Offense Section 298",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 298 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-299",
        "section_number": "299",
        "offense_title": "Penal Code Statutory Offense Section 299",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 299 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-300",
        "section_number": "300",
        "offense_title": "Penal Code Statutory Offense Section 300",
        "chapter": "Chapter 12: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 300 of the Penal Code / Bharatiya Nyaya Sanhita:
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
