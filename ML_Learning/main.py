import kagglehub

# Download latest version
path = kagglehub.dataset_download("assmoede98/fruits")

print("Path to dataset files:", path)