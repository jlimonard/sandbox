## Description

Aim of this repo is publish a CV on Github Pages.  
Content is in folder `docs`.  
Source files are of type `markdown` with a little `html`, mainly for lay out.

### pdf
[`utils/md2pdf.py`](utils/md2pdf.py) can transform the text into a `pdf`.
The Github Page displays a link to the downloadable pdf.

Creating a pdf requires a language parameter. Allowed: `en` and `nl`.  
Example call:
`python3 utils/md2pdf.py en`


## Install
See [`install.md`](install.md)
