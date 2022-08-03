from requests_html import HTMLSession
import concurrent.futures
import time


class Reviews:
    def __init__(self, asin):
        self.asin = asin
        self.session = HTMLSession()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.64 '}
        self.url = f'https://www.flipkart.com/poco-x4-pro-5g-laser-blue-128-gb/product-reviews/{self.asin}&page='

    def pagination(self, page):
        r = self.session.get(self.url + str(page))
        # tot_rev = r.html.find('div[data-hook=cr-filter-info-review-rating-count]', first=True).text
        # if not r.html.find('div[data-hook=review]'):
        #     return False
        # else:
        return r.html.find('._27M-vq')

    def parse(self, reviews):
        total = []
        for review in reviews:
            title = review.find('p', first=True).text
            # rating = review.find('i[data-hook=review-star-rating]', first=True).text
            body = review.find('.t-ZTKy', first=True).text.replace('READ MORE', '').replace('\n', '').strip()
            data = {'title': title, 'body': body}
            total.append(data)
        return total


def main():
    amz = Reviews(asin='itm55672e890a619?pid=SMWG99FJBRSJKEYT&lid=LSTSMWG99FJBRSJKEYTWWTVBR&marketplace=FLIPKART')

    results = []
    for i in range(1, 250):
        review = amz.pagination(i)
        time.sleep(0.3)
        #if review is not False:
        results.append(amz.parse(review))
        #else:
        #    print('no more pages')
        #    break

    print(results)


if __name__ == '__main__':
    main()