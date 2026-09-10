# scripts/split_all_large_files.py
import os
import re

MAX_SIZE_BYTES = 250 * 1024  # 250 KB limit

def split_file(filepath):
    size = os.path.getsize(filepath)
    if size <= MAX_SIZE_BYTES:
        return
    
    dirname, filename = os.path.split(filepath)
    basename, ext = os.path.splitext(filename)
    if ext != '.py' or '_part' in basename:
        return
    
    print(f"Splitting {filename} ({size / 1024:.1f} KB)...")
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    # Find all list assignments: VAR_NAME = [
    # and preserve other lines (metadata dicts, imports, docstrings)
    var_ranges = []
    current_var = None
    var_start_line = None
    
    for idx, line in enumerate(lines):
        m = re.match(r'^([A-Z0-9_]+)\s*=\s*\[\s*$', line)
        if m:
            current_var = m.group(1)
            var_start_line = idx
        elif current_var and line.strip() == ']' or line.strip() == '];':
            var_ranges.append((current_var, var_start_line, idx))
            current_var = None
            var_start_line = None
            
    if not var_ranges:
        print(f"No list assignments found in {filename}, skipping.")
        return

    # Extract items inside each list assignment
    # Each item begins with '    {' and ends with '    },' or '    }'
    new_parts = []
    var_part_names = {}
    
    part_counter = 1
    for var_name, start_idx, end_idx in var_ranges:
        items = []
        current_item = []
        in_item = False
        
        for l in lines[start_idx+1:end_idx]:
            if l.startswith('    {'):
                in_item = True
                current_item = [l]
            elif in_item:
                current_item.append(l)
                if l.startswith('    }') or l.startswith('    },'):
                    items.append(''.join(current_item))
                    current_item = []
                    in_item = False
        if current_item:
            items.append(''.join(current_item))
            
        print(f"  Variable {var_name}: {len(items)} items found")
        
        # Chunk items into ~50 items per part (~120-180 KB)
        chunk_size = 50
        var_part_names[var_name] = []
        
        for i in range(0, len(items), chunk_size):
            chunk = items[i:i + chunk_size]
            part_filename = f"{basename}_part{part_counter:02d}.py"
            part_filepath = os.path.join(dirname, part_filename)
            part_var_name = f"{var_name}_PART_{part_counter:02d}"
            
            with open(part_filepath, 'w', encoding='utf-8') as pf:
                pf.write(f'\"\"\"\nPart {part_counter:02d} for {basename}\nModular codification slice under 250 KB\n\"\"\"\n\n{part_var_name} = [\n')
                for item in chunk:
                    if not item.endswith('\n'):
                        item += '\n'
                    if not item.rstrip().endswith(','):
                        # Ensure trailing comma
                        item = item.rstrip() + ',\n'
                    pf.write(item)
                pf.write(']\n')
                
            var_part_names[var_name].append((f"{basename}_part{part_counter:02d}", part_var_name))
            part_counter += 1

    # Rewrite the original file as an aggregator module
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f'\"\"\"\n{basename} - Aggregator Module\nPreserves backward compatibility while keeping all underlying files < 250 KB\n\"\"\"\n\n')
        
        # Write imports
        for var_name, parts in var_part_names.items():
            for pmod, pvar in parts:
                f.write(f"from .{pmod} import {pvar}\n")
            f.write("\n")
            
        # Write aggregations
        for var_name, parts in var_part_names.items():
            pvars = [pvar for _, pvar in parts]
            f.write(f"{var_name} = " + " + ".join(pvars) + "\n\n")

    new_size = os.path.getsize(filepath)
    print(f"  Rewrote {filename} -> {new_size / 1024:.1f} KB (created {part_counter - 1} parts)")

def main():
    target_dirs = [
        os.path.join(".", "legal_data", "statutes"),
        os.path.join(".", "legal_data", "precedents"),
        os.path.join(".", "legal_data", "pleadings"),
    ]
    for d in target_dirs:
        for f in sorted(os.listdir(d)):
            if f.endswith(".py") and not "_part" in f and f != "__init__.py":
                fp = os.path.join(d, f)
                split_file(fp)

if __name__ == "__main__":
    main()
