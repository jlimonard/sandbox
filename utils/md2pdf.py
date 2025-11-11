import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import tempfile

import pypandoc


@dataclass
class LanguageConfig:
    """Configuration for a specific language."""

    input_file_md: str
    output_file_pdf: str


# Language configurations
LANGUAGE_CONFIGS = {
    "en": LanguageConfig(input_file_md="index.md", output_file_pdf="resumé-jlimonard.pdf"),
    "nl": LanguageConfig(input_file_md="index_nl.md", output_file_pdf="resumé-jlimonard-nl.pdf"),
}


def remove_header_footer(markdown_content: str) -> str:
    """Remove <header> and <footer> tags and their content.
    re.DOTALL: match any character including newlines
    """
    # Remove <header>...</header> (case-insensitive, multiline)
    content = re.sub(r"<header>.*?</header>", "", markdown_content, flags=re.IGNORECASE | re.DOTALL)
    # Remove <footer>...</footer> (case-insensitive, multiline)
    content = re.sub(r"<footer>.*?</footer>", "", content, flags=re.IGNORECASE | re.DOTALL)
    return content


def make_pdf() -> None:
    parser = argparse.ArgumentParser(description="..")
    parser.add_argument("language", type=str, default="en", help="allowed: en|nl")
    args = parser.parse_args()
    language: str = args.language

    # Get configuration for the selected language
    config = LANGUAGE_CONFIGS[language]

    markdown_file: Path = Path(f"docs/{config.input_file_md}").absolute()
    pdf_file: Path = Path(f"pdf/{config.output_file_pdf}").absolute()

    content: str = markdown_file.read_text(encoding="utf-8")
    # Remove header (laguage selection) and footer (pdf link) from the markdown - makes no sense in the pdf
    cleaned_content: str = remove_header_footer(content)
    # Write cleaned content to a temporary file (required by pypandoc.convert_file (arg source_file))
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", delete=False, encoding="utf-8"
    ) as temp_file:
        temp_file.write(cleaned_content)
        temp_file_path = temp_file.name

    try:
        _: str = pypandoc.convert_file(
            source_file=temp_file_path,
            to="pdf",
            outputfile=pdf_file,
            extra_args=[
                "--pdf-engine=xelatex",
            ],
        )
        print(f"Conversion to pdf completed (language used: {language})!")
    finally:
        # Clean up temporary cleaned_content file
        Path(temp_file_path).unlink()


if __name__ == "__main__":
    make_pdf()
