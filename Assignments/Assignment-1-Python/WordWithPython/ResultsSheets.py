import os, sys  # Standard Python Libraries
import xlwings as xw  # pip install xlwings
from docxtpl import DocxTemplate  # pip install docxtpl
import win32com.client as win32  # pip install pywin32

# -- Documentation:
# python-docx-template: https://docxtpl.readthedocs.io/en/latest/

# Change path to current working directory
os.chdir(sys.path[0])



def convert_to_pdf(doc):
    """Convert given word document to pdf"""
    word = win32.DispatchEx("Word.Application")
    new_name = doc.replace(".docx", r".pdf")
    worddoc = word.Documents.Open(doc)
    worddoc.SaveAs(new_name, FileFormat=17)
    worddoc.Close()
    return None


def main():
    wb = xw.Book.caller()
    xl_sheet = wb.sheets["StudentResults"]
    doc = DocxTemplate("PythonForm.docx")
    
    # -- Get values from Excel
    contexts = xl_sheet.range("A2").options(dict, expand="table", numbers=int).value

    for context in contexts:
        print(context)
        data = {'StudentName':'This', 'Knumber':' That'}

        output_name = f'test_Report_{context}.docx'
        print(output_name)
        doc.render(data)
        doc.save(output_name)


    # -- Convert to PDF [OPTIONAL]
        #path_to_word_document = os.path.join(os.getcwd(), output_name)
        #convert_to_pdf(path_to_word_document)    


    # -- Render & Save Word Document
#    output_name = f'test_Report_{context["StudentName"]}.docx'
#    output_name = f'test_Report_test.docx'
#    doc.render(context)
#    doc.save(output_name)



if __name__ == "__main__":
    xw.Book("StudentNames.xlsx").set_mock_caller()
    main()