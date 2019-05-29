from imdby.utils import *
from imdby.movie import movie
from imdby.plot import plot
from imdby.plot_keywords import plot_keywords
from imdby.company import company
from imdby.parental_guide import parental_guide
from imdby.technical_spec import technical_spec
from imdby.release_info import release_info
from imdby.taglines import taglines
from imdby.cast_and_crew import cast_and_crew

# main class which passes the titleid to each indiviual class
class imdb:
    def __init__(self, titleid):
        start_time = datetime.now()
        movie.__init__(self, titleid)
        plot.__init__(self, titleid)
        plot_keywords.__init__(self, titleid)
        parental_guide.__init__(self, titleid)
        company.__init__(self, titleid)
        technical_spec.__init__(self, titleid)
        release_info.__init__(self, titleid)
        taglines.__init__(self, titleid)
        cast_and_crew.__init__(self, titleid)

        time_delta = datetime.now() - start_time
        sys.stdout.write('\r' + str("Calculating time taken for imdb basic info. data extraction") + ":  " + str(time_delta.seconds) +  "  seconds" +  '\r')
        sys.stdout.flush()
