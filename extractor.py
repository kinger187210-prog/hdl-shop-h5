import re
import json
import os

def extract_products(text):
    products = []
    # Pattern to find product-like entries
    # Typically: Title followed by Price and Min. order
    # Example:
    # High Quality ABS Air Deflectors...
    # $14.50-16
    # Min. order: 1 set
    
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
            
        # Check if line looks like a title (relatively long, no price)
        if len(line) > 10 and '$' not in line and 'Min. order' not in line:
            # Look ahead for price and min order
            found_price = None
            found_moq = None
            for j in range(i + 1, min(i + 5, len(lines))):
                next_line = lines[j].strip()
                if not next_line: continue
                if '$' in next_line and not found_price:
                    found_price = next_line
                if 'Min. order:' in next_line and not found_moq:
                    found_moq = next_line
                if found_price and found_moq:
                    products.append({
                        "name": line,
                        "price": found_price,
                        "moq": found_moq
                    })
                    break
    return products

# I'll manually paste or read the content if I could, but I'll use the data I just saw.
# Since I can't "read" the tool output directly into Python without writing it to a file first or having it in my context.
# I will use the tool output I received in the previous turn.

# I'll create a list of results based on what I saw in the tool outputs.
# Wait, I have the full tool output in my context. I can process it.

# I'll write a script that takes a file with the content and extracts.
# I'll save the content to a temporary file first.
