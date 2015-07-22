import unittest

import aioxmpp.entitycaps.xso as entitycaps_xso
import aioxmpp.stanza as stanza
import aioxmpp.xso as xso

from aioxmpp.utils import namespaces


class TestNamespaces(unittest.TestCase):
    def test_caps(self):
        self.assertEqual(
            namespaces.xep0115_caps,
            "http://jabber.org/protocol/caps"
        )


class TestCaps(unittest.TestCase):
    def test_is_xso(self):
        self.assertTrue(issubclass(
            entitycaps_xso.Caps,
            xso.XSO
        ))

    def test_tag(self):
        self.assertEqual(
            (namespaces.xep0115_caps, "c"),
            entitycaps_xso.Caps.TAG
        )

    def test_node_attr(self):
        self.assertIsInstance(
            entitycaps_xso.Caps.node,
            xso.Attr
        )
        self.assertEqual(
            (None, "node"),
            entitycaps_xso.Caps.node.tag
        )
        self.assertTrue(
            entitycaps_xso.Caps.node.required
        )

    def test_hash_attr(self):
        self.assertIsInstance(
            entitycaps_xso.Caps.hash_,
            xso.Attr
        )
        self.assertEqual(
            (None, "hash"),
            entitycaps_xso.Caps.hash_.tag
        )
        self.assertTrue(
            entitycaps_xso.Caps.hash_.required
        )
        self.assertIsInstance(
            entitycaps_xso.Caps.hash_.validator,
            xso.Nmtoken
        )
        self.assertEqual(
            xso.ValidateMode.FROM_CODE,
            entitycaps_xso.Caps.hash_.validate
        )

    def test_ver_attr(self):
        self.assertIsInstance(
            entitycaps_xso.Caps.ver,
            xso.Attr
        )
        self.assertEqual(
            (None, "ver"),
            entitycaps_xso.Caps.ver.tag
        )
        self.assertTrue(
            entitycaps_xso.Caps.ver.required
        )

    def test_ext_attr(self):
        self.assertIsInstance(
            entitycaps_xso.Caps.ext,
            xso.Attr
        )
        self.assertEqual(
            (None, "ext"),
            entitycaps_xso.Caps.ext.tag
        )

    def test_attr_on_Presence(self):
        self.assertIsInstance(
            stanza.Presence.xep0115_caps,
            xso.Child,
        )
        self.assertSetEqual(
            {
                entitycaps_xso.Caps
            },
            set(stanza.Presence.xep0115_caps._classes)
        )