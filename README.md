# PDF and Office File Compression Tool

## Overview

This script is designed to compress PDF files and copy Office files (`.docx`, `.pptx`, `.xlsx`) within a specified folder. It compresses PDF files by utilizing the PyMuPDF library (`fitz`) and copies Office files directly without compression. The script outputs the compressed files into a subfolder named `compressed` within the specified folder and provides a log indicating the compression ratio for each processed file.

## Requirements

- Python 3.x
- PyMuPDF (`pip install PyMuPDF`)

## Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. **Install required Python packages**:
   ```bash
   pip install PyMuPDF
   ```

## Usage

1. **Run the script**:
   ```bash
   python your_script_name.py
   ```

2. **Provide the folder path** when prompted:
   - The script will ask for the path to the folder containing the files you want to compress.

3. **Check the `compressed` folder**:
   - The script creates a subfolder named `compressed` within the provided folder path. All compressed or copied files will be located there.

4. **Review the log**:
   - The script prints out the compression ratio for each file processed. For example, "example.pdf: Compressed by 25.32%".

## Functionality

- **PDF Compression**: Compresses PDF files by deflating the file size.
- **Office Files Handling**: Copies `.docx`, `.pptx`, and `.xlsx` files without compression.
- **Log Generation**: A log is generated indicating the compression ratio for each processed file.

## Code Explanation

- **compress_pdf(file_path, output_path)**: Compresses the PDF file at `file_path` and saves it to `output_path`.
- **copy_file(file_path, output_path)**: Copies any file from `file_path` to `output_path`.
- **get_compression_ratio(original_size, compressed_size)**: Calculates the compression ratio as a percentage.
- **compress_files_in_folder(folder_path)**: Processes all files in the specified folder, compressing PDFs and copying Office files, saving the results to a `compressed` subfolder.

## Example

```bash
Enter the folder path: /path/to/your/folder
```

### Italian Version

---

# Strumento di Compressione per PDF e File Office

## Panoramica

Questo script è progettato per comprimere i file PDF e copiare i file Office (`.docx`, `.pptx`, `.xlsx`) all'interno di una cartella specificata. Comprimi i file PDF utilizzando la libreria PyMuPDF (`fitz`) e copia direttamente i file Office senza compressione. Lo script salva i file compressi in una sottocartella chiamata `compressed` all'interno della cartella specificata e fornisce un log che indica il rapporto di compressione per ogni file elaborato.

## Requisiti

- Python 3.x
- PyMuPDF (`pip install PyMuPDF`)

## Installazione

1. **Clona il repository** (se applicabile):
   ```bash
   git clone https://github.com/tuoaccount/turoepository.git
   cd tuoepository
   ```

2. **Installa i pacchetti Python richiesti**:
   ```bash
   pip install PyMuPDF
   ```

## Utilizzo

1. **Esegui lo script**:
   ```bash
   python nome_script.py
   ```

2. **Fornisci il percorso della cartella** quando richiesto:
   - Lo script chiederà il percorso della cartella contenente i file che si desidera comprimere.

3. **Controlla la cartella `compressed`**:
   - Lo script crea una sottocartella chiamata `compressed` all'interno del percorso della cartella fornita. Tutti i file compressi o copiati saranno lì.

4. **Rivedi il log**:
   - Lo script visualizza il rapporto di compressione per ogni file elaborato. Ad esempio, "example.pdf: Compressed by 25.32%".

## Funzionalità

- **Compressione PDF**: Comprime i file PDF riducendone la dimensione.
- **Gestione File Office**: Copia i file `.docx`, `.pptx`, e `.xlsx` senza compressione.
- **Generazione Log**: Viene generato un log che indica il rapporto di compressione per ogni file elaborato.

## Spiegazione del Codice

- **compress_pdf(file_path, output_path)**: Comprimi il file PDF in `file_path` e salvalo in `output_path`.
- **copy_file(file_path, output_path)**: Copia qualsiasi file da `file_path` a `output_path`.
- **get_compression_ratio(original_size, compressed_size)**: Calcola il rapporto di compressione come percentuale.
- **compress_files_in_folder(folder_path)**: Elabora tutti i file nella cartella specificata, comprimendo i PDF e copiando i file Office, salvando i risultati in una sottocartella `compressed`.

## Esempio

```bash
Inserisci il percorso della cartella: /percorso/alla/cartella
```
