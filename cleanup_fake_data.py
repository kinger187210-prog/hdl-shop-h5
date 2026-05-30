import json
import re

def is_fake_image(url):
    if not url:
        return True
    
    # Extract the potential hash part
    # Pattern: https://s.alicdn.com/@sc04/kf/H123456789.jpg...
    match = re.search(r'/kf/([^./]+)', url)
    if not match:
        return False
    
    filename = match.group(1)
    
    # Check for sequential digits
    if any(s in filename for s in ["012345", "123456", "234567", "345678", "456789", "567890"]):
        return True
    if any(s in filename for s in ["987654", "876543", "765432", "654321", "543210"]):
        return True
    
    # Check for repeated digits (4 or more)
    if re.search(r'(\d)\1{4,}', filename):
        return True
        
    return False

def cleanup():
    input_file = 'dist/hdl_inventory.json'
    output_file = 'dist/hdl_inventory.json'
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    original_count = len(data)
    cleaned_data = [p for p in data if not is_fake_image(p.get('sPicUrl', ''))]
    final_count = len(cleaned_data)
    
    removed_count = original_count - final_count
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=2)
    
    print(f"Original Count: {original_count}")
    print(f"Removed (Fake): {removed_count}")
    print(f"Final Count: {final_count}")

if __name__ == "__main__":
    cleanup()
