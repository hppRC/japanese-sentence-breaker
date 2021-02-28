from japanese_sentence_breaker import __version__, break_line


def test_version():
    assert __version__ == '0.1.0'


def test_break():
    text = "これはテストです。文の流れを考慮し、句点区切りで文章を分割します。「例えば。」このようなカッコ内のテキストは分割しません。"
    splitted = """\
これはテストです。
文の流れを考慮し、句点区切りで文章を分割します。
「例えば。」このようなカッコ内のテキストは分割しません。\
"""
    assert splitted == break_line(text)


def test_no_break():
    text = "「例1。」『例2。』【例3。】。"
    splitted = "「例1。」『例2。』【例3。】。"
    assert splitted == break_line(text)


def test_no_period():
    text = "これはテストです"
    splitted = "これはテストです"
    assert splitted == break_line(text)


def test_unbalanced():
    text = "これは「テストです。｛整合性の取れないカッコは消去されます。）"
    splitted = """\
これはテストです。
整合性の取れないカッコは消去されます。\
"""
    assert splitted == break_line(text)


def test_ignore_unbalanced():
    text = "これは「テストです。｛整合性のないカッコは無視されます。）改行はできません。"
    splitted = "これは「テストです。｛整合性のないカッコは無視されます。）改行はできません。"
    assert splitted == break_line(text, ignore_unbalanced=True)
