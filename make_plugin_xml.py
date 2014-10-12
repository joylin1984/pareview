'''
Substitute a string "__SCRIPT_PLACEHOLDER__" in the XML template file with the script 
preforming proper XML escaping.
Usage: python make_plugin_xml.py <xml_template> <script>
'''

import os
import sys
import inspect
import textwrap


def escapeForXmlAttribute(s):

    # http://www.w3.org/TR/2000/WD-xml-c14n-20000119.html#charescaping
    # In character data and attribute values, the character information items "<" and "&" are represented by "&lt;" and "&amp;" respectively.
    # In attribute values, the double-quote character information item (") is represented by "&quot;".
    # In attribute values, the character information items TAB (#x9), newline (#xA), and carriage-return (#xD) are represented by "&#x9;", "&#xA;", and "&#xD;" respectively.

    s = s.replace('&', '&amp;') # Must be done first!
    s = s.replace('<', '&lt;')
    s = s.replace('>', '&gt;')
    s = s.replace('"', '&quot;')
    s = s.replace('\r', '&#xD;')
    s = s.replace('\n', '&#xA;\n')
    s = s.replace('\t', '&#x9;')
    return s
  
def main():

    if len(sys.argv) != 3:
        print 'Usage: %s <xml_template> <script>' % sys.argv[0]
        sys.exit(1)

    
    xml_template_file=sys.argv[1]
    output_xml=xml_template_file.replace("_template","")
    with open(xml_template_file, "rt") as file:
        xml_template=file.read()
    with open(sys.argv[2], "rt") as file:
        script=file.read()

    xml_template=xml_template.replace("__SCRIPT_PLACEHOLDER__", escapeForXmlAttribute(script))
    with open(output_xml, "wt") as file:
        file.write(xml_template)
    

if __name__ == '__main__':
    main()  
  
