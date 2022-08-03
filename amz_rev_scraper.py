from requests_html import HTMLSession
import concurrent.futures
import analyzer
import time


class Reviews:
    def __init__(self, asin):
        self.asin = asin
        self.session = HTMLSession()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.64 '}
        self.url = f'https://www.amazon.in/product-reviews/{self.asin}/ref=cm_cr_arp_d_paging_btm_next_2?ref_%2Fref=cm_cr_dp_d_show_all_btm%3Fie%3DUTF8&reviewerType=all_reviews&pageNumber='
        # self.tot_rev = self.session.get(self.url + str(1)).html.find('div[data-hook=cr-filter-info-review-rating-count]', first=True).text

    def pagination(self, page):
        r = self.session.get(self.url + str(page))
        # tot_rev = r.html.find('div[data-hook=cr-filter-info-review-rating-count]', first=True).text
        # if not r.html.find('div[data-hook=review]'):
        #     return False
        # else:
        return r.html.find('div[data-hook=review]')

    def parse(self, reviews):
        total = []
        for review in reviews:
            title = review.find('a[data-hook=review-title]', first=True).text
            # rating = review.find('i[data-hook=review-star-rating]', first=True).text
            body = review.find('span[data-hook=review-body]', first=True).text.replace('\n', '').strip()
            data = {'title': title, 'body': body}
            total.append(data)
        return total
