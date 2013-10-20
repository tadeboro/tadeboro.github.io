#!/bin/bash

cat tmpl-head.html > index.html
Markdown.pl index.md >> index.html
cat tmpl-tail.html >> index.html

exit 0
