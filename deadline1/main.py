import re 

print("OK") if float(re.findall(r'(\d+\.\d+)%', open("SRR15859207_flagstat.txt", "r").read())[0]) > 90 else print("not OK")
