import subprocess

example = ['IRF', 'Rate_eq', 'Exp_Conv_IRF', 'Dmp_Osc_Conv_IRF',
'Fit_Static_voigt', 'Fit_Static_thy',
'Fit_Transient_Exp', 'Fit_Transient_Raise', 'Fit_Transient_Both',
'Associated_Difference_Spectrum']
for e in example:
    subprocess.run(['jupyter', 'nbconvert', '--to', 'markdown',
                    f'{e}.ipynb', '--output',
                    f'{e}.md'])
    subprocess.run(['rm', '-rf',
                    f'../TRXASprefitpack/docs/source/{e}_files/'])
    subprocess.run(['mv', '-f', f'{e}.md', f'{e}_files',
                    '../TRXASprefitpack/docs/source/'])
