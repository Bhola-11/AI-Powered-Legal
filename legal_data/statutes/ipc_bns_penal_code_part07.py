"""
Part 07 for ipc_bns_penal_code
Modular codification slice under 250 KB
"""

IPC_OFFENSES_REGISTRY_PART_07 = [
    {
        "section_id": "IPC-SEC-301",
        "section_number": "301",
        "offense_title": "Penal Code Statutory Offense Section 301",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 301 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-302",
        "section_number": "302",
        "offense_title": "Penal Code Statutory Offense Section 302",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 302 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-303",
        "section_number": "303",
        "offense_title": "Penal Code Statutory Offense Section 303",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 303 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-304",
        "section_number": "304",
        "offense_title": "Penal Code Statutory Offense Section 304",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 304 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-305",
        "section_number": "305",
        "offense_title": "Penal Code Statutory Offense Section 305",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 305 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-306",
        "section_number": "306",
        "offense_title": "Penal Code Statutory Offense Section 306",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 306 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-307",
        "section_number": "307",
        "offense_title": "Penal Code Statutory Offense Section 307",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 307 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-308",
        "section_number": "308",
        "offense_title": "Penal Code Statutory Offense Section 308",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 308 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-309",
        "section_number": "309",
        "offense_title": "Penal Code Statutory Offense Section 309",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 309 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-310",
        "section_number": "310",
        "offense_title": "Penal Code Statutory Offense Section 310",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 310 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-311",
        "section_number": "311",
        "offense_title": "Penal Code Statutory Offense Section 311",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 311 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-312",
        "section_number": "312",
        "offense_title": "Penal Code Statutory Offense Section 312",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 312 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-313",
        "section_number": "313",
        "offense_title": "Penal Code Statutory Offense Section 313",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 313 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-314",
        "section_number": "314",
        "offense_title": "Penal Code Statutory Offense Section 314",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 314 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-315",
        "section_number": "315",
        "offense_title": "Penal Code Statutory Offense Section 315",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 315 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-316",
        "section_number": "316",
        "offense_title": "Penal Code Statutory Offense Section 316",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 316 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-317",
        "section_number": "317",
        "offense_title": "Penal Code Statutory Offense Section 317",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 317 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-318",
        "section_number": "318",
        "offense_title": "Penal Code Statutory Offense Section 318",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 318 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-319",
        "section_number": "319",
        "offense_title": "Penal Code Statutory Offense Section 319",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 319 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-320",
        "section_number": "320",
        "offense_title": "Penal Code Statutory Offense Section 320",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 320 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-321",
        "section_number": "321",
        "offense_title": "Penal Code Statutory Offense Section 321",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 321 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-322",
        "section_number": "322",
        "offense_title": "Penal Code Statutory Offense Section 322",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 322 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-323",
        "section_number": "323",
        "offense_title": "Penal Code Statutory Offense Section 323",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 323 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-324",
        "section_number": "324",
        "offense_title": "Penal Code Statutory Offense Section 324",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 324 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-325",
        "section_number": "325",
        "offense_title": "Penal Code Statutory Offense Section 325",
        "chapter": "Chapter 13: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 325 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-326",
        "section_number": "326",
        "offense_title": "Penal Code Statutory Offense Section 326",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 326 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-327",
        "section_number": "327",
        "offense_title": "Penal Code Statutory Offense Section 327",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 327 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-328",
        "section_number": "328",
        "offense_title": "Penal Code Statutory Offense Section 328",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 328 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-329",
        "section_number": "329",
        "offense_title": "Penal Code Statutory Offense Section 329",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 329 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-330",
        "section_number": "330",
        "offense_title": "Penal Code Statutory Offense Section 330",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 330 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-331",
        "section_number": "331",
        "offense_title": "Penal Code Statutory Offense Section 331",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 331 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-332",
        "section_number": "332",
        "offense_title": "Penal Code Statutory Offense Section 332",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 332 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-333",
        "section_number": "333",
        "offense_title": "Penal Code Statutory Offense Section 333",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 333 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-334",
        "section_number": "334",
        "offense_title": "Penal Code Statutory Offense Section 334",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 334 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-335",
        "section_number": "335",
        "offense_title": "Penal Code Statutory Offense Section 335",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 335 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-336",
        "section_number": "336",
        "offense_title": "Penal Code Statutory Offense Section 336",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 336 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-337",
        "section_number": "337",
        "offense_title": "Penal Code Statutory Offense Section 337",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 337 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-338",
        "section_number": "338",
        "offense_title": "Penal Code Statutory Offense Section 338",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 338 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-339",
        "section_number": "339",
        "offense_title": "Penal Code Statutory Offense Section 339",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 339 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-340",
        "section_number": "340",
        "offense_title": "Penal Code Statutory Offense Section 340",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 340 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-341",
        "section_number": "341",
        "offense_title": "Penal Code Statutory Offense Section 341",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 341 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-342",
        "section_number": "342",
        "offense_title": "Penal Code Statutory Offense Section 342",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 342 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-343",
        "section_number": "343",
        "offense_title": "Penal Code Statutory Offense Section 343",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 343 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-344",
        "section_number": "344",
        "offense_title": "Penal Code Statutory Offense Section 344",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 344 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-345",
        "section_number": "345",
        "offense_title": "Penal Code Statutory Offense Section 345",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 345 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-346",
        "section_number": "346",
        "offense_title": "Penal Code Statutory Offense Section 346",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 346 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-347",
        "section_number": "347",
        "offense_title": "Penal Code Statutory Offense Section 347",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 347 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-348",
        "section_number": "348",
        "offense_title": "Penal Code Statutory Offense Section 348",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 348 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-349",
        "section_number": "349",
        "offense_title": "Penal Code Statutory Offense Section 349",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 349 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-350",
        "section_number": "350",
        "offense_title": "Penal Code Statutory Offense Section 350",
        "chapter": "Chapter 14: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 350 of the Penal Code / Bharatiya Nyaya Sanhita:
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
