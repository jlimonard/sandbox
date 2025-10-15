import argparse
from pathlib import Path

import pypandoc


def toggle_pdf_link_line(index_file_path: str, action: str) -> None:
    LINE_PDF_LINK: str = "This page as [pdf](https://github.com/jlimonard/sandbox/blob/main/pdf/resumé-jlimonard.pdf)."

    with open(index_file_path, "r") as f_reader:
        lines = f_reader.readlines()

    if action == "DELETE":
        # remove the line that contains ...This page as [pdf] ...
        with open(index_file_path, "w") as f_writer:
            for line in lines:
                if LINE_PDF_LINK not in line:
                    f_writer.write(line)
    elif action == "ADD":
        # add the line that contains ...This page as [pdf] ...
        with open(index_file_path, "a") as f_writer2:  # a = append
            f_writer2.write(LINE_PDF_LINK)


def make_pdf():
    parser = argparse.ArgumentParser(description="..")
    parser.add_argument("language", type=str, help="allowed: nl|en")
    args = parser.parse_args()
    language: str = args.language

    if language == "en":
        index_md: str = "index.md"
        pdf_file: str = "resumé-jlimonard.pdf"
    elif language == "nl":
        index_md: str = "index_nl.md"
        pdf_file: str = "resumé-jlimonard-nl.pdf"

    index_file_name: str = f"docs/{index_md}"
    markdown_file: Path = Path(index_file_name).absolute()
    target_pdf_file: Path = Path(f"pdf/{pdf_file}").absolute()

    # delete line that has this page as pdf
    toggle_pdf_link_line(index_file_name, "DELETE")

    # Convert the index.md to pdf
    _: str = pypandoc.convert_file(
        source_file=markdown_file,
        to="pdf",
        outputfile=target_pdf_file,
        extra_args=[
            "--pdf-engine=xelatex",
        ],
    )
    # re add line that has this page as pdf
    toggle_pdf_link_line(index_file_name, "ADD")

    print("Conversion to pdf completed!")


if __name__ == "__main__":
    make_pdf()
