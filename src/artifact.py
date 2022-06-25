import numpy as np
from util import *

RATE_4OP = 0.2

class Artifact:
    def __init__(self, type) -> None:
        self.type = type
        self.options={"main":None, "sub1":None, "sub2":None, "sub3":None, "sub4":None}

        # main option
        if (type == "flower"):
            self.main_option = ["HP_+"]
            self.main_option_p = [1.0]
            self.__set_main_option()
        elif (type == "plume"):
            self.main_option = ["ATK_+"]
            self.main_option_p = [1.0]
            self.__set_main_option()
        elif (type == "sands"):
            self.main_option = [ \
                "HP_%", \
                "ATK_%", \
                "DEF_%", \
                "Elemental_Mastery", \
                "Energy_Recharge" \
            ]
            self.main_option_p = [0.2668, 0.2666, 0.2666, 0.1, 0.1]
            self.__set_main_option()
        elif (type == "goblet"):
            self.main_option = [ \
                "HP_%", \
                "ATK_%", \
                "DEF_%", \
                "Pyro_DMG_Bonus", \
                "Electro_DMG_Bonus", \
                "Cryo_DMG_Bonus", \
                "Hydro_DMG_Bonus", \
                "Anemo_DMG_Bonus", \
                "Geo_DMG_Bonus", \
                "Physical_DMG_Bonus", \
                "Elemental_Mastery" \
            ]
            self.main_option_p = [0.2125, 0.2125, 0.2, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.025]
            self.__set_main_option()
        elif (type == "circlet"):
            self.main_option = [ \
                "HP_%", \
                "ATK_%", \
                "DEF_%", \
                "CRIT_Rate", \
                "CRIT_DMG", \
                "Healing_Bonus", \
                "Elemental_Mastery" \
            ]
            self.main_option_p = [0.22, 0.22, 0.22, 0.1, 0.1, 0.1, 0.04]
            self.__set_main_option()
        else:
            print_error("type is incorrect.")

        # sub option
        if (type == "flower"):
            self.sub_option = [
                "ATK_+", \
                "DEF_+", \
                "HP_%", \
                "ATK_%", \
                "DEF_%", \
                "Energy_Recharge", \
                "Elemental_Mastery", \
                "CRIT_Rate", \
                "CRIT_DMG"
            ]
            self.sub_option_p = [0.1579, 0.1579, 0.1053, 0.1053, 0.1053, 0.1053, 0.1053, 0.0789, 0.0789]
            self.__set_sub_option()
        elif (type == "plume"):
            self.sub_option = [
                "HP_+", \
                "DEF_+", \
                "HP_%", \
                "ATK_%", \
                "DEF_%", \
                "Energy_Recharge", \
                "Elemental_Mastery", \
                "CRIT_Rate", \
                "CRIT_DMG" \
            ]
            self.sub_option_p = [0.1579, 0.1579, 0.1053, 0.1053, 0.1053, 0.1053, 0.1053, 0.0789, 0.0789]
            self.__set_sub_option()
        elif (type == "sands"):
            if (self.options["main"] == "HP_%"):
                self.sub_option = [
                    "HP_+", \
                    "ATK_+", \
                    "DEF_+", \
                    "ATK_%", \
                    "DEF_%", \
                    "Energy_Recharge", \
                    "Elemental_Mastery", \
                    "CRIT_Rate", \
                    "CRIT_DMG" \
                ]
            elif (self.options["main"] == "ATK_%"):
                self.sub_option = [
                    "HP_+", \
                    "ATK_+", \
                    "DEF_+", \
                    "HP_%", \
                    "DEF_%", \
                    "Energy_Recharge", \
                    "Elemental_Mastery", \
                    "CRIT_Rate", \
                    "CRIT_DMG" \
                ]
            elif (self.options["main"] == "DEF_%"):
                self.sub_option = [
                    "HP_+", \
                    "ATK_+", \
                    "DEF_+", \
                    "HP_%", \
                    "ATK_%", \
                    "Energy_Recharge", \
                    "Elemental_Mastery", \
                    "CRIT_Rate", \
                    "CRIT_DMG" \
                ]
            elif (self.options["main"] == "Energy_Recharge"):
                self.sub_option = [
                    "HP_+", \
                    "ATK_+", \
                    "DEF_+", \
                    "HP_%", \
                    "ATK_%", \
                    "DEF_%", \
                    "Elemental_Mastery", \
                    "CRIT_Rate", \
                    "CRIT_DMG" \
                ]
            elif (self.options["main"] == "Elemental_Mastery"):
                self.sub_option = [
                    "HP_+", \
                    "ATK_+", \
                    "DEF_+", \
                    "HP_%", \
                    "ATK_%", \
                    "DEF_%", \
                    "Energy_Recharge", \
                    "CRIT_Rate", \
                    "CRIT_DMG" \
                ]
            else:
                print_error("self.options is incorrect")
            self.sub_option_p = [0.15, 0.15, 0.15, 0.1, 0.1, 0.1, 0.1, 0.075, 0.075]
            self.__set_sub_option()
        elif (type == "goblet"):
            if (self.options["main"] == "HP_%"):
                self.sub_option = [
                    "HP_+", \
                    "ATK_+", \
                    "DEF_+", \
                    "ATK_%", \
                    "DEF_%", \
                    "Energy_Recharge", \
                    "Elemental_Mastery", \
                    "CRIT_Rate", \
                    "CRIT_DMG" \
                ]
                self.sub_option_p = [0.15, 0.15, 0.15, 0.1, 0.1, 0.1, 0.1, 0.075, 0.075]
            elif (self.options["main"] == "ATK_%"):
                self.sub_option = [
                    "HP_+", \
                    "ATK_+", \
                    "DEF_+", \
                    "HP_%", \
                    "DEF_%", \
                    "Energy_Recharge", \
                    "Elemental_Mastery", \
                    "CRIT_Rate", \
                    "CRIT_DMG" \
                ]
                self.sub_option_p = [0.15, 0.15, 0.15, 0.1, 0.1, 0.1, 0.1, 0.075, 0.075]
            elif (self.options["main"] == "DEF_%"):
                self.sub_option = [
                    "HP_+", \
                    "ATK_+", \
                    "DEF_+", \
                    "HP_%", \
                    "ATK_%", \
                    "Energy_Recharge", \
                    "Elemental_Mastery", \
                    "CRIT_Rate", \
                    "CRIT_DMG" \
                ]
                self.sub_option_p = [0.15, 0.15, 0.15, 0.1, 0.1, 0.1, 0.1, 0.075, 0.075]
            elif (self.options["main"] in \
                    [ \
                        "Pyro_DMG_Bonus", \
                        "Electro_DMG_Bonus", \
                        "Cryo_DMG_Bonus", \
                        "Hydro_DMG_Bonus", \
                        "Anemo_DMG_Bonus", \
                        "Geo_DMG_Bonus", \
                        "Physical_DMG_Bonus" \
                    ] \
                ):
                self.sub_option = [
                    "HP_+", \
                    "ATK_+", \
                    "DEF_+", \
                    "HP_%", \
                    "ATK_%", \
                    "DEF_%", \
                    "Energy_Recharge", \
                    "Elemental_Mastery", \
                    "CRIT_Rate", \
                    "CRIT_DMG" \
                ]
                self.sub_option_p = [0.1364, 0.1364, 0.1364, 0.0909, 0.0909, 0.0909, 0.0909, 0.0909, 0.0682, 0.0682]
            elif (self.options["main"] == "Elemental_Mastery"):
                self.sub_option = [
                    "HP_+", \
                    "ATK_+", \
                    "DEF_+", \
                    "HP_%", \
                    "ATK_%", \
                    "DEF_%", \
                    "Energy_Recharge", \
                    "CRIT_Rate", \
                    "CRIT_DMG" \
                ]
                self.sub_option_p = [0.15, 0.15, 0.15, 0.1, 0.1, 0.1, 0.1, 0.075, 0.075]
            else:
                print_error("self.options is incorrect")
            self.__set_sub_option()
        elif (type == "circlet"):
            if (self.options["main"] == "HP_%"):
                self.sub_option = [
                    "HP_+", \
                    "ATK_+", \
                    "DEF_+", \
                    "ATK_%", \
                    "DEF_%", \
                    "Energy_Recharge", \
                    "Elemental_Mastery", \
                    "CRIT_Rate", \
                    "CRIT_DMG" \
                ]
                self.sub_option_p = [0.15, 0.15, 0.15, 0.1, 0.1, 0.1, 0.1, 0.075, 0.075]
            elif (self.options["main"] == "ATK_%"):
                self.sub_option = [
                    "HP_+", \
                    "ATK_+", \
                    "DEF_+", \
                    "HP_%", \
                    "DEF_%", \
                    "Energy_Recharge", \
                    "Elemental_Mastery", \
                    "CRIT_Rate", \
                    "CRIT_DMG" \
                ]
                self.sub_option_p = [0.15, 0.15, 0.15, 0.1, 0.1, 0.1, 0.1, 0.075, 0.075]
            elif (self.options["main"] == "DEF_%"):
                self.sub_option = [
                    "HP_+", \
                    "ATK_+", \
                    "DEF_+", \
                    "HP_%", \
                    "ATK_%", \
                    "Energy_Recharge", \
                    "Elemental_Mastery", \
                    "CRIT_Rate", \
                    "CRIT_DMG" \
                ]
                self.sub_option_p = [0.15, 0.15, 0.15, 0.1, 0.1, 0.1, 0.1, 0.075, 0.075]
            elif (self.options["main"] == "CRIT_Rate"):
                self.sub_option = [
                    "HP_+", \
                    "ATK_+", \
                    "DEF_+", \
                    "HP_%", \
                    "ATK_%", \
                    "DEF_%", \
                    "Energy_Recharge", \
                    "Elemental_Mastery", \
                    "CRIT_DMG" \
                ]
                self.sub_option_p = [0.1463, 0.1463, 0.1463, 0.0976, 0.0976, 0.0976, 0.0976, 0.0976, 0.0732]
            elif (self.options["main"] == "CRIT_DMG"):
                self.sub_option = [
                    "HP_+", \
                    "ATK_+", \
                    "DEF_+", \
                    "HP_%", \
                    "ATK_%", \
                    "DEF_%", \
                    "Energy_Recharge", \
                    "Elemental_Mastery", \
                    "CRIT_Rate" \
                ]
                self.sub_option_p = [0.1463, 0.1463, 0.1463, 0.0976, 0.0976, 0.0976, 0.0976, 0.0976, 0.0732]
            elif (self.options["main"] == "Healing_Bonus"):
                self.sub_option = [
                    "HP_+", \
                    "ATK_+", \
                    "DEF_+", \
                    "HP_%", \
                    "ATK_%", \
                    "DEF_%", \
                    "Energy_Recharge", \
                    "Elemental_Mastery", \
                    "CRIT_Rate", \
                    "CRIT_DMG" \
                ]
                self.sub_option_p = [0.1364, 0.1364, 0.1364, 0.0909, 0.0909, 0.0909, 0.0909, 0.0909, 0.0682, 0.0682]
            elif (self.options["main"] == "Elemental_Mastery"):
                self.sub_option = [
                    "HP_+", \
                    "ATK_+", \
                    "DEF_+", \
                    "HP_%", \
                    "ATK_%", \
                    "DEF_%", \
                    "Energy_Recharge", \
                    "CRIT_Rate", \
                    "CRIT_DMG" \
                ]
                self.sub_option_p = [0.15, 0.15, 0.15, 0.1, 0.1, 0.1, 0.1, 0.075, 0.075]
            else:
                print_error("self.options is incorrect")
            self.__set_sub_option()

    def __set_main_option(self):
        if (sum(self.main_option_p) > 1.0):
            self.main_option_p[0] = self.main_option_p[0] - (sum(self.main_option_p) - 1.0)
        self.options["main"] = np.random.choice(self.main_option, p=self.main_option_p)

    def __set_sub_option(self):
        if (sum(self.sub_option_p) > 1.0):
            self.sub_option_p[0] = self.sub_option_p[0] - (sum(self.sub_option_p) - 1.0)
        if (np.random.random() <= RATE_4OP):
            sub_options = list(np.random.choice(self.sub_option, size=4, replace=False, p=self.sub_option_p))
        else:
            sub_options = list(np.random.choice(self.sub_option, size=3, replace=False, p=self.sub_option_p))
            sub_options.append(None)
        sub_options.sort(key=lambda x: (x is None, x))
        self.options["sub1"] = sub_options[0]
        self.options["sub2"] = sub_options[1]
        self.options["sub3"] = sub_options[2]
        self.options["sub4"] = sub_options[3]


def main():

    flower = Artifact(type="flower")
    print("flower.options: {}".format(flower.options))

    plume = Artifact(type="plume")
    print("plume.options: {}".format(plume.options))

    sands = Artifact(type="sands")
    print("sands.options: {}".format(sands.options))

    goblet = Artifact(type="goblet")
    print("goblet.options: {}".format(goblet.options))

    circlet = Artifact(type="circlet")
    print("circlet: {}".format(circlet.options))


if __name__ == '__main__':
    main()
