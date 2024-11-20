def read_mecab_file(file_path):
    """
    MeCabの解析結果を読み込み、形態素ごとの辞書を作成。
    1文を形態素のリストとして表現し、全体をリストで返す。

    Args:
        file_path (str): MeCab解析結果が保存されたファイルパス

    Returns:
        list: 文ごとの形態素辞書のリスト
    """
    sentences = []
    with open(file_path, 'r', encoding='utf-8') as f:
        sentence = []
        for line in f:
            line = line.strip()
            if not line or line == "EOS":  # 空行や文の終わりをスキップ
                if sentence:
                    sentences.append(sentence)
                    sentence = []
                continue
            if '\t' not in line:  # タブがない行はスキップ
                continue
            surface, features = line.split('\t')
            features = features.split(',')
            morph = {
                'surface': surface,
                'base': features[6] if len(features) > 6 and features[6] != '*' else surface,  # 基本形が欠けている場合、表層形を使う
                'pos': features[0],
                'pos1': features[1] if len(features) > 1 else '*'
            }
            sentence.append(morph)
    return sentences
