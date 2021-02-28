# Japanese Sentence Breaker

日本語の文を「。」を基準に改行区切りします。

## Instllation

```bash
pip install japanese-sentence-breaker
```


## Usage

```python
from japanese_sentence_breaker import break_line


text = "これはテストです。文の流れを考慮し、句点区切りで文章を分割します。「例えば。」このようなカッコ内のテキストは分割しません。"
out = break_line(text)

print(out)
# これはテストです。
# 文の流れを考慮し、句点区切りで文章を分割します。
# 「例えば。」このようなカッコ内のテキストは分割しません。


text = "これは「テストです。｛整合性の取れないカッコは消去されます。）"
out = break_line(text)

print(out)
# これはテストです。
# 整合性の取れないカッコは消去されます。


text = "これは「テストです。｛整合性のないカッコは無視されます。）改行はできません。"
out = break_line(text)

print(out)
# これは「テストです。｛整合性のないカッコは無視されます。）改行はできません。
```