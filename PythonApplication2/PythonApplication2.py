# Скрипт для фывфвыфывфв

import numpy as np

# Женские Имена
NFF_char = '<LocalizedString identifier="NAME_FEMALE_FIRST">'
global_char = '</LocalizedString>'

# Женсие Фамилии
NLF_char = '<LocalizedString identifier="NAME_FEMALE_LAST">{0} '

# Мужские Имена
MFN_char = '<LocalizedString identifier="NAME_MALE_FIRST">'

# Мужские фамилии
MLN_char = '<LocalizedString identifier="NAME_MALE_LAST">{0} '

FemFirstNames = np.loadtxt('input/femFirstName.txt', dtype='str') # Женские Имена

FemLastNames = np.loadtxt('input/femLastName.txt', dtype='str') # Женсие Фамилии

MaleFirstNames = np.loadtxt('input/MaleFirstName.txt', dtype='str') # Мужские Имена

MaleLastNames = np.loadtxt('input/MaleLastName.txt', dtype='str') # Мужские фамилии


ffn_file = open("output/FemaleFirstNames_out.txt", "w+")
fln_file = open("output/FemaleLastNames_out.txt", "w+")
mfn_file = open("output/MaleFirstNames_out.txt", "w+")
mln_file = open("output/MaleLasttNames_out.txt", "w+")

# Женские Имена
for word in FemFirstNames:

    print('<LocalizedString identifier="NAME_FEMALE_FIRST">', word, '</LocalizedString>',sep='')
    
    ffn_file.write('\t'+ f"{NFF_char}{word}{global_char}"+ '\n')

# Женсие Фамилии
for word in FemLastNames:

    fln_file.write('\t'+ f"{NLF_char}{word}{global_char}"+ '\n')


# Мужские Имена
for word in MaleFirstNames:

    mfn_file.write('\t'+ f"{MFN_char}{word}{global_char}"+ '\n')

# Мужские фамилии
for word in MaleLastNames:

    mln_file.write('\t'+ f"{MLN_char}{word}{global_char}"+ '\n')

ffn_file.close
fln_file.close
mln_file.close
mfn_file.close
