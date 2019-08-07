import numpy as np

schema_train_transaction = {'TransactionID': np.int32,
 'isFraud': np.int8,
 'TransactionDT': np.int32,
 'TransactionAmt': np.float16,
 'ProductCD': 'object',
 'card1': np.int16,
 'card2': np.float16,
 'card3': np.float16,
 'card4': 'object',
 'card5': np.float16,
 'card6': 'object',
 'addr1': np.float16,
 'addr2': np.float16,
 'dist1': np.float16,
 'dist2': np.float16,
 'P_emaildomain': 'object',
 'R_emaildomain': 'object',
 'C1': np.float16,
 'C2': np.float16,
 'C3': np.float16,
 'C4': np.float16,
 'C5': np.float16,
 'C6': np.float16,
 'C7': np.float16,
 'C8': np.float16,
 'C9': np.float16,
 'C10': np.float16,
 'C11': np.float16,
 'C12': np.float16,
 'C13': np.float16,
 'C14': np.float16,
 'D1': np.float16,
 'D2': np.float16,
 'D3': np.float16,
 'D4': np.float16,
 'D5': np.float16,
 'D6': np.float16,
 'D7': np.float16,
 'D8': np.float16,
 'D9': np.float16,
 'D10': np.float16,
 'D11': np.float16,
 'D12': np.float16,
 'D13': np.float16,
 'D14': np.float16,
 'D15': np.float16,
 'M1': 'object',
 'M2': 'object',
 'M3': 'object',
 'M4': 'object',
 'M5': 'object',
 'M6': 'object',
 'M7': 'object',
 'M8': 'object',
 'M9': 'object',
 'V1': np.float16,
 'V2': np.float16,
 'V3': np.float16,
 'V4': np.float16,
 'V5': np.float16,
 'V6': np.float16,
 'V7': np.float16,
 'V8': np.float16,
 'V9': np.float16,
 'V10': np.float16,
 'V11': np.float16,
 'V12': np.float16,
 'V13': np.float16,
 'V14': np.float16,
 'V15': np.float16,
 'V16': np.float16,
 'V17': np.float16,
 'V18': np.float16,
 'V19': np.float16,
 'V20': np.float16,
 'V21': np.float16,
 'V22': np.float16,
 'V23': np.float16,
 'V24': np.float16,
 'V25': np.float16,
 'V26': np.float16,
 'V27': np.float16,
 'V28': np.float16,
 'V29': np.float16,
 'V30': np.float16,
 'V31': np.float16,
 'V32': np.float16,
 'V33': np.float16,
 'V34': np.float16,
 'V35': np.float16,
 'V36': np.float16,
 'V37': np.float16,
 'V38': np.float16,
 'V39': np.float16,
 'V40': np.float16,
 'V41': np.float16,
 'V42': np.float16,
 'V43': np.float16,
 'V44': np.float16,
 'V45': np.float16,
 'V46': np.float16,
 'V47': np.float16,
 'V48': np.float16,
 'V49': np.float16,
 'V50': np.float16,
 'V51': np.float16,
 'V52': np.float16,
 'V53': np.float16,
 'V54': np.float16,
 'V55': np.float16,
 'V56': np.float16,
 'V57': np.float16,
 'V58': np.float16,
 'V59': np.float16,
 'V60': np.float16,
 'V61': np.float16,
 'V62': np.float16,
 'V63': np.float16,
 'V64': np.float16,
 'V65': np.float16,
 'V66': np.float16,
 'V67': np.float16,
 'V68': np.float16,
 'V69': np.float16,
 'V70': np.float16,
 'V71': np.float16,
 'V72': np.float16,
 'V73': np.float16,
 'V74': np.float16,
 'V75': np.float16,
 'V76': np.float16,
 'V77': np.float16,
 'V78': np.float16,
 'V79': np.float16,
 'V80': np.float16,
 'V81': np.float16,
 'V82': np.float16,
 'V83': np.float16,
 'V84': np.float16,
 'V85': np.float16,
 'V86': np.float16,
 'V87': np.float16,
 'V88': np.float16,
 'V89': np.float16,
 'V90': np.float16,
 'V91': np.float16,
 'V92': np.float16,
 'V93': np.float16,
 'V94': np.float16,
 'V95': np.float16,
 'V96': np.float16,
 'V97': np.float16,
 'V98': np.float16,
 'V99': np.float16,
 'V100': np.float16,
 'V101': np.float16,
 'V102': np.float16,
 'V103': np.float16,
 'V104': np.float16,
 'V105': np.float16,
 'V106': np.float16,
 'V107': np.float16,
 'V108': np.float16,
 'V109': np.float16,
 'V110': np.float16,
 'V111': np.float16,
 'V112': np.float16,
 'V113': np.float16,
 'V114': np.float16,
 'V115': np.float16,
 'V116': np.float16,
 'V117': np.float16,
 'V118': np.float16,
 'V119': np.float16,
 'V120': np.float16,
 'V121': np.float16,
 'V122': np.float16,
 'V123': np.float16,
 'V124': np.float16,
 'V125': np.float16,
 'V126': np.float32,
 'V127': np.float32,
 'V128': np.float32,
 'V129': np.float16,
 'V130': np.float16,
 'V131': np.float16,
 'V132': np.float32,
 'V133': np.float32,
 'V134': np.float32,
 'V135': np.float32,
 'V136': np.float32,
 'V137': np.float32,
 'V138': np.float16,
 'V139': np.float16,
 'V140': np.float16,
 'V141': np.float16,
 'V142': np.float16,
 'V143': np.float16,
 'V144': np.float16,
 'V145': np.float16,
 'V146': np.float16,
 'V147': np.float16,
 'V148': np.float16,
 'V149': np.float16,
 'V150': np.float16,
 'V151': np.float16,
 'V152': np.float16,
 'V153': np.float16,
 'V154': np.float16,
 'V155': np.float16,
 'V156': np.float16,
 'V157': np.float16,
 'V158': np.float16,
 'V159': np.float16,
 'V160': np.float32,
 'V161': np.float16,
 'V162': np.float16,
 'V163': np.float16,
 'V164': np.float32,
 'V165': np.float32,
 'V166': np.float32,
 'V167': np.float16,
 'V168': np.float16,
 'V169': np.float16,
 'V170': np.float16,
 'V171': np.float16,
 'V172': np.float16,
 'V173': np.float16,
 'V174': np.float16,
 'V175': np.float16,
 'V176': np.float16,
 'V177': np.float16,
 'V178': np.float16,
 'V179': np.float16,
 'V180': np.float16,
 'V181': np.float16,
 'V182': np.float16,
 'V183': np.float16,
 'V184': np.float16,
 'V185': np.float16,
 'V186': np.float16,
 'V187': np.float16,
 'V188': np.float16,
 'V189': np.float16,
 'V190': np.float16,
 'V191': np.float16,
 'V192': np.float16,
 'V193': np.float16,
 'V194': np.float16,
 'V195': np.float16,
 'V196': np.float16,
 'V197': np.float16,
 'V198': np.float16,
 'V199': np.float16,
 'V200': np.float16,
 'V201': np.float16,
 'V202': np.float32,
 'V203': np.float32,
 'V204': np.float32,
 'V205': np.float16,
 'V206': np.float16,
 'V207': np.float16,
 'V208': np.float16,
 'V209': np.float16,
 'V210': np.float16,
 'V211': np.float32,
 'V212': np.float32,
 'V213': np.float32,
 'V214': np.float32,
 'V215': np.float32,
 'V216': np.float32,
 'V217': np.float16,
 'V218': np.float16,
 'V219': np.float16,
 'V220': np.float16,
 'V221': np.float16,
 'V222': np.float16,
 'V223': np.float16,
 'V224': np.float16,
 'V225': np.float16,
 'V226': np.float16,
 'V227': np.float16,
 'V228': np.float16,
 'V229': np.float16,
 'V230': np.float16,
 'V231': np.float16,
 'V232': np.float16,
 'V233': np.float16,
 'V234': np.float16,
 'V235': np.float16,
 'V236': np.float16,
 'V237': np.float16,
 'V238': np.float16,
 'V239': np.float16,
 'V240': np.float16,
 'V241': np.float16,
 'V242': np.float16,
 'V243': np.float16,
 'V244': np.float16,
 'V245': np.float16,
 'V246': np.float16,
 'V247': np.float16,
 'V248': np.float16,
 'V249': np.float16,
 'V250': np.float16,
 'V251': np.float16,
 'V252': np.float16,
 'V253': np.float16,
 'V254': np.float16,
 'V255': np.float16,
 'V256': np.float16,
 'V257': np.float16,
 'V258': np.float16,
 'V259': np.float16,
 'V260': np.float16,
 'V261': np.float16,
 'V262': np.float16,
 'V263': np.float32,
 'V264': np.float32,
 'V265': np.float32,
 'V266': np.float16,
 'V267': np.float16,
 'V268': np.float16,
 'V269': np.float16,
 'V270': np.float16,
 'V271': np.float16,
 'V272': np.float16,
 'V273': np.float16,
 'V274': np.float32,
 'V275': np.float16,
 'V276': np.float32,
 'V277': np.float32,
 'V278': np.float32,
 'V279': np.float16,
 'V280': np.float16,
 'V281': np.float16,
 'V282': np.float16,
 'V283': np.float16,
 'V284': np.float16,
 'V285': np.float16,
 'V286': np.float16,
 'V287': np.float16,
 'V288': np.float16,
 'V289': np.float16,
 'V290': np.float16,
 'V291': np.float16,
 'V292': np.float16,
 'V293': np.float16,
 'V294': np.float16,
 'V295': np.float16,
 'V296': np.float16,
 'V297': np.float16,
 'V298': np.float16,
 'V299': np.float16,
 'V300': np.float16,
 'V301': np.float16,
 'V302': np.float16,
 'V303': np.float16,
 'V304': np.float16,
 'V305': np.float16,
 'V306': np.float32,
 'V307': np.float32,
 'V308': np.float32,
 'V309': np.float16,
 'V310': np.float16,
 'V311': np.float16,
 'V312': np.float16,
 'V313': np.float16,
 'V314': np.float16,
 'V315': np.float16,
 'V316': np.float32,
 'V317': np.float32,
 'V318': np.float32,
 'V319': np.float32,
 'V320': np.float32,
 'V321': np.float32,
 'V322': np.float16,
 'V323': np.float16,
 'V324': np.float16,
 'V325': np.float16,
 'V326': np.float16,
 'V327': np.float16,
 'V328': np.float16,
 'V329': np.float16,
 'V330': np.float16,
 'V331': np.float32,
 'V332': np.float32,
 'V333': np.float32,
 'V334': np.float16,
 'V335': np.float16,
 'V336': np.float16,
 'V337': np.float32,
 'V338': np.float32,
 'V339': np.float32}


schema_train_identity = {'TransactionID': np.int32,
 'id_01': np.float16,
 'id_02': np.float32,
 'id_03': np.float16,
 'id_04': np.float16,
 'id_05': np.float16,
 'id_06': np.float16,
 'id_07': np.float16,
 'id_08': np.float16,
 'id_09': np.float16,
 'id_10': np.float16,
 'id_11': np.float16,
 'id_12': 'object',
 'id_13': np.float16,
 'id_14': np.float16,
 'id_15': 'object',
 'id_16': 'object',
 'id_17': np.float16,
 'id_18': np.float16,
 'id_19': np.float16,
 'id_20': np.float16,
 'id_21': np.float16,
 'id_22': np.float16,
 'id_23': 'object',
 'id_24': np.float16,
 'id_25': np.float16,
 'id_26': np.float16,
 'id_27': 'object',
 'id_28': 'object',
 'id_29': 'object',
 'id_30': 'object',
 'id_31': 'object',
 'id_32': np.float16,
 'id_33': 'object',
 'id_34': 'object',
 'id_35': 'object',
 'id_36': 'object',
 'id_37': 'object',
 'id_38': 'object',
 'DeviceType': 'object',
 'DeviceInfo': 'object'}

schema_test_transaction = {'TransactionID': np.int32,
 'TransactionDT': np.int32,
 'TransactionAmt': np.float16,
 'ProductCD': 'object',
 'card1': np.int16,
 'card2': np.float16,
 'card3': np.float16,
 'card4': 'object',
 'card5': np.float16,
 'card6': 'object',
 'addr1': np.float16,
 'addr2': np.float16,
 'dist1': np.float16,
 'dist2': np.float16,
 'P_emaildomain': 'object',
 'R_emaildomain': 'object',
 'C1': np.float16,
 'C2': np.float16,
 'C3': np.float16,
 'C4': np.float16,
 'C5': np.float16,
 'C6': np.float16,
 'C7': np.float16,
 'C8': np.float16,
 'C9': np.float16,
 'C10': np.float16,
 'C11': np.float16,
 'C12': np.float16,
 'C13': np.float16,
 'C14': np.float16,
 'D1': np.float16,
 'D2': np.float16,
 'D3': np.float16,
 'D4': np.float16,
 'D5': np.float16,
 'D6': np.float16,
 'D7': np.float16,
 'D8': np.float16,
 'D9': np.float16,
 'D10': np.float16,
 'D11': np.float16,
 'D12': np.float16,
 'D13': np.float16,
 'D14': np.float16,
 'D15': np.float16,
 'M1': 'object',
 'M2': 'object',
 'M3': 'object',
 'M4': 'object',
 'M5': 'object',
 'M6': 'object',
 'M7': 'object',
 'M8': 'object',
 'M9': 'object',
 'V1': np.float16,
 'V2': np.float16,
 'V3': np.float16,
 'V4': np.float16,
 'V5': np.float16,
 'V6': np.float16,
 'V7': np.float16,
 'V8': np.float16,
 'V9': np.float16,
 'V10': np.float16,
 'V11': np.float16,
 'V12': np.float16,
 'V13': np.float16,
 'V14': np.float16,
 'V15': np.float16,
 'V16': np.float16,
 'V17': np.float16,
 'V18': np.float16,
 'V19': np.float16,
 'V20': np.float16,
 'V21': np.float16,
 'V22': np.float16,
 'V23': np.float16,
 'V24': np.float16,
 'V25': np.float16,
 'V26': np.float16,
 'V27': np.float16,
 'V28': np.float16,
 'V29': np.float16,
 'V30': np.float16,
 'V31': np.float16,
 'V32': np.float16,
 'V33': np.float16,
 'V34': np.float16,
 'V35': np.float16,
 'V36': np.float16,
 'V37': np.float16,
 'V38': np.float16,
 'V39': np.float16,
 'V40': np.float16,
 'V41': np.float16,
 'V42': np.float16,
 'V43': np.float16,
 'V44': np.float16,
 'V45': np.float16,
 'V46': np.float16,
 'V47': np.float16,
 'V48': np.float16,
 'V49': np.float16,
 'V50': np.float16,
 'V51': np.float16,
 'V52': np.float16,
 'V53': np.float16,
 'V54': np.float16,
 'V55': np.float16,
 'V56': np.float16,
 'V57': np.float16,
 'V58': np.float16,
 'V59': np.float16,
 'V60': np.float16,
 'V61': np.float16,
 'V62': np.float16,
 'V63': np.float16,
 'V64': np.float16,
 'V65': np.float16,
 'V66': np.float16,
 'V67': np.float16,
 'V68': np.float16,
 'V69': np.float16,
 'V70': np.float16,
 'V71': np.float16,
 'V72': np.float16,
 'V73': np.float16,
 'V74': np.float16,
 'V75': np.float16,
 'V76': np.float16,
 'V77': np.float16,
 'V78': np.float16,
 'V79': np.float16,
 'V80': np.float16,
 'V81': np.float16,
 'V82': np.float16,
 'V83': np.float16,
 'V84': np.float16,
 'V85': np.float16,
 'V86': np.float16,
 'V87': np.float16,
 'V88': np.float16,
 'V89': np.float16,
 'V90': np.float16,
 'V91': np.float16,
 'V92': np.float16,
 'V93': np.float16,
 'V94': np.float16,
 'V95': np.float16,
 'V96': np.float16,
 'V97': np.float16,
 'V98': np.float16,
 'V99': np.float16,
 'V100': np.float16,
 'V101': np.float16,
 'V102': np.float16,
 'V103': np.float16,
 'V104': np.float16,
 'V105': np.float16,
 'V106': np.float16,
 'V107': np.float16,
 'V108': np.float16,
 'V109': np.float16,
 'V110': np.float16,
 'V111': np.float16,
 'V112': np.float16,
 'V113': np.float16,
 'V114': np.float16,
 'V115': np.float16,
 'V116': np.float16,
 'V117': np.float16,
 'V118': np.float16,
 'V119': np.float16,
 'V120': np.float16,
 'V121': np.float16,
 'V122': np.float16,
 'V123': np.float16,
 'V124': np.float16,
 'V125': np.float16,
 'V126': np.float32,
 'V127': np.float32,
 'V128': np.float32,
 'V129': np.float16,
 'V130': np.float32,
 'V131': np.float32,
 'V132': np.float32,
 'V133': np.float32,
 'V134': np.float32,
 'V135': np.float32,
 'V136': np.float32,
 'V137': np.float32,
 'V138': np.float16,
 'V139': np.float16,
 'V140': np.float16,
 'V141': np.float16,
 'V142': np.float16,
 'V143': np.float16,
 'V144': np.float16,
 'V145': np.float16,
 'V146': np.float16,
 'V147': np.float16,
 'V148': np.float16,
 'V149': np.float16,
 'V150': np.float16,
 'V151': np.float16,
 'V152': np.float16,
 'V153': np.float16,
 'V154': np.float16,
 'V155': np.float16,
 'V156': np.float16,
 'V157': np.float16,
 'V158': np.float16,
 'V159': np.float32,
 'V160': np.float32,
 'V161': np.float16,
 'V162': np.float16,
 'V163': np.float16,
 'V164': np.float32,
 'V165': np.float32,
 'V166': np.float32,
 'V167': np.float16,
 'V168': np.float16,
 'V169': np.float16,
 'V170': np.float16,
 'V171': np.float16,
 'V172': np.float16,
 'V173': np.float16,
 'V174': np.float16,
 'V175': np.float16,
 'V176': np.float16,
 'V177': np.float16,
 'V178': np.float16,
 'V179': np.float16,
 'V180': np.float16,
 'V181': np.float16,
 'V182': np.float16,
 'V183': np.float16,
 'V184': np.float16,
 'V185': np.float16,
 'V186': np.float16,
 'V187': np.float16,
 'V188': np.float16,
 'V189': np.float16,
 'V190': np.float16,
 'V191': np.float16,
 'V192': np.float16,
 'V193': np.float16,
 'V194': np.float16,
 'V195': np.float16,
 'V196': np.float16,
 'V197': np.float16,
 'V198': np.float16,
 'V199': np.float16,
 'V200': np.float16,
 'V201': np.float16,
 'V202': np.float32,
 'V203': np.float32,
 'V204': np.float32,
 'V205': np.float16,
 'V206': np.float16,
 'V207': np.float32,
 'V208': np.float16,
 'V209': np.float16,
 'V210': np.float16,
 'V211': np.float32,
 'V212': np.float32,
 'V213': np.float32,
 'V214': np.float32,
 'V215': np.float32,
 'V216': np.float32,
 'V217': np.float16,
 'V218': np.float16,
 'V219': np.float16,
 'V220': np.float16,
 'V221': np.float16,
 'V222': np.float16,
 'V223': np.float16,
 'V224': np.float16,
 'V225': np.float16,
 'V226': np.float16,
 'V227': np.float16,
 'V228': np.float16,
 'V229': np.float16,
 'V230': np.float16,
 'V231': np.float16,
 'V232': np.float16,
 'V233': np.float16,
 'V234': np.float16,
 'V235': np.float16,
 'V236': np.float16,
 'V237': np.float16,
 'V238': np.float16,
 'V239': np.float16,
 'V240': np.float16,
 'V241': np.float16,
 'V242': np.float16,
 'V243': np.float16,
 'V244': np.float16,
 'V245': np.float16,
 'V246': np.float16,
 'V247': np.float16,
 'V248': np.float16,
 'V249': np.float16,
 'V250': np.float16,
 'V251': np.float16,
 'V252': np.float16,
 'V253': np.float16,
 'V254': np.float16,
 'V255': np.float16,
 'V256': np.float16,
 'V257': np.float16,
 'V258': np.float16,
 'V259': np.float16,
 'V260': np.float16,
 'V261': np.float16,
 'V262': np.float16,
 'V263': np.float32,
 'V264': np.float32,
 'V265': np.float32,
 'V266': np.float16,
 'V267': np.float16,
 'V268': np.float16,
 'V269': np.float16,
 'V270': np.float16,
 'V271': np.float16,
 'V272': np.float16,
 'V273': np.float32,
 'V274': np.float32,
 'V275': np.float32,
 'V276': np.float32,
 'V277': np.float32,
 'V278': np.float32,
 'V279': np.float16,
 'V280': np.float16,
 'V281': np.float16,
 'V282': np.float16,
 'V283': np.float16,
 'V284': np.float16,
 'V285': np.float16,
 'V286': np.float16,
 'V287': np.float16,
 'V288': np.float16,
 'V289': np.float16,
 'V290': np.float16,
 'V291': np.float16,
 'V292': np.float16,
 'V293': np.float16,
 'V294': np.float16,
 'V295': np.float16,
 'V296': np.float16,
 'V297': np.float16,
 'V298': np.float16,
 'V299': np.float16,
 'V300': np.float16,
 'V301': np.float16,
 'V302': np.float16,
 'V303': np.float16,
 'V304': np.float16,
 'V305': np.float16,
 'V306': np.float32,
 'V307': np.float32,
 'V308': np.float32,
 'V309': np.float16,
 'V310': np.float32,
 'V311': np.float16,
 'V312': np.float32,
 'V313': np.float16,
 'V314': np.float16,
 'V315': np.float16,
 'V316': np.float32,
 'V317': np.float32,
 'V318': np.float32,
 'V319': np.float32,
 'V320': np.float32,
 'V321': np.float32,
 'V322': np.float16,
 'V323': np.float16,
 'V324': np.float16,
 'V325': np.float16,
 'V326': np.float16,
 'V327': np.float16,
 'V328': np.float16,
 'V329': np.float16,
 'V330': np.float16,
 'V331': np.float32,
 'V332': np.float32,
 'V333': np.float32,
 'V334': np.float16,
 'V335': np.float16,
 'V336': np.float16,
 'V337': np.float32,
 'V338': np.float32,
 'V339': np.float32}

schema_test_identity = {'TransactionID': np.int32,
 'id_01': np.float16,
 'id_02': np.float32,
 'id_03': np.float16,
 'id_04': np.float16,
 'id_05': np.float16,
 'id_06': np.float16,
 'id_07': np.float16,
 'id_08': np.float16,
 'id_09': np.float16,
 'id_10': np.float16,
 'id_11': np.float16,
 'id_12': 'object',
 'id_13': np.float16,
 'id_14': np.float16,
 'id_15': 'object',
 'id_16': 'object',
 'id_17': np.float16,
 'id_18': np.float16,
 'id_19': np.float16,
 'id_20': np.float16,
 'id_21': np.float16,
 'id_22': np.float16,
 'id_23': 'object',
 'id_24': np.float16,
 'id_25': np.float16,
 'id_26': np.float16,
 'id_27': 'object',
 'id_28': 'object',
 'id_29': 'object',
 'id_30': 'object',
 'id_31': 'object',
 'id_32': np.float16,
 'id_33': 'object',
 'id_34': 'object',
 'id_35': 'object',
 'id_36': 'object',
 'id_37': 'object',
 'id_38': 'object',
 'DeviceType': 'object',
 'DeviceInfo': 'object'}