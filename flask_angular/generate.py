# -*- coding: utf-8 -*-
from flask.ext.script import Manager
from flask.ext.angular import get_path_to_source_file
from flask.ext.angular import get_path_to_spec_file
from flask.ext.angular import get_path_to_component_file
from flask.ext.angular import render, get_path_from_root, ensure_dir
from flask.ext.angular import source_section, specs_section
from os import path
import json

manager = Manager(usage="Perform angular.js generate operations")


def make_list_of_sources(raw_sources):
    sources = list()
    if isinstance(raw_sources, str):
        sources.append(raw_sources)
    else:
        sources.extend(raw_sources)
    return sources


def add_file_in_section(section_name, path_from_source):
    data = {}
    with open(get_path_to_component_file(), "r") as component:
        data = json.load(component)
    items_in_section = []
    if section_name in data:
        items_in_section = make_list_of_sources(data[section_name])
    if path_from_source not in items_in_section:
        items_in_section.append(path_from_source)
    data[section_name] = items_in_section
    with open(get_path_to_component_file(), "w") as component:
        json.dump(data, component, indent=4)


def add_source_file_to_component(path_from_source):
    add_file_in_section(source_section, path_from_source)


def add_spec_file_to_component(path_from_source):
    add_file_in_section(specs_section, path_from_source)


def create_source_file(file_name, location, template, **template_args):
    source = create_file(
        file_name,
        location,
        template,
        get_path_to_source_file,
        **template_args)
    add_source_file_to_component(source)


def create_spec_file(file_name, location, template, **template_args):
    spec = create_file(
        file_name,
        location,
        template,
        get_path_to_spec_file,
        **template_args)
    add_spec_file_to_component(spec)


def create_file(file_name, location, template, get_path, **template_args):
    local_path = path.join(location, file_name + ".coffee")
    path_from_source = get_path(local_path)
    path_from_root = get_path_from_root(path_from_source)
    ensure_dir(path_from_root)
    with open(path_from_root, "w") as module:
        module.write(render(template, **template_args))
    return path_from_source


@manager.command
def module(module_name):
    '''
    Create module in your angular project
    '''
    create_source_file(
        module_name,
        "modules",
        "module.coffee",
        name=module_name)


@manager.command
def controller(module_name, controller_name):
    '''
    Create controller
    '''
    create_source_file(
        controller_name,
        "controllers",
        "controller.coffee",
        name=controller_name,
        module=module_name)

    create_spec_file(
        controller_name+"_spec",
        "controllers",
        "controller_spec.coffee",
        name=controller_name,
        module=module_name)


@manager.command
def resource(module_name, resource_name, path_to_resource):
    '''
    Create resource
    '''
    create_source_file(
        resource_name,
        "resources",
        "resource.coffee",
        name=resource_name,
        module=module_name,
        path_to_resource=path_to_resource)


@manager.command
def service(module_name, service_name):
    '''
    Create service
    '''
    create_source_file(
        service_name,
        "services",
        "service.coffee",
        name=service_name,
        module=module_name)
    create_spec_file(
        service_name+"_spec",
        "services",
        "service_spec.coffee",
        name=service_name,
        module=module_name)


@manager.command
def filter(module_name, filter_name):
    '''
    Create filter
    '''
    create_source_file(
        filter_name,
        "filters",
        "filter.coffee",
        name=filter_name,
        module=module_name)
    create_spec_file(
        filter_name+"_spec",
        "filters",
        "filter_spec.coffee",
        name=filter_name,
        module=module_name)
