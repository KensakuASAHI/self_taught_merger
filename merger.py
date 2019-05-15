#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib

# Main program
def main():
    # Config: input python_ex???.py dir.
    target_dir = './self_taught/'
    
    # Output HTML header part
    print("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>The self taught programmer (python code)</title>
  <script src="https://cdn.rawgit.com/google/code-prettify/master/loader/run_prettify.js?lang=py&skin=sons-of-obsidian"></script>
  <style type="text/css">
    .codefont {font-family: Consolas, Menlo, "Liberation Mono", Courier, monospace}
  </style>
</head>
<body>""")
    
    # Output HTML body part
    for n in range(313):
        import_file(target_dir + 'python_ex' + str(n) + '.py', n)
    
    # Output HTML footer part
    print("""</body>
</html>""")

# Read a file and output HTML content part
def import_file(filename, n):
    # Read from file
    fp = open(filename, "r")
    contents = fp.read()
    fp.close()
    # Output file contetns
    name_part = pathlib.Path(filename).name
    print('<div id="fid' + str(n) + '">')
    print('  <p>' + name_part + '</p>')
    print('  <pre class="prettyprint linenums lang-py codefont">')
    print(contents)
    print('  </pre>')
    print('</div>')

if __name__ == '__main__':
    main()
