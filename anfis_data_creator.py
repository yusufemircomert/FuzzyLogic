import pandas as pd
import numpy as np
import os

def prepare_anfis_data_strict(source_file='academicPerformanceData.xlsx'):
    print("⚙️ Preparing Large Dataset for ANFIS...")
    
    if not os.path.exists(source_file):
        print(f"❌ ERROR: '{source_file}' not found!")
        return

    # Read Excel
    try:
        df = pd.read_excel(source_file, header=1)
    except:
        df = pd.read_excel(source_file)

    # Cleaning
    df = df.dropna(axis=1, how='all')
    if len(df.columns) > 8:
        df = df.iloc[:, :8]
    
    df.columns = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'Remarks']
    
    # Target Cleaning
    df['Remarks'] = df['Remarks'].astype(str).str.replace('Class', '').str.strip()
    df = df[df['Remarks'].apply(lambda x: x.isdigit())]
    df['Remarks'] = df['Remarks'].astype(int)

    # --- PDF RULE: 10,000 samples per class (Total 50,000) ---
    # If a class has fewer than 10,000 samples, we will upsample (copy) to reach the count.
    
    def get_large_balanced_sample(dataframe, n_per_class, seed):
        return dataframe.groupby('Remarks', group_keys=False).apply(
            lambda x: x.sample(n=n_per_class, replace=True, random_state=seed) 
            if len(x) < n_per_class else x.sample(n=n_per_class, random_state=seed)
        )

    # Dataset for Iteration 1
    anfis_data_1 = get_large_balanced_sample(df, n_per_class=10000, seed=101)
    
    # Dataset for Iteration 2 (Different seed)
    anfis_data_2 = get_large_balanced_sample(df, n_per_class=10000, seed=202)

    # --- PDF RULE: 1/4 Test, 3/4 Train ---
    from sklearn.model_selection import train_test_split
    
    # Split Set 1
    X1 = anfis_data_1.drop('Remarks', axis=1)
    y1 = anfis_data_1['Remarks']
    X_train_1, X_test_1, y_train_1, y_test_1 = train_test_split(X1, y1, test_size=0.25, random_state=42)
    
    # Split Set 2
    X2 = anfis_data_2.drop('Remarks', axis=1)
    y2 = anfis_data_2['Remarks']
    X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X2, y2, test_size=0.25, random_state=42)

    # Save Files (as CSV)
    # Concatenate and save Train and Test so we can easily load them in the model code
    train_1 = pd.concat([X_train_1, y_train_1], axis=1)
    test_1 = pd.concat([X_test_1, y_test_1], axis=1)
    
    train_2 = pd.concat([X_train_2, y_train_2], axis=1)
    test_2 = pd.concat([X_test_2, y_test_2], axis=1)
    
    train_1.to_csv('anfis_train_1.csv', index=False)
    test_1.to_csv('anfis_test_1.csv', index=False)
    train_2.to_csv('anfis_train_2.csv', index=False)
    test_2.to_csv('anfis_test_2.csv', index=False)

    print(f"✅ Iteration 1: Train ({len(train_1)}), Test ({len(test_1)}) ready.")
    print(f"✅ Iteration 2: Train ({len(train_2)}), Test ({len(test_2)}) ready.")
    print("💾 Files saved.")


# Run the preparation function
if __name__ == "__main__":
    prepare_anfis_data_strict()    