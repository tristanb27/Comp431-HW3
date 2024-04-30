import re
import os

def read_forward_file(file_path):
    sender = None
    rec = []
    msg = ""
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("From:"):
                sender = re.search(r'<(.*?)>', line).group(1)
            elif line.startswith("To:"):
                rec = re.search(r'<(.*?)>', line).group(1)
                rec.append(rec)
            else:
                msg += line
    
    return sender, rec, msg

# Function to emulate SMTP responses
def emulate_smtp_responses(file_path):
    sender, rec, _ = read_forward_file(file_path)
    
    if sender is None:
        print("Error: Sender not found in forward file.")
        return
    
    print(f"MAIL FROM:<{sender}>")
    print("250 OK")
    
    for recipient in rec:
        print(f"RCPT TO:<{rec}>")
        print("250 OK")

# Main function
def main():
    forward_dir = "forward/"
    forward_files = os.listdir(forward_dir)
    
    for file_name in forward_files:
        file_path = os.path.join(forward_dir, file_name)
        print(f"Processing file: {file_name}")
        emulate_smtp_responses(file_path)
        print()

if __name__ == "__main__":
    main()