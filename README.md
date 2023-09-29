# QR Code Helper CLI

This is a simple CLI to generate QR codes to URLS from the command line.

## Installation

To install the CLI, clone the repo (optionally create a virtual env with your favorite environment managing tool) and run the following command:

```bash
pip install -r requirements.txt
```

## Usage

Basic usage to generate a qr code using a `--url`/`-u` flag.

```bash
python qr.py --url someurl.com
```

You can specify the output file name with the `--output`/`-o` flag. Otherwise it will default to `qr.png`.

```bash
python qr.py --url someurl.com --output someoutput.png
```

And add an image to the QR code with the `--image-path`/`i` flag.

```bash
python qr.py --url someurl.com --image-path somelogo.png
```

There are additional options to change the color of the QR code, for a full list of options run:

```bash
python qr.py --help
```
