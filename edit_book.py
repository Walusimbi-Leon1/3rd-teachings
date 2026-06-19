#!/usr/bin/env python3
"""
Edit and expand the Philosophical Wisdom raw text into 3rd Teachings book.md.
Handles grammar fixes, punctuation, and minor expansions while preserving Leon's unique voice.
"""

import re

with open('philosophical-wisdom-raw.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Title and header
text = text.replace(
    'Philosophical Wisdom by Leon (SGSS)',
    '# 3rd Teachings: Philosophical Wisdom\n\n**By Leon (SGSS)**'
)

# 2. Fix common grammar issues

# Fix "a human" -> consistency (keep "a human")
# Fix "your all" -> "all your"
text = re.sub(r'\byour all\b', 'all your', text, flags=re.IGNORECASE)
text = re.sub(r'\byou all life\b', 'all your life', text, flags=re.IGNORECASE)

# Fix "its" vs "it's" (context-dependent, do basic fixes)
text = re.sub(r"\bit's ashaming\b", "it's a shame", text, flags=re.IGNORECASE)

# Fix "the Gods" consistency - already mostly consistent
# Fix "to the Gods" -> keep as is (it's a stylistic choice)

# Fix obvious spelling errors
spelling_fixes = {
    'ashaming': 'a shame',
    'behavour': 'behavior',
    'behaviours': 'behaviors',
    'brillant': 'brilliant',
    'brillance': 'brilliance',
    'brillantness': 'brilliance',
    'wisedom': 'wisdom',
    'dissapointed': 'disappointed',
    'disapointed': 'disappointed',
    'occured': 'occurred',
    'ocurred': 'occurred',
    'recieve': 'receive',
    'recieved': 'received',
    'beleive': 'believe',
    'beleif': 'belief',
    'beleifs': 'beliefs',
    'wich': 'which',
    'definately': 'definitely',
    'defenetly': 'definitely',
    'heven': 'heaven',
    'hevens': 'heavens',
    'untill': 'until',
    'untill': 'until',
    'tommorow': 'tomorrow',
    'tommorrow': 'tomorrow',
    'priviledge': 'privilege',
    'priviledges': 'privileges',
    'judgement': 'judgment',
    'judgements': 'judgments',
    'resurection': 'resurrection',
    'enourmous': 'enormous',
    'embarass': 'embarrass',
    'embarassed': 'embarrassed',
    'pysically': 'physically',
    'phillosopher': 'philosopher',
    'phillosophy': 'philosophy',
    'phillosophical': 'philosophical',
    'phillosophers': 'philosophers',
}

for wrong, correct in spelling_fixes.items():
    text = re.sub(r'\b' + re.escape(wrong) + r'\b', correct, text, flags=re.IGNORECASE)

# 3. Fix punctuation - spaces before semicolons
text = re.sub(r'\s+;', ';', text)
# Fix spaces before commas
text = re.sub(r'\s+,', ',', text)
# Fix double spaces
text = re.sub(r'  +', ' ', text)
# Fix spaces before periods
text = re.sub(r'\s+\.', '.', text)
# Ensure period at end of sentences that end with letters
text = re.sub(r'([a-zA-Z])\n([A-Z])', r'\1.\n\2', text)

# 4. Fix "LTP" -> "LPT" (there are some LTP03 etc that should be LPT)
text = re.sub(r'\bLTP0(\d+)', r'LPT0\1', text)
text = re.sub(r'\bLTP(\d+)', r'LPT\1', text)

# 5. Fix "LPTO" -> "LPT" 
text = re.sub(r'\bLPTO(\d+)', r'LPT\1', text)

# 6. Clean up reference codes - ensure consistent format
# (TsX) LPTXXX should have a space
text = re.sub(r'(\([A-Za-z0-9+]+\s*\))([A-Za-z])', r'\1 \2', text)

# 7. Date format consistency (ensure dates are h2 headers)
text = re.sub(r'^(\d{1,2}/\d{1,2}/\d{4})$', r'## \1', text, flags=re.MULTILINE)

with open('book.md', 'w', encoding='utf-8') as f:
    f.write(text)

chars = len(text)
print(f"✅ Written to book.md: {chars} chars")
print(f"📈 Change from original: {chars - 162541} chars ({((chars/162541)-1)*100:.1f}%)")
