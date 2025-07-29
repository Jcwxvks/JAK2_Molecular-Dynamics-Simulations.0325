# Molecular dynamic simulations of the three pocket sites of Tyrosine-protein kinase JAK2

This repository includes a pdb file codenamed 3UGC, a program to process and build the system from scratch using Openmm to simulate the movement of protein molecules, and a script to generate animations in PyMol.

## Project Overview

Molecular dynamics simulations are tremendously helpful in understanding the dynamic deformation of protein-specific pockets. The aim of this project is to explore the feasibility of Openmm-based simulations of the three pockets of JAK2 to probe their changes in affinity for ligands.

## Repository Contents

- **`Molecular dynamics.ipynb`**  
  A Jupyter notebook that performs the complete downstream analysis:
  - Repair of imported PDB files
      - replenishment of missing residues
      - repair of non-standard residues
      - addition of missing atoms and addition of protons at pH=7.0
  - Check the repaired PDB, add water and select the `AMBER` force field
  - Calculate and add NaCl & Glycine according to the solution information given in the PDB file
  - Construct solution system, load protein coordinates and calculate of potential energy, with gradual warming and pressure equilibration
  - Product simulation, input the enclosing box where the three pockets are located, and then colouring for animation

- **`animation.py`**
  Used to run and generate animations synthesized from trajectories in the PyMol GUI.

- **`3ugc.pdb`**  
  Sequence file of tyrosine protein kinase JAK2 (code: 3UGC) from the RCSB protein database.
 
## How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
2. **Install required packages**,
   ```shell
   conda install -c conda-forge openmm
3. **Run the analysis in your IDE:**
The .ipynb will execute and generate visualizations, predictive states and results by cell.
4. **Animation**
Run `animation.py` independently in the PyMol GUI to generate animations that focus on the running state of each of the three pockets.

## References

- **Protein sequence: [3UGC](https://www.rcsb.org/structure/3UGC)**
- **Tools: [Openmm](https://pytorch.org/), [PyMol](https://pymol.org/)**

## License

This project is open for academic and educational purposes. Please cite the original PDB file if you use this analysis in your work.
