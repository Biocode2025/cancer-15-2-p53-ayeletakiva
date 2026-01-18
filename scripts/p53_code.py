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
          #break
        else:
          AA_protein += (RNA_codon_table[codon])
  return AA_protein


