from imdby.utils.config import base_uri, imdb_uris
from imdby.utils.helpers import catch, catch_dict, unicode
from imdby.utils.utils import BeautifulSoup, get, pd, re


# Retrieves IMDb Plot Details
class plot:

    """
    Collects IMDb Plot Details of the multi-media content in IMDb when title_id is given.
    :param title_id: Unique identification for every multimedia in IMdb.
    """

    def __init__(self, title_id):
        self.title_id = title_id
        self.plot_uri = imdb_uris["plotsummary"] % self.title_id
        soup = BeautifulSoup(get(self.plot_uri).text, 'lxml')

        """
        :returns: Movie Title
        """
        movie_tag = soup.select_one('h3[itemprop="name"]')
        self.title = catch(lambda: unicode(movie_tag.a.get_text()))
        self.title_url = catch(lambda: unicode(
            '%s%s' % (base_uri, movie_tag.a['href'][1:])))
        self.year = catch(lambda: int(re.findall(
            r"\d+", unicode(movie_tag.select_one('.nobr').get_text()))[0]))

        """
        :returns: Movie Plot
        """
        self.plot = catch(lambda: unicode(soup.select_one(
            '#synopsis').findNext('ul').get_text()).replace("\'", ""))

        """
        :returns: Movies Summaries
        """
        block = catch(lambda: soup.select_one(
            '#summaries').findNext('ul').select('li'))
        self.summaries = [catch(lambda: unicode(
            ' '.join(tag.text.split()))) for tag in block]

        """
        :returns: Creates Dict from the above info. if available.
        """
        self.imdb_plot_metadata = catch_dict(lambda: {"Movie Name": self.title,
                                                      "Movie URI": self.title_url,
                                                      "Title ID": self.title_id,
                                                      "Year": self.year,
                                                      "Movie Plot URI": self.plot_uri,
                                                      "Plot": self.plot,
                                                      "Summaries": self.summaries})
