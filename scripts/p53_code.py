import random
#פונקציות של מוטציה:

#פונקציה המקבלת את רצף הנגיף, בוחרת מיקום אקראי ברצף ומחליפה בו את הנוקלאוטיד באופן רנדומלי, מחזירה את רצף הגנום עם המוטציה
def Mutate_DNA(seq):
  base_list = ["A", "T", "C", "G"]
  rand_base = random.randrange(0,len(seq))
  if seq[rand_base] == "A":
    base_list.remove("A")
  elif seq[rand_base] == "T":
    base_list.remove("T")
  elif seq[rand_base] == "C":
    base_list.remove("C")
  elif seq[rand_base] == "G":
    base_list.remove("G")
  new_base = random.choice(base_list)
  mut_seq = seq[0:rand_base] + new_base + seq[rand_base+1:]
  return mut_seq
#פונקציה המכניסה במיקום אקראי לרצף נוקלאוטיד נוסף
def Insert_DNA(seq):
  base_list = ["A", "T", "C", "G"]
  rand_base = random.randrange(0,len(seq))
  new_base = random.choice(base_list)
  mut_seq = seq[0:rand_base] + new_base + seq[rand_base:]
  return mut_seq
 
# פונקציה המסירה נוקלאוטיד במקום אקראי ברצף
def Delete_DNA(seq):
  rand_base = random.randrange(0,len(seq))
  mut_seq = seq[0:rand_base] + seq[rand_base+1:]
  return mut_seq

#פונקציה המקבלת קובץ דנ"א והופכת אותו לרצף רנ"א
def DNA_RNA_Cod(DNA):
  delimiter = ""
  line_list = []
  DNA = DNA.upper()
  for ch in DNA:
    if ch == "T":
      line_list.append("U")
    else:
      line_list.append(ch)
  RNA = delimiter.join(line_list)
  return RNA

#פונקציה שמקבלת קובץ חומצות אמיניות ואת הקיצורים שלהן ומכניסה אותן למילון גלובלי
def Read_dict():
  global RNA_codon_table
  file = open("data/codon_AA.txt")
  for line in file:
    line = line.rstrip("\r\n")
    (codon,dev,AA) = line.partition("\t")
    RNA_codon_table[codon] = AA
  file.close()


#פונקציה המקבלת רצף רנ"א ומתרגמת אותו לחומצות האמיניות מהן הוא מורכב
def RNA_prot(RNA):
  AA_protein = ""
  for i in range(0, len(RNA), 3):
    codon = RNA[i:i+3]
    if len(codon) == 3:
      if codon in RNA_codon_table:
        if RNA_codon_table[codon] == "*":
          AA_protein += (RNA_codon_table[codon])
          break
        else:
          AA_protein += (RNA_codon_table[codon])
  return AA_protein


### main program ###

#יצירת מילון הקודונים
RNA_codon_table = {}
Read_dict()

file = open("data/human_p53_coding.txt")
results_file = open("results/mutated_p53.fasta", "w")
p53_seq = ""
for line in file:
  if line[0] == ">":
    continue
  else:
    line = line.rstrip("\n\r")
    line = line.upper()
    p53_seq += line


mut_p53_seq = p53_seq
gen = 3
for i in range(gen):
  rand_mut = random.randrange(0,3)
  if rand_mut == 0:
    mut_p53_seq = Mutate_DNA(mut_p53_seq)
  elif rand_mut == 1:
    mut_p53_seq = Insert_DNA(mut_p53_seq)
  elif rand_mut == 2:
    mut_p53_seq = Delete_DNA(mut_p53_seq)


#תעתוק ותרגום הרצף המקורי  והרצף החדש
mut_p53_seq = DNA_RNA_Cod(mut_p53_seq)
mut_p53_seq = RNA_prot(mut_p53_seq)
p53_seq = DNA_RNA_Cod(p53_seq)
p53_seq = RNA_prot(p53_seq)

results_file.write("original protein sequance:\n%s\n" %p53_seq)
results_file.write("mutated protein sequance:\n%s\n" %mut_p53_seq)
conc = input("What is your conclusion? Did the protein get shorter?")
results_file.write(conc)
file.close()
results_file.close()
