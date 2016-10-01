# ./_phys.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:856de6fbf2f74fe1f2e6074566c54e1d93619838
# Generated 2016-09-30 11:49:56.011471 by PyXB version 1.2.5 using Python 3.5.2.final.0
# Namespace eml://ecoinformatics.org/physical-2.1.1 [xmlns:phys]

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
Namespace = pyxb.namespace.NamespaceForURI('eml://ecoinformatics.org/physical-2.1.1', create_if_missing=True)
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

from _nsgroup import physical # {eml://ecoinformatics.org/physical-2.1.1}physical
from _nsgroup import CTD_ANON_48 as CTD_ANON # None
from _nsgroup import CTD_ANON_49 as CTD_ANON_ # None
from _nsgroup import CTD_ANON_50 as CTD_ANON_2 # None
from _nsgroup import CTD_ANON_51 as CTD_ANON_3 # None
from _nsgroup import STD_ANON_16 as STD_ANON # None
from _nsgroup import CTD_ANON_52 as CTD_ANON_4 # None
from _nsgroup import STD_ANON_17 as STD_ANON_ # None
from _nsgroup import CTD_ANON_53 as CTD_ANON_5 # None
from _nsgroup import CTD_ANON_54 as CTD_ANON_6 # None
from _nsgroup import CTD_ANON_55 as CTD_ANON_7 # None
from _nsgroup import STD_ANON_18 as STD_ANON_2 # None
from _nsgroup import CTD_ANON_56 as CTD_ANON_8 # None
from _nsgroup import CTD_ANON_57 as CTD_ANON_9 # None
from _nsgroup import STD_ANON_19 as STD_ANON_3 # None
from _nsgroup import CTD_ANON_58 as CTD_ANON_10 # None
from _nsgroup import PhysicalOnlineType # {eml://ecoinformatics.org/physical-2.1.1}PhysicalOnlineType
from _nsgroup import PhysicalType # {eml://ecoinformatics.org/physical-2.1.1}PhysicalType
from _nsgroup import PhysicalDistributionType # {eml://ecoinformatics.org/physical-2.1.1}PhysicalDistributionType