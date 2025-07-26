import PyPDF2

def split_pdf(input_pdf, output_folder="splits"):
    reader = PyPDF2.PdfReader(input_pdf)
    num_pages = len(reader.pages)

    import os
    os.makedirs(output_folder, exist_ok=True)

    for i in range(num_pages):
        writer = PyPDF2.PdfWriter()
        writer.add_page(reader.pages[i])

        output_filename = f"{output_folder}/page_{i+1}.pdf"
        with open(output_filename, "wb") as f:
            writer.write(f)

        print(f"Saved: {output_filename}")

if __name__ == "__main__":
    split_pdf("file1.pdf")
