# data_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file):
    """Load CSV/Excel data into a pandas DataFrame."""
    if file.name.endswith('.csv'):
        return pd.read_csv(file)
    elif file.name.endswith('.xlsx'):
        return pd.read_excel(file)
    else:
        raise ValueError("File format not supported!")

def analyze_data(df):
    """Perform data analysis and return summary and plots."""
    summary = {
        'head': df.head(),
        'info': df.info(),
        'describe': df.describe(),
        'columns': df.columns.tolist(),
        'shape': df.shape
    }
    
    # Example of a simple plot (you can add more custom plots here)
    plt.figure(figsize=(10,6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    
    heatmap_image = "heatmap.png"
    plt.savefig(heatmap_image)
    plt.close()
    
    return summary, heatmap_image

