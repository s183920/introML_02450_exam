import toolbox_extended as te
import toolbox_02450 as tb
import numpy as np
import pandas as pd
from exam_toolbox import *
import re
import os


class exam:

    # ----------------------------------------------- OPG 1-----------------------------------------------
    def opg1():

        return "E"

    # ----------------------------------------------- OPG 2-----------------------------------------------
    def opg2():

        return "E"

    # ----------------------------------------------- OPG 3-----------------------------------------------
    def opg3():

        return "E"

    # ----------------------------------------------- OPG 4-----------------------------------------------
    def opg4():

        return "E"

    # ----------------------------------------------- OPG 5-----------------------------------------------
    def opg5():

        return "E"

    # ----------------------------------------------- OPG 6-----------------------------------------------
    def opg6():

        return "E"

    # ----------------------------------------------- OPG 7-----------------------------------------------
    def opg7():

        return "E"

    # ----------------------------------------------- OPG 8-----------------------------------------------
    def opg8():

        return "E"

    # ----------------------------------------------- OPG 9-----------------------------------------------
    def opg9():

        return "E"

    # ----------------------------------------------- OPG 10-----------------------------------------------
    def opg10():

        return "E"

    # ----------------------------------------------- OPG 11-----------------------------------------------
    def opg11():

        return "E"

    # ----------------------------------------------- OPG 12-----------------------------------------------
    def opg12():

        return "E"

    # ----------------------------------------------- OPG 13-----------------------------------------------
    def opg13():

        return "E"

    # ----------------------------------------------- OPG 14-----------------------------------------------
    def opg14():
        print()
        return "E"

    # ----------------------------------------------- OPG 15-----------------------------------------------
    def opg15():

        return "E"

    # ----------------------------------------------- OPG 16-----------------------------------------------
    def opg16():

        return "E"

    # ----------------------------------------------- OPG 17-----------------------------------------------
    def opg17():

        return "E"

    # ----------------------------------------------- OPG 18-----------------------------------------------
    def opg18():

        return "E"

    # ----------------------------------------------- OPG 19-----------------------------------------------
    def opg19():

        return "E"

    # ----------------------------------------------- OPG 20-----------------------------------------------
    def opg20():

        return "E"

    # ----------------------------------------------- OPG 21-----------------------------------------------
    def opg21():

        return "E"

    # ----------------------------------------------- OPG 22-----------------------------------------------
    def opg22():

        return "E"

    # ----------------------------------------------- OPG 23-----------------------------------------------
    def opg23():

        return "E"

    # ----------------------------------------------- OPG 24-----------------------------------------------
    def opg24():

        return "E"

    # ----------------------------------------------- OPG 25-----------------------------------------------
    def opg25():

        return "E"

    # ----------------------------------------------- OPG 26-----------------------------------------------
    def opg26():

        return "E"

    # ----------------------------------------------- OPG 27-----------------------------------------------
    def opg27():

        return "E"

    # -------------------------------- answers dataframe -------------------------------------------------
    def answers(show=True, csv=False, excel=True):
        ans = pd.DataFrame(
            columns=["Student number: s183920"]
        )  # columns = ["OPG", "svar"])

        ans.loc[0] = ""
        ans.loc[1] = "Q01: {}".format(exam.opg1())
        ans.loc[2] = "Q02: {}".format(exam.opg2())
        ans.loc[3] = "Q03: {}".format(exam.opg3())
        ans.loc[4] = "Q04: {}".format(exam.opg4())
        ans.loc[5] = "Q05: {}".format(exam.opg5())
        ans.loc[6] = "Q06: {}".format(exam.opg6())
        ans.loc[7] = "Q07: {}".format(exam.opg7())
        ans.loc[8] = "Q08: {}".format(exam.opg8())
        ans.loc[9] = "Q09: {}".format(exam.opg9())
        ans.loc[10] = "Q10: {}".format(exam.opg10())
        ans.loc[11] = ""

        ans.loc[12] = "Q11: {}".format(exam.opg11())
        ans.loc[13] = "Q12: {}".format(exam.opg12())
        ans.loc[14] = "Q13: {}".format(exam.opg13())
        ans.loc[15] = "Q14: {}".format(exam.opg14())
        ans.loc[16] = "Q15: {}".format(exam.opg15())
        ans.loc[17] = "Q16: {}".format(exam.opg16())
        ans.loc[18] = "Q17: {}".format(exam.opg17())
        ans.loc[19] = "Q18: {}".format(exam.opg18())
        ans.loc[20] = "Q19: {}".format(exam.opg19())
        ans.loc[21] = "Q20: {}".format(exam.opg20())
        ans.loc[22] = ""

        ans.loc[23] = "Q21: {}".format(exam.opg21())
        ans.loc[24] = "Q22: {}".format(exam.opg22())
        ans.loc[25] = "Q23: {}".format(exam.opg23())
        ans.loc[26] = "Q24: {}".format(exam.opg24())
        ans.loc[27] = "Q25: {}".format(exam.opg25())
        ans.loc[28] = "Q26: {}".format(exam.opg26())
        ans.loc[29] = "Q27: {}".format(exam.opg27())

        if excel:
            ans.to_excel(re.sub(".py", "_answers.xlsx", __file__), index=False)
        if csv:
            ans.to_csv(re.sub(".py", "_answers.csv", __file__), index=False)
        if show:
            print(ans)

        return ans


exam.answers()
