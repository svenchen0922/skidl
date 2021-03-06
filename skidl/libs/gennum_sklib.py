from skidl import Pin, Part, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

gennum = SchLib(tool=SKIDL).add_parts(*[
        Part(name='GS2962',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='GS4910B',dest=TEMPLATE,tool=SKIDL,do_erc=True,aliases=['GS4911B']),
        Part(name='GS9020',dest=TEMPLATE,tool=SKIDL,ref_prefix='U',num_units=1,do_erc=True,pins=[
            Pin(num='1',name='VDD',do_erc=True),
            Pin(num='2',name='GND',do_erc=True),
            Pin(num='3',name='GND',do_erc=True),
            Pin(num='4',name='VDD',do_erc=True),
            Pin(num='5',name='VDD_SDI',do_erc=True),
            Pin(num='6',name='SDI',do_erc=True),
            Pin(num='7',name='SDI',do_erc=True),
            Pin(num='8',name='VDD_SDI',do_erc=True),
            Pin(num='9',name='VDD_SCI',do_erc=True),
            Pin(num='10',name='SCI',do_erc=True),
            Pin(num='20',name='P5',func=Pin.BIDIR,do_erc=True),
            Pin(num='30',name='GND',do_erc=True),
            Pin(num='40',name='FL0',func=Pin.BIDIR,do_erc=True),
            Pin(num='50',name='GND',do_erc=True),
            Pin(num='60',name='DOUT9',func=Pin.OUTPUT,do_erc=True),
            Pin(num='70',name='SDO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='80',name='ANC_DATA',func=Pin.OUTPUT,do_erc=True),
            Pin(num='11',name='SCI',do_erc=True),
            Pin(num='21',name='SCL/P4',func=Pin.BIDIR,do_erc=True),
            Pin(num='31',name='RESET',do_erc=True),
            Pin(num='41',name='S1',func=Pin.BIDIR,do_erc=True),
            Pin(num='51',name='VDD',do_erc=True),
            Pin(num='61',name='V',func=Pin.OUTPUT,do_erc=True),
            Pin(num='71',name='SDO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='12',name='VDD_SCI',do_erc=True),
            Pin(num='22',name='SDA/P3',func=Pin.BIDIR,do_erc=True),
            Pin(num='32',name='STD3',func=Pin.OUTPUT,do_erc=True),
            Pin(num='42',name='S0',func=Pin.BIDIR,do_erc=True),
            Pin(num='52',name='DOUT1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='62',name='H',func=Pin.OUTPUT,do_erc=True),
            Pin(num='72',name='SGND',do_erc=True),
            Pin(num='13',name='VDD',do_erc=True),
            Pin(num='23',name='A2/P2',func=Pin.BIDIR,do_erc=True),
            Pin(num='33',name='STD2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='43',name='F_R/W',do_erc=True),
            Pin(num='53',name='DOUT2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='63',name='F0',func=Pin.OUTPUT,do_erc=True),
            Pin(num='73',name='VBLANKS/L',do_erc=True),
            Pin(num='14',name='GND',do_erc=True),
            Pin(num='24',name='A1/P1',func=Pin.BIDIR,do_erc=True),
            Pin(num='34',name='STD1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='44',name='INTERRUPT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='54',name='DOUT3',func=Pin.OUTPUT,do_erc=True),
            Pin(num='64',name='F1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='74',name='BYPASS_EDH',do_erc=True),
            Pin(num='15',name='HOSTIF_MODE',do_erc=True),
            Pin(num='25',name='A0/P0',func=Pin.BIDIR,do_erc=True),
            Pin(num='35',name='STD0',func=Pin.OUTPUT,do_erc=True),
            Pin(num='45',name='FLYWDIS',do_erc=True),
            Pin(num='55',name='DOUT4',func=Pin.OUTPUT,do_erc=True),
            Pin(num='65',name='F2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='75',name='SDOMODE',do_erc=True),
            Pin(num='16',name='FIFOE/S',do_erc=True),
            Pin(num='26',name='R/W',do_erc=True),
            Pin(num='36',name='FL4',func=Pin.BIDIR,do_erc=True),
            Pin(num='46',name='NO_EDH',func=Pin.OUTPUT,do_erc=True),
            Pin(num='56',name='DOUT5',func=Pin.OUTPUT,do_erc=True),
            Pin(num='66',name='FLAG_MAP',do_erc=True),
            Pin(num='76',name='BLANK_EN',do_erc=True),
            Pin(num='17',name='CRC_MODE',do_erc=True),
            Pin(num='27',name='A/D',do_erc=True),
            Pin(num='37',name='FL3',func=Pin.BIDIR,do_erc=True),
            Pin(num='47',name='FIFO_RESET',func=Pin.OUTPUT,do_erc=True),
            Pin(num='57',name='DOUT6',func=Pin.OUTPUT,do_erc=True),
            Pin(num='67',name='GND',do_erc=True),
            Pin(num='77',name='ANC_CHKSM',do_erc=True),
            Pin(num='18',name='P7',func=Pin.BIDIR,do_erc=True),
            Pin(num='28',name='CS',do_erc=True),
            Pin(num='38',name='FL2',func=Pin.BIDIR,do_erc=True),
            Pin(num='48',name='PCLKOUT',func=Pin.OUTPUT,do_erc=True),
            Pin(num='58',name='DOUT7',func=Pin.OUTPUT,do_erc=True),
            Pin(num='68',name='VDD',do_erc=True),
            Pin(num='78',name='CLIP_TRS',do_erc=True),
            Pin(num='19',name='P6',func=Pin.BIDIR,do_erc=True),
            Pin(num='29',name='VDD',do_erc=True),
            Pin(num='39',name='FL1',func=Pin.BIDIR,do_erc=True),
            Pin(num='49',name='DOUT0',func=Pin.OUTPUT,do_erc=True),
            Pin(num='59',name='DOUT8',func=Pin.OUTPUT,do_erc=True),
            Pin(num='69',name='SVDD',do_erc=True),
            Pin(num='79',name='TRS_ERR',func=Pin.OUTPUT,do_erc=True)]),
        Part(name='GS9025',dest=TEMPLATE,tool=SKIDL,ref_prefix='U',num_units=1,do_erc=True,pins=[
            Pin(num='1',name='DDI',do_erc=True),
            Pin(num='2',name='DDI',do_erc=True),
            Pin(num='3',name='VCC_75',do_erc=True),
            Pin(num='4',name='VCC',do_erc=True),
            Pin(num='5',name='VEE',do_erc=True),
            Pin(num='6',name='SDI',do_erc=True),
            Pin(num='7',name='SDI',do_erc=True),
            Pin(num='8',name='VCC',do_erc=True),
            Pin(num='9',name='VEE',do_erc=True),
            Pin(num='10',name='CD_ADJ',do_erc=True),
            Pin(num='20',name='RVCO',do_erc=True),
            Pin(num='30',name='VEE',do_erc=True),
            Pin(num='40',name='SSI/CD',func=Pin.OUTPUT,do_erc=True),
            Pin(num='11',name='AGC-',do_erc=True),
            Pin(num='21',name='CBG',do_erc=True),
            Pin(num='31',name='SDO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='41',name='A/D',do_erc=True),
            Pin(num='12',name='AGC+',do_erc=True),
            Pin(num='22',name='VCC',do_erc=True),
            Pin(num='32',name='SDO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='42',name='SMPTE',do_erc=True),
            Pin(num='13',name='VCC',do_erc=True),
            Pin(num='23',name='SS2',func=Pin.BIDIR,do_erc=True),
            Pin(num='33',name='VEE',do_erc=True),
            Pin(num='43',name='OEM',func=Pin.OUTPUT,do_erc=True),
            Pin(num='14',name='VEE',do_erc=True),
            Pin(num='24',name='SS1',func=Pin.BIDIR,do_erc=True),
            Pin(num='34',name='VEE',do_erc=True),
            Pin(num='44',name='VCC_75',do_erc=True),
            Pin(num='15',name='LF+',do_erc=True),
            Pin(num='25',name='SS0',func=Pin.BIDIR,do_erc=True),
            Pin(num='35',name='VCC',do_erc=True),
            Pin(num='16',name='LFS',do_erc=True),
            Pin(num='26',name='AUTO/MAN',do_erc=True),
            Pin(num='36',name='CLK_EN',do_erc=True),
            Pin(num='17',name='LF-',do_erc=True),
            Pin(num='27',name='VEE',do_erc=True),
            Pin(num='37',name='VEE',do_erc=True),
            Pin(num='18',name='VEE',do_erc=True),
            Pin(num='28',name='SCO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='38',name='COSC',do_erc=True),
            Pin(num='19',name='RVCO_RTN',do_erc=True),
            Pin(num='29',name='SCO',func=Pin.OUTPUT,do_erc=True),
            Pin(num='39',name='LOCK',func=Pin.OUTPUT,do_erc=True)]),
        Part(name='GS9032',dest=TEMPLATE,tool=SKIDL,ref_prefix='U',num_units=1,do_erc=True,pins=[
            Pin(num='1',name='PD9',do_erc=True),
            Pin(num='2',name='PD8',do_erc=True),
            Pin(num='3',name='PD7',do_erc=True),
            Pin(num='4',name='PD6',do_erc=True),
            Pin(num='5',name='PD5',do_erc=True),
            Pin(num='6',name='PD4',do_erc=True),
            Pin(num='7',name='PD3',do_erc=True),
            Pin(num='8',name='PD2',do_erc=True),
            Pin(num='9',name='PD1',do_erc=True),
            Pin(num='10',name='PD0',do_erc=True),
            Pin(num='20',name='LOCK_DET',func=Pin.OUTPUT,do_erc=True),
            Pin(num='30',name='R_SET1',do_erc=True),
            Pin(num='40',name='LBWC',do_erc=True),
            Pin(num='11',name='PCLKIN',do_erc=True),
            Pin(num='21',name='SS0',do_erc=True),
            Pin(num='31',name='BYPASS',do_erc=True),
            Pin(num='41',name='LF+',do_erc=True),
            Pin(num='12',name='VEE3',do_erc=True),
            Pin(num='22',name='R_SET0',do_erc=True),
            Pin(num='32',name='AUTO/MAN',do_erc=True),
            Pin(num='42',name='LF-',do_erc=True),
            Pin(num='13',name='VCC3',do_erc=True),
            Pin(num='23',name='VEE',do_erc=True),
            Pin(num='33',name='RESET',do_erc=True),
            Pin(num='43',name='VEE',do_erc=True),
            Pin(num='14',name='C_OSC',do_erc=True),
            Pin(num='24',name='SDO0',func=Pin.OUTPUT,do_erc=True),
            Pin(num='34',name='VCC1',do_erc=True),
            Pin(num='44',name='SYNC_DIS',do_erc=True),
            Pin(num='15',name='SS2',do_erc=True),
            Pin(num='25',name='SDO0',func=Pin.OUTPUT,do_erc=True),
            Pin(num='35',name='VEE1',do_erc=True),
            Pin(num='16',name='SS1',do_erc=True),
            Pin(num='26',name='VEE',do_erc=True),
            Pin(num='36',name='R_VCO+',do_erc=True),
            Pin(num='17',name='VCC2',do_erc=True),
            Pin(num='27',name='SDO1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='37',name='C_BG',do_erc=True),
            Pin(num='18',name='VEE2',do_erc=True),
            Pin(num='28',name='SDO1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='38',name='R_VCO-',do_erc=True),
            Pin(num='19',name='SDO1_ENABLE',do_erc=True),
            Pin(num='29',name='VEE',do_erc=True),
            Pin(num='39',name='VEE',do_erc=True)])])