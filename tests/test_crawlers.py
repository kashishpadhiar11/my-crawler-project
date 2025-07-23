import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crawlers.gnosis import crawl_gnosis

def test_gnosis_crawler():
    data = crawl_gnosis()
    assert isinstance(data, dict)
    assert "url" in data and "text" in data
    assert len(data["text"]) > 0
