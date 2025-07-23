from pathlib import Path

async def download_and_verify(page, locator: str, download_dir="downloads"):
    download_path = Path(download_dir)
    download_path.mkdir(parents=True, exist_ok=True)

    async with page.expect_download() as download_info:
        await page.click(locator)

    download = await download_info.value

    save_path = download_path / download.suggested_filename
    await download.save_as(save_path)

    assert save_path.exists(), f"❌ Download failed: {save_path.name} not found."
    print(f"✅ File downloaded successfully: {save_path}")

    return save_path
