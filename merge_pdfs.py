import PyPDF2
import os

def merge_pdfs(pdf_list, output_name="merged.pdf"):
    merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        if os.path.exists(pdf):
            merger.append(pdf)
        else:
            print(f"File not found: {pdf}")

    merger.write(output_name)
    merger.close()
    print(f"Merged PDF saved as: {output_name}")

if __name__ == "__main__":
    # Example usage
    files_to_merge = ["file1.pdf", "file2.pdf"]
    merge_pdfs(files_to_merge)
