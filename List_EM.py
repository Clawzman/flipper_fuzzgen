import random
import os
import sys

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

ASCII_TITLE = f"""{Colors.OKGREEN}
                    .-')    .-') _            ('-.  _   .-')    
                   ( OO ). (  OO) )         _(  OO)( '.( OO )_  
 ,--.      ,-.-') (_)---\\_)/     '._       (,------.,--.   ,--.)
 |  |.-')  |  |OO)/    _ | |'--...__)       |  .---'|   `.'   | 
 |  | OO ) |  |  \\  :` `. '--.  .--'       |  |    |         | 
 |  |`-' | |  |(_/ '..`''.)   |  |         (|  '--. |  |'.'|  | 
(|  '---.',|  |_.'.-._)   \\   |  |          |  .--' |  |   |  | 
 |      |(_|  |   \\       /   |  |          |  `---.|  |   |  | 
 `------'  `--'    `-----'    `--'          `------'`--'   `--'  by CyberClawz {Colors.ENDC}
"""

class Fuzzer:
    RFID_PROTOCOLS = {
        "1": ("EM4100 w/prefix", 5, 0xFFFFFFFFFF, [0x00, 0x01, 0x02, 0x03]),
        "2": ("HID Prox w/prefix", 6, 0xFFFFFFFFFFFF, [0xA0, 0xB0, 0xC0]),
        "3": ("Indala w/prefix", 4, 0xFFFFFFFF, [0x20, 0x21, 0x22]),
        "4": ("IoProx", 4, 0xFFFFFFFF, []),
        "5": ("PAC/Stanley", 4, 0xFFFFFFFF, []),
        "6": ("Paradox", 6, 0xFFFFFFFFFFFF, []),
        "7": ("Viking", 4, 0xFFFFFFFF, []),
        "8": ("Pyramid", 4, 0xFFFFFFFF, []),
        "9": ("Keri", 4, 0xFFFFFFFF, []),
        "10": ("Nexwatch", 8, 0xFFFFFFFFFFFFFFFF, []),
        "11": ("H10301", 3, 0xFFFFFF, []),
        "12": ("Jablotron", 5, 0xFFFFFFFFFF, []),
        "13": ("Electra", 8, 0xFFFFFFFFFFFFFFFF, []),
        "14": ("IDTeck", 8, 0xFFFFFFFFFFFFFFFF, []),
        "15": ("Gallagher", 8, 0xFFFFFFFFFFFFFFFF, []),
    }
    
    NFC_PROTOCOLS = {
        "16": ("MIFARE Classic 1K", 4, 0xFFFFFFFF, []),
        "17": ("MIFARE Classic 4K", 4, 0xFFFFFFFF, []),
        "18": ("MIFARE Ultralight", 7, 0xFFFFFFFFFFFFFF, []),
        "19": ("DESFire EV1", 16, 0xFFFFFFFFFFFFFFFF, []),
        "20": ("iCLASS w/prefix", 8, 0xFFFFFFFFFFFFFFFF, [0xEC]),
        "21": ("FeliCa", 8, 0xFFFFFFFFFFFFFFFF, []),
    }
    
    IBUTTON_PROTOCOLS = {
        "22": ("Dallas DS1990 w/prefix", 8, 0xFFFFFFFFFFFFFFFF, [0x01, 0x02]),
        "23": ("Cyfral", 2, 0xFFFF, []),
        "24": ("Metacom", 4, 0xFFFFFFFF, []),
        "25": ("Maxim iButton", 8, 0xFFFFFFFFFFFFFFFF, []),
        "26": ("Keypad/Access Control", 8, 0xFFFFFFFFFFFFFFFF, []),
        "27": ("Temperature iButton", 8, 0xFFFFFFFFFFFFFFFF, []),
        "28": ("Custom iButton", 8, 0xFFFFFFFFFFFFFFFF, []),
    }
    
    def __init__(self):
        self.protocols = {**self.RFID_PROTOCOLS, **self.NFC_PROTOCOLS, **self.IBUTTON_PROTOCOLS}
    
    def generate_ids(self, id_type, output_file, num_ids, use_prefix):
        name, id_length, id_max, prefixes = self.protocols[id_type]
        print(f"{Colors.OKCYAN}Generating {num_ids} {name} IDs...{Colors.ENDC}")
        
        try:
            with open(output_file, 'w') as file:
                for i in range(num_ids):
                    if use_prefix and prefixes:
                        prefix = random.choice(prefixes)
                        prefix_hex = f"{prefix:02X}"
                        remaining_length = id_length - len(prefix_hex) // 2
                        remaining_id = random.randint(0, (1 << (remaining_length * 8)) - 1)
                        remaining_id_hex = f"{remaining_id:0{remaining_length * 2}X}"
                        card_id_str = prefix_hex + remaining_id_hex
                    else:
                        card_id = random.randint(0, id_max)
                        card_id_str = f"{card_id:0{id_length * 2}X}"
                    
                    file.write(card_id_str + '\n')
                    if (i + 1) % 10000 == 0:
                        print(f"{Colors.OKBLUE}{i + 1} IDs generated...{Colors.ENDC}")
                
                file.write('\n')
            print(f"{Colors.OKGREEN}Dictionary saved to '{output_file}'.{Colors.ENDC}")
        except IOError as e:
            print(f"{Colors.FAIL}Error writing to file: {e}{Colors.ENDC}")
            sys.exit(1)

if __name__ == '__main__':
    print(ASCII_TITLE)
    fuzzer = Fuzzer()
    
    print(f"{Colors.HEADER}{Colors.BOLD}Flipper Zero RFID/NFC/iButton Fuzzer Generator{Colors.ENDC}")
    print(f"{Colors.OKCYAN}------------------------------------------------{Colors.ENDC}")

    while True:
        print(f"\n{Colors.BOLD}{Colors.OKCYAN}Select the protocol category to generate:{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.HEADER}RFID Protocols:{Colors.ENDC}")
        for key, (name, _, _, _) in fuzzer.RFID_PROTOCOLS.items():
            print(f"{Colors.OKCYAN}{key}. {name}{Colors.ENDC}")

        print(f"\n{Colors.BOLD}{Colors.HEADER}NFC Protocols:{Colors.ENDC}")
        for key, (name, _, _, _) in fuzzer.NFC_PROTOCOLS.items():
            print(f"{Colors.OKCYAN}{key}. {name}{Colors.ENDC}")

        print(f"\n{Colors.BOLD}{Colors.HEADER}iButton Protocols:{Colors.ENDC}")
        for key, (name, _, _, _) in fuzzer.IBUTTON_PROTOCOLS.items():
            print(f"{Colors.OKCYAN}{key}. {name}{Colors.ENDC}")

        choice = input(f"\n{Colors.BOLD}Enter your choice (1-28): {Colors.ENDC}").strip()

        if choice in fuzzer.protocols:
            # Check if the selected protocol has prefixes available
            name, _, _, prefixes = fuzzer.protocols[choice]
            use_prefix = False
            if prefixes:  # Only prompt for prefix option if prefixes are available
                use_prefix = input(f"{Colors.BOLD}Use manufacturer-specific prefixes? (y/n): {Colors.ENDC}").strip().lower() == 'y'
            
            num_ids = input(f"{Colors.BOLD}Enter number of IDs to generate (default: 100,000): {Colors.ENDC}").strip()
            num_ids = int(num_ids) if num_ids.isdigit() and int(num_ids) > 0 else 100000

            output_file = input(f"{Colors.BOLD}Enter output filename (default: 'fuzz_list.txt'): {Colors.ENDC}").strip()
            output_file = output_file if output_file else 'fuzz_list.txt'
            if not output_file.endswith('.txt'):
                output_file += '.txt'

            fuzzer.generate_ids(choice, output_file, num_ids, use_prefix)
            break

