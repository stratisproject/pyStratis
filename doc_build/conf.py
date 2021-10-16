# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../'))
os.environ['SPHINX_BUILD'] = '1'

# -- Project information -----------------------------------------------------

project = 'PyStratis'
copyright = '2021, Tjaden Froyda'
author = 'Tjaden Froyda'

# The full version, including alpha/beta/rc tags
release = '1.0.7.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']
add_module_names = False
python_use_unqualified_type_names = True
napoleon_numpy_docstring = True
autoclass_content = 'class'
autodoc_typehints = 'signature'
autodoc_inherit_docstrings = False
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__call__',
    'undoc-members': False,
    'inherited-members': True,
    'show_inheritance': True,
    'exclude-members': ("construct, copy, dict, update_forward_refs, schema, schema_json, validate, parse_raw, parse_file, parse_obj, json, from_orm, "
                        "use_enum_values, extra, json_encoders, allow_population_by_field_name, route, Config, validate_class, calculate_checksum, validate_values"
                        "validate_value, validate_allowed_types, update, get, put, post, delete, endpoints, api_route")
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '*setup.py', '../integration_tests', '*conftest.py']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
