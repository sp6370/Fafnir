import sys

DATA_FILE_PATH = "data.txt" # assume file will always exist
RECORD_ITEM_SIZE = 8
RECORD_SIZE = 18

def encode_data(data_str, isKey):    
    return data_str.rjust(RECORD_ITEM_SIZE, " ") if isKey else data_str.rjust(RECORD_ITEM_SIZE, "0")

def decode_data(data_str, isKey):    
    return data_str.strip() if isKey else str(int(data_str))

def set(key, value):
    file = open(DATA_FILE_PATH, 'rb+') # add error handling later
    
    # read each line & try to find the key.
    line = file.readline()

    if len(line) == 0:
        print("KEY NOT FOUND: Empty file adding it!")
        file.write(f"{encode_data(key, True)}={encode_data(value, False)}\n".encode())
        file.flush()
        file.close()
        return

    while line:
        line_data = line.decode("utf-8")
        old_key, _ = line_data.split("=")
        old_key = decode_data(old_key, True)        
        if old_key == key:
            print("EXISTING KEY FOUND: OVERWRITING IT")
            file.seek(-RECORD_SIZE, 1)
            file.write(f"{encode_data(key, True)}={encode_data(value, False)}\n".encode())
            file.flush()
            file.close()            
            return
        else:
            line = file.readline()
        
    print("KEY NOT FOUND: ADDING IT")
    file.write(f"{encode_data(key, True)}={encode_data(value, False)}\n".encode())
    file.flush()
    file.close()

def get(key):
    file = open(DATA_FILE_PATH, 'r') # add error handling later
    line = file.readline()
    while line:
        file_key, key_val = line.split("=")
        file_key = decode_data(file_key, True)

        if file_key == key:
            print("KEY FOUND: HIT")
            key_val = decode_data(key_val, False)
            file.close()   
            return key_val

        line = file.readline()
    
    print("KEY NOT FOUND: MISS")
    file.close()
    return None


if __name__ == '__main__':
    # set("a", "1")
    # set("b", "2")
    # set("c", "3")
    # set("b", "100")
    # set("d", "200")
    # set("a", "123")
    # get("a")
    # get("z")

    if len(sys.argv) == 4:
        key = sys.argv[2]
        value = sys.argv[3]
        set(key, value)
    elif len(sys.argv) == 3:
        key = sys.argv[2]
        result = get(key)
        print(result)
    else:
        print("ERROR!!!")