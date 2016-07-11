import SES3DPy
import numpy as np
outdir='/lustre/janus_scratch/life9360/EA_ses3d_working_dir/INPUT'
Qmodel=SES3DPy.Q_model( fmin=1.0/100., fmax=1/5.);
# Qmodel=SES3DPy.Q_model( QArr=np.array([80.0]), fmin=1.0/1000., fmax=1/20.);
Qmodel.Qdiscrete();

# D=np.array([1.684, 0.838, 1.357]);
# tau_s=np.array([3.2, 17.692, 74.504]);
# Qmodel.PlotQdiscrete( D=D, tau_s=tau_s );
Qmodel.PlotQdiscrete();
Qmodel.WriteRelax(outdir=outdir)