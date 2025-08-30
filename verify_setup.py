#!/usr/bin/env python3
"""
Setup verification script for the Multilingual Language Learning Tool.
Run this script to verify that all dependencies are properly installed.
"""

import sys
import importlib

def check_package(package_name, import_name=None):
    """Check if a package is installed and can be imported."""
    if import_name is None:
        import_name = package_name

    try:
        importlib.import_module(import_name)
        print(f"✅ {package_name}: Successfully imported")
        return True
    except ImportError as e:
        print(f"❌ {package_name}: Import failed - {e}")
        return False
    except Exception as e:
        print(f"⚠️  {package_name}: Warning - {e}")
        return True

def main():
    """Main verification function."""
    print("🔍 Verifying Multilingual Language Learning Tool Setup")
    print("=" * 60)

    # Core packages
    packages = [
        ("pandas", "pandas"),
        ("numpy", "numpy"),
        ("matplotlib", "matplotlib"),
        ("seaborn", "seaborn"),
        ("nltk", "nltk"),
        ("scikit-learn", "sklearn"),
        ("datasets", "datasets"),
        ("sentence-transformers", "sentence_transformers"),
        ("bertopic", "bertopic"),
        ("pysrt", "pysrt"),
        ("torch", "torch"),
        ("ipywidgets", "ipywidgets"),
        ("umap-learn", "umap"),
        ("hdbscan", "hdbscan")
    ]

    print(f"Python version: {sys.version}")
    print("-" * 60)

    success_count = 0
    total_count = len(packages)

    for package_name, import_name in packages:
        if check_package(package_name, import_name):
            success_count += 1

    print("-" * 60)
    print(f"📊 Results: {success_count}/{total_count} packages successfully imported")

    if success_count == total_count:
        print("🎉 All packages are ready! You can now run the notebook.")
        print("\nNext steps:")
        print("1. Start Jupyter Notebook: jupyter notebook")
        print("2. Open: multilingual_language_learning_tool.ipynb")
        print("3. Run all cells to begin the analysis")
    else:
        print("⚠️  Some packages failed to import. Please check the installation.")
        missing_count = total_count - success_count
        print(f"Try reinstalling the missing {missing_count} package(s) with:")
        print("pip install -r requirements.txt")

    print("\n🔗 Project files:")
    print("- Main notebook: multilingual_language_learning_tool.ipynb")
    print("- Sample data: sample_subtitles.srt")
    print("- CEFR words: ENGLISH_CERF_WORDS.csv")
    print("- Documentation: README.md")

if __name__ == "__main__":
    main()
