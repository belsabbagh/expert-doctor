from experta import *

from src.disease import Disease


class Greetings(KnowledgeEngine):

    def __init__(self, symptom_map, if_not_matched, get_treatments, get_details):
        self.symptom_map = symptom_map
        self.if_not_matched = if_not_matched
        self.get_details = get_details
        self.get_treatments = get_treatments
        KnowledgeEngine.__init__(self)

    # code giving instructions on how to use the Expert System
    @DefFacts()
    def _initial_action(self):
        print("")
        print("This is a knowledge based bot to diagnose diseases")
        print("")
        print("Do you feel any of the following symptoms?")
        print("Reply high or low or no")
        print("")
        yield Fact(action="find_disease")

    # taking various input from user
    @Rule(Fact(action="find_disease"), NOT(Fact(headache=W())), salience=4)
    def symptom_0(self):
        self.declare(Fact(headache=input("headache: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(back_pain=W())), salience=1)
    def symptom_1(self):
        self.declare(Fact(back_pain=input("back pain: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(chest_pain=W())), salience=1)
    def symptom_2(self):
        self.declare(Fact(chest_pain=input("chest pain: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(cough=W())), salience=3)
    def symptom_3(self):
        self.declare(Fact(cough=input("cough: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(fainting=W())), salience=1)
    def symptom_4(self):
        self.declare(Fact(fainting=input("fainting: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(fatigue=W())), salience=1)
    def symptom_5(self):
        self.declare(Fact(fatigue=input("fatigue: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(sunken_eyes=W())), salience=1)
    def symptom_6(self):
        self.declare(Fact(sunken_eyes=input("sunken eyes: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(low_body_temp=W())), salience=1)
    def symptom_7(self):
        self.declare(Fact(low_body_temp=input("low body temperature: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(restlessness=W())), salience=1)
    def symptom_8(self):
        self.declare(Fact(restlessness=input("restlessness: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(sore_throat=W())), salience=1)
    def symptom_9(self):
        self.declare(Fact(sore_throat=input("sore throat: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(fever=W())), salience=1)
    def symptom_10(self):
        self.declare(Fact(fever=input("fever: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(nausea=W())), salience=1)
    def symptom_11(self):
        self.declare(Fact(nausea=input("nausea: ")))

    @Rule(Fact(action="find_disease"), NOT(Fact(blurred_vision=W())), salience=1)
    def symptom_12(self):
        self.declare(Fact(blurred_vision=input("blurred_vision: ")))

    # different rules checking for each disease match
    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="high"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="low"),
        Fact(sunken_eyes="no"),
        Fact(nausea="high"),
        Fact(blurred_vision="no"),
    )
    def disease_0(self):
        self.declare(Fact(disease="Jaundice"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="high"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def disease_1(self):
        self.declare(Fact(disease="Alzheimers"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="high"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="low"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def disease_2(self):
        self.declare(Fact(disease="Arthritis"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="high"),
        Fact(cough="low"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="high"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def disease_3(self):
        self.declare(Fact(disease="Tuberculosis"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="high"),
        Fact(cough="high"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="low"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def disease_4(self):
        self.declare(Fact(disease="Asthma"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="low"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="high"),
        Fact(fainting="no"),
        Fact(sore_throat="high"),
        Fact(fatigue="no"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="low"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def disease_5(self):
        self.declare(Fact(disease="Sinusitis"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="low"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def disease_6(self):
        self.declare(Fact(disease="Epilepsy"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="high"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="high"),
        Fact(blurred_vision="no"),
    )
    def disease_7(self):
        self.declare(Fact(disease="Heart Disease"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="high"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="low"),
        Fact(blurred_vision="low"),
    )
    def disease_8(self):
        self.declare(Fact(disease="Diabetes"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="low"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="high"),
        Fact(blurred_vision="low"),
    )
    def disease_9(self):
        self.declare(Fact(disease="Glaucoma"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="high"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="low"),
        Fact(blurred_vision="no"),
    )
    def disease_10(self):
        self.declare(Fact(disease="Hyperthyroidism"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="high"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="no"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="high"),
        Fact(sunken_eyes="no"),
        Fact(nausea="high"),
        Fact(blurred_vision="no"),
    )
    def disease_11(self):
        self.declare(Fact(disease="Heat Stroke"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="no"),
        Fact(back_pain="no"),
        Fact(chest_pain="no"),
        Fact(cough="no"),
        Fact(fainting="yes"),
        Fact(sore_throat="no"),
        Fact(fatigue="no"),
        Fact(restlessness="no"),
        Fact(low_body_temp="high"),
        Fact(fever="no"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def disease_12(self):
        self.declare(Fact(disease="Hypothermia"))

    @Rule(
        Fact(action="find_disease"),
        Fact(headache="high"),
        Fact(back_pain="no"),
        Fact(chest_pain="high"),
        Fact(cough="high"),
        Fact(fainting="no"),
        Fact(sore_throat="high"),
        Fact(fatigue="high"),
        Fact(restlessness="no"),
        Fact(low_body_temp="no"),
        Fact(fever="high"),
        Fact(sunken_eyes="no"),
        Fact(nausea="no"),
        Fact(blurred_vision="no"),
    )
    def disease_13(self):
        self.declare(Fact(disease="Coronavirus"))

    # when the user's input doesn't match any disease in the knowledge base
    @Rule(Fact(action="find_disease"), Fact(disease=MATCH.disease), salience=-998)
    def disease(self, disease_name):
        print("")
        id_disease = disease_name
        disease_details = self.get_details(id_disease)
        treatments = self.get_treatments(id_disease)
        print("")
        print("Your symptoms match %s\n" % id_disease)
        print("A short description of the disease is given below :\n")
        print(disease_details + "\n")
        print(
            "The common medications and procedures suggested by other real doctors are: \n"
        )
        print(treatments + "\n")

    @Rule(
        Fact(action="find_disease"),
        Fact(headache=MATCH.headache),
        Fact(back_pain=MATCH.back_pain),
        Fact(chest_pain=MATCH.chest_pain),
        Fact(cough=MATCH.cough),
        Fact(fainting=MATCH.fainting),
        Fact(sore_throat=MATCH.sore_throat),
        Fact(fatigue=MATCH.fatigue),
        Fact(low_body_temp=MATCH.low_body_temp),
        Fact(restlessness=MATCH.restlessness),
        Fact(fever=MATCH.fever),
        Fact(sunken_eyes=MATCH.sunken_eyes),
        Fact(nausea=MATCH.nausea),
        Fact(blurred_vision=MATCH.blurred_vision),
        NOT(Fact(disease=MATCH.disease)),
        salience=-999
    )
    def not_matched(
            self,
            headache,
            back_pain,
            chest_pain,
            cough,
            fainting,
            sore_throat,
            fatigue,
            restlessness,
            low_body_temp,
            fever,
            sunken_eyes,
            nausea,
            blurred_vision,
    ):
        print("\nThe bot did not find any diseases that match your exact symptoms.")
        symptoms = Disease(
            headache,
            back_pain,
            chest_pain,
            cough,
            fainting,
            sore_throat,
            fatigue,
            restlessness,
            low_body_temp,
            fever,
            sunken_eyes,
            nausea,
            blurred_vision
        )
        symptoms_list = symptoms.tolist()
        max_count = 0
        max_disease = ""
        for disease_name, disease_symptom_values in self.symptom_map.items():
            count = 0
            for ref_symptom, in_symptom in zip(disease_symptom_values, symptoms_list):
                if ref_symptom == in_symptom and (in_symptom in ['high', 'low', 'yes']):
                    count = count + 1
            if count > max_count:
                max_count, max_disease = count, disease_name
        if max_disease != "":
            self.if_not_matched(max_disease)
