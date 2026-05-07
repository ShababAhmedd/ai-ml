import nbformat

# === CONFIG ===
SOURCE_FILE = "python.ipynb"      # your notebook
TARGET_FILE = "numpy.ipynb"   # output file
SECTION_NAME = "# ndarray"           # section you want to extract
# ==============

nb = nbformat.read(SOURCE_FILE, as_version=4)

new_nb = nbformat.v4.new_notebook()
collect = False

for cell in nb.cells:
    # Detect section headers in markdown cells
    if cell.cell_type == "markdown" and cell.source.strip().lower().startswith("# "):
        if cell.source.strip().lower() == SECTION_NAME.lower():
            collect = True
        else:
            collect = False
    
    if collect:
        new_nb.cells.append(cell)

# Save the output file
nbformat.write(new_nb, TARGET_FILE)
print("Created:", TARGET_FILE)
