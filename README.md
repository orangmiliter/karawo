# karawo
Karawo merupakan aplikasi untuk mendukung analisis bibliometrika dengan melakukan scraping data dari portal Garda Rujukan Digital (Garuda) dengan luaran berupa berkas Research Information System (.ris).

### install requirements

```python
pip install bs4
```

### Penggunaan
**Pencarian berdasarakan nama pengarang** 
```bash 
python karawo.py --author "dedy affandy"
```
**Pencarian berdasarkan abstrak**
```bash
python karawo.py --abstract "forensik digital"
```
**Pencarian berdasarkan title / judul**
```bash
python karawo.py --title "forensik digital" --> search by title name
```
