# Movie Recommendation System
- Developed a front-end movie recommender using the TMDB dataset and NLP to analyze movie metadata. 
- Implemented content-based filtering for real-time, personalized recommendations based on descriptions, 
  tags, actors, genres, and directors. 

## Detailed explaination
⭐ General & Technical Highlights
Developed a content-based movie recommendation system using the TMDB 5000 Movies and Credits dataset (20+ features, 5000+ entries).

Engineered custom features by extracting and cleaning JSON-formatted fields (cast, crew, genres, keywords) from raw CSV data.

Combined multiple metadata fields (title, cast, crew, keywords, genres) to generate a rich textual description for each movie.

🧠 NLP & Feature Engineering
Applied Bag-of-Words model using CountVectorizer with max_features=5000 and English stopwords removal to transform text into sparse feature vectors.

Preprocessed data using techniques such as tokenization, lowercasing, whitespace removal, and duplicate filtering for optimal feature quality.

🧮 Similarity Computation
Utilized cosine similarity to compute pairwise similarity scores between movie vectors to address issues of high-dimensional sparsity.

Avoided Euclidean distance due to curse of dimensionality in sparse vector space.

🛠️ Core Logic & Functionality
Implemented a recommendation function that returns the top 5 most similar movies to a given input based on cosine similarity scores.

Optimized search by building an index map for faster lookup and similarity retrieval in large datasets.

🚀 Tools & Libraries
Technologies used: Python, Pandas, NumPy, scikit-learn, CountVectorizer, and cosine_similarity from sklearn.metrics.pairwise.

Dataset operations performed with Pandas for merging, filtering, and preprocessing; handled complex JSON structures without external parsing libraries.

Deployed the model using Streamlit to allow users to search for any movie and get recommendations with a simple UI.
