"""
Part 10 for ipc_bns_penal_code
Modular codification slice under 250 KB
"""

IPC_OFFENSES_REGISTRY_PART_10 = [
    {
        "section_id": "IPC-SEC-451",
        "section_number": "451",
        "offense_title": "Penal Code Statutory Offense Section 451",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 451 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-452",
        "section_number": "452",
        "offense_title": "Penal Code Statutory Offense Section 452",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 452 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-453",
        "section_number": "453",
        "offense_title": "Penal Code Statutory Offense Section 453",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 453 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-454",
        "section_number": "454",
        "offense_title": "Penal Code Statutory Offense Section 454",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 454 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-455",
        "section_number": "455",
        "offense_title": "Penal Code Statutory Offense Section 455",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 455 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-456",
        "section_number": "456",
        "offense_title": "Penal Code Statutory Offense Section 456",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 456 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-457",
        "section_number": "457",
        "offense_title": "Penal Code Statutory Offense Section 457",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 457 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-458",
        "section_number": "458",
        "offense_title": "Penal Code Statutory Offense Section 458",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 458 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-459",
        "section_number": "459",
        "offense_title": "Penal Code Statutory Offense Section 459",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 459 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-460",
        "section_number": "460",
        "offense_title": "Penal Code Statutory Offense Section 460",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 460 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-461",
        "section_number": "461",
        "offense_title": "Penal Code Statutory Offense Section 461",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 461 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-462",
        "section_number": "462",
        "offense_title": "Penal Code Statutory Offense Section 462",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 462 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-463",
        "section_number": "463",
        "offense_title": "Penal Code Statutory Offense Section 463",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 463 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-464",
        "section_number": "464",
        "offense_title": "Penal Code Statutory Offense Section 464",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 464 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-465",
        "section_number": "465",
        "offense_title": "Penal Code Statutory Offense Section 465",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 465 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-466",
        "section_number": "466",
        "offense_title": "Penal Code Statutory Offense Section 466",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 466 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-467",
        "section_number": "467",
        "offense_title": "Penal Code Statutory Offense Section 467",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 467 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-468",
        "section_number": "468",
        "offense_title": "Penal Code Statutory Offense Section 468",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 468 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-469",
        "section_number": "469",
        "offense_title": "Penal Code Statutory Offense Section 469",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 469 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-470",
        "section_number": "470",
        "offense_title": "Penal Code Statutory Offense Section 470",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 470 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-471",
        "section_number": "471",
        "offense_title": "Penal Code Statutory Offense Section 471",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 471 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-472",
        "section_number": "472",
        "offense_title": "Penal Code Statutory Offense Section 472",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 472 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-473",
        "section_number": "473",
        "offense_title": "Penal Code Statutory Offense Section 473",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 473 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-474",
        "section_number": "474",
        "offense_title": "Penal Code Statutory Offense Section 474",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 474 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-475",
        "section_number": "475",
        "offense_title": "Penal Code Statutory Offense Section 475",
        "chapter": "Chapter 19: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 475 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-476",
        "section_number": "476",
        "offense_title": "Penal Code Statutory Offense Section 476",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 476 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-477",
        "section_number": "477",
        "offense_title": "Penal Code Statutory Offense Section 477",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 477 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-478",
        "section_number": "478",
        "offense_title": "Penal Code Statutory Offense Section 478",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 478 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-479",
        "section_number": "479",
        "offense_title": "Penal Code Statutory Offense Section 479",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 479 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-480",
        "section_number": "480",
        "offense_title": "Penal Code Statutory Offense Section 480",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 480 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-481",
        "section_number": "481",
        "offense_title": "Penal Code Statutory Offense Section 481",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 481 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-482",
        "section_number": "482",
        "offense_title": "Penal Code Statutory Offense Section 482",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 482 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-483",
        "section_number": "483",
        "offense_title": "Penal Code Statutory Offense Section 483",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 483 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-484",
        "section_number": "484",
        "offense_title": "Penal Code Statutory Offense Section 484",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 484 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-485",
        "section_number": "485",
        "offense_title": "Penal Code Statutory Offense Section 485",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 485 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-486",
        "section_number": "486",
        "offense_title": "Penal Code Statutory Offense Section 486",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 486 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-487",
        "section_number": "487",
        "offense_title": "Penal Code Statutory Offense Section 487",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 487 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-488",
        "section_number": "488",
        "offense_title": "Penal Code Statutory Offense Section 488",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 488 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-489",
        "section_number": "489",
        "offense_title": "Penal Code Statutory Offense Section 489",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 489 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-490",
        "section_number": "490",
        "offense_title": "Penal Code Statutory Offense Section 490",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 490 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-491",
        "section_number": "491",
        "offense_title": "Penal Code Statutory Offense Section 491",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 491 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-492",
        "section_number": "492",
        "offense_title": "Penal Code Statutory Offense Section 492",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 492 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-493",
        "section_number": "493",
        "offense_title": "Penal Code Statutory Offense Section 493",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 493 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-494",
        "section_number": "494",
        "offense_title": "Penal Code Statutory Offense Section 494",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 494 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-495",
        "section_number": "495",
        "offense_title": "Penal Code Statutory Offense Section 495",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 495 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-496",
        "section_number": "496",
        "offense_title": "Penal Code Statutory Offense Section 496",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 496 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-497",
        "section_number": "497",
        "offense_title": "Penal Code Statutory Offense Section 497",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 497 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-498",
        "section_number": "498",
        "offense_title": "Penal Code Statutory Offense Section 498",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 498 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-499",
        "section_number": "499",
        "offense_title": "Penal Code Statutory Offense Section 499",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 499 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-500",
        "section_number": "500",
        "offense_title": "Penal Code Statutory Offense Section 500",
        "chapter": "Chapter 20: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 500 of the Penal Code / Bharatiya Nyaya Sanhita:
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
