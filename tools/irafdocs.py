#! /usr/bin/env python3
"""irafdocs.py: compile IRAF documentation
"""
import pathlib
import re
from lxml import etree
from io import StringIO

from py_w3c.validators.html.validator import HTMLValidator

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
        lines = iraf.help(f'{pkg}.{name}', device=device, Stdout=True,
                          Stderr="/dev/null")
        if len(lines) < 2:
            raise Exception
    except Exception:
        lines = iraf.help(name, device=device, Stdout=True,
                          Stderr="/dev/null")
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
        name = None
        outfile = docpath / 'index.rst'
    else:
        name = task.getName().rsplit('.',1)[-1]
        outfile = docpath / f'{name}.rst'
    if outfile.exists():
        return name
        
    with outfile.open('w') as fp:
        title = name
        if title is None:
            title = "IRAF task help"
        if shortdesc:
            title += ': ' + shortdesc
        fp.write(f'{title}\n{"="*len(title)}\n\n.. toctree:: :maxdepth: 1\n\n')
        for cname, desc in packages:
            ccname = process_task(cname, name, desc)
            if ccname is not None:
                fp.write(f'   {ccname.replace(".", "/")}\n')
    return name


def process_other(task, shortdesc):
    h3 = re.compile(r'<h2(.*?)>(.*?)</h2>')
    if isinstance(task, str):
        name = task.split('.')[-1]
        pkg = task.split('.')[0]
        full_name = task
    else:
        name = task.getName()
        pkg = task.getPkgname()
        full_name = f"{pkg}.{name}"
    outfile = docpath / f'{full_name.replace(".","/")}.rst'
    if not outfile.parent.exists():
        outfile.parent.mkdir()
    lines = get_help(task, device='html')
    if len(lines) < 10:
        return None
    if 'doctype html' not in lines[0].lower():
        return None
    try:
        etree.parse(StringIO('\n'.join(lines)), etree.HTMLParser(recover=False))
    except Exception as e:
        print(f'{full_name}: {e}')
        with open(f'err/{full_name}.html', 'w') as fp:
            fp.write('\n'.join(lines))
    #html_validator = HTMLValidator()
    #html_validator.validate_fragment('\n'.join(lines))
    #for e in html_validator.errors:
    #    if 'Duplicate ID' in e['message']:
    #        continue
    #    print(f"{full_name}:{e.get('lastLine')}: {e.get('message')}")
    lines = lines[14:-2]
    if len(lines) < 10:
        return None
    with outfile.open('w') as fp:
        title = name
        if shortdesc:
            title += ': ' + shortdesc
        fp.write(f'.. _{name}:\n\n')
        fp.write(f'{title}\n{"="*len(title)}\n\n')
        fp.write(f'**Package: {pkg}**\n\n')
        fp.write('.. raw:: html\n\n')
        prolog = True
        for line in lines:
            if h3.findall(line):
                hdr = h3.sub(r'\2', line)
                if hdr != 'NAME':
                    prolog = False
                line = '<h3>' + hdr.capitalize() + '</h3>'
            if not prolog:
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

    
