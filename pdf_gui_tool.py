import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import os

class PDFToolApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger & Splitter")
        self.root.geometry("400x300")

        # Buttons
        tk.Button(root, text="Merge PDFs", width=20, command=self.merge_pdfs).pack(pady=15)
        tk.Button(root, text="Split a PDF", width=20, command=self.split_pdf).pack(pady=15)

        # Status
        self.status = tk.Label(root, text="", fg="green")
        self.status.pack(pady=20)

    def merge_pdfs(self):
        files = filedialog.askopenfilenames(title="Select PDFs to Merge", filetypes=[("PDF Files", "*.pdf")])
        if not files:
            return

        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", title="Save Merged PDF As")
        if not output_file:
            return

        try:
            merger = PyPDF2.PdfMerger()
            for file in files:
                merger.append(file)
            merger.write(output_file)
            merger.close()
            self.status.config(text=f"Merged PDF saved at:\n{output_file}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def split_pdf(self):
        file = filedialog.askopenfilename(title="Select a PDF to Split", filetypes=[("PDF Files", "*.pdf")])
        if not file:
            return

        output_dir = filedialog.askdirectory(title="Select Output Folder for Split Pages")
        if not output_dir:
            return

        try:
            reader = PyPDF2.PdfReader(file)
            for i in range(len(reader.pages)):
                writer = PyPDF2.PdfWriter()
                writer.add_page(reader.pages[i])
                output_path = os.path.join(output_dir, f"page_{i+1}.pdf")
                with open(output_path, "wb") as f:
                    writer.write(f)
            self.status.config(text=f"Split into {len(reader.pages)} pages.\nSaved in:\n{output_dir}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFToolApp(root)
    root.mainloop()
