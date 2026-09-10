"""
Part 04 for ipc_bns_penal_code
Modular codification slice under 250 KB
"""

IPC_OFFENSES_REGISTRY_PART_04 = [
    {
        "section_id": "IPC-SEC-151",
        "section_number": "151",
        "offense_title": "Penal Code Statutory Offense Section 151",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 151 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-152",
        "section_number": "152",
        "offense_title": "Penal Code Statutory Offense Section 152",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 152 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-153",
        "section_number": "153",
        "offense_title": "Penal Code Statutory Offense Section 153",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 153 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-154",
        "section_number": "154",
        "offense_title": "Penal Code Statutory Offense Section 154",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 154 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-155",
        "section_number": "155",
        "offense_title": "Penal Code Statutory Offense Section 155",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 155 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-156",
        "section_number": "156",
        "offense_title": "Penal Code Statutory Offense Section 156",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 156 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-157",
        "section_number": "157",
        "offense_title": "Penal Code Statutory Offense Section 157",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 157 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-158",
        "section_number": "158",
        "offense_title": "Penal Code Statutory Offense Section 158",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 158 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-159",
        "section_number": "159",
        "offense_title": "Penal Code Statutory Offense Section 159",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 159 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-160",
        "section_number": "160",
        "offense_title": "Penal Code Statutory Offense Section 160",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 160 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-161",
        "section_number": "161",
        "offense_title": "Penal Code Statutory Offense Section 161",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 161 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-162",
        "section_number": "162",
        "offense_title": "Penal Code Statutory Offense Section 162",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 162 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-163",
        "section_number": "163",
        "offense_title": "Penal Code Statutory Offense Section 163",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 163 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-164",
        "section_number": "164",
        "offense_title": "Penal Code Statutory Offense Section 164",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 164 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-165",
        "section_number": "165",
        "offense_title": "Penal Code Statutory Offense Section 165",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 165 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-166",
        "section_number": "166",
        "offense_title": "Penal Code Statutory Offense Section 166",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 166 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-167",
        "section_number": "167",
        "offense_title": "Penal Code Statutory Offense Section 167",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 167 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-168",
        "section_number": "168",
        "offense_title": "Penal Code Statutory Offense Section 168",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 168 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-169",
        "section_number": "169",
        "offense_title": "Penal Code Statutory Offense Section 169",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 169 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-170",
        "section_number": "170",
        "offense_title": "Penal Code Statutory Offense Section 170",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 170 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-171",
        "section_number": "171",
        "offense_title": "Penal Code Statutory Offense Section 171",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 171 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-172",
        "section_number": "172",
        "offense_title": "Penal Code Statutory Offense Section 172",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 172 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-173",
        "section_number": "173",
        "offense_title": "Penal Code Statutory Offense Section 173",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 173 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-174",
        "section_number": "174",
        "offense_title": "Penal Code Statutory Offense Section 174",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 174 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-175",
        "section_number": "175",
        "offense_title": "Penal Code Statutory Offense Section 175",
        "chapter": "Chapter 7: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 175 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-176",
        "section_number": "176",
        "offense_title": "Penal Code Statutory Offense Section 176",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 176 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-177",
        "section_number": "177",
        "offense_title": "Penal Code Statutory Offense Section 177",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 177 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-178",
        "section_number": "178",
        "offense_title": "Penal Code Statutory Offense Section 178",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 178 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-179",
        "section_number": "179",
        "offense_title": "Penal Code Statutory Offense Section 179",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 179 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-180",
        "section_number": "180",
        "offense_title": "Penal Code Statutory Offense Section 180",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 180 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-181",
        "section_number": "181",
        "offense_title": "Penal Code Statutory Offense Section 181",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 181 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-182",
        "section_number": "182",
        "offense_title": "Penal Code Statutory Offense Section 182",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 182 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-183",
        "section_number": "183",
        "offense_title": "Penal Code Statutory Offense Section 183",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 183 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-184",
        "section_number": "184",
        "offense_title": "Penal Code Statutory Offense Section 184",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 184 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-185",
        "section_number": "185",
        "offense_title": "Penal Code Statutory Offense Section 185",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 185 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-186",
        "section_number": "186",
        "offense_title": "Penal Code Statutory Offense Section 186",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 186 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-187",
        "section_number": "187",
        "offense_title": "Penal Code Statutory Offense Section 187",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 187 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-188",
        "section_number": "188",
        "offense_title": "Penal Code Statutory Offense Section 188",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 188 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-189",
        "section_number": "189",
        "offense_title": "Penal Code Statutory Offense Section 189",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 189 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-190",
        "section_number": "190",
        "offense_title": "Penal Code Statutory Offense Section 190",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 190 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-191",
        "section_number": "191",
        "offense_title": "Penal Code Statutory Offense Section 191",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 191 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-192",
        "section_number": "192",
        "offense_title": "Penal Code Statutory Offense Section 192",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 192 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-193",
        "section_number": "193",
        "offense_title": "Penal Code Statutory Offense Section 193",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 193 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-194",
        "section_number": "194",
        "offense_title": "Penal Code Statutory Offense Section 194",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 194 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-195",
        "section_number": "195",
        "offense_title": "Penal Code Statutory Offense Section 195",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 195 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-196",
        "section_number": "196",
        "offense_title": "Penal Code Statutory Offense Section 196",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 196 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-197",
        "section_number": "197",
        "offense_title": "Penal Code Statutory Offense Section 197",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 197 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-198",
        "section_number": "198",
        "offense_title": "Penal Code Statutory Offense Section 198",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 198 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-199",
        "section_number": "199",
        "offense_title": "Penal Code Statutory Offense Section 199",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 199 of the Penal Code / Bharatiya Nyaya Sanhita:
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
        "section_id": "IPC-SEC-200",
        "section_number": "200",
        "offense_title": "Penal Code Statutory Offense Section 200",
        "chapter": "Chapter 8: Crimes, Offenses against Person, Property & the State",
        "substantive_definition": """Section 200 of the Penal Code / Bharatiya Nyaya Sanhita:
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
