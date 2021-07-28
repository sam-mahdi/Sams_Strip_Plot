hnca='Delta_Prime_HNCA.list'
hncacb='Delta_Prime_HNCACB.list'
hncaco=''
hncoca='Delta_Prime_HNCOCA.list'
hnco='Delta_Prime_HNCO.list'
NOE='Delta_Prime_N15_NOE.list'

carbon_tolerance=0.2
hydrogen_tolerance=0.1

i_minus_CA=57.7
i_minus_CB=39.6
i_minus_CO=''
i_nitrogen=121.470

NOE_NH=[]
NOE_HA=[]
i_NOE=[]

"""i-1 matches"""
CA_matches=[]
CA_CB_matches=[]
CO_matches=[]
CA_CO_matches=[]
CA_CB_CO_matches=[]
NOE_NH_matches=[]
NOE_HA_matches=[]

"""i+1 matches"""
i_CA_matches=[]
i_CA_CA_matches=[]
CA_CO_i_CA_matches=[]
CA_CB_i_CA_matches=[]
CA_CB_CO_i_CA_matches=[]

"""i-1 matches"""

CA_only_flag=False
CA_CB_flag=True
CA_CO_flag=False
CA_CB_CO_flag=False

"""i+1 matches"""
i_CA_flag=False
for_CA_CO_flag=False
i_CA_CA_flag=False
CA_CO_i_CA_flag=False
for_CA_CB_CO_flag=False
CA_CB_i_CA_flag=False
CA_CB_CO_i_CA_flag=False

NH_flag=True
HA_flag=True
"""i-1 matches"""
display_CA_only_flag=False
display_CA_CB_only_flag=True
display_CA_CO_only_flag=False
display_CA_CB_CO_flag=False

"""i+1 matches"""
display_i_CA_flag=False
display_i_CA_CA_flag=False
display_CA_CO_i_CA_flag=False
display_CA_CB_i_CA_flag=False
display_CA_CB_CO_i_CA_flag=False
display_for_CA_CO_flag=False
display_for_CA_CB_CO_flag=False


display_NH_NOE_flag=True
display_HA_NOE_flag=True
display_combined_NH_HA_NOE_flag=True




def HNCA_match():
    global CA_matches
    with open(hnca) as hnca_file:
        for lines in hnca_file:
            if lines == '' or lines == '\n':
                continue
            if lines.strip().split()[0]=='Assignment':
                continue
            nitrogen_value=float(lines.strip().split()[1])
            CA_value=float(lines.strip().split()[2])
            if CA_value > (i_minus_CA-carbon_tolerance) and CA_value < (i_minus_CA+carbon_tolerance):
                CA_matches.append(nitrogen_value)

def HNCACB_match():
    global CA_CB_matches
    for entries in CA_matches:
        with open(hncacb) as hncacb_file:
            for lines in hncacb_file:
                if lines == '' or lines == '\n':
                    continue
                if lines.split() == []:
                    continue
                if lines.strip().split()[0]=='Assignment':
                    continue
                nitrogen_value=float(lines.strip().split()[1])
                CB_value=float(lines.strip().split()[2])
                if nitrogen_value == entries:
                    if CB_value > (i_minus_CB-carbon_tolerance) and CB_value < (i_minus_CB+carbon_tolerance):
                        CA_CB_matches.append(nitrogen_value)


def HNCACO():
    global CO_matches
    with open(hncaco) as hnco_file:
        for lines in hnco_file:
            if lines == '' or lines == '\n':
                continue
            if lines.strip().split()[0]=='Assignment':
                continue
            nitrogen_value=float(lines.strip().split()[1])
            CO_value=float(lines.strip().split()[2])
            if CO_value > (i_minus_CO-carbon_tolerance) and CO_value < (i_minus_CO+carbon_tolerance):
                CO_matches.append(nitrogen_value)

def HNCOCA():
    global i_CA_matches
    with open(hncoca) as hncoca_file:
        for lines in hncoca_file:
            if lines == '' or lines == '\n':
                continue
            if lines.strip().split()[0]=='Assignment':
                continue
            nitrogen_value=float(lines.strip().split()[1])
            i_CA_value=float(lines.strip().split()[2])
            if i_CA_value > (i_minus_CA-carbon_tolerance) and CO_value < (i_minus_CA+carbon_tolerance):
                i_CA_matches.append(nitrogen_value)

def i_HNCO():
    global CO_matches
    with open(hnco) as hnco_file:
        for lines in hnco_file:
            if lines == '' or lines == '\n':
                continue
            if lines.strip().split()[0]=='Assignment':
                continue
            nitrogen_value=float(lines.strip().split()[1])
            CO_value=float(lines.strip().split()[2])
            if CO_value > (i_minus_CO-carbon_tolerance) and CO_value < (i_minus_CO+carbon_tolerance):
                CO_matches.append(nitrogen_value)


def HNCOCA_HNCA():
    for entries in i_CA_matches:
        for values in CA_matches:
            if entries == values:
                i_CA_CA_matches.append(entries)

def HNCA_HNCACO_HNCOCA():
    global CA_CO_i_CA_matches
    for entries in CA_CO_matches:
        for values in i_CA_matches:
            if entries == values:
                CA_CO_i_CA_matches.append(entries)

def HNCA_HNCACO():
    global CA_CO_matches
    for entries in CA_matches:
        for values in CO_matches:
            if entries == values:
                CA_CO_matches.append(entries)

def HNCA_CB_HNCACO():
    global CA_CB_CO_matches
    for entries in CA_CB_matches:
        for values in CO_matches:
            if entries == values:
                CA_CB_CO_matches.append(entries)

def HNCA_CB_i_CA():
    global CA_CB_i_CA_matches
    for entries in CA_CB_matches:
        for values in i_CA_matches:
            if entries == values:
                CA_CB_i_CA_matches.append(entries)

def HNCA_CB_CO_i_CA():
    global CA_CB_CO_i_CA_matches
    for entries in CA_CB_CO_matches:
        for values in i_CA_matches:
            if entries == values:
                CA_CB_CO_i_CA_matches.append(entries)

def NOE_matches(list):
    global NOE_NH
    global NOE_HA
    for entries in list:
        with open(NOE) as noe_file:
            for lines in noe_file:
                if lines == '' or lines == '\n':
                    continue
                if lines.strip().split()[0]=='Assignment':
                    continue
                nitrogen=float(lines.strip().split()[1])
                hydrogen=float(lines.strip().split()[2])
                if entries == nitrogen:
                    if hydrogen < 12 and hydrogen > 6:
                        NOE_NH.append(str(nitrogen)+' '+str(hydrogen))
                    if hydrogen < 6 and hydrogen > 3.5:
                        NOE_HA.append(str(nitrogen)+' '+str(hydrogen))

def i_noes():
    global i_NOE
    with open(NOE) as noe_file:
        for lines in noe_file:
            if lines == '' or lines == '\n':
                continue
            if lines.strip().split()[0]=='Assignment':
                continue
            nitrogen=float(lines.strip().split()[1])
            hydrogen=float(lines.strip().split()[2])
            if nitrogen == i_nitrogen:
                i_NOE.append(hydrogen)

def NOE_i_NH_match():
    global NOE_NH_matches
    for values in i_NOE:
        for entries in NOE_NH:
            nitrogen=float(entries.split()[0])
            hydrogen=float(entries.split()[1])
            if hydrogen > (values-hydrogen_tolerance) and hydrogen < (values+hydrogen_tolerance):
                if nitrogen not in NOE_NH_matches:
                    NOE_NH_matches.append(nitrogen)
def NOE_i_HA_match():
    global NOE_HA_matches
    for values in i_NOE:
        for entries in NOE_HA:
            nitrogen=float(entries.split()[0])
            hydrogen=float(entries.split()[1])
            if hydrogen > (values-hydrogen_tolerance) and hydrogen < (values+hydrogen_tolerance):
                if nitrogen not in NOE_HA_matches:
                    NOE_HA_matches.append(nitrogen)

def run():
    i_noes()
    if CA_only_flag is True:
        print('CA Only')
        HNCA_match()
        list=CA_matches
    if CA_CB_flag is True:
        print('CA and CB')
        HNCA_match()
        HNCACB_match()
        list=CA_CB_matches
    if CA_CO_flag is True:
        print('CA and CO')
        HNCA_match()
        HNCACO()
        HNCA_HNCACO()
        list=CA_CO_matches
    if CA_CB_CO_flag is True:
        print('CA, CB, and CO')
        HNCA_match()
        HNCACO()
        HNCACB_match()
        HNCA_CB_HNCACO()
        list=CA_CB_CO_matches
    if i_CA_flag is True:
        print('i_CA [HNCOCA]')
        HNCOCA()
        list=i_CA_matches
    if i_CA_CA_flag is True:
        print('HNCOCA and CA')
        HNCA()
        HNCOCA()
        HNCOCA_HNCA()
        list=i_CA_CA_matches
    if for_CA_CO_flag is True:
        print('CA and CO')
        HNCA()
        i_HNCO()
        HNCA_HNCACO()
        list=CA_CO_matches
    if CA_CO_i_CA_flag is True:
        print('CA, CO, and HNCOCA')
        HNCA()
        i_HNCO()
        HNCA_HNCACO()
        HNCA_HNCACO_HNCOCA()
        list=CA_CO_i_CA_matches
    if for_CA_CB_CO_flag is True:
        print('CA, CB, CO')
        HNCA()
        HNCACB()
        i_HNCO()
        HNCA_CB_HNCACO()
        list=CA_CB_CO_matches
    if CA_CB_i_CA_flag is True:
        print('CA, CB, HNCOCA')
        HNCA()
        HNCACB()
        HNCOCA()
        HNCA_CB_i_CA()
        list=CA_CB_i_CA_matches
    if CA_CB_CO_i_CA_flag is True:
        print('CA, CB, CO, HNCOCA')
        HNCA()
        HNCACB()
        i_HNCO()
        HNCA_CB_HNCACO()
        HNCOCA()
        HNCA_CB_CO_i_CA()
        list=CA_CB_CO_i_CA_matches
    if NH_flag is True:
        NOE_matches(list)
        NOE_i_NH_match()
    if HA_flag is True:
        NOE_matches(list)
        NOE_i_HA_match()

def display():
    run()
    if display_CA_only_flag is True:
        for entries in CA_matches:
            print(entries)
    if display_CA_CB_only_flag is True:
        for entries in CA_CB_matches:
            print(entries)
    if display_CA_CO_only_flag is True or display_for_CA_CO_flag is True:
        for entries in CA_CO_matches:
            print(entries)
    if display_CA_CB_CO_flag is True or display_for_CA_CB_CO_flag is True:
        for entries in CA_CB_CO_matches:
            print(entries)
    if display_i_CA_flag is True:
        for entries in i_CA_matches:
            print(entries)
    if display_i_CA_CA_flag is True:
        for entries in i_CA_CA_matches:
            print(entries)
    if display_CA_CO_i_CA_flag is True:
        for entries in CA_CO_i_CA_matches:
            print(entries)
    if display_CA_CB_i_CA_flag is True:
        for entries in CA_CB_i_CA_matches:
            print(entries)
    if display_CA_CB_CO_i_CA_flag is True:
        for entries in CA_CB_CO_i_CA_matches:
            print(entries)
    if display_NH_NOE_flag is True:
        print('NOE_NH_Matches')
        for entries in NOE_NH_matches:
            print(entries)
    if display_HA_NOE_flag is True:
        print('NOE_HA_Matches')
        for entries in NOE_HA_matches:
            print(entries)
    if display_combined_NH_HA_NOE_flag is True:
        print('NH and HA combined')
        for entries in set.intersection(set(NOE_HA_matches),set(NOE_NH_matches)):
            print(entries)

display()
