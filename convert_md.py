import subprocess

example = ['IRF', 'Rate_eq', 'basic', 'broad']

for e in example:
    subprocess.run(['jupyter', 'nbconvert', '--to', 'markdown',
                    f'{e}.ipynb', '--output',
                    f'../TRXAS-pre-fit-pack/docs/source/{e}.md'])
