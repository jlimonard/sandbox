import pypandoc
from pathlib import Path

# Download pandoc if not already installed
# pypandoc.download_pandoc()

source_markdown_file: Path = Path("docs/README.md").absolute()
target_pdf_file: Path = Path("pdf/resumé-jlimonard.pdf").absolute()

# Convert the README.md to PDF
output: str = pypandoc.convert_file(
    source_file=source_markdown_file,
    to="pdf",
    outputfile=target_pdf_file,
    extra_args=[
        "--pdf-engine=xelatex",
    ],
)

print("Conversion to pdf completed!")