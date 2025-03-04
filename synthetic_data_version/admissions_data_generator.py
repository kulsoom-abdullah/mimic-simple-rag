# admissions_data_generator.py
import pandas as pd
import random
from datetime import datetime, timedelta

# Generate synthetic admission data
def generate_synthetic_admissions(num_records=20):
    data = []
    for i in range(num_records):
        subject_id = random.randint(1000, 9999)
        hadm_id = random.randint(100000, 999999)
        admittime = datetime.now() - timedelta(days=random.randint(1, 365))
        data.append({
            "subject_id": subject_id,
            "hadm_id": hadm_id,
            "admittime": admittime.strftime("%Y-%m-%d %H:%M:%S")
        })
    return pd.DataFrame(data)

# Save to CSV
if __name__ == "__main__":
    synthetic_data = generate_synthetic_admissions()
    synthetic_data.to_csv("synthetic_admissions.csv", index=False)
    print("Synthetic admissions data saved to synthetic_admissions.csv")