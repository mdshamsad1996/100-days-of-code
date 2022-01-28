"""This module provide RP tree main module"""

from html import entities
import os
import pathlib
import sys
from sys import prefix

from debugpy import connect

PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "

class _TreeGenerator:
    def __init__(self, root_dir, dir_only):
        self._root_dir = pathlib.Path(root_dir)
        self._dir_only = dir_only
        self._tree = []
    
        
    def _build_tree(self):
        self._tree_head()
        self._tree_body(self._root_dir)
        return self._tree
    
    
    def _tree_head(self):
        self._tree.append(f"{self._root_dir}{os.sep}")
        self._tree.append(PIPE)
    
        
    def _tree_body(self,directory, prefix=""):
        entries = self._parse_entries(directory)
        entries_count = len(entries)
        for index,entry in enumerate(entries):
            connector = ELBOW if index == entries_count - 1 else TEE
            if entry.is_dir():
                self._add_directory(entry, index, entries_count, prefix, connector)
            else:
                self._add_file(entry,prefix, connector)
                
                
    def _parse_entries(self, directory):
        entries = directory.iterdir()
        if self._dir_only:
            entries = [entry for entry in entries if entry.is_dir()]
            return entries  
        entries = sorted(entries, key = lambda entry: entry.is_file())
        return entries
    
        
    def _add_directory(self, directory, index,  entries_count, prefix, connector):
        self._tree.append(f"{prefix}{connector}{directory.name}")
        if index != entries_count-1:
            prefix += PIPE_PREFIX
        else:
            prefix += SPACE_PREFIX
        self._tree_body(directory,prefix)
        self._tree.append(prefix.rstrip())
    
    
    def _add_file(self, file, prefix, connector):
        self._tree.append(f"{prefix}{connector}{file.name}")
        

class DirectoryTree:
    def __init__(self, root_dir, dir_only=False, output_file=sys.stdout) -> None:
        self.dir_only = dir_only
        self._generator = _TreeGenerator(root_dir, dir_only)
        self._output_file = output_file

               
    def generator(self):
        tree = self._generator._build_tree()
        if (self._output_file != sys.stdout):
            # Wrap the tree in mark down block
            tree.insert(0,"```")
            tree.append("```")
            self._output_file=open(
                self._output_file, mode="w", encoding="utf-8"
            )
        with self._output_file as stream:
            for entry in tree:
                print(entry, file=stream)
        