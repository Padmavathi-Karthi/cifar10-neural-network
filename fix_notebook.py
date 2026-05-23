import nbformat

# Replace with your notebook filename
notebook_path = "Padma_CIFAR10.ipynb"

# Load notebook
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Remove problematic widget metadata
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

# Clear outputs from all cells
for cell in nb.cells:
    if cell.cell_type == "code":
        cell.outputs = []
        cell.execution_count = None

# Save cleaned notebook
with open(notebook_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("Notebook cleaned successfully!")