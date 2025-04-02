import os
import shutil

"""
Get a list of all type B images's names (with extension) and put them in test_list.txt with one per line. Then run this script after running your classifier.
Make sure you have a set that's already separated, for calculating the threshold and testing your classifier's accuracy.
False positives and undetected images will be copied to test/false_positive and test/undetected for further debugging.
"""
TYPEA_FOLDER = "TypeA"  # Change these
TYPEB_FOLDER = "TypeB"


def main() -> None:
    os.makedirs("test", exist_ok=True)
    os.makedirs("test/false_positive", exist_ok=True)
    os.makedirs("test/undetected", exist_ok=True)
    total = 0
    for i in os.listdir("TYPEA_FOLDER"):
        total += 1
    for i in os.listdir("TYPEB_FOLDER"):
        total += 1
    success = []
    false_positive = []
    undetected = []
    with open("test_list.txt", "r") as f:
        na = f.read()
    na = na.split("\n")
    typeA_img = os.listdir("TYPEA_FOLDER")
    typeB_img = os.listdir("TYPEB_FOLDER")
    for i in typeB_img:
        if i in na:
            success.append(i)
        else:
            false_positive.append(i)
            shutil.copy(os.path.join("typeB_img", i), "test/false_positive")
    for i in typeA_img:
        if i in na:
            undetected.append(i)
            shutil.copy(os.path.join("typeA_img", i), "test/undetected")
        else:
            success.append(i)
    print(f"Success: {len(success)}/{total}")
    print(f"False Positive: {len(false_positive)}/{total}")
    print(f"Undetected: {len(undetected)}/{total}")


if "__main__" == __name__:
    main()
