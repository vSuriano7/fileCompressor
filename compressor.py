import os
import fitz  # pip install PyMuPDF
from pathlib import Path
from shutil import copyfile

def compress_pdf(file_path, output_path):
    doc = fitz.open(file_path)
    doc.save(output_path, deflate=True)
    doc.close()

def copy_file(file_path, output_path):
    copyfile(file_path, output_path)

def get_compression_ratio(original_size, compressed_size):
    return (original_size - compressed_size) / original_size * 100

def compress_files_in_folder(folder_path):
    folder = Path(folder_path)
    compressed_folder = folder / 'compressed'
    compressed_folder.mkdir(exist_ok=True)
    
    log = []
    
    for file_path in folder.glob('*'):
        if file_path.is_file() and file_path.suffix.lower() in ['.pdf', '.docx', '.pptx', '.xlsx']:
            original_size = file_path.stat().st_size
            compressed_file_path = compressed_folder / file_path.name
            
            if file_path.suffix.lower() == '.pdf':
                temp_compressed_file_path = compressed_folder / (file_path.stem + '_compressed.pdf')
                compress_pdf(file_path, temp_compressed_file_path)
                compressed_size = temp_compressed_file_path.stat().st_size
                if compressed_size < original_size:
                    compressed_file_path = temp_compressed_file_path
                else:
                    compressed_file_path = compressed_folder / file_path.name
                    copy_file(file_path, compressed_file_path)
                    compressed_size = original_size
                    temp_compressed_file_path.unlink()  # Delete the temporary compressed file
            else:
                copy_file(file_path, compressed_file_path)
                compressed_size = original_size
            
            compression_ratio = get_compression_ratio(original_size, compressed_size)
            log.append(f'{file_path.name}: Compressed by {compression_ratio:.2f}%')
    
    return log

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ").strip()
    log = compress_files_in_folder(folder_path)
    for entry in log:
        print(entry)
