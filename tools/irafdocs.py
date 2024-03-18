#! /usr/bin/env python3
"""irafdocs.py: compile IRAF documentation
"""
import os
import pathlib
import re
import shutil
from lxml import etree
from lxml.html import html5parser
from io import StringIO
import json

# from py_w3c.validators.html.validator import HTMLValidator

from pyraf import iraf
from pyraf.iraftask import IrafCLTask, IrafPkg, IrafError
from iraf import softools, mkhelpdb, flprcache


def tabwithspace(s):
    s1 = ""
    i = 0
    in_entity = False
    for c in s:
        if c == "\t":
            s1 += " " * (8 - i % 8)
            i += 8 - i % 8
        else:
            s1 += c
            if c == "&":
                in_entity = True
            if in_entity and c == ";":
                in_entity = False
            if not in_entity:
                i += 1
    return s1


def min_indention(lines):
    return min((len(l) - len(l.lstrip()) for l in lines if l.strip() != ""))


def unindent(lines):
    if len(lines) == 0:
        return lines
    u = min_indention(lines)
    return [(l[u:] if l.strip() != "" else "") for l in lines]


def get_help(task, device="text", option="help"):
    if isinstance(task, str):
        name = task.split(".")[-1]
        pkg = task.split(".")[0]
    else:
        name = task.getName()
        pkg = task.getPkgname()
    if name == "clpackage" and pkg == "clpackage":
        name = ""
    try:
        lines = iraf.help(
            f"{pkg}.{name}",
            device=device,
            option=option,
            Stdout=True,
            Stderr="/dev/null",
        )
        if len(lines) < 2:
            raise Exception
    except Exception:
        lines = iraf.help(
            name, device=device, option=option, Stdout=True, Stderr="/dev/null"
        )

    if device == "text":
        return lines

    if len(lines) < 10:
        return None
    if "doctype html" not in lines[0].lower():
        return None
    err = False
    # print(f'{full_name}...')
    #    try:
    #        etree.parse(StringIO('\n'.join(lines)), html5parser.HTMLParser(strict=True))
    #    except Exception as e:
    #        print(f'{full_name}: {e}')
    #        err = True
    # html_validator = HTMLValidator()
    # html_validator.validate_fragment('\n'.join(lines))
    # for e in html_validator.errors:
    #    if 'Duplicate ID' in e['message']:
    #        continue
    #    print(f"{full_name}:{e.get('lastLine')}: {e.get('message')}")
    #    err = True
    if err:
        with open(f"err/{full_name}.html", "w") as fp:
            fp.write("\n".join(lines))
    #    lines = lines[14:-2]
    lines = lines[:-2]
    if len(lines) < 10:
        return None

    prolog = True
    olines = []
    h3 = re.compile(r"<h2>(.*?)</h2>")
    sec = re.compile(r'<section id="s_(.*?)">')
    in_code = False
    codelines = []
    for line in lines:
        if h3.findall(line):
            hdr = h3.sub(r"\1", line)
            line = "<h3>" + hdr.capitalize() + "</h3>"
        if sec.findall(line):
            section = sec.sub(r"\1", line)
            if section != "name":
                prolog = False
        if "<pre>" in line:
            line = line.replace(
                "<pre>", '<div class="highlight-default-notranslate"><pre>'
            )
            codelines = []
            olines.append(line)
            in_code = True
        elif "</pre>" in line:
            line = line.replace("</pre>", "</pre></div>")
            olines += unindent(codelines)
            olines.append(line)
            in_code = False
        elif not prolog and not in_code:
            olines.append(line)
        elif in_code:
            codelines.append(tabwithspace(line.replace("<br>", "")).rstrip())
    return olines


def get_menu(task):
    pkgname = task.getName()
    menu = list()
    lines = get_help(task)
    for line in lines:
        if "-" in line:
            name, desc = line.split("-", 1)
        elif "*" in line:
            name, desc = line.split("*", 1)
        else:
            continue
        name = name.strip()
        if " " in name:  # Probably not a menu line
            continue
        if desc.endswith("[up]"):
            desc = desc[:-4]
        desc = desc.strip()
        menu.append((name, desc))
    return menu


redirs = {}


def process_task(path, name, pkgname=None, desc=None):
    if pkgname is not None:
        full_name = f"{pkgname}.{name}"
    else:
        full_name = name
    try:
        task = iraf.getTask(full_name)
    except Exception:
        return process_other(path, full_name, desc)

    if isinstance(task, IrafPkg) or full_name == "language":
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

    print(f"\nPackage {task.getName()}:")
    if task.getName() == "clpackage":
        name = None
        outfile = path / "index.rst"
    else:
        name = task.getName().rsplit(".", 1)[-1]
        outfile = path / name / "index.rst"
    if outfile.exists():
        return name
    if not outfile.parent.exists():
        outfile.parent.mkdir()

    with outfile.open("w") as fp:
        title = name
        if title is None:
            title = "Package and Task Reference"
        if shortdesc:
            title += ": " + shortdesc
        fp.write(f'{title}\n{"="*len(title)}\n\n.. toctree:: :maxdepth: 1\n\n')
        if name is not None:
            path = path / name
        for cname, desc in packages:
            ccname = process_task(path, cname, name, desc)
            if ccname is not None:
                fp.write(f"   {ccname}\n")

        lines = get_help(task, device="html", option="sysdoc")
        if lines is not None and len(lines) > 10:
            fp.write(".. raw:: html\n\n  ")
            fp.write("\n  ".join(lines))
            fp.write("\n")

    redirs[f"tasks/by-name/{name}"] = "../" + str(
        path.relative_to("doc/tasks") / f"index.html"
    )
    return f"{name}/index"


def process_other(path, task, shortdesc):
    if isinstance(task, str):
        name = task.split(".")[-1]
        pkg = task.split(".")[0]
        full_name = task
    else:
        name = task.getName()
        pkg = task.getPkgname()
        full_name = f"{pkg}.{name}"
    print(f"    {full_name}")
    outfile = path / f"{name}.rst"
    if not outfile.parent.exists():
        outfile.parent.mkdir()
    lines = get_help(task, device="html")
    if lines is None:
        return None

    with outfile.open("w") as fp:
        title = name
        if shortdesc:
            title += ": " + shortdesc
        fp.write(f".. _{name}:\n\n")
        fp.write(f'{title}\n{"="*len(title)}\n\n')
        fp.write(f"**Package: {pkg}**\n\n")
        fp.write(".. raw:: html\n\n  ")
        fp.write("\n  ".join(lines))
        fp.write("\n")

    redirs[f"tasks/by-name/{name}"] = "../" + str(
        path.relative_to("doc/tasks") / f"{name}.html"
    )
    return name


def copy_static(target):
    for target_path in target.rglob("*.rst"):
        if str(target_path.relative_to(target)) not in (
            "index.rst",
            "extradocs.rst",
        ):
            target_path.unlink()

    src = pathlib.Path(os.environ["iraf"]) / "doc"
    for src_path in src.rglob("*.rst"):
        target_path = target / src_path.relative_to(src)
        if str(target_path.relative_to(target)) != "index.rst":
            target_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(src_path, target_path)


def external_packages():
    extern = pathlib.Path(os.environ["iraf"]) / "extern"
    for ext_path in sorted(extern.glob("*")):
        if ext_path.is_dir():
            try:
                mkhelpdb(
                    helpdir=f"{ext_path}/lib/root.hd",
                    helpdb=f"{ext_path}/lib/helpdb.mip",
                )
            except IrafError:  # happens when the helpdb file cannot be written
                pass
            flprcache("mkhelpdb")
            yield ext_path.name


extpkg_desc = {
    "adccdrom": "Astronomical Data Center (ADC) CD-ROM tools",
    "ctio": "Tools for the Cerro Tololo Inter-American Observatory",
    "deitab": "DEIMOS tables package",
    "fitsutil": "Utilities for single and multiple FITS files",
    "gemini": "Gemini data reduction package",
    "gmisc": "Miscellaneous Gemini related Tasks",
    "guiapps": "Prototype GUI application",
    "mscdb": "MSCRED support files",
    "mscred": "Mosaic CCD reduction package",
    "nfextern": "General IR reductions/NEWFIRM package",
    "rvsao": "IRAF Radial Velocity Package from SAO",
    "sptable": "IRAF package for tabular spectra",
    "st4gem": "Selected tools from STSDAS for use by the GEMINI package",
    "ucsclris": "UCSC LRIS mask making",
    "vo": "Virtual Observatory package from NOAO IRAF v2.16.1",
    "xdimsum": "Deep Infrared Mosaicing Software",
}


if __name__ == "__main__":
    docpath = pathlib.Path("doc")

    copy_static(docpath)

    process_task(docpath / "tasks", "clpackage")
    external_index = (
        "External packages\n" "=================\n" ".. toctree:: :maxdepth: 1\n\n"
    )

    have_ext = False
    for pkg in external_packages():
        have_ext = True
        process_task(docpath / "tasks", pkg, desc=extpkg_desc[pkg])
        external_index += f"  {pkg}/index\n"

    if have_ext:
        with (docpath / "tasks" / "extern.rst").open("w") as fp:
            fp.write(external_index)

    with (docpath / "redirects.json").open("w") as fp:
        json.dump(redirs, fp)
