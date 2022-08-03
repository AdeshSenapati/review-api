import analyzer
import flip_rev_scraper as flp
import concurrent.futures
import time


def get_results(url):
    try:
        url = url
        if 'www.flipkart.com' not in url:
            return {'data': 'Please enter a valid url of only Flipkart products'}
        asin_code = url.split('/')
        # print(asin_code[5])
        amz_rev = flp.Reviews(asin=asin_code[5])

        results = []
        NUM_THREADS = 30

        def get_data(page):

            review = amz_rev.pagination(page)
            time.sleep(0.3)
            # if review is not False:
            results.append(amz_rev.parse(review))
            # else:
            #    print('no more pages')
            #    break

        pages = range(1, 30)
        with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
            executor.map(get_data, pages)
        # print(results)
        sm = []
        for i in results:
            for j in i:
                lm = j['title']+''+j['body']
                sm.append(lm)

        ss = '. '.join(i for i in sm)
        # print(ss)
        return analyzer.sentiment_scores(ss)
    except:
        return {'data': 'Internal Server Error...Please try again later...'}

