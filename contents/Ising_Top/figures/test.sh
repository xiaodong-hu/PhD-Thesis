#!/bin/bash

# Directory containing EPS files
INPUT_DIR="/home/hxd/Dropbox/PhD-Thesis/contents/Ising_Top/figures"

# Check if Inkscape is installed
if ! command -v inkscape &> /dev/null
then
    echo "Inkscape could not be found. Please install it and try again."
    exit 1
fi

# Create output directory if it doesn't exist
OUTPUT_DIR="${INPUT_DIR}/pdf_files"
mkdir -p "$OUTPUT_DIR"

# Loop through all EPS files in the input directory
for eps_file in "$INPUT_DIR"/*.eps
do
    # Get the base name of the file (without path and extension)
    base_name=$(basename "$eps_file" .eps)
    
    # Define the output PDF file path
    pdf_file="${OUTPUT_DIR}/${base_name}.pdf"
    
    # Convert EPS to PDF using Inkscape
    inkscape "$eps_file" --export-filename="$pdf_file"
    
    # Check if the conversion was successful
    if [ $? -eq 0 ]; then
        echo "Successfully converted: $eps_file to $pdf_file"
    else
        echo "Failed to convert: $eps_file"
    fi
done

echo "Conversion process completed."

