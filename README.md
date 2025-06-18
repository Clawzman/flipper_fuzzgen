# Flipper Fuzzer/Bruteforce
# Flipper Zero RFID/NFC/iButton Fuzzer List Generator

This is a **Flipper Zero RFID/NFC/iButton Fuzzer List Generator** script that allows users to generate random RFID, NFC, and iButton IDs for various protocols. The tool is designed to help with testing and experimentation with RFID/NFC amd iButton technologies.

The script supports generating IDs for multiple protocols, including popular ones like **EM4100**, **HID Prox**, **MIFARE Classic**, **iClass**, and more. 
You can choose to generate IDs with or without manufacturer-specific prefixes based on the selected protocol.

## Features:
- **Supports multiple protocols**: Generate IDs for 15 RFID protocols, 5 NFC protocols, and 7 iButton protocols.
- **Prefix option**: Choose to generate IDs with manufacturer-specific prefixes (if available).
- **Choose specific prefix(es)**: If multiple prefixes are available for a protocol,the user can, use all available prefixes (default), or select one or more prefixes manually by index.
- **Customizable ID length**: Control the number of IDs to generate and the length of each ID.
- **Output options**: IDs are saved to a `.txt` file, making it easy to use for testing or other purposes.
- **Easy to use**: The script is simple to run and interact with via the terminal.

## Protocols Supported:
- **RFID Protocols**: EM4100, HID Prox, Indala, IoProx, PAC/Stanley, Paradox, Viking, Pyramid, Keri, Nexwatch, H10301, Jablotron, Electra, IDTeck, Gallagher.
- **NFC Protocols**: MIFARE Classic 1K, MIFARE Classic 4K, MIFARE Ultralight, DESFire EV1, iCLASS, FeliCa.
- **iButton Protocols**: Dallas DS1990, Cyfral, Metacom, Maxim iButton, Keypad/Access Control, Temperature iButton, Custom iButton.

## Installation:
1. Clone or download this repository to your local machine.
2. Make sure you have **Python 3** installed on your system.
3. Install any necessary dependencies (if any are specified, or you can install them manually if needed).

## Usage:
1. Navigate to the directory where the script is located using your terminal/command prompt.
2. Run the script with Python:
   ```bash
   python List_EM.py
