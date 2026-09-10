import os

def generate_statutes(base_dir):
    stat_dir = os.path.join(base_dir, 'legal_data', 'statutes')
    os.makedirs(stat_dir, exist_ok=True)
    
    with open(os.path.join(stat_dir, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write('# Legal Data Statutes Package\n')
        
    print("Statutes generator ready.")

if __name__ == '__main__':
    generate_statutes('.')
