[![PyPI Version][pypi-v-image]][pypi-v-link]

[pypi-v-image]: https://img.shields.io/pypi/v/imdby.svg 
[pypi-v-link]: https://pypi.org/project/imdby

# imdby

**imdby** is a Python package useful to retrieve and manage the data of the [IMDb](https://www.imdb.com/) movie database about movies, people, characters and companies.

## Main features

- imdby is a Python package useful to retrieve and manage the data of the IMDb movie database about movies, people, characters and companies.

- Platform-independent and written in Python 3 it can retrieve data from both the IMDb's web server and a local copy of the whole database.

- imdby package can be very easily used by programmers and developers to provide access to the IMDb's data to their programs.

- Some simple example scripts - useful for the end users - are included in this package;

imdby powers many other software and has been used in various research papers. _`Curious about that`_?    


## Installation

Whenever possible, please use the latest version from the repository::

```bash
pip install git+https://github.com/santhoshse7en/imdb
```

But if you want, you can also install the latest release from PyPI::

```bash
pip install imdby
```

## Usage

Download it by clicking the green download button here on Github. Here's an example that demonstrates how to use imdby:

```python
# create an instance of the IMDb class
from imdby.imdb import imdb

# get a movie
details = imdb('tt4154796')

# print the names of the directors of the movie
print('Directors:')
for i in range(len(details.directors)):
    print(details.directors[i])

# print the genres of the movie
print('Genres:')
for i in range(len(details.genre)):
    print(details.genre[i])
```
Directory of IMDb class

![dir](https://user-images.githubusercontent.com/47944792/58084265-2b3bc300-7bd8-11e9-9169-cc60542593f1.PNG)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
