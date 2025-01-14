# WARNING: The convert command is deprecated in IMv7, use "magick" instead of "convert" or "magick convert"
#!/bin/bash

# Check if directory argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory_path>"
    exit 1
fi

# Store directory path and create compressed directory path
INPUT_DIR="${1%/}"  # Remove trailing slash if present
COMPRESSED_DIR="${INPUT_DIR}_compressed"

# Check if input directory exists
if [ ! -d "$INPUT_DIR" ]; then
    echo "Error: Directory '$INPUT_DIR' does not exist"
    exit 1
fi

# Create compressed directory
mkdir -p "$COMPRESSED_DIR"

# Copy directory structure
find "$INPUT_DIR" -type d -print0 | while IFS= read -r -d '' dir; do
    # Get relative path
    rel_path="${dir#$INPUT_DIR}"
    if [ -n "$rel_path" ]; then
        mkdir -p "$COMPRESSED_DIR$rel_path"
    fi
done

# Process video files
echo "Processing video files..."
find "$INPUT_DIR" -type f \( -name "*.mp4" -o -name "*.avi" -o -name "*.mov" -o -name "*.mkv" \) -print0 | while IFS= read -r -d '' video; do
    # Get relative path
    rel_path="${video#$INPUT_DIR}"
    output_path="$COMPRESSED_DIR$rel_path"
    
    # Create output directory if it doesn't exist
    mkdir -p "$(dirname "$output_path")"
    
    echo "Compressing: $rel_path"
    ffmpeg -i "$video" -vcodec libx264 -crf 23 "${output_path%.*}.mp4" -y 2>/dev/null
done

# Process image files
echo -e "\nProcessing image files..."
find "$INPUT_DIR" -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.gif" \) -print0 | while IFS= read -r -d '' image; do
    # Get relative path
    rel_path="${image#$INPUT_DIR}"
    output_path="$COMPRESSED_DIR$rel_path"
    
    # Create output directory if it doesn't exist
    mkdir -p "$(dirname "$output_path")"
    
    echo "Converting: $rel_path"
    convert "$image" -resize 600x -quality 90 "${output_path%.*}.png"
done

echo -e "\nProcessing complete! Check '${COMPRESSED_DIR}' for processed files." 