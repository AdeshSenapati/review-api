import analyzer
import amz_rev_scraper as amz
import time


def get_results(url):
    try:
        url = url
        if 'www.amazon.in' not in url:
            return {'data': 'Please enter a valid url of only Amazon products'}
        asin_code = url.split('/')
        # print(asin_code[5])
        amz_rev = amz.Reviews(asin=asin_code[5])

        results = []
        count = 0
        for i in range(1, 250):
            review = amz_rev.pagination(i)
            time.sleep(0.3)
            # if review is not False:
            results.append(amz_rev.parse(review))
            # else:
            #    print('no more pages')
            #    break

            # print('\r', 'Running.. page no.', str(count), end='')
            count = count + 1

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


