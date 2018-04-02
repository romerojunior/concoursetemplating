#!/usr/bin/env python

import os
import yaml
import errno
from glob import glob
from jinja2 import Environment, FileSystemLoader


class ConcourseAttributes:
    def __init__(self, attribute_file):
        self.attribute_file = attribute_file
        self._attribute_map = None
 
    @property
    def attribute_map(self):
        if self._attribute_map is None:
            with open(self.attribute_file, 'r') as stream:
                self._attribute_map = yaml.load(stream)
        return self._attribute_map


class ConcoursePipelines:
    def __init__(self, root_dir):
        if os.path.isdir(root_dir):
            self.root_dir = root_dir
        else:
            strerror = "Directory not found"
            raise IOError(errno.ENOENT, strerror, root_dir)


class ConcourseTemplating:
    def __init__(self, attributes, pipelines):
        self.attributes = attributes
        self.pipelines = pipelines
        self._environment = Environment(
            loader=FileSystemLoader(
                self.pipelines.root_dir
                )
        )

    def list_templates(self):
        return [ self._environment.get_template(template) \
            for template in self._environment.list_templates() ]
    
    def apply_attributes(self):
        for template in self.list_templates():
            print template.render(self.attributes.attribute_map) 


# testing:
ci_templating = ConcourseTemplating(
    ConcourseAttributes(attribute_file='/Users/romerojnr/Repositories/templating/attributes.yml'), 
    ConcoursePipelines(root_dir='/Users/romerojnr/Repositories/templating/example')
)

ci_templating.apply_attributes()

