# ===== CREATE REQUIRED FOLDERS =====

import os

folders = ['data', 'models', 'outputs', 'reports']

for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"✅ Created '{folder}' folder")
    else:
        print(f"✓ '{folder}' folder already exists")

print("\n✅ All required folders ready!")
print("\nFolder structure:")
for folder in folders:
    print(f"  📁 {folder}/")