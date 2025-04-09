import sys
from pathlib import Path

repo_root_dir = Path(__file__).parent.parent
sys.path.append(str(repo_root_dir))

from musescore_scraper import MuseScraper

url = "https://musescore.com/user/29857994/scores/8600405"

with MuseScraper() as ms:
    ms.to_pdf(url)
