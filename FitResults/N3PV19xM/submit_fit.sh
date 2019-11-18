#!/bin/bash
#
#SBATCH --job-name=NPfit
#SBATCH --output=output.txt
#SBATCH --array=0-300
#SBATCH --partition=12hr

srun /home/bissolotti/Codes/NangaParbat/cli/../run/RunFit /home/bissolotti/Codes/NangaParbat/cli/../run/../mN3PV19xFlu/ /home/bissolotti/Codes/NangaParbat/cli/../run/../mN3PV19xFlu/fitconfig.yaml /home/bissolotti/Codes/NangaParbat/cli/../run/../mN3PV19xFlu/data /home/bissolotti/Codes/NangaParbat/cli/../run/../mN3PV19xFlu/tables $SLURM_ARRAY_TASK_ID y n