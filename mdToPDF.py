from pathlib import Path

from markdown import markdown
from weasyprint import CSS, HTML

md_README_path = Path("README.md")
md_naudojimo_Instrucija_path = Path("Naudojimo_Instrucija.md")
md_programuotojo_Instrucija_path = Path("Programuotojo_Instrucija.md")
pdf_path = Path("README.pdf")
css_path = Path("src/css/mdfile.css")


def makeMDtoPDF(md_path: Path, css_path: Path):
    print()
    md_text = md_path.read_text(encoding="utf-8")

    html_body = markdown(
        md_text, extensions=["fenced_code", "tables", "toc", "codehilite"]
    )

    html = f"""<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
    {html_body}
    </body>
    </html>
    """

    HTML(string=html, base_url=md_path.parent).write_pdf(
        Path("docs") / md_path.with_suffix(".pdf").name,
        stylesheets=[CSS(filename=css_path)],
    )


makeMDtoPDF(md_README_path, css_path)
makeMDtoPDF(md_naudojimo_Instrucija_path, css_path)
# makeMDtoPDF(md_programuotojo_Instrucija_path, css_path)
