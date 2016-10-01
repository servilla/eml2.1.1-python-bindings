# ./_txt.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:cefc7d021f2586f94a3171f92b483a933b97ce9f
# Generated 2016-09-30 11:49:56.009283 by PyXB version 1.2.5 using Python 3.5.2.final.0
# Namespace eml://ecoinformatics.org/text-2.1.1 [xmlns:txt]

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
import pyxb.binding.datatypes
import pyxb.binding.xml_

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('eml://ecoinformatics.org/text-2.1.1', create_if_missing=True)
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


# Complex type {eml://ecoinformatics.org/text-2.1.1}TextType with content type MIXED
class TextType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TextType')
    _XSDLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 91, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element section uses Python identifier section
    __section = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'section'), 'section', '__emlecoinformatics_orgtext_2_1_1_TextType_section', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 104, 6), )

    
    section = property(__section.value, __section.set, None, '')

    
    # Element para uses Python identifier para
    __para = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'para'), 'para', '__emlecoinformatics_orgtext_2_1_1_TextType_para', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 116, 6), )

    
    para = property(__para.value, __para.set, None, '')

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__emlecoinformatics_orgtext_2_1_1_TextType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 131, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        __section.name() : __section,
        __para.name() : __para
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })
_module_typeBindings.TextType = TextType
Namespace.addCategoryObject('typeBinding', 'TextType', TextType)


# Complex type {eml://ecoinformatics.org/text-2.1.1}ParagraphType with content type MIXED
class ParagraphType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ParagraphType')
    _XSDLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 134, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__emlecoinformatics_orgtext_2_1_1_ParagraphType_value', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 148, 2), )

    
    value_ = property(__value.value, __value.set, None, '')

    
    # Element itemizedlist uses Python identifier itemizedlist
    __itemizedlist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'itemizedlist'), 'itemizedlist', '__emlecoinformatics_orgtext_2_1_1_ParagraphType_itemizedlist', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 157, 6), )

    
    itemizedlist = property(__itemizedlist.value, __itemizedlist.set, None, '')

    
    # Element orderedlist uses Python identifier orderedlist
    __orderedlist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'orderedlist'), 'orderedlist', '__emlecoinformatics_orgtext_2_1_1_ParagraphType_orderedlist', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 170, 6), )

    
    orderedlist = property(__orderedlist.value, __orderedlist.set, None, '')

    
    # Element emphasis uses Python identifier emphasis
    __emphasis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'emphasis'), 'emphasis', '__emlecoinformatics_orgtext_2_1_1_ParagraphType_emphasis', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 183, 6), )

    
    emphasis = property(__emphasis.value, __emphasis.set, None, '')

    
    # Element subscript uses Python identifier subscript
    __subscript = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'subscript'), 'subscript', '__emlecoinformatics_orgtext_2_1_1_ParagraphType_subscript', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 201, 6), )

    
    subscript = property(__subscript.value, __subscript.set, None, '')

    
    # Element superscript uses Python identifier superscript
    __superscript = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'superscript'), 'superscript', '__emlecoinformatics_orgtext_2_1_1_ParagraphType_superscript', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 211, 6), )

    
    superscript = property(__superscript.value, __superscript.set, None, '')

    
    # Element literalLayout uses Python identifier literalLayout
    __literalLayout = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'literalLayout'), 'literalLayout', '__emlecoinformatics_orgtext_2_1_1_ParagraphType_literalLayout', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 221, 6), )

    
    literalLayout = property(__literalLayout.value, __literalLayout.set, None, '')

    
    # Element ulink uses Python identifier ulink
    __ulink = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ulink'), 'ulink', '__emlecoinformatics_orgtext_2_1_1_ParagraphType_ulink', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 237, 6), )

    
    ulink = property(__ulink.value, __ulink.set, None, '')

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__emlecoinformatics_orgtext_2_1_1_ParagraphType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 272, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        __value.name() : __value,
        __itemizedlist.name() : __itemizedlist,
        __orderedlist.name() : __orderedlist,
        __emphasis.name() : __emphasis,
        __subscript.name() : __subscript,
        __superscript.name() : __superscript,
        __literalLayout.name() : __literalLayout,
        __ulink.name() : __ulink
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })
_module_typeBindings.ParagraphType = ParagraphType
Namespace.addCategoryObject('typeBinding', 'ParagraphType', ParagraphType)


# Complex type [anonymous] with content type MIXED
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 194, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__emlecoinformatics_orgtext_2_1_1_CTD_ANON_value', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 196, 10), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__emlecoinformatics_orgtext_2_1_1_CTD_ANON_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 198, 9)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        __value.name() : __value
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type MIXED
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 231, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__emlecoinformatics_orgtext_2_1_1_CTD_ANON__value', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 233, 10), )

    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        __value.name() : __value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type MIXED
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 246, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element citetitle uses Python identifier citetitle
    __citetitle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'citetitle'), 'citetitle', '__emlecoinformatics_orgtext_2_1_1_CTD_ANON_2_citetitle', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 248, 12), )

    
    citetitle = property(__citetitle.value, __citetitle.set, None, '')

    
    # Attribute url uses Python identifier url
    __url = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'url'), 'url', '__emlecoinformatics_orgtext_2_1_1_CTD_ANON_2_url', pyxb.binding.datatypes.anySimpleType)
    __url._DeclarationLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 259, 10)
    __url._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 259, 10)
    
    url = property(__url.value, __url.set, None, '')

    _ElementMap.update({
        __citetitle.name() : __citetitle
    })
    _AttributeMap.update({
        __url.name() : __url
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type {eml://ecoinformatics.org/text-2.1.1}SectionType with content type ELEMENT_ONLY
class SectionType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SectionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 275, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'title'), 'title', '__emlecoinformatics_orgtext_2_1_1_SectionType_title', False, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 287, 6), )

    
    title = property(__title.value, __title.set, None, '')

    
    # Element para uses Python identifier para
    __para = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'para'), 'para', '__emlecoinformatics_orgtext_2_1_1_SectionType_para', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 299, 8), )

    
    para = property(__para.value, __para.set, None, '')

    
    # Element section uses Python identifier section
    __section = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'section'), 'section', '__emlecoinformatics_orgtext_2_1_1_SectionType_section', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 313, 8), )

    
    section = property(__section.value, __section.set, None, '')

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__emlecoinformatics_orgtext_2_1_1_SectionType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 327, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __para.name() : __para,
        __section.name() : __section
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })
_module_typeBindings.SectionType = SectionType
Namespace.addCategoryObject('typeBinding', 'SectionType', SectionType)


# Complex type {eml://ecoinformatics.org/text-2.1.1}ListType with content type ELEMENT_ONLY
class ListType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ListType')
    _XSDLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 330, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element listitem uses Python identifier listitem
    __listitem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'listitem'), 'listitem', '__emlecoinformatics_orgtext_2_1_1_ListType_listitem', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 342, 8), )

    
    listitem = property(__listitem.value, __listitem.set, None, '')

    _ElementMap.update({
        __listitem.name() : __listitem
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ListType = ListType
Namespace.addCategoryObject('typeBinding', 'ListType', ListType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 356, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element para uses Python identifier para
    __para = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'para'), 'para', '__emlecoinformatics_orgtext_2_1_1_CTD_ANON_3_para', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 358, 14), )

    
    para = property(__para.value, __para.set, None, '')

    
    # Element itemizedlist uses Python identifier itemizedlist
    __itemizedlist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'itemizedlist'), 'itemizedlist', '__emlecoinformatics_orgtext_2_1_1_CTD_ANON_3_itemizedlist', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 372, 14), )

    
    itemizedlist = property(__itemizedlist.value, __itemizedlist.set, None, '')

    
    # Element orderedlist uses Python identifier orderedlist
    __orderedlist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'orderedlist'), 'orderedlist', '__emlecoinformatics_orgtext_2_1_1_CTD_ANON_3_orderedlist', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 385, 14), )

    
    orderedlist = property(__orderedlist.value, __orderedlist.set, None, '')

    _ElementMap.update({
        __para.name() : __para,
        __itemizedlist.name() : __itemizedlist,
        __orderedlist.name() : __orderedlist
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type {eml://ecoinformatics.org/text-2.1.1}SubSuperScriptType with content type MIXED
class SubSuperScriptType (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SubSuperScriptType')
    _XSDLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 404, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__emlecoinformatics_orgtext_2_1_1_SubSuperScriptType_value', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 417, 5), )

    
    value_ = property(__value.value, __value.set, None, '')

    
    # Element subscript uses Python identifier subscript
    __subscript = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'subscript'), 'subscript', '__emlecoinformatics_orgtext_2_1_1_SubSuperScriptType_subscript', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 426, 6), )

    
    subscript = property(__subscript.value, __subscript.set, None, '')

    
    # Element superscript uses Python identifier superscript
    __superscript = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'superscript'), 'superscript', '__emlecoinformatics_orgtext_2_1_1_SubSuperScriptType_superscript', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 436, 6), )

    
    superscript = property(__superscript.value, __superscript.set, None, '')

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__emlecoinformatics_orgtext_2_1_1_SubSuperScriptType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 447, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        __value.name() : __value,
        __subscript.name() : __subscript,
        __superscript.name() : __superscript
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })
_module_typeBindings.SubSuperScriptType = SubSuperScriptType
Namespace.addCategoryObject('typeBinding', 'SubSuperScriptType', SubSuperScriptType)


# Complex type {eml://ecoinformatics.org/text-2.1.1}i18nString with content type SIMPLE
class i18nString (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'i18nString')
    _XSDLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 450, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__emlecoinformatics_orgtext_2_1_1_i18nString_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 460, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })
_module_typeBindings.i18nString = i18nString
Namespace.addCategoryObject('typeBinding', 'i18nString', i18nString)


text = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'text'), TextType, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 77, 2))
Namespace.addCategoryObject('elementBinding', text.name().localName(), text)



TextType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'section'), SectionType, scope=TextType, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 104, 6)))

TextType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'para'), ParagraphType, scope=TextType, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 116, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 104, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 116, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TextType._UseForTag(pyxb.namespace.ExpandedName(None, 'section')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 104, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TextType._UseForTag(pyxb.namespace.ExpandedName(None, 'para')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 116, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TextType._Automaton = _BuildAutomaton()




ParagraphType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), i18nString, scope=ParagraphType, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 148, 2)))

ParagraphType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'itemizedlist'), ListType, scope=ParagraphType, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 157, 6)))

ParagraphType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'orderedlist'), ListType, scope=ParagraphType, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 170, 6)))

ParagraphType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'emphasis'), CTD_ANON, scope=ParagraphType, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 183, 6)))

ParagraphType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'subscript'), SubSuperScriptType, scope=ParagraphType, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 201, 6)))

ParagraphType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'superscript'), SubSuperScriptType, scope=ParagraphType, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 211, 6)))

ParagraphType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'literalLayout'), CTD_ANON_, scope=ParagraphType, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 221, 6)))

ParagraphType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ulink'), CTD_ANON_2, scope=ParagraphType, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 237, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 147, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 148, 2))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 237, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ParagraphType._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 148, 2))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ParagraphType._UseForTag(pyxb.namespace.ExpandedName(None, 'itemizedlist')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 157, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ParagraphType._UseForTag(pyxb.namespace.ExpandedName(None, 'orderedlist')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 170, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ParagraphType._UseForTag(pyxb.namespace.ExpandedName(None, 'emphasis')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 183, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ParagraphType._UseForTag(pyxb.namespace.ExpandedName(None, 'subscript')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 201, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ParagraphType._UseForTag(pyxb.namespace.ExpandedName(None, 'superscript')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 211, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ParagraphType._UseForTag(pyxb.namespace.ExpandedName(None, 'literalLayout')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 221, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ParagraphType._UseForTag(pyxb.namespace.ExpandedName(None, 'ulink')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 237, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ParagraphType._Automaton = _BuildAutomaton_()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), i18nString, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 196, 10)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 196, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 196, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_2()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), i18nString, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 233, 10)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 233, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 233, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_3()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'citetitle'), i18nString, scope=CTD_ANON_2, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 248, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 247, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'citetitle')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 248, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_4()




SectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'title'), i18nString, scope=SectionType, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 287, 6)))

SectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'para'), ParagraphType, scope=SectionType, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 299, 8)))

SectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'section'), SectionType, scope=SectionType, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 313, 8)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 287, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SectionType._UseForTag(pyxb.namespace.ExpandedName(None, 'title')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 287, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SectionType._UseForTag(pyxb.namespace.ExpandedName(None, 'para')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 299, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SectionType._UseForTag(pyxb.namespace.ExpandedName(None, 'section')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 313, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SectionType._Automaton = _BuildAutomaton_5()




ListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'listitem'), CTD_ANON_3, scope=ListType, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 342, 8)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ListType._UseForTag(pyxb.namespace.ExpandedName(None, 'listitem')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 342, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ListType._Automaton = _BuildAutomaton_6()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'para'), ParagraphType, scope=CTD_ANON_3, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 358, 14)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'itemizedlist'), ListType, scope=CTD_ANON_3, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 372, 14)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'orderedlist'), ListType, scope=CTD_ANON_3, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 385, 14)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'para')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 358, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'itemizedlist')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 372, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'orderedlist')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 385, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_7()




SubSuperScriptType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'value'), i18nString, scope=SubSuperScriptType, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 417, 5)))

SubSuperScriptType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'subscript'), SubSuperScriptType, scope=SubSuperScriptType, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 426, 6)))

SubSuperScriptType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'superscript'), SubSuperScriptType, scope=SubSuperScriptType, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 436, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 416, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 417, 5))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SubSuperScriptType._UseForTag(pyxb.namespace.ExpandedName(None, 'value')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 417, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SubSuperScriptType._UseForTag(pyxb.namespace.ExpandedName(None, 'subscript')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 426, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SubSuperScriptType._UseForTag(pyxb.namespace.ExpandedName(None, 'superscript')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml-text.xsd', 436, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SubSuperScriptType._Automaton = _BuildAutomaton_8()

