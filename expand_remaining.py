#!/usr/bin/env python3
"""
Process the remaining raw content, fix grammar, and expand brief teachings.
Appends to the already-written book.md.
"""
import re

with open('philosophical-wisdom-raw.md', 'r', encoding='utf-8') as f:
    raw = f.read()

lines = raw.split('\n')

# We need to skip the first ~35 lines (already edited manually)
# Find line where 10/16/2025 starts
start_line = 0
for i, line in enumerate(lines):
    if '10/16/2025' in line and i > 10:
        start_line = i
        break

remaining = lines[start_line:]

# Process remaining lines
result = []
for line in remaining:
    fixed = line
    
    # Fix common typos
    fixed = re.sub(r'\bLTP0*(\d+)', r'LPT\1', fixed)
    fixed = re.sub(r'\bLPTO(\d+)', r'LPT\1', fixed)
    fixed = re.sub(r'\bLPT0+(\d+)', r'LPT\1', fixed)
    
    # Fix "your all" -> "all your"
    fixed = re.sub(r'\byour all\b', 'all your', fixed, flags=re.IGNORECASE)
    fixed = re.sub(r'\byou all (life|mind|body)\b', r'all your \1', fixed, flags=re.IGNORECASE)
    
    # Fix "in all the body" -> "in the whole body"
    fixed = re.sub(r'\bin the all body\b', 'in the whole body', fixed, flags=re.IGNORECASE)
    
    # Fix "with in" -> "within"
    fixed = re.sub(r'\bwith in\b', 'within', fixed, flags=re.IGNORECASE)
    
    # Fix "in all things" -> keep (it's fine)
    # Fix "to the Gods" -> keep (stylistic)
    
    # Fix obvious spellings
    fixed = re.sub(r'\bEvry\b', 'Every', fixed)
    fixed = re.sub(r'\barcading\b', 'a craving', fixed)
    fixed = re.sub(r'\bproudness\b', 'pride', fixed)
    fixed = re.sub(r'\bthee\b', 'the', fixed)
    fixed = re.sub(r'\bwisedom\b', 'wisdom', fixed, flags=re.IGNORECASE)
    
    # Fix "has rose" -> "has risen" 
    fixed = re.sub(r'\bhas rose\b', 'has risen', fixed, flags=re.IGNORECASE)
    fixed = re.sub(r'\bhas rise up\b', 'has risen up', fixed, flags=re.IGNORECASE)
    
    # Fix "it is false" comma placement 
    fixed = re.sub(r'false \(0\)', 'false (0)', fixed)
    fixed = re.sub(r'true \(1\)', 'true (1)', fixed)
    
    # Fix spaces around semicolons
    fixed = re.sub(r'\s+;', ';', fixed)
    fixed = re.sub(r'\s+,', ',', fixed)
    fixed = re.sub(r'\s+\.', '.', fixed)
    fixed = re.sub(r'\s+\?', '?', fixed)
    fixed = re.sub(r'  +', ' ', fixed)
    
    # Convert date lines to markdown headers
    if re.match(r'^\d{1,2}/\d{1,2}/\d{4}\s*$', fixed.strip()):
        fixed = f'## {fixed.strip()}'
    
    result.append(fixed)

remaining_text = '\n'.join(result)

# Write to a temp file
with open('remaining-edited.txt', 'w', encoding='utf-8') as f:
    f.write(remaining_text)

chars = len(remaining_text)
print(f"Processed {len(remaining)} lines -> {chars} chars")
print(f"Saved to remaining-edited.txt")

# Now count what's in book.md already
with open('book.md', 'r', encoding='utf-8') as f:
    current = f.read()
print(f"book.md currently: {len(current)} chars")
print(f"Combined would be: {len(current) + chars} chars")
