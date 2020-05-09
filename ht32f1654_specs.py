HARDWARE_REGISTERS = {
    0x40000000: 'USART0.DR',
    0x40000004: 'USART0.RBR',
    0x40000008: 'USART0.TBR',
    0x4000000C: 'USART0.IER',
    0x40000010: 'USART0.IIR',
    0x40000014: 'USART0.FCR',
    0x40000018: 'USART0.LCR',
    0x4000001C: 'USART0.MCR',
    0x40000020: 'USART0.LSR',
    0x40000024: 'USART0.SR',
    0x40000028: 'USART0.MSR',
    0x4000002C: 'USART0.TPR',
    0x40000030: 'USART0.MDR',
    0x40000034: 'USART0.ICR',
    0x40000038: 'USART0.RCR',
    0x4000003C: 'USART0.SCR',
    0x40000040: 'USART0.FSR',
    0x40000044: 'USART0.DLR',
    0x40000048: 'USART0.DTR',
    0x40040000: 'USART1.DR',
    0x40040004: 'USART1.RBR',
    0x40040008: 'USART1.TBR',
    0x4004000C: 'USART1.IER',
    0x40040010: 'USART1.IIR',
    0x40040014: 'USART1.FCR',
    0x40040018: 'USART1.LCR',
    0x4004001C: 'USART1.MCR',
    0x40040020: 'USART1.LSR',
    0x40040024: 'USART1.SR',
    0x40040028: 'USART1.MSR',
    0x4004002C: 'USART1.TPR',
    0x40040030: 'USART1.MDR',
    0x40040034: 'USART1.ICR',
    0x40040038: 'USART1.RCR',
    0x4004003C: 'USART1.SCR',
    0x40040040: 'USART1.FSR',
    0x40040044: 'USART1.DLR',
    0x40040048: 'USART1.DTR',
    0x40001000: 'UART0.DR',
    0x40001004: 'UART0.RBR',
    0x40001008: 'UART0.TBR',
    0x4000100C: 'UART0.IER',
    0x40001010: 'UART0.IIR',
    0x40001014: 'UART0.FCR',
    0x40001018: 'UART0.LCR',
    0x4000101C: 'UART0.MCR',
    0x40001020: 'UART0.LSR',
    0x40001024: 'UART0.SR',
    0x40001028: 'UART0.MSR',
    0x4000102C: 'UART0.TPR',
    0x40001030: 'UART0.MDR',
    0x40001034: 'UART0.ICR',
    0x40001038: 'UART0.RCR',
    0x4000103C: 'UART0.SCR',
    0x40001040: 'UART0.FSR',
    0x40001044: 'UART0.DLR',
    0x40001048: 'UART0.DTR',
    0x40041000: 'UART1.DR',
    0x40041004: 'UART1.RBR',
    0x40041008: 'UART1.TBR',
    0x4004100C: 'UART1.IER',
    0x40041010: 'UART1.IIR',
    0x40041014: 'UART1.FCR',
    0x40041018: 'UART1.LCR',
    0x4004101C: 'UART1.MCR',
    0x40041020: 'UART1.LSR',
    0x40041024: 'UART1.SR',
    0x40041028: 'UART1.MSR',
    0x4004102C: 'UART1.TPR',
    0x40041030: 'UART1.MDR',
    0x40041034: 'UART1.ICR',
    0x40041038: 'UART1.RCR',
    0x4004103C: 'UART1.SCR',
    0x40041040: 'UART1.FSR',
    0x40041044: 'UART1.DLR',
    0x40041048: 'UART1.DTR',
    0x40004000: 'SPI0.CR0',
    0x40004004: 'SPI0.CR1',
    0x40004008: 'SPI0.IER',
    0x4000400C: 'SPI0.CPR',
    0x40004010: 'SPI0.DR',
    0x40004014: 'SPI0.SR',
    0x40004018: 'SPI0.FCR',
    0x4000401C: 'SPI0.FSR',
    0x40004020: 'SPI0.FTOCR',
    0x40044000: 'SPI1.CR0',
    0x40044004: 'SPI1.CR1',
    0x40044008: 'SPI1.IER',
    0x4004400C: 'SPI1.CPR',
    0x40044010: 'SPI1.DR',
    0x40044014: 'SPI1.SR',
    0x40044018: 'SPI1.FCR',
    0x4004401C: 'SPI1.FSR',
    0x40044020: 'SPI1.FTOCR',
    0x40010000: 'ADC.RESERVE0',
    0x40010004: 'ADC.RST',
    0x40010008: 'ADC.CONV',
    0x4001000C: 'ADC.HCONV',
    0x40010010: 'ADC.LST.0',
    0x40010014: 'ADC.LST.1',
    0x40010018: 'ADC.LST.2',
    0x4001001C: 'ADC.LST.3',
    0x40010020: 'ADC.HLST',
    0x40010024: 'ADC.RESERVE1.0',
    0x40010028: 'ADC.RESERVE1.1',
    0x4001002C: 'ADC.RESERVE1.2',
    0x40010030: 'ADC.OFR.0',
    0x40010034: 'ADC.OFR.1',
    0x40010038: 'ADC.OFR.2',
    0x4001003C: 'ADC.OFR.3',
    0x40010040: 'ADC.OFR.4',
    0x40010044: 'ADC.OFR.5',
    0x40010048: 'ADC.OFR.6',
    0x4001004C: 'ADC.OFR.7',
    0x40010050: 'ADC.OFR.8',
    0x40010054: 'ADC.OFR.9',
    0x40010058: 'ADC.OFR.10',
    0x4001005C: 'ADC.OFR.11',
    0x40010060: 'ADC.OFR.12',
    0x40010064: 'ADC.OFR.13',
    0x40010068: 'ADC.OFR.14',
    0x4001006C: 'ADC.OFR.15',
    0x40010070: 'ADC.STR.0',
    0x40010074: 'ADC.STR.1',
    0x40010078: 'ADC.STR.2',
    0x4001007C: 'ADC.STR.3',
    0x40010080: 'ADC.STR.4',
    0x40010084: 'ADC.STR.5',
    0x40010088: 'ADC.STR.6',
    0x4001008C: 'ADC.STR.7',
    0x40010090: 'ADC.STR.8',
    0x40010094: 'ADC.STR.9',
    0x40010098: 'ADC.STR.10',
    0x4001009C: 'ADC.STR.11',
    0x400100A0: 'ADC.STR.12',
    0x400100A4: 'ADC.STR.13',
    0x400100A8: 'ADC.STR.14',
    0x400100AC: 'ADC.STR.15',
    0x400100B0: 'ADC.DR.0',
    0x400100B4: 'ADC.DR.1',
    0x400100B8: 'ADC.DR.2',
    0x400100BC: 'ADC.DR.3',
    0x400100C0: 'ADC.DR.4',
    0x400100C4: 'ADC.DR.5',
    0x400100C8: 'ADC.DR.6',
    0x400100CC: 'ADC.DR.7',
    0x400100D0: 'ADC.DR.8',
    0x400100D4: 'ADC.DR.9',
    0x400100D8: 'ADC.DR.10',
    0x400100DC: 'ADC.DR.11',
    0x400100E0: 'ADC.DR.12',
    0x400100E4: 'ADC.DR.13',
    0x400100E8: 'ADC.DR.14',
    0x400100EC: 'ADC.DR.15',
    0x400100F0: 'ADC.HDR.0',
    0x400100F4: 'ADC.HDR.1',
    0x400100F8: 'ADC.HDR.2',
    0x400100FC: 'ADC.HDR.3',
    0x40010100: 'ADC.TCR',
    0x40010104: 'ADC.TSR',
    0x40010108: 'ADC.RESERVE2.0',
    0x4001010C: 'ADC.RESERVE2.1',
    0x40010110: 'ADC.HTCR',
    0x40010114: 'ADC.HTSR',
    0x40010118: 'ADC.RESERVE3.0',
    0x4001011C: 'ADC.RESERVE3.1',
    0x40010120: 'ADC.WCR',
    0x40010124: 'ADC.LTR',
    0x40010128: 'ADC.UTR',
    0x4001012C: 'ADC.RESERVE4',
    0x40010130: 'ADC.IER',
    0x40010134: 'ADC.IRAW',
    0x40010138: 'ADC.ISR',
    0x4001013C: 'ADC.ICLR',
    0x40010140: 'ADC.PDMAR',
    0x40018000: 'CMP_OP0.OPACR',
    0x40018004: 'CMP_OP0.OFVCR',
    0x40018008: 'CMP_OP0.CMPIER',
    0x4001800C: 'CMP_OP0.CMPRSR',
    0x40018010: 'CMP_OP0.CMPISR',
    0x40018014: 'CMP_OP0.CMPICLR',
    0x40018100: 'CMP_OP1.OPACR',
    0x40018104: 'CMP_OP1.OFVCR',
    0x40018108: 'CMP_OP1.CMPIER',
    0x4001810C: 'CMP_OP1.CMPRSR',
    0x40018110: 'CMP_OP1.CMPISR',
    0x40018114: 'CMP_OP1.CMPICLR',
    0x40058000: 'CMP0.CR',
    0x40058004: 'CMP0.VALR',
    0x40058008: 'CMP0.IER',
    0x4005800C: 'CMP0.TFR',
    0x40058100: 'CMP1.CR',
    0x40058104: 'CMP1.VALR',
    0x40058108: 'CMP1.IER',
    0x4005810C: 'CMP1.TFR',
    0x400B0000: 'GPIOA.DIRCR',
    0x400B0004: 'GPIOA.INER',
    0x400B0008: 'GPIOA.PUR',
    0x400B000C: 'GPIOA.PDR',
    0x400B0010: 'GPIOA.ODR',
    0x400B0014: 'GPIOA.DRVR',
    0x400B0018: 'GPIOA.LOCKR',
    0x400B001C: 'GPIOA.DINR',
    0x400B0020: 'GPIOA.DOUTR',
    0x400B0024: 'GPIOA.SRR',
    0x400B0028: 'GPIOA.RR',
    0x400B2000: 'GPIOB.DIRCR',
    0x400B2004: 'GPIOB.INER',
    0x400B2008: 'GPIOB.PUR',
    0x400B200C: 'GPIOB.PDR',
    0x400B2010: 'GPIOB.ODR',
    0x400B2014: 'GPIOB.DRVR',
    0x400B2018: 'GPIOB.LOCKR',
    0x400B201C: 'GPIOB.DINR',
    0x400B2020: 'GPIOB.DOUTR',
    0x400B2024: 'GPIOB.SRR',
    0x400B2028: 'GPIOB.RR',
    0x400B4000: 'GPIOC.DIRCR',
    0x400B4004: 'GPIOC.INER',
    0x400B4008: 'GPIOC.PUR',
    0x400B400C: 'GPIOC.PDR',
    0x400B4010: 'GPIOC.ODR',
    0x400B4014: 'GPIOC.DRVR',
    0x400B4018: 'GPIOC.LOCKR',
    0x400B401C: 'GPIOC.DINR',
    0x400B4020: 'GPIOC.DOUTR',
    0x400B4024: 'GPIOC.SRR',
    0x400B4028: 'GPIOC.RR',
    0x400B6000: 'GPIOD.DIRCR',
    0x400B6004: 'GPIOD.INER',
    0x400B6008: 'GPIOD.PUR',
    0x400B600C: 'GPIOD.PDR',
    0x400B6010: 'GPIOD.ODR',
    0x400B6014: 'GPIOD.DRVR',
    0x400B6018: 'GPIOD.LOCKR',
    0x400B601C: 'GPIOD.DINR',
    0x400B6020: 'GPIOD.DOUTR',
    0x400B6024: 'GPIOD.SRR',
    0x400B6028: 'GPIOD.RR',
    0x400B8000: 'GPIOE.DIRCR',
    0x400B8004: 'GPIOE.INER',
    0x400B8008: 'GPIOE.PUR',
    0x400B800C: 'GPIOE.PDR',
    0x400B8010: 'GPIOE.ODR',
    0x400B8014: 'GPIOE.DRVR',
    0x400B8018: 'GPIOE.LOCKR',
    0x400B801C: 'GPIOE.DINR',
    0x400B8020: 'GPIOE.DOUTR',
    0x400B8024: 'GPIOE.SRR',
    0x400B8028: 'GPIOE.RR',
    0x40022000: 'AFIO.ESSR.0',
    0x40022004: 'AFIO.ESSR.1',
    0x40022008: 'AFIO.RESERVE0.0',
    0x4002200C: 'AFIO.RESERVE0.1',
    0x40022010: 'AFIO.RESERVE0.2',
    0x40022014: 'AFIO.RESERVE0.3',
    0x40022018: 'AFIO.RESERVE0.4',
    0x4002201C: 'AFIO.RESERVE0.5',
    0x40022020: 'AFIO.GPACFGR.0',
    0x40022024: 'AFIO.GPACFGR.1',
    0x40022028: 'AFIO.GPBCFGR.0',
    0x4002202C: 'AFIO.GPBCFGR.1',
    0x40022030: 'AFIO.GPCCFGR.0',
    0x40022034: 'AFIO.GPCCFGR.1',
    0x40022038: 'AFIO.GPDCFGR.0',
    0x4002203C: 'AFIO.GPDCFGR.1',
    0x40024000: 'EXTI.CFGR0',
    0x40024004: 'EXTI.CFGR1',
    0x40024008: 'EXTI.CFGR2',
    0x4002400C: 'EXTI.CFGR3',
    0x40024010: 'EXTI.CFGR4',
    0x40024014: 'EXTI.CFGR5',
    0x40024018: 'EXTI.CFGR6',
    0x4002401C: 'EXTI.CFGR7',
    0x40024020: 'EXTI.CFGR8',
    0x40024024: 'EXTI.CFGR9',
    0x40024028: 'EXTI.CFGR10',
    0x4002402C: 'EXTI.CFGR11',
    0x40024030: 'EXTI.CFGR12',
    0x40024034: 'EXTI.CFGR13',
    0x40024038: 'EXTI.CFGR14',
    0x4002403C: 'EXTI.CFGR15',
    0x40024040: 'EXTI.CR',
    0x40024044: 'EXTI.EDGEFLGR',
    0x40024048: 'EXTI.EDGESR',
    0x4002404C: 'EXTI.SSCR',
    0x40024050: 'EXTI.WAKUPCR',
    0x40024054: 'EXTI.WAKUPPOLR',
    0x40024058: 'EXTI.WAKUPFLG',
    0x40048000: 'I2C0.CR',
    0x40048004: 'I2C0.IER',
    0x40048008: 'I2C0.ADDR',
    0x4004800C: 'I2C0.SR',
    0x40048010: 'I2C0.SHPGR',
    0x40048014: 'I2C0.SLPGR',
    0x40048018: 'I2C0.DR',
    0x4004801C: 'I2C0.TAR',
    0x40048020: 'I2C0.ADDMR',
    0x40048024: 'I2C0.ADDSR',
    0x40048028: 'I2C0.TOUT',
    0x40049000: 'I2C1.CR',
    0x40049004: 'I2C1.IER',
    0x40049008: 'I2C1.ADDR',
    0x4004900C: 'I2C1.SR',
    0x40049010: 'I2C1.SHPGR',
    0x40049014: 'I2C1.SLPGR',
    0x40049018: 'I2C1.DR',
    0x4004901C: 'I2C1.TAR',
    0x40049020: 'I2C1.ADDMR',
    0x40049024: 'I2C1.ADDSR',
    0x40049028: 'I2C1.TOUT',
    0x40068000: 'WDT.CR',
    0x40068004: 'WDT.MR0',
    0x40068008: 'WDT.MR1',
    0x4006800C: 'WDT.SR',
    0x40068010: 'WDT.PR',
    0x40068014: 'WDT.RESERVED0',
    0x40068018: 'WDT.CSR',
    0x4006A000: 'RTC.CNT',
    0x4006A004: 'RTC.CMP',
    0x4006A008: 'RTC.CR',
    0x4006A00C: 'RTC.SR',
    0x4006A010: 'RTC.IWEN',
    0x4006A100: 'PWRCU.SR',
    0x4006A104: 'PWRCU.CR',
    0x4006A108: 'PWRCU.TEST',
    0x4006A10C: 'PWRCU.HSIRCR',
    0x4006A110: 'PWRCU.LVDCSR',
    0x4006A114: 'PWRCU.RESERVE1.0',
    0x4006A118: 'PWRCU.RESERVE1.1',
    0x4006A11C: 'PWRCU.RESERVE1.2',
    0x4006A120: 'PWRCU.RESERVE1.3',
    0x4006A124: 'PWRCU.RESERVE1.4',
    0x4006A128: 'PWRCU.RESERVE1.5',
    0x4006A12C: 'PWRCU.RESERVE1.6',
    0x4006A130: 'PWRCU.RESERVE1.7',
    0x4006A134: 'PWRCU.RESERVE1.8',
    0x4006A138: 'PWRCU.RESERVE1.9',
    0x4006A13C: 'PWRCU.RESERVE1.10',
    0x4006A140: 'PWRCU.RESERVE1.11',
    0x4006A144: 'PWRCU.RESERVE1.12',
    0x4006A148: 'PWRCU.RESERVE1.13',
    0x4006A14C: 'PWRCU.RESERVE1.14',
    0x4006A150: 'PWRCU.RESERVE1.15',
    0x4006A154: 'PWRCU.RESERVE1.16',
    0x4006A158: 'PWRCU.RESERVE1.17',
    0x4006A15C: 'PWRCU.RESERVE1.18',
    0x4006A160: 'PWRCU.RESERVE1.19',
    0x4006A164: 'PWRCU.RESERVE1.20',
    0x4006A168: 'PWRCU.RESERVE1.21',
    0x4006A16C: 'PWRCU.RESERVE1.22',
    0x4006A170: 'PWRCU.RESERVE1.23',
    0x4006A174: 'PWRCU.RESERVE1.24',
    0x4006A178: 'PWRCU.RESERVE1.25',
    0x4006A17C: 'PWRCU.RESERVE1.26',
    0x4006A180: 'PWRCU.RESERVE1.27',
    0x4006A184: 'PWRCU.RESERVE1.28',
    0x4006A188: 'PWRCU.RESERVE1.29',
    0x4006A18C: 'PWRCU.RESERVE1.30',
    0x4006A190: 'PWRCU.RESERVE1.31',
    0x4006A194: 'PWRCU.RESERVE1.32',
    0x4006A198: 'PWRCU.RESERVE1.33',
    0x4006A19C: 'PWRCU.RESERVE1.34',
    0x4006A1A0: 'PWRCU.RESERVE1.35',
    0x4006A1A4: 'PWRCU.RESERVE1.36',
    0x4006A1A8: 'PWRCU.RESERVE1.37',
    0x4006A1AC: 'PWRCU.RESERVE1.38',
    0x4006A1B0: 'PWRCU.RESERVE1.39',
    0x4006A1B4: 'PWRCU.RESERVE1.40',
    0x4006A1B8: 'PWRCU.RESERVE1.41',
    0x4006A1BC: 'PWRCU.RESERVE1.42',
    0x4006A1C0: 'PWRCU.RESERVE1.43',
    0x4006A1C4: 'PWRCU.RESERVE1.44',
    0x4006A1C8: 'PWRCU.RESERVE1.45',
    0x4006A1CC: 'PWRCU.RESERVE1.46',
    0x4006A1D0: 'PWRCU.RESERVE1.47',
    0x4006A1D4: 'PWRCU.RESERVE1.48',
    0x4006A1D8: 'PWRCU.RESERVE1.49',
    0x4006A1DC: 'PWRCU.RESERVE1.50',
    0x4006A1E0: 'PWRCU.RESERVE1.51',
    0x4006A1E4: 'PWRCU.RESERVE1.52',
    0x4006A1E8: 'PWRCU.RESERVE1.53',
    0x4006A1EC: 'PWRCU.RESERVE1.54',
    0x4006A1F0: 'PWRCU.RESERVE1.55',
    0x4006A1F4: 'PWRCU.RESERVE1.56',
    0x4006A1F8: 'PWRCU.RESERVE1.57',
    0x4006A1FC: 'PWRCU.RESERVE1.58',
    0x4006A200: 'PWRCU.BAKREG.0',
    0x4006A204: 'PWRCU.BAKREG.1',
    0x4006A208: 'PWRCU.BAKREG.2',
    0x4006A20C: 'PWRCU.BAKREG.3',
    0x4006A210: 'PWRCU.BAKREG.4',
    0x4006A214: 'PWRCU.BAKREG.5',
    0x4006A218: 'PWRCU.BAKREG.6',
    0x4006A21C: 'PWRCU.BAKREG.7',
    0x4006A220: 'PWRCU.BAKREG.8',
    0x4006A224: 'PWRCU.BAKREG.9',
    0x40080000: 'FLASH.TADR',
    0x40080004: 'FLASH.WRDR',
    0x40080008: 'FLASH.RESERVED0',
    0x4008000C: 'FLASH.OCMR',
    0x40080010: 'FLASH.OPCR',
    0x40080014: 'FLASH.OIER',
    0x40080018: 'FLASH.OISR',
    0x4008001C: 'FLASH.RESERVED1',
    0x40080020: 'FLASH.PPSR.0',
    0x40080024: 'FLASH.PPSR.1',
    0x40080028: 'FLASH.PPSR.2',
    0x4008002C: 'FLASH.PPSR.3',
    0x40080030: 'FLASH.CPSR',
    0x40080034: 'FLASH.RESERVED2.0',
    0x40080038: 'FLASH.RESERVED2.1',
    0x4008003C: 'FLASH.RESERVED2.2',
    0x40080040: 'FLASH.RESERVED2.3',
    0x40080044: 'FLASH.RESERVED2.4',
    0x40080048: 'FLASH.RESERVED2.5',
    0x4008004C: 'FLASH.RESERVED2.6',
    0x40080050: 'FLASH.RESERVED2.7',
    0x40080054: 'FLASH.RESERVED2.8',
    0x40080058: 'FLASH.RESERVED2.9',
    0x4008005C: 'FLASH.RESERVED2.10',
    0x40080060: 'FLASH.RESERVED2.11',
    0x40080064: 'FLASH.RESERVED2.12',
    0x40080068: 'FLASH.RESERVED2.13',
    0x4008006C: 'FLASH.RESERVED2.14',
    0x40080070: 'FLASH.RESERVED2.15',
    0x40080074: 'FLASH.RESERVED2.16',
    0x40080078: 'FLASH.RESERVED2.17',
    0x4008007C: 'FLASH.RESERVED2.18',
    0x40080080: 'FLASH.RESERVED2.19',
    0x40080084: 'FLASH.RESERVED2.20',
    0x40080088: 'FLASH.RESERVED2.21',
    0x4008008C: 'FLASH.RESERVED2.22',
    0x40080090: 'FLASH.RESERVED2.23',
    0x40080094: 'FLASH.RESERVED2.24',
    0x40080098: 'FLASH.RESERVED2.25',
    0x4008009C: 'FLASH.RESERVED2.26',
    0x400800A0: 'FLASH.RESERVED2.27',
    0x400800A4: 'FLASH.RESERVED2.28',
    0x400800A8: 'FLASH.RESERVED2.29',
    0x400800AC: 'FLASH.RESERVED2.30',
    0x400800B0: 'FLASH.RESERVED2.31',
    0x400800B4: 'FLASH.RESERVED2.32',
    0x400800B8: 'FLASH.RESERVED2.33',
    0x400800BC: 'FLASH.RESERVED2.34',
    0x400800C0: 'FLASH.RESERVED2.35',
    0x400800C4: 'FLASH.RESERVED2.36',
    0x400800C8: 'FLASH.RESERVED2.37',
    0x400800CC: 'FLASH.RESERVED2.38',
    0x400800D0: 'FLASH.RESERVED2.39',
    0x400800D4: 'FLASH.RESERVED2.40',
    0x400800D8: 'FLASH.RESERVED2.41',
    0x400800DC: 'FLASH.RESERVED2.42',
    0x400800E0: 'FLASH.RESERVED2.43',
    0x400800E4: 'FLASH.RESERVED2.44',
    0x400800E8: 'FLASH.RESERVED2.45',
    0x400800EC: 'FLASH.RESERVED2.46',
    0x400800F0: 'FLASH.RESERVED2.47',
    0x400800F4: 'FLASH.RESERVED2.48',
    0x400800F8: 'FLASH.RESERVED2.49',
    0x400800FC: 'FLASH.RESERVED2.50',
    0x40080100: 'FLASH.VMCR',
    0x40080104: 'FLASH.RESERVED3.0',
    0x40080108: 'FLASH.RESERVED3.1',
    0x4008010C: 'FLASH.RESERVED3.2',
    0x40080110: 'FLASH.RESERVED3.3',
    0x40080114: 'FLASH.RESERVED3.4',
    0x40080118: 'FLASH.RESERVED3.5',
    0x4008011C: 'FLASH.RESERVED3.6',
    0x40080120: 'FLASH.RESERVED3.7',
    0x40080124: 'FLASH.RESERVED3.8',
    0x40080128: 'FLASH.RESERVED3.9',
    0x4008012C: 'FLASH.RESERVED3.10',
    0x40080130: 'FLASH.RESERVED3.11',
    0x40080134: 'FLASH.RESERVED3.12',
    0x40080138: 'FLASH.RESERVED3.13',
    0x4008013C: 'FLASH.RESERVED3.14',
    0x40080140: 'FLASH.RESERVED3.15',
    0x40080144: 'FLASH.RESERVED3.16',
    0x40080148: 'FLASH.RESERVED3.17',
    0x4008014C: 'FLASH.RESERVED3.18',
    0x40080150: 'FLASH.RESERVED3.19',
    0x40080154: 'FLASH.RESERVED3.20',
    0x40080158: 'FLASH.RESERVED3.21',
    0x4008015C: 'FLASH.RESERVED3.22',
    0x40080160: 'FLASH.RESERVED3.23',
    0x40080164: 'FLASH.RESERVED3.24',
    0x40080168: 'FLASH.RESERVED3.25',
    0x4008016C: 'FLASH.RESERVED3.26',
    0x40080170: 'FLASH.RESERVED3.27',
    0x40080174: 'FLASH.RESERVED3.28',
    0x40080178: 'FLASH.RESERVED3.29',
    0x4008017C: 'FLASH.RESERVED3.30',
    0x40080180: 'FLASH.MDID',
    0x40080184: 'FLASH.PNSR',
    0x40080188: 'FLASH.PSSR',
    0x4008018C: 'FLASH.RESERVED4.0',
    0x40080190: 'FLASH.RESERVED4.1',
    0x40080194: 'FLASH.RESERVED4.2',
    0x40080198: 'FLASH.RESERVED4.3',
    0x4008019C: 'FLASH.RESERVED4.4',
    0x400801A0: 'FLASH.RESERVED4.5',
    0x400801A4: 'FLASH.RESERVED4.6',
    0x400801A8: 'FLASH.RESERVED4.7',
    0x400801AC: 'FLASH.RESERVED4.8',
    0x400801B0: 'FLASH.RESERVED4.9',
    0x400801B4: 'FLASH.RESERVED4.10',
    0x400801B8: 'FLASH.RESERVED4.11',
    0x400801BC: 'FLASH.RESERVED4.12',
    0x400801C0: 'FLASH.RESERVED4.13',
    0x400801C4: 'FLASH.RESERVED4.14',
    0x400801C8: 'FLASH.RESERVED4.15',
    0x400801CC: 'FLASH.RESERVED4.16',
    0x400801D0: 'FLASH.RESERVED4.17',
    0x400801D4: 'FLASH.RESERVED4.18',
    0x400801D8: 'FLASH.RESERVED4.19',
    0x400801DC: 'FLASH.RESERVED4.20',
    0x400801E0: 'FLASH.RESERVED4.21',
    0x400801E4: 'FLASH.RESERVED4.22',
    0x400801E8: 'FLASH.RESERVED4.23',
    0x400801EC: 'FLASH.RESERVED4.24',
    0x400801F0: 'FLASH.RESERVED4.25',
    0x400801F4: 'FLASH.RESERVED4.26',
    0x400801F8: 'FLASH.RESERVED4.27',
    0x400801FC: 'FLASH.RESERVED4.28',
    0x40080200: 'FLASH.CFCR',
    0x40080204: 'FLASH.RESERVED5.0',
    0x40080208: 'FLASH.RESERVED5.1',
    0x4008020C: 'FLASH.RESERVED5.2',
    0x40080210: 'FLASH.RESERVED5.3',
    0x40080214: 'FLASH.RESERVED5.4',
    0x40080218: 'FLASH.RESERVED5.5',
    0x4008021C: 'FLASH.RESERVED5.6',
    0x40080220: 'FLASH.RESERVED5.7',
    0x40080224: 'FLASH.RESERVED5.8',
    0x40080228: 'FLASH.RESERVED5.9',
    0x4008022C: 'FLASH.RESERVED5.10',
    0x40080230: 'FLASH.RESERVED5.11',
    0x40080234: 'FLASH.RESERVED5.12',
    0x40080238: 'FLASH.RESERVED5.13',
    0x4008023C: 'FLASH.RESERVED5.14',
    0x40080240: 'FLASH.RESERVED5.15',
    0x40080244: 'FLASH.RESERVED5.16',
    0x40080248: 'FLASH.RESERVED5.17',
    0x4008024C: 'FLASH.RESERVED5.18',
    0x40080250: 'FLASH.RESERVED5.19',
    0x40080254: 'FLASH.RESERVED5.20',
    0x40080258: 'FLASH.RESERVED5.21',
    0x4008025C: 'FLASH.RESERVED5.22',
    0x40080260: 'FLASH.RESERVED5.23',
    0x40080264: 'FLASH.RESERVED5.24',
    0x40080268: 'FLASH.RESERVED5.25',
    0x4008026C: 'FLASH.RESERVED5.26',
    0x40080270: 'FLASH.RESERVED5.27',
    0x40080274: 'FLASH.RESERVED5.28',
    0x40080278: 'FLASH.RESERVED5.29',
    0x4008027C: 'FLASH.RESERVED5.30',
    0x40080280: 'FLASH.RESERVED5.31',
    0x40080284: 'FLASH.RESERVED5.32',
    0x40080288: 'FLASH.RESERVED5.33',
    0x4008028C: 'FLASH.RESERVED5.34',
    0x40080290: 'FLASH.RESERVED5.35',
    0x40080294: 'FLASH.RESERVED5.36',
    0x40080298: 'FLASH.RESERVED5.37',
    0x4008029C: 'FLASH.RESERVED5.38',
    0x400802A0: 'FLASH.RESERVED5.39',
    0x400802A4: 'FLASH.RESERVED5.40',
    0x400802A8: 'FLASH.RESERVED5.41',
    0x400802AC: 'FLASH.RESERVED5.42',
    0x400802B0: 'FLASH.RESERVED5.43',
    0x400802B4: 'FLASH.RESERVED5.44',
    0x400802B8: 'FLASH.RESERVED5.45',
    0x400802BC: 'FLASH.RESERVED5.46',
    0x400802C0: 'FLASH.RESERVED5.47',
    0x400802C4: 'FLASH.RESERVED5.48',
    0x400802C8: 'FLASH.RESERVED5.49',
    0x400802CC: 'FLASH.RESERVED5.50',
    0x400802D0: 'FLASH.RESERVED5.51',
    0x400802D4: 'FLASH.RESERVED5.52',
    0x400802D8: 'FLASH.RESERVED5.53',
    0x400802DC: 'FLASH.RESERVED5.54',
    0x400802E0: 'FLASH.RESERVED5.55',
    0x400802E4: 'FLASH.RESERVED5.56',
    0x400802E8: 'FLASH.RESERVED5.57',
    0x400802EC: 'FLASH.RESERVED5.58',
    0x400802F0: 'FLASH.RESERVED5.59',
    0x400802F4: 'FLASH.RESERVED5.60',
    0x400802F8: 'FLASH.RESERVED5.61',
    0x400802FC: 'FLASH.RESERVED5.62',
    0x40080300: 'FLASH.SBVT.0',
    0x40080304: 'FLASH.SBVT.1',
    0x40080308: 'FLASH.SBVT.2',
    0x4008030C: 'FLASH.SBVT.3',
    0x40088000: 'CKCU.GCFGR',
    0x40088004: 'CKCU.GCCR',
    0x40088008: 'CKCU.GCSR',
    0x4008800C: 'CKCU.GCIR',
    0x40088010: 'CKCU.RESERVED0.0',
    0x40088014: 'CKCU.RESERVED0.1',
    0x40088018: 'CKCU.PLLCFGR',
    0x4008801C: 'CKCU.PLLCR',
    0x40088020: 'CKCU.AHBCFGR',
    0x40088024: 'CKCU.AHBCCR',
    0x40088028: 'CKCU.APBCFGR',
    0x4008802C: 'CKCU.APBCCR0',
    0x40088030: 'CKCU.APBCCR1',
    0x40088034: 'CKCU.CKST',
    0x40088038: 'CKCU.APBPCSR0',
    0x4008803C: 'CKCU.APBPCSR1',
    0x40088040: 'CKCU.HSICR',
    0x40088044: 'CKCU.HSIATCR',
    0x40088048: 'CKCU.RESERVED1.0',
    0x4008804C: 'CKCU.RESERVED1.1',
    0x40088050: 'CKCU.RESERVED1.2',
    0x40088054: 'CKCU.RESERVED1.3',
    0x40088058: 'CKCU.RESERVED1.4',
    0x4008805C: 'CKCU.RESERVED1.5',
    0x40088060: 'CKCU.RESERVED1.6',
    0x40088064: 'CKCU.RESERVED1.7',
    0x40088068: 'CKCU.RESERVED1.8',
    0x4008806C: 'CKCU.RESERVED1.9',
    0x40088070: 'CKCU.RESERVED1.10',
    0x40088074: 'CKCU.RESERVED1.11',
    0x40088078: 'CKCU.RESERVED1.12',
    0x4008807C: 'CKCU.RESERVED1.13',
    0x40088080: 'CKCU.RESERVED1.14',
    0x40088084: 'CKCU.RESERVED1.15',
    0x40088088: 'CKCU.RESERVED1.16',
    0x4008808C: 'CKCU.RESERVED1.17',
    0x40088090: 'CKCU.RESERVED1.18',
    0x40088094: 'CKCU.RESERVED1.19',
    0x40088098: 'CKCU.RESERVED1.20',
    0x4008809C: 'CKCU.RESERVED1.21',
    0x400880A0: 'CKCU.RESERVED1.22',
    0x400880A4: 'CKCU.RESERVED1.23',
    0x400880A8: 'CKCU.RESERVED1.24',
    0x400880AC: 'CKCU.RESERVED1.25',
    0x400880B0: 'CKCU.RESERVED1.26',
    0x400880B4: 'CKCU.RESERVED1.27',
    0x400880B8: 'CKCU.RESERVED1.28',
    0x400880BC: 'CKCU.RESERVED1.29',
    0x400880C0: 'CKCU.RESERVED1.30',
    0x400880C4: 'CKCU.RESERVED1.31',
    0x400880C8: 'CKCU.RESERVED1.32',
    0x400880CC: 'CKCU.RESERVED1.33',
    0x400880D0: 'CKCU.RESERVED1.34',
    0x400880D4: 'CKCU.RESERVED1.35',
    0x400880D8: 'CKCU.RESERVED1.36',
    0x400880DC: 'CKCU.RESERVED1.37',
    0x400880E0: 'CKCU.RESERVED1.38',
    0x400880E4: 'CKCU.RESERVED1.39',
    0x400880E8: 'CKCU.RESERVED1.40',
    0x400880EC: 'CKCU.RESERVED1.41',
    0x400880F0: 'CKCU.RESERVED1.42',
    0x400880F4: 'CKCU.RESERVED1.43',
    0x400880F8: 'CKCU.RESERVED1.44',
    0x400880FC: 'CKCU.RESERVED1.45',
    0x40088100: 'RSTCU.GRSR',
    0x40088104: 'RSTCU.AHBPRST',
    0x40088108: 'RSTCU.APBPRST0',
    0x4008810C: 'RSTCU.APBPRST1',
    0x40088110: 'CKCU.RESERVED1.50',
    0x40088114: 'CKCU.RESERVED1.51',
    0x40088118: 'CKCU.RESERVED1.52',
    0x4008811C: 'CKCU.RESERVED1.53',
    0x40088120: 'CKCU.RESERVED1.54',
    0x40088124: 'CKCU.RESERVED1.55',
    0x40088128: 'CKCU.RESERVED1.56',
    0x4008812C: 'CKCU.RESERVED1.57',
    0x40088130: 'CKCU.RESERVED1.58',
    0x40088134: 'CKCU.RESERVED1.59',
    0x40088138: 'CKCU.RESERVED1.60',
    0x4008813C: 'CKCU.RESERVED1.61',
    0x40088140: 'CKCU.RESERVED1.62',
    0x40088144: 'CKCU.RESERVED1.63',
    0x40088148: 'CKCU.RESERVED1.64',
    0x4008814C: 'CKCU.RESERVED1.65',
    0x40088150: 'CKCU.RESERVED1.66',
    0x40088154: 'CKCU.RESERVED1.67',
    0x40088158: 'CKCU.RESERVED1.68',
    0x4008815C: 'CKCU.RESERVED1.69',
    0x40088160: 'CKCU.RESERVED1.70',
    0x40088164: 'CKCU.RESERVED1.71',
    0x40088168: 'CKCU.RESERVED1.72',
    0x4008816C: 'CKCU.RESERVED1.73',
    0x40088170: 'CKCU.RESERVED1.74',
    0x40088174: 'CKCU.RESERVED1.75',
    0x40088178: 'CKCU.RESERVED1.76',
    0x4008817C: 'CKCU.RESERVED1.77',
    0x40088180: 'CKCU.RESERVED1.78',
    0x40088184: 'CKCU.RESERVED1.79',
    0x40088188: 'CKCU.RESERVED1.80',
    0x4008818C: 'CKCU.RESERVED1.81',
    0x40088190: 'CKCU.RESERVED1.82',
    0x40088194: 'CKCU.RESERVED1.83',
    0x40088198: 'CKCU.RESERVED1.84',
    0x4008819C: 'CKCU.RESERVED1.85',
    0x400881A0: 'CKCU.RESERVED1.86',
    0x400881A4: 'CKCU.RESERVED1.87',
    0x400881A8: 'CKCU.RESERVED1.88',
    0x400881AC: 'CKCU.RESERVED1.89',
    0x400881B0: 'CKCU.RESERVED1.90',
    0x400881B4: 'CKCU.RESERVED1.91',
    0x400881B8: 'CKCU.RESERVED1.92',
    0x400881BC: 'CKCU.RESERVED1.93',
    0x400881C0: 'CKCU.RESERVED1.94',
    0x400881C4: 'CKCU.RESERVED1.95',
    0x400881C8: 'CKCU.RESERVED1.96',
    0x400881CC: 'CKCU.RESERVED1.97',
    0x400881D0: 'CKCU.RESERVED1.98',
    0x400881D4: 'CKCU.RESERVED1.99',
    0x400881D8: 'CKCU.RESERVED1.100',
    0x400881DC: 'CKCU.RESERVED1.101',
    0x400881E0: 'CKCU.RESERVED1.102',
    0x400881E4: 'CKCU.RESERVED1.103',
    0x400881E8: 'CKCU.RESERVED1.104',
    0x400881EC: 'CKCU.RESERVED1.105',
    0x400881F0: 'CKCU.RESERVED1.106',
    0x400881F4: 'CKCU.RESERVED1.107',
    0x400881F8: 'CKCU.RESERVED1.108',
    0x400881FC: 'CKCU.RESERVED1.109',
    0x40088200: 'CKCU.RESERVED1.110',
    0x40088204: 'CKCU.RESERVED1.111',
    0x40088208: 'CKCU.RESERVED1.112',
    0x4008820C: 'CKCU.RESERVED1.113',
    0x40088210: 'CKCU.RESERVED1.114',
    0x40088214: 'CKCU.RESERVED1.115',
    0x40088218: 'CKCU.RESERVED1.116',
    0x4008821C: 'CKCU.RESERVED1.117',
    0x40088220: 'CKCU.RESERVED1.118',
    0x40088224: 'CKCU.RESERVED1.119',
    0x40088228: 'CKCU.RESERVED1.120',
    0x4008822C: 'CKCU.RESERVED1.121',
    0x40088230: 'CKCU.RESERVED1.122',
    0x40088234: 'CKCU.RESERVED1.123',
    0x40088238: 'CKCU.RESERVED1.124',
    0x4008823C: 'CKCU.RESERVED1.125',
    0x40088240: 'CKCU.RESERVED1.126',
    0x40088244: 'CKCU.RESERVED1.127',
    0x40088248: 'CKCU.RESERVED1.128',
    0x4008824C: 'CKCU.RESERVED1.129',
    0x40088250: 'CKCU.RESERVED1.130',
    0x40088254: 'CKCU.RESERVED1.131',
    0x40088258: 'CKCU.RESERVED1.132',
    0x4008825C: 'CKCU.RESERVED1.133',
    0x40088260: 'CKCU.RESERVED1.134',
    0x40088264: 'CKCU.RESERVED1.135',
    0x40088268: 'CKCU.RESERVED1.136',
    0x4008826C: 'CKCU.RESERVED1.137',
    0x40088270: 'CKCU.RESERVED1.138',
    0x40088274: 'CKCU.RESERVED1.139',
    0x40088278: 'CKCU.RESERVED1.140',
    0x4008827C: 'CKCU.RESERVED1.141',
    0x40088280: 'CKCU.RESERVED1.142',
    0x40088284: 'CKCU.RESERVED1.143',
    0x40088288: 'CKCU.RESERVED1.144',
    0x4008828C: 'CKCU.RESERVED1.145',
    0x40088290: 'CKCU.RESERVED1.146',
    0x40088294: 'CKCU.RESERVED1.147',
    0x40088298: 'CKCU.RESERVED1.148',
    0x4008829C: 'CKCU.RESERVED1.149',
    0x400882A0: 'CKCU.RESERVED1.150',
    0x400882A4: 'CKCU.RESERVED1.151',
    0x400882A8: 'CKCU.RESERVED1.152',
    0x400882AC: 'CKCU.RESERVED1.153',
    0x400882B0: 'CKCU.RESERVED1.154',
    0x400882B4: 'CKCU.RESERVED1.155',
    0x400882B8: 'CKCU.RESERVED1.156',
    0x400882BC: 'CKCU.RESERVED1.157',
    0x400882C0: 'CKCU.RESERVED1.158',
    0x400882C4: 'CKCU.RESERVED1.159',
    0x400882C8: 'CKCU.RESERVED1.160',
    0x400882CC: 'CKCU.RESERVED1.161',
    0x400882D0: 'CKCU.RESERVED1.162',
    0x400882D4: 'CKCU.RESERVED1.163',
    0x400882D8: 'CKCU.RESERVED1.164',
    0x400882DC: 'CKCU.RESERVED1.165',
    0x400882E0: 'CKCU.RESERVED1.166',
    0x400882E4: 'CKCU.RESERVED1.167',
    0x400882E8: 'CKCU.RESERVED1.168',
    0x400882EC: 'CKCU.RESERVED1.169',
    0x400882F0: 'CKCU.RESERVED1.170',
    0x400882F4: 'CKCU.RESERVED1.171',
    0x400882F8: 'CKCU.RESERVED1.172',
    0x400882FC: 'CKCU.RESERVED1.173',
    0x40088300: 'CKCU.LPCR',
    0x40088304: 'CKCU.MCUDBGCR',
    0x40043000: 'SCI0.CR',
    0x40043004: 'SCI0.SR',
    0x40043008: 'SCI0.CCR',
    0x4004300C: 'SCI0.ETU',
    0x40043010: 'SCI0.GT',
    0x40043014: 'SCI0.WT',
    0x40043018: 'SCI0.IER',
    0x4004301C: 'SCI0.IPR',
    0x40043020: 'SCI0.TXB',
    0x40043024: 'SCI0.RXB',
    0x40043028: 'SCI0.PSC',
    0x4003A000: 'SCI1.CR',
    0x4003A004: 'SCI1.SR',
    0x4003A008: 'SCI1.CCR',
    0x4003A00C: 'SCI1.ETU',
    0x4003A010: 'SCI1.GT',
    0x4003A014: 'SCI1.WT',
    0x4003A018: 'SCI1.IER',
    0x4003A01C: 'SCI1.IPR',
    0x4003A020: 'SCI1.TXB',
    0x4003A024: 'SCI1.RXB',
    0x4003A028: 'SCI1.PSC',
    0x40076000: 'BFTM0.CR',
    0x40076004: 'BFTM0.SR',
    0x40076008: 'BFTM0.CNTR',
    0x4007600C: 'BFTM0.CMP',
    0x40077000: 'BFTM1.CR',
    0x40077004: 'BFTM1.SR',
    0x40077008: 'BFTM1.CNTR',
    0x4007700C: 'BFTM1.CMP',
    0x40090000: 'PDMA.PDMACH0.CR',
    0x40090004: 'PDMA.PDMACH0.SADR',
    0x40090008: 'PDMA.PDMACH0.DADR',
    0x4009000C: 'PDMA.PDMACH0.CADR',
    0x40090010: 'PDMA.PDMACH0.TSR',
    0x40090014: 'PDMA.PDMACH0.CTSR',
    0x40090018: 'PDMA.PDMACH1.CR',
    0x4009001C: 'PDMA.PDMACH1.SADR',
    0x40090020: 'PDMA.PDMACH1.DADR',
    0x40090024: 'PDMA.PDMACH1.CADR',
    0x40090028: 'PDMA.PDMACH1.TSR',
    0x4009002C: 'PDMA.PDMACH1.CTSR',
    0x40090030: 'PDMA.PDMACH2.CR',
    0x40090034: 'PDMA.PDMACH2.SADR',
    0x40090038: 'PDMA.PDMACH2.DADR',
    0x4009003C: 'PDMA.PDMACH2.CADR',
    0x40090040: 'PDMA.PDMACH2.TSR',
    0x40090044: 'PDMA.PDMACH2.CTSR',
    0x40090048: 'PDMA.PDMACH3.CR',
    0x4009004C: 'PDMA.PDMACH3.SADR',
    0x40090050: 'PDMA.PDMACH3.DADR',
    0x40090054: 'PDMA.PDMACH3.CADR',
    0x40090058: 'PDMA.PDMACH3.TSR',
    0x4009005C: 'PDMA.PDMACH3.CTSR',
    0x40090060: 'PDMA.PDMACH4.CR',
    0x40090064: 'PDMA.PDMACH4.SADR',
    0x40090068: 'PDMA.PDMACH4.DADR',
    0x4009006C: 'PDMA.PDMACH4.CADR',
    0x40090070: 'PDMA.PDMACH4.TSR',
    0x40090074: 'PDMA.PDMACH4.CTSR',
    0x40090078: 'PDMA.PDMACH5.CR',
    0x4009007C: 'PDMA.PDMACH5.SADR',
    0x40090080: 'PDMA.PDMACH5.DADR',
    0x40090084: 'PDMA.PDMACH5.CADR',
    0x40090088: 'PDMA.PDMACH5.TSR',
    0x4009008C: 'PDMA.PDMACH5.CTSR',
    0x40090090: 'PDMA.PDMACH6.CR',
    0x40090094: 'PDMA.PDMACH6.SADR',
    0x40090098: 'PDMA.PDMACH6.DADR',
    0x4009009C: 'PDMA.PDMACH6.CADR',
    0x400900A0: 'PDMA.PDMACH6.TSR',
    0x400900A4: 'PDMA.PDMACH6.CTSR',
    0x400900A8: 'PDMA.PDMACH7.CR',
    0x400900AC: 'PDMA.PDMACH7.SADR',
    0x400900B0: 'PDMA.PDMACH7.DADR',
    0x400900B4: 'PDMA.PDMACH7.CADR',
    0x400900B8: 'PDMA.PDMACH7.TSR',
    0x400900BC: 'PDMA.PDMACH7.CTSR',
    0x400900C0: 'PDMA.RESERVED0.0',
    0x400900C4: 'PDMA.RESERVED0.1',
    0x400900C8: 'PDMA.RESERVED0.2',
    0x400900CC: 'PDMA.RESERVED0.3',
    0x400900D0: 'PDMA.RESERVED0.4',
    0x400900D4: 'PDMA.RESERVED0.5',
    0x400900D8: 'PDMA.RESERVED0.6',
    0x400900DC: 'PDMA.RESERVED0.7',
    0x400900E0: 'PDMA.RESERVED0.8',
    0x400900E4: 'PDMA.RESERVED0.9',
    0x400900E8: 'PDMA.RESERVED0.10',
    0x400900EC: 'PDMA.RESERVED0.11',
    0x400900F0: 'PDMA.RESERVED0.12',
    0x400900F4: 'PDMA.RESERVED0.13',
    0x400900F8: 'PDMA.RESERVED0.14',
    0x400900FC: 'PDMA.RESERVED0.15',
    0x40090100: 'PDMA.RESERVED0.16',
    0x40090104: 'PDMA.RESERVED0.17',
    0x40090108: 'PDMA.RESERVED0.18',
    0x4009010C: 'PDMA.RESERVED0.19',
    0x40090110: 'PDMA.RESERVED0.20',
    0x40090114: 'PDMA.RESERVED0.21',
    0x40090118: 'PDMA.RESERVED0.22',
    0x4009011C: 'PDMA.RESERVED0.23',
    0x40090120: 'PDMA.ISR0',
    0x40090124: 'PDMA.ISR1',
    0x40090128: 'PDMA.ISCR0',
    0x4009012C: 'PDMA.ISCR1',
    0x40090130: 'PDMA.IER0',
    0x40090134: 'PDMA.IER1',
    0x400A8000: 'USB.CSR',
    0x400A8004: 'USB.IER',
    0x400A8008: 'USB.ISR',
    0x400A800C: 'USB.FCR',
    0x400A8010: 'USB.DEVAR',
    0x400A8014: 'USB.EP0CSR',
    0x400A8018: 'USB.EP0IER',
    0x400A801C: 'USB.EP0ISR',
    0x400A8020: 'USB.EP0TCR',
    0x400A8024: 'USB.EP0CFGR',
    0x400A8028: 'USB.EP1CSR',
    0x400A802C: 'USB.EP1IER',
    0x400A8030: 'USB.EP1ISR',
    0x400A8034: 'USB.EP1TCR',
    0x400A8038: 'USB.EP1CFGR',
    0x400A803C: 'USB.EP2CSR',
    0x400A8040: 'USB.EP2IER',
    0x400A8044: 'USB.EP2ISR',
    0x400A8048: 'USB.EP2TCR',
    0x400A804C: 'USB.EP2CFGR',
    0x400A8050: 'USB.EP3CSR',
    0x400A8054: 'USB.EP3IER',
    0x400A8058: 'USB.EP3ISR',
    0x400A805C: 'USB.EP3TCR',
    0x400A8060: 'USB.EP3CFGR',
    0x400A8064: 'USB.EP4CSR',
    0x400A8068: 'USB.EP4IER',
    0x400A806C: 'USB.EP4ISR',
    0x400A8070: 'USB.EP4TCR',
    0x400A8074: 'USB.EP4CFGR',
    0x400A8078: 'USB.EP5CSR',
    0x400A807C: 'USB.EP5IER',
    0x400A8080: 'USB.EP5ISR',
    0x400A8084: 'USB.EP5TCR',
    0x400A8088: 'USB.EP5CFGR',
    0x400A808C: 'USB.EP6CSR',
    0x400A8090: 'USB.EP6IER',
    0x400A8094: 'USB.EP6ISR',
    0x400A8098: 'USB.EP6TCR',
    0x400A809C: 'USB.EP6CFGR',
    0x400A80A0: 'USB.EP7CSR',
    0x400A80A4: 'USB.EP7IER',
    0x400A80A8: 'USB.EP7ISR',
    0x400A80AC: 'USB.EP7TCR',
    0x400A80B0: 'USB.EP7CFGR',
    0x40098000: 'EBI.CR',
    0x40098004: 'EBI.PCR',
    0x40098008: 'EBI.SR',
    0x4009800C: 'EBI.RESERVED1',
    0x40098010: 'EBI.ATR0',
    0x40098014: 'EBI.RTR0',
    0x40098018: 'EBI.WTR0',
    0x4009801C: 'EBI.PR0',
    0x40098020: 'EBI.ATR1',
    0x40098024: 'EBI.RTR1',
    0x40098028: 'EBI.WTR1',
    0x4009802C: 'EBI.PR1',
    0x40098030: 'EBI.ATR2',
    0x40098034: 'EBI.RTR2',
    0x40098038: 'EBI.WTR2',
    0x4009803C: 'EBI.PR2',
    0x40098040: 'EBI.ATR3',
    0x40098044: 'EBI.RTR3',
    0x40098048: 'EBI.WTR3',
    0x4009804C: 'EBI.PR3',
    0x40098050: 'EBI.IEN',
    0x40098054: 'EBI.IF',
    0x40098058: 'EBI.IFC',
    0x4008A000: 'CRC.CR',
    0x4008A004: 'CRC.SDR',
    0x4008A008: 'CRC.CSR',
    0x4008A00C: 'CRC.DR',
    0x40026000: 'I2S.CR',
    0x40026004: 'I2S.IER',
    0x40026008: 'I2S.CDR',
    0x4002600C: 'I2S.TXDR',
    0x40026010: 'I2S.RXDR',
    0x40026014: 'I2S.FCR',
    0x40026018: 'I2S.SR',
    0x4002601C: 'I2S.RCNTR',
    0x400A0000: 'SDIO.BLKSIZE',
    0x400A0004: 'SDIO.BLKCNT',
    0x400A0008: 'SDIO.ARG',
    0x400A000C: 'SDIO.TMR',
    0x400A0010: 'SDIO.CMD',
    0x400A0014: 'SDIO.RESP0',
    0x400A0018: 'SDIO.RESP1',
    0x400A001C: 'SDIO.RESP2',
    0x400A0020: 'SDIO.RESP3',
    0x400A0024: 'SDIO.DR',
    0x400A0028: 'SDIO.PSR',
    0x400A002C: 'SDIO.CR',
    0x400A0030: 'SDIO.RESERVED0.0',
    0x400A0034: 'SDIO.RESERVED0.1',
    0x400A0038: 'SDIO.CLKCR',
    0x400A003C: 'SDIO.TMOCR',
    0x400A0040: 'SDIO.SWRST',
    0x400A0044: 'SDIO.SR',
    0x400A0048: 'SDIO.SER',
    0x400A004C: 'SDIO.IER',
    0x400CC000: 'CSIF.ENR',
    0x400CC004: 'CSIF.CR',
    0x400CC008: 'CSIF.IMGWH',
    0x400CC00C: 'CSIF.WCR0',
    0x400CC010: 'CSIF.WCR1',
    0x400CC014: 'CSIF.SMP',
    0x400CC018: 'CSIF.SMPCOL',
    0x400CC01C: 'CSIF.SMPROW',
    0x400CC020: 'CSIF.FIFO0',
    0x400CC024: 'CSIF.FIFO1',
    0x400CC028: 'CSIF.FIFO2',
    0x400CC02C: 'CSIF.FIFO3',
    0x400CC030: 'CSIF.FIFO4',
    0x400CC034: 'CSIF.FIFO5',
    0x400CC038: 'CSIF.FIFO6',
    0x400CC03C: 'CSIF.FIFO7',
    0x400CC040: 'CSIF.IER',
    0x400CC044: 'CSIF.SR',
    0x400C8000: 'AES.CR',
    0x400C8004: 'AES.SR',
    0x400C8008: 'AES.PDMAR',
    0x400C800C: 'AES.ISR',
    0x400C8010: 'AES.IER',
    0x400C8014: 'AES.DINR',
    0x400C8018: 'AES.DOUTR',
    0x400C801C: 'AES.KEYR.0',
    0x400C8020: 'AES.KEYR.1',
    0x400C8024: 'AES.KEYR.2',
    0x400C8028: 'AES.KEYR.3',
    0x400C802C: 'AES.KEYR.4',
    0x400C8030: 'AES.KEYR.5',
    0x400C8034: 'AES.KEYR.6',
    0x400C8038: 'AES.KEYR.7',
    0x400C803C: 'AES.IVR.0',
    0x400C8040: 'AES.IVR.1',
    0x400C8044: 'AES.IVR.2',
    0x400C8048: 'AES.IVR.3',
}


INTERRUPT_TABLE = [
    'Reset',
    'NMI',
    'Hard_Fault',
    'Memory_Management_Fault',
    'Bus_Fault',
    'Usage_Fault',
    'Reserved_0',
    'Reserved_1',
    'Reserved_2',
    'Reserved_3',
    'SVCCall',
    'Debug_Monitor',
    'Reserved_4',
    'PendSV',
    'SysTick',
    'CKRDY',
    'LVD',
    'BOD',
    'WDT',
    'RTC',
    'FMC',
    'EVWUP',
    'LPWUPIRQ7',
    'EXTI0',
    'EXTI1',
    'EXTI2',
    'EXTI3',
    'EXTI4',
    'EXTI5',
    'EXTI6',
    'EXTI7',
    'EXTI8',
    'EXTI9',
    'EXTI10',
    'EXTI11',
    'EXTI12',
    'EXTI13',
    'EXTI14',
    'EXTI15',
    'COMP',
    'ADC',
    'Reserved_5',
    'MCTM0_BRK',
    'MCTM0_UP',
    'MCTM0_TR_UP2',
    'MCTM0_CC',
    'MCTM1_BRK',
    'MCTM1_UP',
    'MCTM1_TR_UP2',
    'MCTM1_CC',
    'GPTM0',
    'GPTM1',
    'Reserved_6',
    'Reserved_7',
    'Reserved_8',
    'Reserved_9',
    'BFTM0',
    'BFTM1',
    'I2C0',
    'I2C1',
    'SPI0',
    'SPI1',
    'USART0',
    'USART1',
    'UART0',
    'UART1',
    'SCI',
    'I2S',
    'USB',
    'Reserved_10',
    'PDMA_CH0',
    'PDMA_CH1',
    'PDMA_CH2',
    'PDMA_CH3',
    'PDMA_CH4',
    'PDMA_CH5',
    'PDMA_CH6',
    'PDMA_CH7',
    'Reserved_11',
    'Reserved_12',
    'Reserved_13',
    'Reserved_14',
    'Reserved_15',
    'EBI'
]