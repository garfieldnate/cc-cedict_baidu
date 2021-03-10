# CC-CEDICT Baidu Result Counts

In `result_count.csv` you will find the words from CC-CEDICT and the number of results returned by the [Baidu](https://www.baidu.com/) search engine. The file is a two-column CSV format with headers. Here is a small sample:

    query,result_count
    2019冠狀病毒病,21400000
    DNA鑒定,19700000
    〥,2280000
    一時半刻,70500

My original purpose for collecting this data was to provide rough frequency statistics for Chinese words, as I couldn't find any frequency data with a permissive license. "Rough" is a key word here, because there are some major caveats:

* The result count is the document frequency (number of pages that use the word), not the term frequency (number of occurrence of the word).
* Baidu only provides an approximate number of search hits.
* Multiple entries with the same spelling will have the same number of results; it is not possible to distinguish the result counts for multiple meanings of the same word.
* Single-character words, or words which appear as a part of other words, likely have an inflated result count.

## Data Package Usage

TODO

## CC-CEDICT Version

The dictionary data was downloaded on 2021-01-28.

## License

The data are released under the same terms as CC-CEDICT itself, the [Creative Commons Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/legalcode) license.
