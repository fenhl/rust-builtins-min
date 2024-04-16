import os
import shutil
import subprocess

subprocess.run(
    ['cargo', '+nightly-2024-04-14', 'build', '-Zbuild-std=core', '--release', '--target=mips-ultra64-cpu.json'],
    env={**os.environ, 'RUSTFLAGS': '-Csymbol-mangling-version=v0'},
    check=True,
)
subprocess.run(['armips', 'build.asm'], check=True)

subprocess.run(
    ['cargo', '+nightly', 'build', '-Zbuild-std=core', '--release', '--target=mips-ultra64-cpu.json'],
    env={**os.environ, 'RUSTFLAGS': '-Csymbol-mangling-version=v0'},
    check=True,
)
if subprocess.run(['armips', 'build.asm']).returncode == 0:
    raise Exception('Latest nightly succeeded')
print('Latest nightly failed')
