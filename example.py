#!/usr/bin/env python

from ConcourseTemplating import ConcourseTemplating, ConcoursePipelines, ConcourseAttributes

if __name__== "__main__":
    ci_templating = ConcourseTemplating(
        ConcourseAttributes(attribute_file='attributes.yml'), 
        ConcoursePipelines(root_dir='example')
    )
    ci_templating.apply_attributes()