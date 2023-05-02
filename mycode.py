import sys

def cEncoder(key:int, note: str) -> str:
    note = note.upper()
    cInput = ""
    count = 0
    
    for character in note:
        characterWord = ord(character)
        if characterWord < 65 or characterWord > 90:
            continue
        
        if count % 50 == 0 and len(cInput) != 0:
            cInput += "\n"
        elif count % 5 == 0 and len(cInput) != 0:
            cInput += " "
            
        cInput += chr(65 + (characterWord - 65 + key) % 26)
        count += 1
    
    return cInput

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error: Invalid arguments. Provide <key> <string> in the format: python3 gitceaser.py <key> <string>")
        sys.exit(1)
    
    key = int(sys.argv[1])
    note = sys.argv[2]
    
    print(cEncoder(key, note))
    sys.exit(0)