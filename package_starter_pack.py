"""
PoseLab Starter Pack Packaging Script
Creates the final ZIP structure for Gumroad distribution
"""

import os
import shutil
import sys
from pathlib import Path

# Fix Windows console encoding for emojis
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Configuration
DRIVE_BASE = Path(r"G:\My Drive\ColabNotebooks\BiomechanicsAnalysis\___WORKOUTS\data\processed")
REPO_BASE = Path(r"C:\Users\jrkag\Personal_Projects\2D-video-based-exercise-classification-main")
OUTPUT_BASE = Path(r"C:\Users\jrkag\Personal_Projects\PoseLab_Starter_Pack_v1")

# Exercise name mapping: Google Drive folder → Standardized name
EXERCISE_MAPPING = {
    "Burpees": "burpees",
    "burpees": "burpees",
    "Jumping Jacks": "jumping_jacks",
    "jumping_jacks": "jumping_jacks",
    "Mountain Climbers": "mountain_climbers",
    "mountain_climbers": "mountain_climbers",
    "Pushups": "pushups",
    "pushups": "pushups",
    "Squats": "squats",
    "squats": "squats",
}

def create_starter_pack():
    """Create the PoseLab Starter Pack structure"""
    
    print("🚀 Creating PoseLab Starter Pack v1...\n")
    
    # Step 1: Create output directory
    if OUTPUT_BASE.exists():
        print(f"⚠️  {OUTPUT_BASE} already exists. Removing...")
        shutil.rmtree(OUTPUT_BASE)
    
    OUTPUT_BASE.mkdir(parents=True)
    print(f"✅ Created: {OUTPUT_BASE}\n")
    
    # Step 2: Copy code and docs
    print("📋 Copying code and documentation...")
    
    # Copy PoseLab_Demo.ipynb
    demo_source = REPO_BASE / "PoseLab_Demo.ipynb"
    if demo_source.exists():
        shutil.copy2(demo_source, OUTPUT_BASE / "PoseLab_Demo.ipynb")
        print("  ✅ Copied PoseLab_Demo.ipynb")
    
    # Copy _archive folder (docs + legacy pipeline)
    archive_source = REPO_BASE / "_archive"
    if archive_source.exists():
        # Copy entire _archive as legacy_xgb_pipeline structure
        target_archive = OUTPUT_BASE / "legacy_xgb_pipeline"
        shutil.copytree(archive_source / "legacy_xgb_pipeline", target_archive)
        print("  ✅ Copied legacy_xgb_pipeline/")
        
        # Copy docs to root
        if (archive_source / "00_README_GET_STARTED.md").exists():
            shutil.copy2(
                archive_source / "00_README_GET_STARTED.md",
                OUTPUT_BASE / "00_README_GET_STARTED.md"
            )
            print("  ✅ Copied 00_README_GET_STARTED.md")
        
        if (archive_source / "LICENSE.txt").exists():
            shutil.copy2(
                archive_source / "LICENSE.txt",
                OUTPUT_BASE / "LICENSE.txt"
            )
            print("  ✅ Copied LICENSE.txt")
    
    # Copy models
    models_source = REPO_BASE / "models"
    if models_source.exists():
        target_models = OUTPUT_BASE / "models"
        shutil.copytree(models_source, target_models)
        print("  ✅ Copied models/")
    
    print()
    
    # Step 3: Process data files
    print("📊 Processing data files...")
    
    data_dir = OUTPUT_BASE / "data"
    data_dir.mkdir(exist_ok=True)
    
    if not DRIVE_BASE.exists():
        print(f"⚠️  WARNING: Drive path not found: {DRIVE_BASE}")
        print("   Skipping data processing. You'll need to manually add data.")
        return OUTPUT_BASE
    
    # Process each exercise
    processed_count = 0
    # Get unique standard names and map to all possible drive folder names
    standard_exercises = {"burpees", "jumping_jacks", "mountain_climbers", "pushups", "squats"}
    
    for standard_name in sorted(standard_exercises):
        # Find matching drive folder name (use the version that exists on drive)
        drive_folder_name = None
        for drive_name, std_name in EXERCISE_MAPPING.items():
            if std_name == standard_name:
                # Check both capitalized and lowercase versions
                test_path = DRIVE_BASE / drive_name
                if test_path.exists():
                    drive_folder_name = drive_name
                    break
        
        source_dir = DRIVE_BASE / drive_folder_name
        target_dir = data_dir / standard_name
        
        if not source_dir.exists():
            print(f"  ⚠️  Missing: {drive_folder_name}")
            continue
        
        target_dir.mkdir(exist_ok=True)
        print(f"  📁 Processing {drive_folder_name} → {standard_name}")
        
        # Process each sample folder
        sample_count = 0
        for sample_folder in sorted(source_dir.iterdir()):
            if not sample_folder.is_dir():
                continue
            
            # Handle folder names like "burpees_01" (with underscores) or "Jumping Jacks 01" (with spaces)
            folder_name = sample_folder.name.lower()
            
            # Check if it contains the exercise name and a number
            exercise_match = None
            for ex_name in EXERCISE_MAPPING.values():
                if folder_name.startswith(ex_name):
                    exercise_match = ex_name
                    break
            
            if exercise_match:
                # Extract the number part (e.g., "burpees_01" → "01")
                remaining = folder_name[len(exercise_match):]
                if remaining.startswith('_') or remaining.startswith(' '):
                    num = remaining[1:].strip()
                else:
                    num = remaining.strip()
                
                # Construct base filename
                base_filename = f"{exercise_match}_{num}"
                
                # Copy the two essential CSV files
                files_copied = 0
                for pattern in ["*_data_processed.csv", "*_joint_angles.csv"]:
                    for file in sample_folder.glob(pattern):
                        # Create new filename
                        suffix = "_data_processed.csv" if "data_processed" in file.name else "_joint_angles.csv"
                        new_filename = f"{base_filename}{suffix}"
                        target_file = target_dir / new_filename
                        
                        shutil.copy2(file, target_file)
                        files_copied += 1
                
                if files_copied > 0:
                    sample_count += 1
                    processed_count += 2
            else:
                print(f"    ⚠️  Unexpected folder name format: {sample_folder.name}")
        
        print(f"    ✅ Copied {sample_count} samples ({sample_count * 2} files)")
    
    print(f"\n✅ Total files processed: {processed_count}")
    print()
    
    # Step 4: Final summary
    print("=" * 60)
    print("✅ PoseLab Starter Pack v1 created successfully!")
    print("=" * 60)
    print(f"\n📦 Location: {OUTPUT_BASE}")
    
    # Print structure
    print("\n📂 Structure:")
    for item in sorted(OUTPUT_BASE.rglob("*")):
        if item.is_file():
            depth = len(item.relative_to(OUTPUT_BASE).parts) - 1
            indent = "  " * depth
            print(f"{indent}📄 {item.name}")
        elif item.is_dir() and item != OUTPUT_BASE:
            depth = len(item.relative_to(OUTPUT_BASE).parts) - 1
            indent = "  " * depth
            print(f"{indent}📁 {item.name}/")
    
    print("\n🎯 Next steps:")
    print("  1. Review the files in the output directory")
    print("  2. Create ZIP file: Right-click folder → 'Send to' → 'Compressed folder'")
    print("  3. Upload to Gumroad")
    
    return OUTPUT_BASE

if __name__ == "__main__":
    try:
        output = create_starter_pack()
        print("\n🎉 All done! Ready for packaging.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

