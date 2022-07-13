import subprocess

example = ['basic', 'IRF', 'Rate_eq', 'basic', 'broad', 'dmp_osc', 'BenchMark']
for e in example:
    subprocess.run(['jupyter', 'nbconvert', '--to', 'markdown',
                    f'{e}.ipynb', '--output',
                    f'{e}.md'])
    subprocess.run(['rm', '-rf',
                    f'../TRXASprefitpack/docs/source/{e}_files/'])
    subprocess.run(['mv', '-f', f'{e}.md', f'{e}_files',
                    '../TRXASprefitpack/docs/source/'])
