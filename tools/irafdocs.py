#! /usr/bin/env python3
"""irafdocs.py: compile IRAF documentation
"""
import pathlib
import re
from lxml import etree
from lxml.html import html5parser
from io import StringIO
import json

#from py_w3c.validators.html.validator import HTMLValidator

from pyraf import iraf
from pyraf.iraftask import IrafCLTask, IrafPkg

def tabwithspace(s):
    s1 = ''
    i = 0
    in_entity = False
    for c in s:
        if c == '\t':
            s1 += ' ' * (8 - i % 8)
            i += (8 - i % 8)
        else:
            s1 += c
            if c == '&':
                in_entity = True
            if in_entity and c == ';':
                in_entity = False
            if not in_entity:
                i += 1
    return s1

def min_indention(lines):
    return min((len(l) - len(l.lstrip()) for l in lines if l.strip() != ''))


def unindent(lines):
    if len(lines) == 0:
        return lines
    u = min_indention(lines)
    return [(l[u:] if l.strip() != '' else '')
            for l in lines]

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

    if device == 'text':
        return lines

    if len(lines) < 10:
        return None
    if 'doctype html' not in lines[0].lower():
        return None
    err = False
    #print(f'{full_name}...')
#    try:
#        etree.parse(StringIO('\n'.join(lines)), html5parser.HTMLParser(strict=True))
#    except Exception as e:
#        print(f'{full_name}: {e}')
#        err = True
    #html_validator = HTMLValidator()
    #html_validator.validate_fragment('\n'.join(lines))
    #for e in html_validator.errors:
    #    if 'Duplicate ID' in e['message']:
    #        continue
    #    print(f"{full_name}:{e.get('lastLine')}: {e.get('message')}")
    #    err = True
    if err:
        with open(f'err/{full_name}.html', 'w') as fp:
            fp.write('\n'.join(lines))
#    lines = lines[14:-2]
    lines = lines[:-2]
    if len(lines) < 10:
        return None
    
    prolog = True
    olines = []
    h3 = re.compile(r'<h2>(.*?)</h2>')
    sec = re.compile(r'<section id="s_(.*?)">')
    in_code = False
    codelines = []
    for line in lines:
        if h3.findall(line):
            hdr = h3.sub(r'\1', line)
            line = '<h3>' + hdr.capitalize() + '</h3>'
        if sec.findall(line):
            section = sec.sub(r'\1', line)
            if section != 'name':
                prolog = False
        if '<pre>' in line:
            line = line.replace('<pre>',
                                '<div class="highlight-default-notranslate"><pre>')
            codelines = []
            olines.append(line)
            in_code = True
        elif '</pre>' in line:
            line = line.replace('</pre>', '</pre></div>')
            olines += unindent(codelines)
            olines.append(line)
            in_code = False
        elif not prolog and not in_code:
            olines.append(line)
        elif in_code:
            codelines.append(tabwithspace(line.replace('<br>', '')).rstrip())
    return olines

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

redirs = {}
def process_task(path, name, pkgname=None, desc=None):
    if pkgname is not None:
        full_name = f'{pkgname}.{name}'
    else:
        full_name = name
    try:
        task = iraf.getTask(full_name)
    except Exception:
        return process_other(path, f'{pkgname}.{name}', desc)
    
    if isinstance(task, IrafPkg) or full_name == 'language':
        return process_package(path, task, desc)
    else:
        return process_other(path, task, desc)


def process_package(path, task=None, shortdesc=None):
    packages = get_menu(task)
    if len(packages) < 1:
        return None
    try:
        iraf.load(task.getName(), doprint=False, hush=True)
    except:
        pass

    if task.getName() == 'clpackage':
        name = None
        outfile = path / 'index.rst'
    else:
        name = task.getName().rsplit('.',1)[-1]
        outfile = path / name / 'index.rst'
    if outfile.exists():
        return name
    if not outfile.parent.exists():
        outfile.parent.mkdir()

    with outfile.open('w') as fp:
        title = name
        if title is None:
            title = "Package and Task Reference"
        if shortdesc:
            title += ': ' + shortdesc
        fp.write(f'{title}\n{"="*len(title)}\n\n.. toctree:: :maxdepth: 1\n\n')
        if name is not None:
            path = path / name
        for cname, desc in packages:
            ccname = process_task(path, cname, name, desc)
            if ccname is not None:
                fp.write(f'   {ccname}\n')
    redirs[f'tasks/by-name/{name}'] = '../' + str(path.relative_to('doc/tasks') / f'index.html')
    return f'{name}/index'


def process_other(path, task, shortdesc):
    if isinstance(task, str):
        name = task.split('.')[-1]
        pkg = task.split('.')[0]
        full_name = task
    else:
        name = task.getName()
        pkg = task.getPkgname()
        full_name = f"{pkg}.{name}"
    outfile = path / f'{name}.rst'
    if not outfile.parent.exists():
        outfile.parent.mkdir()
    lines = get_help(task, device='html')
    if lines is None:
        return None

    with outfile.open('w') as fp:
        title = name
        if shortdesc:
            title += ': ' + shortdesc
        fp.write(f'.. _{name}:\n\n')
        fp.write(f'{title}\n{"="*len(title)}\n\n')
        fp.write(f'**Package: {pkg}**\n\n')
        fp.write('.. raw:: html\n\n  ')
        fp.write('\n  '.join(lines))
        fp.write('\n')

    redirs[f'tasks/by-name/{name}'] = '../' + str(path.relative_to('doc/tasks') / f'{name}.html')
    return name


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
    docpath = pathlib.Path('doc/tasks')
    process_task(docpath, 'clpackage')
    with open('doc/redirects.json', 'w') as fp:
        json.dump(redirs, fp)
