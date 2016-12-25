from os import path
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_fscore_support

from sklearn.naive_bayes import MultinomialNB
from tokenization import tag_subtitles
from tokenization import randomize
from tokenization import bag_of_words_and_tf
from tokenization import clean_stopword


#  # Categorize words and plot them
# category_dict = categorize_words(path.relpath("CategoryData"))
# to_be_filtered = ['grunt', 'beep', 'grunts', ',', 'groan', 'speak', 'music']
#
# # for i in categories:
# #     for f in to_be_filtered:
# #         category_dict[i] = category_dict[i].replace(f, '')
#
# for c in categories:
#     cleaned_list = clean_stopword(category_dict[c])
#     stemmed_data = stemming(cleaned_list)
#
#     fd = nltk.FreqDist(stemmed_data)
#     print('Category: ', c)
#     print(fd.most_common(12))
#     fd.plot(12, cumulative=False)

# process_movie_subtitles(path.relpath("ProcessedSubtitles"), path.relpath("CategoryData"))


test_size = 300

text, genre = tag_subtitles(path.relpath('CategoryData'))

to_be_filtered = ['grunt', 'beep', 'grunts', ',', 'groan', 'speak', 'music']
for i in range(len(text)):
    for f in to_be_filtered:
        text[i] = text[i].replace(f, '')

# # Initialize naive bayes object
#
# acc_scores = []
# alpha_values = np.arange(0.1, 2.0, 0.1)
# alpha_values = [0.1, 0.5, 0.01, 0.05, 0.001, 0.005]
# print(alpha_values)
# for a in alpha_values:
#     clf = MultinomialNB(alpha=a)
#     acc = 0
#     print('.', a)
#     for i in range(50):
#         text, genre = randomize(text, genre)
#
#         bow_tf = bag_of_words_and_tf(text)
#
#         clf.fit(bow_tf[test_size:], genre[test_size:])
#
#         test_data = bow_tf[:test_size]
#         test_genre = genre[:test_size]
#
#         predicted = clf.predict(test_data)
#         acc += accuracy_score(test_genre, predicted)*100
#     acc_scores.append(float(acc/50))
#
# print(acc_scores)
#
# plt.plot(alpha_values, acc_scores, 'o')
# plt.axis([0, 5, -1, 100])
#
# plt.xlabel('Alpha values')
# plt.ylabel('Accuracy')
# plt.legend(loc='upper right', numpoints=1)
# plt.title("Accuracies / Alpha values")
#
# #for k, accuracy in zip(k_values, accuracies):
# #    plt.text(k - 0.6, accuracy+1, str(k) + ", " + str(format(accuracy, '.1f')), fontsize=10)
#
# plt.show()


# Classification report for alpha: 0.01
clf = MultinomialNB(alpha=0.01)
text, genre = randomize(text, genre)

bow_tf = bag_of_words_and_tf(text)

clf.fit(bow_tf[test_size:], genre[test_size:])

test_data = bow_tf[:test_size]
test_genre = genre[:test_size]

predicted = clf.predict(test_data)
print('scikit learn score: ', accuracy_score(test_genre, predicted))
print(classification_report(test_genre, predicted))
p, r, f1, s = precision_recall_fscore_support(test_genre, predicted)
print('precision: ', p)
print('recall: ', r)
print('f1 score: ', f1)
f1_scores = [float("{0:.2f}".format(a)) for a in f1]
print(f1_scores)
print('support:', s)