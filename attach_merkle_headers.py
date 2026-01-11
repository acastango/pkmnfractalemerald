#!/usr/bin/env python3
# ============================================================================
# MERKLE =====================================================================
# hash: f7f49b70488cbaa1
# file: attach_merkle_headers.py
# updated: 2026-01-10
# END MERKLE =================================================================
# ============================================================================
"""
==============================================================================
MERKLE HEADER ATTACHMENT
==============================================================================
Attaches merkle hash headers to all tracked files for provenance.

- Markdown files: YAML frontmatter
- Python files: Header comment block
- Text files: Header comment

Run after any significant changes to update headers.
==============================================================================
"""

import os
import re
import hashlib
from datetime import datetime
from typing import Dict, Tuple

# Files to process
TRACKED_EXTENSIONS = {
    '.md': 'markdown',
    '.py': 'python', 
    '.txt': 'text'
}

# Files to skip (already have special handling or should not be modified)
SKIP_FILES = [
    'merkle_state.json',
    'requirements.txt',  # Keep minimal
]

# Directories to skip
SKIP_DIRS = ['__pycache__', '.git', 'oke_state', 'backups']


def compute_hash(content: bytes) -> str:
    """Compute SHA-256 hash, return first 16 chars."""
    return hashlib.sha256(content).hexdigest()[:16]


def compute_content_hash(filepath: str) -> str:
    """Compute hash of file content WITHOUT the header."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Strip existing header if present
    content = strip_existing_header(content, filepath)
    
    return compute_hash(content.encode('utf-8'))


def strip_existing_header(content: str, filepath: str) -> str:
    """Remove existing merkle header from content."""
    ext = os.path.splitext(filepath)[1].lower()
    
    if ext == '.md':
        # Remove YAML frontmatter
        if content.startswith('---'):
            end = content.find('---', 3)
            if end != -1:
                content = content[end+3:].lstrip('\n')
    
    elif ext == '.py':
        # Remove shebang if present
        if content.startswith('#!/'):
            newline = content.find('\n')
            if newline != -1:
                content = content[newline+1:]
        
        # Remove header comment block (between MERKLE markers)
        pattern = r'# ==+ MERKLE ==+\n.*?# ==+ END MERKLE ==+\n# ==+\n'
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        # Also try simpler pattern
        pattern2 = r'# =+\n# MERKLE =+\n.*?# END MERKLE =+\n# =+\n'
        content = re.sub(pattern2, '', content, flags=re.DOTALL)
        
        # Remove any duplicate shebangs that might be in the content
        content = content.lstrip('\n')
        if content.startswith('#!/'):
            newline = content.find('\n')
            if newline != -1:
                content = content[newline+1:].lstrip('\n')
    
    elif ext == '.txt':
        # Remove our specific header format only
        lines = content.split('\n')
        if len(lines) >= 3:
            if (lines[0].startswith('# MERKLE:') and 
                lines[1].startswith('# FILE:') and 
                lines[2].startswith('# UPDATED:')):
                # Remove header lines
                lines = lines[3:]
                # Remove blank line after header if present
                while lines and lines[0] == '':
                    lines.pop(0)
        content = '\n'.join(lines)
    
    return content


def get_file_dependencies(filepath: str, all_files: Dict[str, str]) -> Dict[str, str]:
    """Extract file dependencies (imports, references) and their hashes."""
    deps = {}
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    ext = os.path.splitext(filepath)[1].lower()
    basename = os.path.basename(filepath)
    
    if ext == '.py':
        # Find imports
        import_pattern = r'from (oke_\w+|claude_\w+) import|import (oke_\w+|claude_\w+)'
        for match in re.finditer(import_pattern, content):
            module = match.group(1) or match.group(2)
            module_file = module + '.py'
            if module_file in all_files and module_file != basename:
                deps[module_file] = all_files[module_file]
    
    # Find doc references in any file type
    doc_pattern = r'(docs_\w+\.md|MERKLE_LLM_PROTOCOL\.md|COLLECTIVE_QUERY_FLOW\.md|README\.md)'
    for match in re.finditer(doc_pattern, content):
        doc_file = match.group(1)
        if doc_file in all_files and doc_file != basename:
            deps[doc_file] = all_files[doc_file]
    
    return deps


def create_markdown_header(filepath: str, file_hash: str, deps: Dict[str, str]) -> str:
    """Create YAML frontmatter for markdown files."""
    basename = os.path.basename(filepath)
    now = datetime.now().isoformat()
    
    lines = [
        '---',
        f'merkle: {file_hash}',
        f'file: {basename}',
        f'updated: {now[:10]}',
    ]
    
    if deps:
        lines.append('references:')
        for dep_file, dep_hash in sorted(deps.items()):
            lines.append(f'  - file: {dep_file}')
            lines.append(f'    hash: {dep_hash}')
    
    lines.append('---')
    lines.append('')
    
    return '\n'.join(lines)


def create_python_header(filepath: str, file_hash: str, deps: Dict[str, str]) -> str:
    """Create header comment block for Python files."""
    basename = os.path.basename(filepath)
    now = datetime.now().isoformat()
    
    lines = [
        '#!/usr/bin/env python3',
        '# ============================================================================',
        '# MERKLE =====================================================================',
        f'# hash: {file_hash}',
        f'# file: {basename}',
        f'# updated: {now[:10]}',
    ]
    
    if deps:
        lines.append('# references:')
        for dep_file, dep_hash in sorted(deps.items()):
            lines.append(f'#   {dep_file} [{dep_hash}]')
    
    lines.append('# END MERKLE =================================================================')
    lines.append('# ============================================================================')
    lines.append('')
    
    return '\n'.join(lines)


def create_text_header(filepath: str, file_hash: str) -> str:
    """Create header comment for text files."""
    basename = os.path.basename(filepath)
    now = datetime.now().isoformat()
    
    lines = [
        f'# MERKLE: {file_hash}',
        f'# FILE: {basename}',
        f'# UPDATED: {now[:10]}',
        '',  # Blank line to separate from content
    ]
    
    return '\n'.join(lines)


def process_file(filepath: str, all_hashes: Dict[str, str]) -> Tuple[bool, str]:
    """Process a single file, add/update merkle header."""
    ext = os.path.splitext(filepath)[1].lower()
    basename = os.path.basename(filepath)
    
    if ext not in TRACKED_EXTENSIONS:
        return False, "skipped (extension)"
    
    if basename in SKIP_FILES:
        return False, "skipped (excluded)"
    
    # Read current content
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Strip existing header
    clean_content = strip_existing_header(content, filepath)
    
    # Compute hash of clean content
    file_hash = compute_hash(clean_content.encode('utf-8'))
    
    # Get dependencies
    deps = get_file_dependencies(filepath, all_hashes)
    
    # Create new header
    if ext == '.md':
        header = create_markdown_header(filepath, file_hash, deps)
    elif ext == '.py':
        header = create_python_header(filepath, file_hash, deps)
    elif ext == '.txt':
        header = create_text_header(filepath, file_hash)
    else:
        return False, "unknown type"
    
    # Combine header with clean content
    new_content = header + clean_content
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True, file_hash


def collect_all_files(root_dir: str) -> Dict[str, str]:
    """Collect all trackable files and their paths."""
    files = {}
    
    for entry in os.listdir(root_dir):
        if entry in SKIP_DIRS:
            continue
        
        filepath = os.path.join(root_dir, entry)
        
        if os.path.isfile(filepath):
            ext = os.path.splitext(entry)[1].lower()
            if ext in TRACKED_EXTENSIONS and entry not in SKIP_FILES:
                files[entry] = filepath
    
    return files


def main():
    import sys
    
    root_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    root_dir = os.path.abspath(root_dir)
    
    print("=" * 60)
    print("  MERKLE HEADER ATTACHMENT")
    print("=" * 60)
    print(f"  Directory: {root_dir}")
    print()
    
    # First pass: collect all files and compute preliminary hashes
    print("  Pass 1: Collecting files...")
    all_files = collect_all_files(root_dir)
    
    # Compute hashes for dependency resolution
    all_hashes = {}
    for basename, filepath in all_files.items():
        with open(filepath, 'rb') as f:
            content = f.read()
        all_hashes[basename] = compute_hash(content)
    
    print(f"  Found {len(all_files)} files to process")
    print()
    
    # Second pass: process each file
    print("  Pass 2: Attaching headers...")
    
    results = {'success': 0, 'skipped': 0, 'failed': 0}
    
    for basename, filepath in sorted(all_files.items()):
        success, result = process_file(filepath, all_hashes)
        
        if success:
            print(f"    [OK] {basename} -> {result}")
            results['success'] += 1
        else:
            print(f"    [--] {basename}: {result}")
            results['skipped'] += 1
    
    print()
    print("=" * 60)
    print(f"  Complete: {results['success']} updated, {results['skipped']} skipped")
    print("=" * 60)
    
    # Third pass: rebuild merkle tree
    print()
    print("  Rebuilding merkle state...")
    os.system(f'cd "{root_dir}" && python oke_merkle.py . > /dev/null 2>&1')
    print("  Done.")


if __name__ == "__main__":
    main()
