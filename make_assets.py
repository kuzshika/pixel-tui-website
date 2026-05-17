from PIL import Image

source = Image.open("assets/pixel-tui-logo.jpg").convert("RGB")

for size, output in [(512, "assets/icon-512.png"), (192, "assets/icon-192.png"), (32, "favicon.png")]:
    source.resize((size, size), Image.Resampling.NEAREST).save(output)

og = source.resize((1200, 1200), Image.Resampling.NEAREST)
top = (1200 - 630) // 2
og.crop((0, top, 1200, top + 630)).save("assets/og-image.jpg", quality=88)
