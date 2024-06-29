"""
About:
------

The sina_transliterate tool allows you to transliterate text using the SinaTools' utility. This command-line utility
takes in a text and a desired schema, and outputs the transliterated text.

Usage:
------
Below is the usage information that can be generated by running sina_transliterate --help.

    Usage:
    ------

.. code-block:: none

        sina_transliterate --text=TEXT --schema=SCHEMA

        sina_transliterate --file=FILE --schema=SCHEMA

Options:
--------

.. code-block:: none

  --text TEXT
        Text to be transliterated.
  --schema SCHEMA
        Transliteration schema to be used, which is bw2ar or ar2bw.

Examples:
---------

.. code-block:: none

    sina_transliterate --text "klmp" --schema "bw2ar"
    sina_transliterate --file "path/to/your/file.txt" --schema "ar2bw"

Note:
-----

.. code-block:: none

    For available transliteration schemas and more details, please refer to the SinaTools' documentation or the source code 
    of the function `perform_transliteration`.

"""
import argparse
from sinatools.utils.text_transliteration import perform_transliteration
from sinatools.utils.readfile import read_file

def main():
    parser = argparse.ArgumentParser(description='Perform text transliteration using SinaTools')
    
    # Adding arguments for the text, file, and schema
    parser.add_argument('--text', type=str, help='Text to be transliterated')
    parser.add_argument('--file', type=str, help='File containing the text to be transliterated')
    parser.add_argument('--schema', type=str, required=True, help='Transliteration schema to be used')

    args = parser.parse_args()

    # Check if either text or file is provided
    if args.text is None and args.file is None:
        print("Either --text or --file argument must be provided.")
        return

    text_content = args.text if args.text else " ".join(read_file(args.file))
    # Perform transliteration
    result = perform_transliteration(text_content, args.schema)
    
    print(result)

if __name__ == '__main__':
    main()

#sina_transliterate --text "example text" --schema "bw2ar"
#sina_transliterate --file "path/to/your/file.txt" --schema "bw2ar"