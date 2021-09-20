# CC-CEDICT Baidu Result Counts

In `result_count.csv` you will find the words from [CC-CEDICT](https://cc-cedict.org/wiki/) and the number of results returned by the [Baidu](https://www.baidu.com/) search engine. The file is a two-column CSV format with headers. Here is a small sample:

    query,result_count
    2019冠狀病毒病,21400000
    DNA鑒定,19700000
    〥,2280000
    一時半刻,70500

My original purpose for collecting this data was to provide rough frequency statistics for Chinese words, as I couldn't find any frequency data with a permissive license. "Rough" is a key word here, because there are some major caveats:

## Caveats

* The result count is the document frequency (number of pages that use the word), not the term frequency (number of occurrences of the word in all documents).
* Baidu only provides an approximate number of search hits.
* Multiple entries with the same spelling will have the same number of results; it is not possible to distinguish the result counts for multiple meanings of the same word.
* Single-character words, or words which appear as a part of other words, likely have an inflated result count.
* All searches were done in traditional characters, but Baidu also provides results with simplified characters, so we are relying on their automated conversion and inherit any potential issues from it.
* Baidu complies with Chinese law by heavily censoring articles it presents, which likely reduces or even eliminates results for certain entries.

## Example Data Package Usage

I've provided a `datapackage.json` for convenience. To retrieve and load the data in python:

* `pip install datapackage`

```python
    $ python
    >>> from datapackage import Package
    >>> package = Package('https://raw.githubusercontent.com/garfieldnate/cc-cedict_baidu/master/datapackage.json')
    >>> resource = package.get_resource('result-count')
    >>> data = resource.read(keyed=True)
    >>> data[10000]
    {'query': '周報', 'result_count': 610000}
```

## CC-CEDICT Version

The dictionary data was downloaded on 2021-01-28.

## License

The data are released under the same terms as CC-CEDICT itself, the [Creative Commons Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/legalcode) license.
