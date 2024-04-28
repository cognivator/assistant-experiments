import unittest
from unittest.mock import patch, mock_open

import crawler

class TestWebCrawler(unittest.TestCase):
    def test_valid_url_within_domain(self):
        msg = "Should return True if the URL is within the same domain"
        base_url = "http://example.com"
        url = "http://example.com/page"
        within_domain = True
        visited = set()
        self.assertTrue(crawler.valid_url(base_url, url, within_domain, visited), msg)

    def test_valid_url_relative_root_within_domain(self):
        msg = "Should return True if the relative root URL is within the same domain"
        base_url = "http://example.com"
        url = "/page"
        within_domain = True
        visited = set()
        self.assertTrue(crawler.valid_url(base_url, url, within_domain, visited), msg)

    def test_valid_url_relative_path_within_domain(self):
        msg = "Should return True if the relative path URL is within the same domain"
        base_url = "http://example.com"
        url = "page"
        within_domain = True
        visited = set()
        self.assertTrue(crawler.valid_url(base_url, url, within_domain, visited), msg)

    def test_valid_url_not_within_domain(self):
        msg = "Should return False if the URL is not within the same domain"
        base_url = "http://example.com"
        url = "http://different.com"
        within_domain = True
        visited = set()
        self.assertFalse(crawler.valid_url(base_url, url, within_domain, visited), msg)

    def test_valid_url_no_domain_restriction_out_domain(self):
        msg = "Should return True if there is no domain restriction and URL is not within the same domain"
        base_url = "http://example.com"
        url = "http://different.com"
        within_domain = False
        visited = set()
        self.assertTrue(crawler.valid_url(base_url, url, within_domain, visited), msg)

    def test_valid_url_no_domain_restriction_in_domain(self):
        msg = "Should return True if there is no domain restriction and URL is within the same domain"
        base_url = "http://example.com"
        url = "http://example.com/page"
        within_domain = False
        visited = set()
        self.assertTrue(crawler.valid_url(base_url, url, within_domain, visited), msg)

    def test_valid_url_visited(self):
        msg = "Should return False if the URL is already visited"
        base_url = "http://example.com"
        url = "http://example.com/page"
        within_domain = True
        visited = set()
        visited.add(url)
        self.assertFalse(crawler.valid_url(base_url, url, within_domain, visited), msg)

    # test with url with fragment
    def test_valid_url_visited_fragment(self):
        msg = "Should return False if the URL with fragment is already visited without fragment"
        base_url = "http://example.com"
        url = "http://example.com/page#section"
        within_domain = True
        visited = set()
        visited.add("http://example.com/page")
        self.assertFalse(crawler.valid_url(base_url, url, within_domain, visited), msg)

    @patch('crawler.requests.get')
    def test_fetching_page(self, mock_get):
        msg = "Should fetch the page content and write to a file"
        base_url = "http://example.com"
        url = "http://example.com/"
        within_domain = True
        converter = crawler.html2text.HTML2Text()
        save_path = ""
        max_depth = 1

        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "<html></html>"
        with patch('crawler.open', new_callable=mock_open) as mock_file:
            crawler.crawl_page(base_url, max_depth, converter, save_path, url, within_domain)
            mock_file().write.assert_called_with("> http://example.com/\n\n\n\n")


if __name__ == '__main__':
    unittest.main()
