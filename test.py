import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def get_similarity_percentage(paragraph1, paragraph2):
    # Tokenize the paragraphs into words
    words1 = word_tokenize(paragraph1)
    words2 = word_tokenize(paragraph2)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words1 = [word for word in words1 if word.lower() not in stop_words]
    filtered_words2 = [word for word in words2 if word.lower() not in stop_words]

    # Calculate Jaccard similarity
    intersection = len(set(filtered_words1).intersection(filtered_words2))
    union = len(set(filtered_words1).union(filtered_words2))
    jaccard_similarity = intersection / union

    # Calculate similarity percentage
    similarity_percentage = jaccard_similarity * 100

    return similarity_percentage

# Example paragraphs
paragraph1 = "This is the first paragraph. It contains some text."
paragraph2 = "This is the second paragraph. It contains different text."

# Calculate the similarity percentage
percentage = get_similarity_percentage(paragraph1, paragraph2)

# Print the result
print(f"The paragraphs are {percentage:.2f}% similar.")
