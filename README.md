# basedata
This repo will capture the artefacts and workflow to establish the Base Data based on Wiki Voyage.
Currently, there are two packages:
  - wv_dump_main: download, decompress, and parse dump into raw articles
  - wv_article_parse_main: parse each individual locale article into sections files and create a dictionary that keeps track of available sections


Each package has defined functions as .py files

**Documentation**


WV Parsing Architecture Diagrams: Illustrates the components and the flow of the functions

Function Matrix: structured view of each function including: docstring, paramaters, return statement and out

The "code" directory includes notebooks with important code that will be used for the function logic. The key item in here is the notebook where the article download, decompression, and preprocessing is done.  It is a superset of the required code and will constitute the primary components for the wv_dump_main package

The "output_files" directory includes some of the outputs from the existing code that provide targets and examples of the dictionaries being created and other samples

Project Scope Document
https://docs.google.com/document/d/1LeIxokYXG38J8d-g1Sftg1wNMUT5BuQ2_kbAeTXUM2U
