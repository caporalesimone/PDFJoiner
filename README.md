# PDF Joiner

This app merges 2 PDFs. First contains odd pages, second contains even pages but from latest to the first.

## Requirements:
- All pages should be merged alternatively starting from `pdf1`.
- All the pages of `pdf2` should be taken starting from the latest.
- All pages of `pdf1` should be taken starting from the first.
- Print the number of pages of `pdf1`, `pdf2`, and the `sum` of the pages.
- If the total pages number is odd, add a blank page.
- After `pdf1` is finished, add all the reamaining pages of pdf2.
- If pdf2 has lessa pages than `pdf1`, add the remaining pages of `pdf1`.
- Print a warning message if the pages of `pdf1` are less than pdf2.
- Get `pdf1`, `pdf2`, output as command line parameters.
- Use `pypdf` library.

## Install dependency:
```
$ pip install pypdf
```

## Usage example:
```Usage example:
$ python pdf_joiner.py --pdf1 pdf1.pdf --pdf2 pdf2.pdf --output output.pdf
```

## Output example:
```
$ python pdf_joiner.py --pdf1 pdf1.pdf --pdf2 pdf2.pdf --output output.pdf
PDF 1: pdf1.pdf has 18 pages.
PDF 2: pdf2.pdf has 18 pages.
output.pdf PDF will have 36 pages.
output.pdf written.
```

## Notes:
This app has been written with the help of [ChatGPT](https://openai.com/blog/chatgpt/) with an elementay Python knowledge.