"""Genera un PDF simple a partir de `DOCUMENTO_PROYECTO.md` usando ReportLab.

El PDF se guardará como `DOCUMENTO_PROYECTO.pdf` en la raíz del proyecto.
"""
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def md_to_paragraphs(md_text):
    # Conversión sencilla: trata encabezados (#) como texto en negrita implícito
    lines = md_text.splitlines()
    paras = []
    for line in lines:
        line = line.rstrip()
        if not line:
            paras.append(('spacer', None))
            continue
        # Remove markdown list markers
        if line.startswith('- '):
            line = '• ' + line[2:]
        # Simplistic header handling
        if line.startswith('#'):
            # remove leading # and add bold markers (ReportLab Paragraph supports <b>)
            text = line.lstrip('#').strip()
            paras.append(('para', f'<b>{text}</b>'))
        else:
            paras.append(('para', line))
    return paras


def generate_pdf(md_path='DOCUMENTO_PROYECTO.md', out_pdf='DOCUMENTO_PROYECTO.pdf'):
    with open(md_path, 'r', encoding='utf-8') as f:
        md = f.read()

    doc = SimpleDocTemplate(out_pdf, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    for kind, content in md_to_paragraphs(md):
        if kind == 'spacer':
            story.append(Spacer(1, 8))
        else:
            story.append(Paragraph(content.replace('&', '&amp;'), styles['Normal']))
    doc.build(story)
    print(f'PDF generado: {out_pdf}')


if __name__ == '__main__':
    generate_pdf()
