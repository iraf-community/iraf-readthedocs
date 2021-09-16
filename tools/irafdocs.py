#! /usr/bin/env python3
"""irafdocs.py: compile IRAF documentation
"""
import pathlib
import re

from pyraf import iraf
from pyraf.iraftask import IrafCLTask, IrafPkg

docpath = pathlib.Path('doc')

def get_help(task, device='text'):
    if isinstance(task, str):
        name = task.split('.')[-1]
        pkg = task.split('.')[0]
    else:
        name = task.getName()
        pkg = task.getPkgname()
    try:
        lines = iraf.help(f'{pkg}.{name}', device=device, Stdout=True)
        if len(lines) < 2:
            raise Exception
    except Exception:
        lines = iraf.help(name, device=device, Stdout=True)
    return lines

def get_menu(task):
    pkgname = task.getName()
    menu = list()
    if pkgname == 'clpackage':
        lines = mainhelp.splitlines()
    else:
        lines = get_help(task)
    for line in lines:
        if '-' not in line:
            continue
        name, desc = line.split('-', 1)
        name = name.strip()
        if desc.endswith('[up]'):
            desc = desc[:-4]
        desc = desc.strip()
        menu.append((name, desc))
    return menu

def process_task(name, pkgname=None, desc=None):
    if pkgname is not None:
        full_name = f'{pkgname}.{name}'
    else:
        full_name = name
    try:
        task = iraf.getTask(full_name)
    except Exception:
        return process_other(f'{pkgname}.{name}', desc)
    
    if isinstance(task, IrafPkg) or full_name == 'language':
        return process_package(task, desc)
    else:
        return process_other(task, desc)


def process_package(task=None, shortdesc=None):
    packages = get_menu(task)
    if len(packages) < 1:
        return None
    try:
        iraf.load(task.getName(), doprint=False, hush=True)
    except:
        pass
    
    if task.getName() == 'clpackage':
        full_name = None
        outfile = docpath / 'index.rst'
    else:
        full_name = f"{task.getPkgname()}.{task.getName()}"
        outfile = docpath / f'{full_name}.rst'
    if outfile.exists():
        return full_name
    
    with outfile.open('w') as fp:
        title = task.getName()
        if title == 'clpackage':
            title = "IRAF task help"
        if shortdesc:
            title += ' — ' + shortdesc
        fp.write(f'{title}\n{"="*len(title)}\n\n.. toctree:: :maxdepth: 1\n\n')
        short_name = task.getName().rsplit('.',1)[-1]
        for cname, desc in packages:
            name = process_task(cname, short_name, desc)
            if name is not None:
                fp.write(f'   {name}\n')
    return full_name


def process_other(task, shortdesc):
    remove_anchor = re.compile(r'<A NAME="[^"]*">(.*?)</A>')
    h3 = re.compile(r'<H2>(.*?)</H2>')
    if isinstance(task, str):
        name = task.split('.')[-1]
        pkg = task.split('.')[0]
        full_name = task
    else:
        name = task.getName()
        pkg = task.getPkgname()
        full_name = f"{pkg}.{name}"
    outfile = docpath / f'{full_name}.rst'
    lines = get_help(task, device='html')
    if len(lines) < 12:
        return None
    with outfile.open('w') as fp:
        title = name
        if shortdesc:
            title += ' — ' + shortdesc
        fp.write(f'.. _{name}:\n\n')
        fp.write(f'{title}\n{"="*len(title)}\n\n')
        fp.write(f'**Package: {pkg}**\n\n')
        fp.write('.. raw:: html\n\n')
        for line in lines:
            line = remove_anchor.sub(r'\1', line)
            if h3.findall(line):
                line = '<H3>' + h3.sub(r'\1', line).capitalize() + '</H3>'
            fp.write('  ' + line + '\n')
    return full_name


mainhelp="""
       language - The command language itself
         images - General image processing package
          lists - List processing package
	   plot - Plot package
         dataio - Data format conversion package (RFITS, etc.)
         system - System utilities package
      utilities - Miscellaneous utilities package
       softools - Software tools package
	   noao - The NOAO optical astronomy packages
	  proto - Prototype or interim tasks
       obsolete - Obsolete tasks
"""


if __name__ == '__main__':
    process_task('clpackage')

    
