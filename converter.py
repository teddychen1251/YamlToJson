import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

yaml = open(args.file)
base_name = yaml.name.split("/")[-1].split(".")[0]
print(base_name)
yaml.close()
