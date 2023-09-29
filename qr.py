import click
from pathlib import Path
from PIL import Image
import segno


@click.command()
@click.option(
    "--url",
    "-u",
    type=str,
    help="URL to be encoded in QR code.",
)
@click.option(
    "--image-path",
    "-i",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    help="Path to image file to be placed at center of QR code.",
)
@click.option(
    "--output-path",
    "-o",
    type=click.Path(dir_okay=False, path_type=Path),
    default="qr.png",
    help="Path to output QR code image file.",
)
@click.option(
    "--scale",
    "-s",
    type=int,
    default=1,
    help="Scale factor for QR code image.",
)
@click.option(
    "--dark-color",
    "-d",
    help="Dark color for QR code image.",
)
@click.option(
    "--light-color",
    "-l",
    help="Light color for QR code image.",
)
def main(url, image_path, output_path, scale, dark_color, light_color):
    """
    Generate QR code image from URL and with optional image file at center.
    Optionally specify output path, scale factor, and colors.
    """
    scale *= 10
    kw = {}
    # taking color name from user
    if dark_color:
        kw["dark"] = dark_color
    if light_color:
        kw["light"] = light_color

    # taking url or text
    qr = segno.make_qr(url, error='H')
    img = qr.to_pil(scale=scale, **kw).convert('RGBA')

    # inset the image if provided
    if image_path:
        width, height = img.size
        logo = Image.open(image_path)

        logo_ratio = 0.2
        logo_width = int(logo_ratio * width)
        logo_height = int(logo_ratio * height)

        # adjust image size
        logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)

        # inset the logo
        pos = ((width - logo_width) // 2,
               (height - logo_height) // 2)
        img.paste(logo, pos)

    # save the QR code generated
    if not output_path.parent.exists():
        output_path.parent.mkdir(parents=True)
    img.save(output_path)

    print(f'QR code saved to {output_path}')


if __name__ == '__main__':
    main()
