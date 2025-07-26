import PyPDF2
import os

def merge_pdfs(pdf_list, output_name="merged.pdf"):
    merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        if os.path.exists(pdf):
            merger.append(pdf)
        else:
            print(f"[!] File not found: {pdf}")
    merger.write(output_name)
    merger.close()
    print(f"[✔] Merged PDF saved as: {output_name}")

def split_pdf(input_pdf, output_folder="splits"):
    if not os.path.exists(input_pdf):
        print(f"[!] File not found: {input_pdf}")
        return

    reader = PyPDF2.PdfReader(input_pdf)
    num_pages = len(reader.pages)

    os.makedirs(output_folder, exist_ok=True)

    for i in range(num_pages):
        writer = PyPDF2.PdfWriter()
        writer.add_page(reader.pages[i])
        output_filename = os.path.join(output_folder, f"page_{i+1}.pdf")
        with open(output_filename, "wb") as f:
            writer.write(f)
        print(f"[+] Saved: {output_filename}")

    print(f"[✔] Split into {num_pages} pages.")

def main():
    print("🔧 PDF Tool")
    print("1. Merge PDFs")
    print("2. Split a PDF")
    choice = input("Choose an option (1/2): ")

    if choice == "1":
        print("\nEnter PDF filenames to merge (separated by commas):")
        files = input(">> ").strip().split(",")
        files = [f.strip() for f in files]
        output_name = input("Enter name for merged output file (default: merged.pdf): ") or "merged.pdf"
        merge_pdfs(files, output_name)

    elif choice == "2":
        file = input("Enter the PDF file to split: ").strip()
        output_folder = input("Enter output folder name (default: splits): ") or "splits"
        split_pdf(file, output_folder)

    else:
        print("[!] Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
