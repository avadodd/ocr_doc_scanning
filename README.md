# ocr_doc_scanning
All scripts for preprocessing docx and pdf files and post processing raw text files from AWS textract

Pre-processing
1. lock_file_handling.py sends all the locked file to an error directory
2. naming convention script???
3. -----.py to send all the files through AWS bucket


Post-processing
1. split_docs.py splits raw text documents based on the first data on the table
2. find_specs.py finds the PD#, Series#, Position Title, and copies the text and pastes it in an html file
