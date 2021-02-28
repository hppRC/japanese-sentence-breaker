__version__ = '0.1.0'


MARKS = ["「」", "『』", "【】", "[]", "“”", "()", "（）", "｛｝", "〈〉", "《》", "〔〕"]


def break_line(text, ignore_unbalanced=False):
    print(text)
    res = []
    tmp = ""
    alignments = [0]*len(MARKS)

    for ch in text:
        for i, (left, right) in enumerate(MARKS):
            if ch == left:
                alignments[i] += 1
            elif ch == right:
                alignments[i] -= 1

        if ch == "。" and sum(abs(x) for x in alignments) == 0:
            res.append(tmp.strip() + "。")
            tmp = ""
        else:
            tmp += ch
    else:
        res.append(tmp.strip())

    # 対応の取れていないカッコを消去
    if not ignore_unbalanced and sum(abs(x) for x in alignments):
        tmp = ""
        for ch in text:
            for i, (left, right) in enumerate(MARKS):
                if ch == left and alignments[i] > 0:
                    alignments[i] -= 1
                    break
                elif ch == right and alignments[i] < 0:
                    alignments[i] += 1
                    break
            else:
                tmp += ch
        return break_line(tmp).strip()

    return "\n".join(res).strip()
