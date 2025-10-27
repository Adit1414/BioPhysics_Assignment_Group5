import matplotlib.pyplot as plt
import numpy as np
import sys

# --- Settings ---
PROFILE_FILES = {
    'Best WT Model': 'dope_shope_P11413.profile',
    'Template 1': 'dope_shope_6E07.profile',
    'Template 2': 'dope_shope_6E08.profile',
    'Template 3': 'dope_shope_7SNF.profile',
    'Template 4': 'dope_shope_7SNI.profile'
}

OUTPUT_IMAGE_FILE = 'dope_profile_WT.png'
# -----------------

plt.figure(figsize=(10, 6))

# Load and plot each profile
for label, filepath in PROFILE_FILES.items():
    try:
        # Load the data, skipping comment lines AND only using the first two columns
        data = np.loadtxt(filepath, comments='#', usecols=(1,3))
        
        # Get residue number (column 0) and DOPE score (column 1)
        residues = data[:, 0]
        scores = data[:, 1]
        
        # Make the 'Best WT Model' line bold and black
        if label == 'Best WT Model':
            plt.plot(residues, scores, label=label, color='black', linewidth=2.5)
        else:
            # Plot templates with dashed lines
            plt.plot(residues, scores, label=label, linestyle='--')

    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        print("Please make sure the file exists and is not empty.")
        sys.exit(1)

# --- Format the plot ---
plt.title('DOPE Score Profile: Templates vs Best WT Model', fontsize=16)
plt.xlabel('Residue Number', fontsize=12)
plt.ylabel('DOPE Score', fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle=':', alpha=0.7)

# Set a typical DOPE score range for the y-axis
# You may need to adjust this based on your results
plt.ylim(-0.9, -0.2) 

# Save the final plot
plt.savefig(OUTPUT_IMAGE_FILE)
print(f"Plot saved as {OUTPUT_IMAGE_FILE}")
plt.show()