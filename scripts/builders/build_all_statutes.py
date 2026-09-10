import os

def create_full_statutes():
    base_dir = "."
    stat_dir = os.path.join(base_dir, "legal_data", "statutes")
    os.makedirs(stat_dir, exist_ok=True)
    
    # 1. CPC
    from scripts.builders.build_statutes import write_cpc
    write_cpc(base_dir)
    print("Wrote CPC")

if __name__ == "__main__":
    create_full_statutes()
