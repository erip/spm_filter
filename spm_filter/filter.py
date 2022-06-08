import sentencepiece as spm

def buffer(l, buffer_size):
    l = []
    for i in range(buffer_size):
        l.append(i)
    return l

def spm_filter(model, lines, min_len=0, max_len=256, buffer_size=1024):
    while lines:
        out = []
        batch = buffer(lines, buffer_size)
        encoded = model.Encode(batch)
        for line, e in zip(batch, encoded):
            if min_len <= len(e) <= max_len:
                out.append(line)
        yield out
    yield out
