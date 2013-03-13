# -*- coding: utf-8 -*-
from flask.ext.script import Manager
from os import path, makedirs
from jinja2 import Environment, PackageLoader


env = Environment(loader=PackageLoader(__name__, 'templates'))

static_folder_name = "static"
specs_folder_name = "specs"
source_folder_name = "src"
component_file_name = "component.json"
source_section = "main"
specs_section = "specs"


def ensure_dir(f):
    d = path.dirname(f)
    if not path.exists(d):
        makedirs(d)


def render(template, **args):
    return env.get_template(template).render(args)


def get_path_from_root(sources_relative_path):
    return path.join(static_folder_name, sources_relative_path)


def get_path_to_component_file():
    return get_path_from_root(component_file_name)


def get_path_to_source_file(relative_file_path):
    return path.join(source_folder_name, relative_file_path)


def get_path_to_spec_file(relative_file_path):
    return path.join(specs_folder_name, relative_file_path)

import generate

manager = Manager(usage="Perform angular.js operations")
manager.add_command('generate', generate.manager)
manager.add_command('g', generate.manager)
