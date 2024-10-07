from unittest import TestCase

import tree_sitter_zsh

import tree_sitter


class TestLanguage(TestCase):
    def test_can_load_grammar(self):
        try:
            tree_sitter.Language(tree_sitter_zsh.language())
        except Exception:
            self.fail("Error loading Zsh grammar")
