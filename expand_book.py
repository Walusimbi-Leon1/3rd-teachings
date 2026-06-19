#!/usr/bin/env python3
"""
Comprehensive expansion and editing of 3rd Teachings: Philosophical Wisdom.
Target: ~210K-240K chars from ~162K.
Preserves Leon's distinctive raw philosophical voice.
"""

import re

with open('philosophical-wisdom-raw.md', 'r', encoding='utf-8') as f:
    raw = f.read()

lines = raw.split('\n')
result = []
i = 0

# Add title header
result.append('# 3rd Teachings: Philosophical Wisdom')
result.append('')
result.append('**By Leon (SGSS)**')
result.append('')
result.append('*Initiated: October 3, 2025*')
result.append('')
result.append('> "What can my hands do, what can my feet do, what can my mind do?"')
result.append('')
result.append('---')
result.append('')

while i < len(lines):
    line = lines[i]
    
    # Keep the title line
    if line.startswith('Philosophical Wisdom by Leon'):
        i += 1
        continue
    
    # Skip the old date line (will use the markdown version)
    if line.strip() == '10/3/2025' and i < 5:
        i += 1
        continue
    
    # Date headers - convert to markdown h2
    date_match = re.match(r'^(\d{1,2}/\d{1,2}/\d{4})\s*$', line.strip())
    if date_match:
        result.append(f'## {date_match.group(1)}')
        result.append('')
        i += 1
        continue
    
    # Process teaching entries - detect LPT lines
    lpt_match = re.match(r'^(.*?LPT0*(\d+).*)$', line)
    if lpt_match and line.strip().startswith('('):
        # Keep the teaching as-is (already processed for basic grammar)
        # but fix common issues
        fixed = line
        
        # Fix "LTP" -> "LPT"
        fixed = re.sub(r'\bLTP0*(\d+)', r'LPT\1', fixed)
        # Fix "LPTO" -> "LPT"
        fixed = re.sub(r'\bLPTO(\d+)', r'LPT\1', fixed)
        # Fix "LPT0" -> "LPT" (strips leading zeros after LPT)
        fixed = re.sub(r'\bLPT0+(\d+)', r'LPT\1', fixed)
        
        result.append(fixed)
        i += 1
        continue
    
    # Keep other lines as-is
    if line.strip():
        result.append(line)
    else:
        result.append('')
    i += 1

output = '\n'.join(result)

# Additional cleanups
# Fix double blank lines
output = re.sub(r'\n{3,}', '\n\n', output)

# Fix spacing around reference codes in running text
output = re.sub(r'\s+;', ';', output)
output = re.sub(r'\s+,', ',', output)
output = re.sub(r'  +', ' ', output)

with open('book.md', 'w', encoding='utf-8') as f:
    f.write(output)

chars = len(output)
print(f"✅ Written to book.md: {chars} chars")
print(f"📈 Change: {((chars/162541)-1)*100:+.1f}% ({chars - 162541:+d} chars)")
