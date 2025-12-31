#!/usr/bin/env python3
"""Convert BibTeX file to JSON for Hugo."""

import json
import re
from pathlib import Path

def parse_bibtex(content):
    """Parse BibTeX content into a list of entries."""
    entries = []

    # Match each BibTeX entry
    pattern = r'@(\w+)\{([^,]+),\s*(.*?)\n\}'
    matches = re.findall(pattern, content, re.DOTALL)

    for entry_type, key, fields_str in matches:
        entry = {
            'type': entry_type.lower(),
            'key': key.strip(),
        }

        # Parse fields
        field_pattern = r'(\w+)\s*=\s*\{([^}]*)\}'
        fields = re.findall(field_pattern, fields_str)

        for field_name, field_value in fields:
            field_name = field_name.lower()
            field_value = field_value.strip()

            # Clean up author field
            if field_name == 'author':
                field_value = field_value.replace(' and ', ', ')

            entry[field_name] = field_value

        # Create venue from booktitle or journal
        if 'booktitle' in entry:
            entry['venue'] = entry['booktitle']
        elif 'journal' in entry:
            entry['venue'] = entry['journal']

        entries.append(entry)

    # Sort by year (descending)
    entries.sort(key=lambda x: int(x.get('year', 0)), reverse=True)

    return entries

def main():
    script_dir = Path(__file__).parent
    project_dir = script_dir.parent

    bib_path = project_dir / 'data' / 'publications.bib'
    json_path = project_dir / 'data' / 'publications.json'

    if not bib_path.exists():
        print(f"Error: {bib_path} not found")
        return

    content = bib_path.read_text()
    entries = parse_bibtex(content)

    json_path.write_text(json.dumps(entries, indent=2))
    print(f"Converted {len(entries)} entries to {json_path}")

if __name__ == '__main__':
    main()
