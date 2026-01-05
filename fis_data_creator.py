import pandas as pd
import numpy as np
import os

def create_fis_datasets(source_file='academicPerformanceData.xlsx'):
    print("⚙️ Creating Data Sets for FIS (20 samples per class)...")
    
    if not os.path.exists(source_file):
        print(f"❌ ERROR: '{source_file}' not found! Please upload the file to the main directory.")
        return

    # 1. Read Excel File
    try:
        # Header is sometimes on the 2nd row, trying header=1
        df = pd.read_excel(source_file, header=1)
    except:
        df = pd.read_excel(source_file)

    # 2. Cleaning Operations
    # Drop completely empty columns
    df = df.dropna(axis=1, how='all')
    
    # Keep first 8 columns (x1..x7 and Remarks)
    if len(df.columns) > 8:
        df = df.iloc[:, :8]
        
    # Standardize column names
    df.columns = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'Remarks']
    
    # Clean 'Remarks' column (e.g., 'Class 1' -> 1)
    df['Remarks'] = df['Remarks'].astype(str).str.replace('Class', '').str.strip()
    # Keep only numeric values
    df = df[df['Remarks'].apply(lambda x: x.isdigit())]
    df['Remarks'] = df['Remarks'].astype(int)

    # 3. Sampling Function (Stratified Sampling)
    def get_balanced_sample(dataframe, n_per_class, seed):
        # Take equal number of random samples from each class (1,2,3,4,5)
        return dataframe.groupby('Remarks', group_keys=False).apply(
            lambda x: x.sample(n=min(len(x), n_per_class), random_state=seed)
        )

    # 4. Create Two Different Datasets (PDF Requirement: 2 Iterations)
    # Set 1 (Seed=42)
    fis_subset_1 = get_balanced_sample(df, n_per_class=20, seed=42)
    
    # Set 2 (Seed=99 - Different randomness)
    fis_subset_2 = get_balanced_sample(df, n_per_class=20, seed=99)

    # 5. Save Files
    fis_subset_1.to_csv('fis_subset_1.csv', index=False)
    fis_subset_2.to_csv('fis_subset_2.csv', index=False)
    
    print(f"✅ Success! Files created:")
    print(f"   - fis_subset_1.csv ({len(fis_subset_1)} rows)")
    print(f"   - fis_subset_2.csv ({len(fis_subset_2)} rows)")


    # Run the function
if __name__ == "__main__":
    create_fis_datasets()