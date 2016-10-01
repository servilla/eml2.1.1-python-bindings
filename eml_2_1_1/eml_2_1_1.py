# ./eml_2_1_1.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:5649f4a30ae08b752015291fb9d9e7bb610d52b9
# Generated 2016-09-30 11:49:56.014584 by PyXB version 1.2.5 using Python 3.5.2.final.0
# Namespace eml://ecoinformatics.org/eml-2.1.1

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
import pyxb.binding.datatypes
import pyxb.binding.xml_

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('eml://ecoinformatics.org/eml-2.1.1', create_if_missing=True)
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


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 235, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 116, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element access uses Python identifier access
    __access = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'access'), 'access', '__emlecoinformatics_orgeml_2_1_1_CTD_ANON__access', False, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 118, 8), )

    
    access = property(__access.value, __access.set, None, '')

    
    # Element dataset uses Python identifier dataset
    __dataset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dataset'), 'dataset', '__emlecoinformatics_orgeml_2_1_1_CTD_ANON__dataset', False, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 128, 10), )

    
    dataset = property(__dataset.value, __dataset.set, None, '')

    
    # Element citation uses Python identifier citation
    __citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'citation'), 'citation', '__emlecoinformatics_orgeml_2_1_1_CTD_ANON__citation', False, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 141, 10), )

    
    citation = property(__citation.value, __citation.set, None, '')

    
    # Element software uses Python identifier software
    __software = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'software'), 'software', '__emlecoinformatics_orgeml_2_1_1_CTD_ANON__software', False, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 153, 10), )

    
    software = property(__software.value, __software.set, None, '')

    
    # Element protocol uses Python identifier protocol
    __protocol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'protocol'), 'protocol', '__emlecoinformatics_orgeml_2_1_1_CTD_ANON__protocol', False, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 166, 10), )

    
    protocol = property(__protocol.value, __protocol.set, None, '')

    
    # Element additionalMetadata uses Python identifier additionalMetadata
    __additionalMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'additionalMetadata'), 'additionalMetadata', '__emlecoinformatics_orgeml_2_1_1_CTD_ANON__additionalMetadata', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 179, 8), )

    
    additionalMetadata = property(__additionalMetadata.value, __additionalMetadata.set, None, '')

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__emlecoinformatics_orgeml_2_1_1_CTD_ANON__httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 295, 6)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute packageId uses Python identifier packageId
    __packageId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'packageId'), 'packageId', '__emlecoinformatics_orgeml_2_1_1_CTD_ANON__packageId', pyxb.binding.datatypes.string, required=True)
    __packageId._DeclarationLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 266, 6)
    __packageId._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 266, 6)
    
    packageId = property(__packageId.value, __packageId.set, None, '')

    
    # Attribute system uses Python identifier system
    __system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'system'), 'system', '__emlecoinformatics_orgeml_2_1_1_CTD_ANON__system', _ImportedBinding__nsgroup.SystemType, required=True)
    __system._DeclarationLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 280, 6)
    __system._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 280, 6)
    
    system = property(__system.value, __system.set, None, None)

    
    # Attribute scope uses Python identifier scope
    __scope = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'scope'), 'scope', '__emlecoinformatics_orgeml_2_1_1_CTD_ANON__scope', _ImportedBinding__nsgroup.ScopeType, fixed=True, unicode_default='system')
    __scope._DeclarationLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 281, 6)
    __scope._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 281, 6)
    
    scope = property(__scope.value, __scope.set, None, '')

    _ElementMap.update({
        __access.name() : __access,
        __dataset.name() : __dataset,
        __citation.name() : __citation,
        __software.name() : __software,
        __protocol.name() : __protocol,
        __additionalMetadata.name() : __additionalMetadata
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __packageId.name() : __packageId,
        __system.name() : __system,
        __scope.name() : __scope
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 193, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element describes uses Python identifier describes
    __describes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'describes'), 'describes', '__emlecoinformatics_orgeml_2_1_1_CTD_ANON_2_describes', True, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 195, 14), )

    
    describes = property(__describes.value, __describes.set, None, '')

    
    # Element metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'metadata'), 'metadata', '__emlecoinformatics_orgeml_2_1_1_CTD_ANON_2_metadata', False, pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 212, 14), )

    
    metadata = property(__metadata.value, __metadata.set, None, '')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__emlecoinformatics_orgeml_2_1_1_CTD_ANON_2_id', _ImportedBinding__nsgroup.IDType)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 262, 12)
    __id._UseLocation = pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 262, 12)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __describes.name() : __describes,
        __metadata.name() : __metadata
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


eml = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eml'), CTD_ANON_, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 96, 2))
Namespace.addCategoryObject('elementBinding', eml.name().localName(), eml)



def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 237, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'access'), _ImportedBinding__nsgroup.AccessType, scope=CTD_ANON_, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 118, 8)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dataset'), _ImportedBinding__nsgroup.DatasetType, scope=CTD_ANON_, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 128, 10)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'citation'), _ImportedBinding__nsgroup.CitationType, scope=CTD_ANON_, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 141, 10)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'software'), _ImportedBinding__nsgroup.SoftwareType, scope=CTD_ANON_, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 153, 10)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'protocol'), _ImportedBinding__nsgroup.ProtocolType, scope=CTD_ANON_, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 166, 10)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'additionalMetadata'), CTD_ANON_2, scope=CTD_ANON_, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 179, 8)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 118, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 179, 8))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'access')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 118, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'dataset')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 128, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'citation')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 141, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'software')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 153, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'protocol')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 166, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'additionalMetadata')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 179, 8))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'describes'), _ImportedBinding__nsgroup.NonEmptyStringType, scope=CTD_ANON_2, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 195, 14)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'metadata'), CTD_ANON, scope=CTD_ANON_2, documentation='', location=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 212, 14)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 195, 14))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'describes')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 195, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'metadata')), pyxb.utils.utility.Location('/home/servilla/python/3.5/eml2.1.1/schema/eml.xsd', 212, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()

