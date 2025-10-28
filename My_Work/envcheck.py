# ============================================
# 🧪 Environment Checker – GitHub Codespaces / VS Code / Jupyter
# Author: Dawn Triplett
# Purpose: Unified setup for Python data analysis and visualization
# ============================================

# --- 💻 System Setup ---
import os
import sys
import platform
import datetime
import random

# Try to detect if running inside a Jupyter notebook
try:
    from IPython.display import Markdown, display

    IN_JUPYTER = True
except ImportError:
    IN_JUPYTER = False


def show_header():
    """Display system info in Markdown if in Jupyter, else as plain text."""
    date = datetime.date.today()
    time = datetime.datetime.now().strftime("%H:%M:%S")
    pyver = platform.python_version()
    exe = sys.executable
    cwd = os.getcwd()

    if IN_JUPYTER:
        display(
            Markdown(
                f"""
### 🟢 Environment Info
| Key | Value |
|:----|:------|
| **Date** | {date} |
| **Time** | {time} |
| **Python version** | {pyver} |
| **Executable** | `{exe}` |
| **Working directory** | `{cwd}` |
"""
            )
        )
    else:
        print("🟢 Environment Info")
        print(f"Date: {date}")
        print(f"Time: {time}")
        print(f"Python version: {pyver}")
        print(f"Executable: {exe}")
        print(f"Working directory: {cwd}")
        print("=" * 45)


# --- 📦 Core Libraries ---
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# --- ⚙️ Visualization & Display Settings ---
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({"figure.figsize": (7, 4), "figure.dpi": 100})
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 1000)

# --- 🧩 Reproducibility ---
random.seed(42)
np.random.seed(42)


def show_versions():
    """Show library versions in Markdown if Jupyter, else plain text."""
    versions = {
        "NumPy": np.__version__,
        "Pandas": pd.__version__,
        "Matplotlib": plt.matplotlib.__version__,
        "Seaborn": sns.__version__,
        "SciPy": stats.__version__,
    }

    if IN_JUPYTER:
        rows = "\n".join([f"| **{lib}** | {ver} |" for lib, ver in versions.items()])
        display(
            Markdown(
                f"""
### ✅ Core Libraries Loaded
| Library | Version |
|:---------|:--------:|
{rows}

🚀 **Codespace environment initialized successfully.**
"""
            )
        )
    else:
        print("✅ Core Libraries Loaded")
        for lib, ver in versions.items():
            print(f"{lib:<12}: {ver}")
        print("\n🚀 Codespace environment initialized successfully.\n")


def test():
    """
    Run a tiny end-to-end check:
      • Create a small DataFrame
      • Compute a simple statistic
      • Plot a quick histogram
    Returns: dict of computed values for quick assertions if needed.
    """
    # 1) tiny DataFrame
    df = pd.DataFrame(
        {"x": np.random.randn(200), "group": np.random.choice(list("ABC"), 200)}
    )
    mean_x = df["x"].mean()
    std_x = df["x"].std(ddof=1)
    n = len(df)

    # 2) simple stat (SciPy zscore on first 5 values just to touch SciPy)
    z = stats.zscore(df["x"].head(5).to_numpy())

    # 3) quick plot (kept lightweight)
    ax = sns.histplot(df["x"], bins=20, kde=True)
    ax.set_title("envcheck: quick histogram")
    ax.set_xlabel("x")
    ax.set_ylabel("count")
    # In Jupyter, the figure will display automatically; in terminals, explicitly show:
    try:
        plt.show()
    finally:
        plt.close()  # avoid stacking figures in notebooks

    # Pretty print results
    summary = {
        "n_rows": n,
        "mean_x": float(mean_x),
        "std_x": float(std_x),
        "z_first5": [float(v) for v in z],
    }

    if IN_JUPYTER:
        rows = "\n".join(
            [
                f"| **n_rows** | {summary['n_rows']} |",
                f"| **mean_x** | {summary['mean_x']:.4f} |",
                f"| **std_x** | {summary['std_x']:.4f} |",
                f"| **z_first5** | `{summary['z_first5']}` |",
            ]
        )
        display(
            Markdown(
                f"""
### 🔎 envcheck.test() Results
| Metric | Value |
|:-------|:------|
{rows}
"""
            )
        )
    else:
        print("🔎 envcheck.test() Results")
        print(f"n_rows   : {summary['n_rows']}")
        print(f"mean_x   : {summary['mean_x']:.4f}")
        print(f"std_x    : {summary['std_x']:.4f}")
        print(f"z_first5 : {summary['z_first5']}\n")

    return summary


# --- 🚀 Run Checks on Import ---
show_header()
show_versions()
