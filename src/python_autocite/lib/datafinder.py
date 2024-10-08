class Datafinder:

    def __init__(self, soup):
        self._soup = soup

    def get_authors(self):
        authors = set()
        searches = [
                {'name': 'author'},
                {'property': 'article:author'},
                {'property': 'author'},
                {'rel': 'author'},
                {'property': 'og:site_name'}
                ]

        tags = ["meta", ""]

        author_elements = []
        for t in tags:
            for s in searches:
                author_elements += self._soup.find_all(t, attrs=s)

        for el in author_elements:
            author = self._get_data_from_element(el)
            if (len(author.split()) > 1):
                authors.add(author)

        authors_list = list(authors)
        return authors_list

    def get_title(self):
        searches = [
                {'property': 'og:title'},
                {'class': 'title'}
                ]
        tags = ["title", "meta", ""]

        for t in tags:
            for s in searches:
                el = self._soup.find(t, attrs=s)
                if (el is not None):
                    return self._get_data_from_element(el)

        return '[[[TITLE]]]'

    def get_publication_date(self):
        searches = [
                {'name': 'date'},
                {'property': 'published_time'},
                {'property': 'article:published_time'},
                {'property': 'article:modified_time'},
                {'name': 'timestamp'},
                {'class': 'submitted-date'},
                {'class': 'posted-on'},
                {'class': 'timestamp'},
                {'class': 'date'},

                ]
        tags = ["meta", ""]
        for t in tags:
            for s in searches:
                el = self._soup.find(t, attrs=s)
                if (el is not None):
                    return self._get_data_from_element(el)

        return '[[[PUBLICATION DATE]]]'

    def _get_data_from_element(self, el):
        try:
            return el['content']
        except KeyError:
            return el.text

