punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(s):
    new_s = ''
    for c in s:
        if c in punctuation_chars:
            s.replace(c, '')
        else:
            new_s += c
    return new_s


def get_pos(s):
    tot = 0
    s2 = strip_punctuation(s).lower()
    s3 = s2.split()
    for w in s3:
        if w in positive_words:
            tot += 1
    return tot


def get_neg(s):
    tot = 0
    s2 = strip_punctuation(s).lower()
    s3 = s2.split()
    for w in s3:
        if w in negative_words:
            tot += 1
    return tot


# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

outfile = open("project_twitter_data.csv", "r")
lines = outfile.readlines()
header = lines[0]
header_names = header.strip().split(',')
print(header_names)

data_tot = []
for row in lines[1:]:
    data = []

    vals = row.strip().split(',')
    data.append(int(vals[1]))
    data.append(int(vals[2]))
    pure_val = strip_punctuation(vals[0])
    pos_count = get_pos(pure_val)
    neg_count = get_neg(pure_val)
    net_count = pos_count - neg_count
    data.extend([pos_count, neg_count, net_count])
    data_tot.append(data)
print(data_tot)

outfile2 = open("resulting_data.csv", "w")
outfile2.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile2.write('\n')
for d in data_tot:
    row_string = '{},{},{},{},{}'.format(d[0], d[1], d[2], d[3], d[4])
    outfile2.write(row_string)
    outfile2.write('\n')
outfile.close()
outfile2.close()
