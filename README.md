# tesseract-python
Examples to implement OCR(Optical Character Recognition) using tesseract using Python

## Installation:
- Install tesserct-ocr using this command:
    - On Ubuntu
      ```
      sudo apt-get install tesseract-ocr
      ```
    - On Mac
      ```
      brew install tesseract
      ```
    - On Windows, download installer from [here](https://github.com/UB-Mannheim/tesseract/wiki)


- Install python binding for tesseract, pytesseract, using this pip command:
  ```
  pip install pytesseract
  ```

- Install image processing library in python, pillow using this pip command:
  ```
  pip install pillow
  ```
  
**For working with pdf files:**
- Install imagemagick using this command:
    - On Ubuntu
      ```
      sudo apt-get install imagemagick
      ```
    - For other platforms, download installer from [here](https://imagemagick.org/script/download.php)


- Install python binding for imagemagick, wand, using this pip command:
  ```
  pip install wand
  ```

## Troubleshooting
- In case you encounter an exception `wand.exceptions.PolicyError`, you can try the following command to change the policy in `/etc/ImageMagick-6/policy.xml` for PDFs to `read`:
    - On Ubuntu
    ```
    sudo sed -i 's,<policy domain="coder" rights="none" pattern="PDF" />,<policy domain="coder" rights="read" pattern="PDF" />,g' /etc/ImageMagick-6/policy.xml
    ```
    - This command modifies the policy file for ImageMagick, allowing it to read PDF files without raising a `wand.exceptions.PolicyError`.