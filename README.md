# CSV2QTI
CSV converter to TAO QTI Package
--------------------------------

This project aims to generate TAO QTI Package from a CSV file.

The CSV file must conform to specific structure:

`question_text, correct_answer_index, answers...`

Example of a question in the CSV file:

`"What is opposite of 'Yes'","2","Maybe","No","Never"`

# Usage

See the full documentation with `-h` flag.

`CSV2QTI -h`

Basic usage

`CSV2QTI geography.csv geography Geography_Basic`

This will output a `geography.zip` file which can be imported in TAO as QTI Package

Usage with `tab` set as delimiter and `"` as quote character

`CSV2QTI geography.csv geography Geography_Basic --delimiter='\t' --quotechar='"'`
