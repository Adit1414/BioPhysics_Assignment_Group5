from modeller import *
from modeller.scripts import complete_pdb
import sys

# --- Settings ---
# This list maps the PDB file to the desired output profile file.
# Make sure your PDB files (e.g., '6E07.pdb') exist in this directory!
PDB_FILES_TO_PROCESS = {
    '6E07.pdb': 'dope_shope_6E07.profile',
    '6E08.pdb': 'dope_shope_6E08.profile',
    '7SNF.pdb': 'dope_shope_7SNF.profile',
    '7SNI.pdb': 'dope_shope_7SNI.profile',
    'P11413.pdb': 'dope_shope_P11413.profile'
}
# ----------------

log.verbose()
env = Environ()

env.libs.topology.read(file='$(LIB)/top_heav.lib')
env.libs.parameters.read(file='$(LIB)/par.lib')

print("--- Starting DOPE Profile Generation ---")
successful_files = 0

# Loop over every file in our settings
for pdb_file, profile_file in PDB_FILES_TO_PROCESS.items():
    try:
        print(f"Processing: {pdb_file} -> {profile_file}")

        # Read the PDB file
        mdl = complete_pdb(env, pdb_file)

        # Select all atoms in the model
        s = Selection(mdl)

        # Calculate the DOPE energy profile (per-residue)
        s.assess_dope(output='ENERGY_PROFILE', 
                      file=profile_file,
                      normalize_profile=True, 
                      smoothing_window=15)

        print(f"SUCCESS: Generated {profile_file}")
        successful_files += 1

    except Exception as e:
        print(f"!!! ERROR processing {pdb_file}: {e}")
        print(f"!!! Skipping this file. {profile_file} will be empty or incomplete.")

print("\n--- Generation Complete ---")
print(f"{successful_files} out of {len(PDB_FILES_TO_PROCESS)} files generated successfully.")

if successful_files < len(PDB_FILES_TO_PROCESS):
    print("WARNING: Some files failed. Your Gnuplot script will still show errors.")
    sys.exit(1)
else:
    print("All files generated. You can now run your Gnuplot script.")
    
    