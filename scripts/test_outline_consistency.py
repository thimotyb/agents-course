import os
import sys
from bs4 import BeautifulSoup

def verify_chapter_outline(file_path):
    print(f"Checking {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    main_content = soup.find(class_='module-main')
    if not main_content:
        print(f"Error: .module-main not found in {file_path}")
        return False

    headings = main_content.find_all(['h2', 'h3'])
    
    # Simulate JS logic
    outline_tree = {}
    current_h2 = None
    
    errors = []
    
    for h in headings:
        text = h.get_text().strip()
        if h.name == 'h2':
            current_h2 = text
            outline_tree[current_h2] = []
        elif h.name == 'h3':
            if current_h2 is None:
                errors.append(f"Orphan h3 found: '{text}' (no h2 before it)")
            else:
                outline_tree[current_h2].append(text)
    
    # Specific check for Module 1 Section 2 based on user report
    if "chapter-01.html" in file_path:
        section_2 = "2. Introducing LangChain"
        if section_2 in outline_tree:
            subsections = outline_tree[section_2]
            expected = ["2.1 The Need for a Framework", "2.2 LangChain Architecture", "2.3 Core Object Model"]
            for exp in expected:
                if exp not in subsections:
                    errors.append(f"Missing subsection in outline for '{section_2}': '{exp}'")
        else:
            errors.append(f"Main section '{section_2}' not found in h2 headings")

    if errors:
        for err in errors:
            print(f"FAILED: {err}")
        return False
    
    print(f"SUCCESS: Outline structure for {file_path} is consistent.")
    return True

if __name__ == "__main__":
    target_files = [f"site/chapters/chapter-{i:02d}.html" for i in range(1, 8)]
    all_ok = True
    for f in target_files:
        if os.path.exists(f):
            if not verify_chapter_outline(f):
                all_ok = False
    
    if not all_ok:
        sys.exit(1)
    sys.exit(0)
