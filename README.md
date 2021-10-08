# karawo
Karawo merupakan aplikasi untuk mendukung analisis bibliometrika dengan melakukan scraping data dari portal Garda Rujukan Digital (Garuda) dengan luaran berupa berkas Research Information System (.ris).

#### install requirements

```python
pip install bs4
```

#### Run
```bash
python karawo.py --author "dedy affandy" --> search by author name
python karawo.py --abstract "forensik digital" --> search by abstract
python karawo.py --title "forensik digital" --> search by title name
```
