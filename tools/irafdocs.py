#! /usr/bin/env python3
"""irafdocs.py: compile IRAF documentation
"""
import pathlib
import re

from pyraf import iraf
from pyraf.iraftask import IrafCLTask, IrafPkg

docpath = pathlib.Path('doc')

def get_menu(pkgname):
    menu = list()
    if pkgname == 'clpackage':
        lines = mainhelp.splitlines()
    else:
        lines = iraf.help(pkgname, Stdout=True)
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
    except:
        print(f"Error for task {full_name}")
        return None
    
    if isinstance(task, IrafPkg):
        return process_package(task, desc)
    else:
        return process_other(task, desc)


def process_package(task=None, shortdesc=None):
    packages = get_menu(task.getName())
    if len(packages) < 1:
        return None
    try:
        iraf.load(task.getName(), doprint=False, hush=True)
    except:
        return None
    
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
    full_name = f"{task.getPkgname()}.{task.getName()}"
    outfile = docpath / f'{full_name}.rst'
    with outfile.open('w') as fp:
        title = task.getName()
        if shortdesc:
            title += ' — ' + shortdesc
        fp.write(f'.. _{task.getName()}:\n\n')
        fp.write(f'{title}\n{"="*len(title)}\n\n')
        fp.write(f'**Package: {task.getPkgname()}**\n\n')
        fp.write('.. raw:: html\n\n')
        for line in iraf.help(task, device='html', Stdout=True)[14:-2]:
            line = remove_anchor.sub(r'\1', line)
            if h3.findall(line):
                line = '<H3>' + h3.sub(r'\1', line).capitalize() + '</H3>'
            fp.write('  ' + line + '\n')
    return full_name


mainhelp="""
         dataio - Data format conversion package (RFITS, etc.)
           dbms - Database management package (not yet implemented)
         images - General image processing package
       language - The command language itself
          lists - List processing package
	  local - The template local package
       obsolete - Obsolete tasks
	   noao - The NOAO optical astronomy packages
	   plot - Plot package
	  proto - Prototype or interim tasks
       softools - Software tools package
         system - System utilities package
      utilities - Miscellaneous utilities package
"""


if __name__ == '__main__':
    process_task('clpackage')

    
