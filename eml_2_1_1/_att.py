# ./_att.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:55ea3d3dd5a531255d4c15c62bd6a6882d8d983c
# Generated 2016-09-30 11:49:56.013282 by PyXB version 1.2.5 using Python 3.5.2.final.0
# Namespace eml://ecoinformatics.org/attribute-2.1.1 [xmlns:att]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:4b66897e-8736-11e6-a13e-000c29ae0b70')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import _nsgroup as _ImportedBinding__nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('eml://ecoinformatics.org/attribute-2.1.1', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)

from _nsgroup import attribute # {eml://ecoinformatics.org/attribute-2.1.1}attribute
from _nsgroup import attributeList # {eml://ecoinformatics.org/attribute-2.1.1}attributeList
from _nsgroup import CTD_ANON # None
from _nsgroup import CTD_ANON_ # None
from _nsgroup import CTD_ANON_2 # None
from _nsgroup import CTD_ANON_3 # None
from _nsgroup import CTD_ANON_4 # None
from _nsgroup import CTD_ANON_5 # None
from _nsgroup import CTD_ANON_6 # None
from _nsgroup import CTD_ANON_7 # None
from _nsgroup import Accuracy # {eml://ecoinformatics.org/attribute-2.1.1}Accuracy
from _nsgroup import CTD_ANON_8 # None
from _nsgroup import UnitType # {eml://ecoinformatics.org/attribute-2.1.1}UnitType
from _nsgroup import PrecisionType # {eml://ecoinformatics.org/attribute-2.1.1}PrecisionType
from _nsgroup import CTD_ANON_9 # None
from _nsgroup import CTD_ANON_10 # None
from _nsgroup import CTD_ANON_11 # None
from _nsgroup import STD_ANON_3 as STD_ANON # None
from _nsgroup import CTD_ANON_12 # None
from _nsgroup import CTD_ANON_13 # None
from _nsgroup import CTD_ANON_14 # None
from _nsgroup import CTD_ANON_15 # None
from _nsgroup import CTD_ANON_16 # None
from _nsgroup import CTD_ANON_17 # None
from _nsgroup import CTD_ANON_18 # None
from _nsgroup import NumberType # {eml://ecoinformatics.org/attribute-2.1.1}NumberType
from _nsgroup import AttributeListType # {eml://ecoinformatics.org/attribute-2.1.1}AttributeListType
from _nsgroup import AttributeType # {eml://ecoinformatics.org/attribute-2.1.1}AttributeType
from _nsgroup import NonNumericDomainType # {eml://ecoinformatics.org/attribute-2.1.1}NonNumericDomainType
from _nsgroup import CTD_ANON_84 as CTD_ANON_19 # None
from _nsgroup import NumericDomainType # {eml://ecoinformatics.org/attribute-2.1.1}NumericDomainType
from _nsgroup import DateTimeDomainType # {eml://ecoinformatics.org/attribute-2.1.1}DateTimeDomainType
