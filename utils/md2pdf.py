import pypandoc
from pathlib import Path

INDEX_MD: str = "docs/index.md"

source_markdown_file: Path = Path(INDEX_MD).absolute()
target_pdf_file: Path = Path("pdf/resumé-jlimonard.pdf").absolute()


def toggle_pdf_link_line(action: str) -> None:
    file_path = INDEX_MD
    LINE_PDF_LINK: str = (
        "This page as [pdf](https://github.com/jlimonard/sandbox/blob/main/pdf/resumé-jlimonard.pdf)."
    )

    with open(file_path, "r") as f_reader:
        lines = f_reader.readlines()

    if action == "DELETE":
        # remove the line that contains ...This page as [pdf] ...
        with open(file_path, "w") as f_writer:
            for line in lines:
                if LINE_PDF_LINK not in line:
                    f_writer.write(line)
    elif action == "ADD":
        # add the line that contains ...This page as [pdf] ...
        with open(file_path, "a") as f_writer2:  # a = append
            f_writer2.write(LINE_PDF_LINK)


# delete line that has this page as pdf
toggle_pdf_link_line("DELETE")

# Convert the index.md to pdf
output: str = pypandoc.convert_file(
    source_file=source_markdown_file,
    to="pdf",
    outputfile=target_pdf_file,
    extra_args=[
        "--pdf-engine=xelatex",
    ],
)
# re add line that has this page as pdf
toggle_pdf_link_line("ADD")

print("Conversion to pdf completed!")
