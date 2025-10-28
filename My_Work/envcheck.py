# ============================================
# 🧪 Python Codespace Notebook – Git/GitHub Environments
# Author: Dawn Triplett
# Environments: GitHub Codespaces / VS Code / Jupyter Notebooks
# Created: YYYY-MM-DD
# Purpose: Codespace for testing Python concepts and practicing code
# ============================================

# Run in bash terminal: python My_Work/envcheck.py

# --- 💻 Environment & System Setup ---
import os
import sys
import platform
import datetime

print("🟢 Environment Info (Git-GitHub)")
print(f"Date: {datetime.date.today()}")
print(f"Time: {datetime.datetime.now().strftime('%H:%M:%S')}")
print(f"Python version: {platform.python_version()}")
print(f"Executable: {sys.executable}")
print(f"Working directory: {os.getcwd()}")
print("===========================================\n")

# --- 📦 Core Python Libraries ---
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl  # <- add
import seaborn as sns
import random
from random import randint, choice
import scipy as sp  # <- add (top-level package)
import scipy.stats as stats
from importlib.metadata import version, PackageNotFoundError


def pkg_ver(name: str) -> str:
    try:
        return version(name)
    except PackageNotFoundError:
        return "unknown"


# --- ⚙️ Display & Visualization Settings ---
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({"figure.figsize": (7, 4), "figure.dpi": 100})
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 1000)

# --- 🧩 Version Checks & Reproducibility ---
random.seed(42)
np.random.seed(42)

print(f"NumPy version:      {np.__version__}")
print(f"Pandas version:     {pd.__version__}")
print(f"Matplotlib version: {mpl.__version__}")  # <- use mpl
print(f"Seaborn version:    {pkg_ver('seaborn')}")
print(f"SciPy version:      {sp.__version__}")  # <- optional but correct

print("\n🚀 Codespace environment initialized successfully.")
