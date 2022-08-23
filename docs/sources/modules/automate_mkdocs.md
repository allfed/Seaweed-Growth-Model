#


### add_val
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/automate_mkdocs.py/#L12)
```python
.add_val(
   indices, value, data
)
```


----


### automate_mkdocs_from_docstring
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/automate_mkdocs.py/#L21)
```python
.automate_mkdocs_from_docstring(
   mkdocs_dir: Union[str, Path], mkgendocs_f: str, repo_dir: Path,
   match_string: str
)
```

---
Automates the -pages for mkgendocs package by adding all Python functions in a
directory to the mkgendocs config.

**Args**

* **mkdocs_dir** (typing.Union[str, pathlib.Path]) : textual directory for
* **mkgendocs_f** (str) : The configurations file for the mkgendocs package
* **repo_dir** (pathlib.Path) : textual directory to search for Python functions in
* **match_string** (str) : the text to be matches, after which the functions will be
the hierarchical directory & navigation in Mkdocs
added in mkgendocs format

**Example**


```python

>>> automate_mkdocs_from_docstring('scripts', repo_dir=Path.cwd(), match_string='pages:')
```

**Returns**

* **list**  : list of created markdown files and their relative paths


----


### automate_nav_structure
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/automate_mkdocs.py/#L129)
```python
.automate_nav_structure(
   mkdocs_dir: Union[str, Path], mkdocs_f: str, repo_dir: Path, match_string: str,
   structure: dict
)
```

---
Automates the -pages for mkgendocs package by adding all Python
functions in a directory to the mkgendocs config.

**Args**

* **mkdocs_dir** (typing.Union[str, pathlib.Path]) : textual directory for
* **mkgendocs_f** (str) : The configurations file for the mkgendocs package
* **repo_dir** (pathlib.Path) : textual directory to search for Python functions in
* **match_string** (str) : the text to be matches, after which the functions
the hierarchical directory & navigation in Mkdocs
will be added in mkgendocs format

**Example**


```python

>>> automate_mkdocs_from_docstring('scripts', repo_dir=Path.cwd(), match_string='pages:')
```

**Returns**

* **str**  : feedback message


----


### fix
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/automate_mkdocs.py/#L173)
```python
.fix(
   f
)
```

---
Allows creation of arbitrary length dict item


**Args**

* **f** (type) : Description of parameter `f`.


**Returns**

* **type**  : Description of returned object.


----


### indent
[source](https://github.com/allfed/Seaweed-Growth-Model/blob/master/automate_mkdocs.py/#L186)
```python
.indent(
   string: str
)
```

---
Count the indentation in whitespace characters.

**Args**

* **string** (str) : text with indents


**Returns**

* **int**  : Number of whitespace indentations

