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

