import argparse

parser = argparse.ArgumentParser()
group1 = parser.add_mutually_exclusive_group()
group1.add_argument("-tr", "--train", help="Training", action='store_true')
group1.add_argument("-te", "--test", help="Testing", action='store_true')
group3 = parser.add_argument_group()
group3.add_argument("-pr", "--predict", help="Predict", action='store_true')
group3.add_argument("-w", "--weight", type=int, help="Weight")
group3.add_argument("-s", "--surface", help="Surface")

args = parser.parse_args()
