import numpy as np
import multiprocessing
import os
from tqdm import tqdm
from artifact import *


SHORT_PROGRESS_BAR="{l_bar}{bar:20}{r_bar}{bar:-10b}"
RATE_2PICK = 0.07


def calc_trial_get_artifact(seed, type, options):
    np.random.seed(seed)
    trial = 0
    while (True):
        trial += 1
        pick_artifact = Artifact(type=type)
        if (pick_artifact.options == options):
            break
        if (np.random.random() <= RATE_2PICK):
            pick_artifact = Artifact(type=type)
            if (pick_artifact.options == options):
                break
    trial = 2*trial  # 2 type artifacts in 1 domain
    return trial


def wrap_calc_trial_get_artifact(args):
    return calc_trial_get_artifact(*args)


def calc_average_trial_get_artifact(type, options, sample_num, process):
    artifact_type = ["flower", "plume", "sands", "goblet", "circlet"]
    get_num = []
    if (process == "single"):
        for seed in tqdm(range(sample_num), bar_format=SHORT_PROGRESS_BAR):
            seed += sample_num*artifact_type.index(type)
            get_num.append(calc_trial_get_artifact(seed, type, options))
    elif (process == "multi"):
        pool = multiprocessing.Pool(processes=multiprocessing.cpu_count()-1)
        args = []
        for seed in range(sample_num):
            seed += sample_num*artifact_type.index(type)
            args.append((seed, type, options))
        imap = pool.imap(wrap_calc_trial_get_artifact, args)
        get_num = list(tqdm(imap, total=len(args), bar_format=SHORT_PROGRESS_BAR))
    else:
        print_error("process is incorrect.")
    print_info("type={}: average trial={}: {}".format(type, np.mean(get_num), options))
    np.save(os.path.join("..", "data", type+"_"+"sample="+str(sample_num)+".npy"), np.array(get_num))


def sim_case_1():
    sample_num = 1000
    
    print_info("start flower")
    target_options = {"main":"HP_+", "sub1":"CRIT_DMG", "sub2":"CRIT_Rate", "sub3":"Energy_Recharge", "sub4":"HP_%"}
    calc_average_trial_get_artifact(type="flower", options=target_options, sample_num=sample_num, process="multi")

    print_info("start plume")
    target_options = {"main":"ATK_+", "sub1":"CRIT_DMG", "sub2":"CRIT_Rate", "sub3":"Energy_Recharge", "sub4":"HP_%"}
    calc_average_trial_get_artifact(type="plume", options=target_options, sample_num=sample_num, process="multi")
    
    print_info("start sands")
    target_options = {"main":"HP_%", "sub1":"CRIT_DMG", "sub2":"CRIT_Rate", "sub3":"Energy_Recharge", "sub4":"HP_+"}
    calc_average_trial_get_artifact(type="sands", options=target_options, sample_num=sample_num, process="multi")

    print_info("start goblet")
    target_options = {"main":"Hydro_DMG_Bonus", "sub1":"CRIT_DMG", "sub2":"CRIT_Rate", "sub3":"Energy_Recharge", "sub4":"HP_%"}
    calc_average_trial_get_artifact(type="goblet", options=target_options, sample_num=sample_num, process="multi")

    print_info("start circlet")
    target_options = {"main":"CRIT_Rate", "sub1":"CRIT_DMG", "sub2":"Energy_Recharge", "sub3":"HP_%", "sub4":"HP_+"}
    calc_average_trial_get_artifact(type="circlet", options=target_options, sample_num=sample_num, process="multi")


def main():
    sim_case_1()


if __name__ == "__main__":
    main()
