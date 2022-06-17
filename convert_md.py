import subprocess

example = ['IRF', 'Rate_eq', 'basic', 'broad', 'dmp_osc']

for e in example:
    subprocess.run(['jupyter', 'nbconvert', '--to', 'markdown',
                    f'{e}.ipynb', '--output',
                    f'{e}.md'])
    subprocess.run(['rm', '-rf',
                    f'../TRXAS-pre-fit-pack/docs/source/{e}_files/'])
    subprocess.run(['mv', '-f', f'{e}.md', f'{e}_files',
                    '../TRXAS-pre-fit-pack/docs/source/'])
