# ============================================================
#   FAQ Data — Full Technical Knowledge Base
#   CodeAlpha AI Internship — Task 2  (Expanded: 200 Q&As)
#
#   Domains covered:
#     AI / ML / Deep Learning / NLP
#     LLMs & Generative AI
#     Python | Java | C++ | PHP
#     HTML | CSS | JavaScript
#     SQL & Databases | NoSQL
#     Data Science & Analytics
#     Networking & OS Basics
#     Cloud & DevOps
#     Career & General Tech
# ============================================================

FAQ_DATA = [

    # ════════════════════════════════════════════
    #   ARTIFICIAL INTELLIGENCE — FUNDAMENTALS
    # ════════════════════════════════════════════
    {
        "question": "What is artificial intelligence?",
        "answer": "Artificial Intelligence (AI) is the simulation of human intelligence by machines. It enables computers to learn, reason, problem-solve, understand language, and perceive the environment."
    },
    {
        "question": "What is the difference between AI and machine learning?",
        "answer": "AI is the broad concept of machines mimicking human intelligence. Machine Learning (ML) is a subset of AI where machines learn from data without being explicitly programmed."
    },
    {
        "question": "What is deep learning?",
        "answer": "Deep Learning is a subset of Machine Learning that uses neural networks with many layers (deep networks) to learn patterns from large amounts of data, such as images, audio, and text."
    },
    {
        "question": "What is a neural network?",
        "answer": "A neural network is a series of algorithms that attempt to recognize underlying relationships in data through a process that mimics the way the human brain works, using layers of interconnected nodes."
    },
    {
        "question": "What is natural language processing?",
        "answer": "Natural Language Processing (NLP) is a branch of AI that helps computers understand, interpret, and generate human language. It powers chatbots, translators, and voice assistants."
    },
    {
        "question": "What is supervised learning?",
        "answer": "Supervised learning is a type of ML where the model is trained on labeled data — meaning the correct answer is provided for each training example. Examples: spam detection, image classification."
    },
    {
        "question": "What is unsupervised learning?",
        "answer": "Unsupervised learning is a type of ML where the model finds patterns in data without labeled answers. Examples include clustering (K-Means) and dimensionality reduction (PCA)."
    },
    {
        "question": "What is reinforcement learning?",
        "answer": "Reinforcement learning is a type of ML where an agent learns by interacting with an environment and receiving rewards or penalties for its actions. It is used in game playing and robotics."
    },
    {
        "question": "What is overfitting in machine learning?",
        "answer": "Overfitting occurs when a model learns the training data too well, including noise, and performs poorly on new unseen data. It can be fixed using regularization, dropout, or cross-validation."
    },
    {
        "question": "What is a training and test set?",
        "answer": "A training set is the data used to train the model. A test set is separate data used to evaluate how well the model performs on unseen examples. Typically split 80/20 or 70/30."
    },
    {
        "question": "What is cross validation?",
        "answer": "Cross-validation is a technique to evaluate ML models by dividing data into multiple folds. The model is trained on some folds and tested on the remaining fold, repeated multiple times for reliability."
    },
    {
        "question": "What is a decision tree?",
        "answer": "A decision tree is a supervised ML algorithm that makes decisions by splitting data based on feature values, forming a tree-like structure of conditions. It is easy to interpret and visualize."
    },
    {
        "question": "What is random forest?",
        "answer": "Random Forest is an ensemble learning method that builds multiple decision trees and merges their results for more accurate and stable predictions. It reduces overfitting compared to a single tree."
    },
    {
        "question": "What is a support vector machine?",
        "answer": "A Support Vector Machine (SVM) is a supervised learning algorithm that finds the best boundary (hyperplane) to separate data into different classes. It works well for both linear and non-linear problems."
    },
    {
        "question": "What is data preprocessing?",
        "answer": "Data preprocessing is the process of cleaning and transforming raw data before feeding it into an ML model. Steps include handling missing values, encoding categorical variables, normalization, and feature selection."
    },
    {
        "question": "What is feature engineering?",
        "answer": "Feature engineering is the process of using domain knowledge to create or transform variables (features) from raw data to improve model performance."
    },
    {
        "question": "What is normalization in machine learning?",
        "answer": "Normalization scales numerical data to a fixed range (usually 0 to 1) so that no single feature dominates due to its magnitude. It helps models train faster and more accurately."
    },
    {
        "question": "What is a confusion matrix?",
        "answer": "A confusion matrix is a table used to evaluate classification model performance. It shows the counts of True Positives, True Negatives, False Positives, and False Negatives."
    },
    {
        "question": "What is accuracy precision and recall?",
        "answer": "Accuracy is the percentage of correct predictions. Precision is how many predicted positives are actually positive. Recall is how many actual positives were correctly identified. F1-score balances precision and recall."
    },
    {
        "question": "What are the applications of AI?",
        "answer": "AI is used in healthcare (diagnosis), finance (fraud detection), transportation (self-driving cars), entertainment (recommendations), education, agriculture, cybersecurity, and many more fields."
    },
    {
        "question": "What is computer vision?",
        "answer": "Computer vision is a field of AI that enables machines to interpret and understand visual information from the world, such as images and videos. Applications include face recognition and object detection."
    },
    {
        "question": "What is object detection?",
        "answer": "Object detection is a computer vision technique that identifies and locates objects in images or videos by drawing bounding boxes around them. Popular models include YOLO and Faster R-CNN."
    },
    {
        "question": "What is a chatbot?",
        "answer": "A chatbot is an AI-powered program that simulates human conversation. It can use rule-based logic, NLP, or deep learning to understand and respond to user queries."
    },
    {
        "question": "What is sentiment analysis?",
        "answer": "Sentiment analysis is an NLP technique to identify the emotional tone (positive, negative, neutral) behind text data. It is used in product reviews, social media monitoring, and customer feedback."
    },
    {
        "question": "How do I start learning AI?",
        "answer": "Start with Python basics, then learn NumPy, Pandas, and Matplotlib. Move on to Scikit-learn for ML, then explore deep learning with TensorFlow or PyTorch. Practice on Kaggle datasets and build projects."
    },
    {
        "question": "What is the difference between data science and AI?",
        "answer": "Data Science focuses on extracting insights from data using statistics and visualization. AI focuses on building systems that can simulate intelligent behavior. They overlap heavily in machine learning."
    },
    {
        "question": "What is big data?",
        "answer": "Big Data refers to extremely large datasets that cannot be processed by traditional tools. It is characterized by Volume, Velocity, and Variety (3 Vs). Tools like Hadoop and Spark are used to process big data."
    },
    {
        "question": "What is transfer learning?",
        "answer": "Transfer learning is a technique where a model trained on one task is reused as the starting point for a different but related task. It saves training time and works well with limited data."
    },
    {
        "question": "What is a generative adversarial network?",
        "answer": "A GAN consists of two neural networks — a Generator that creates fake data and a Discriminator that tries to detect it. They compete until the generator produces realistic outputs. Used for image synthesis and deepfakes."
    },
    {
        "question": "What is gradient descent?",
        "answer": "Gradient descent is an optimization algorithm used to minimize a model's loss function by iteratively updating weights in the direction of the steepest descent. Variants include SGD, Adam, and RMSProp."
    },
    {
        "question": "What is backpropagation?",
        "answer": "Backpropagation is the algorithm used to train neural networks. It calculates the gradient of the loss function with respect to each weight by propagating errors backward through the network."
    },
    {
        "question": "What is an activation function?",
        "answer": "An activation function determines whether a neuron should fire or not. Common functions include ReLU (most popular), Sigmoid (binary classification), Softmax (multi-class), and Tanh."
    },
    {
        "question": "What is K-Means clustering?",
        "answer": "K-Means is an unsupervised ML algorithm that groups data into K clusters based on similarity. It iteratively assigns each data point to the nearest cluster center and recalculates the centers."
    },

    # ════════════════════════════════════════════
    #   LLMs & GENERATIVE AI
    # ════════════════════════════════════════════
    {
        "question": "What is a large language model?",
        "answer": "A Large Language Model (LLM) is a deep learning model trained on massive amounts of text data to understand and generate human language. Examples include GPT-4, Claude, Gemini, and LLaMA."
    },
    {
        "question": "What is ChatGPT?",
        "answer": "ChatGPT is an AI chatbot developed by OpenAI, built on the GPT (Generative Pre-trained Transformer) architecture. It can answer questions, write code, summarize text, and hold natural conversations."
    },
    {
        "question": "What is a transformer model?",
        "answer": "The Transformer is a deep learning architecture introduced by Google in 2017. It uses self-attention mechanisms to process sequences in parallel, forming the backbone of all modern LLMs like GPT, BERT, and Claude."
    },
    {
        "question": "What is prompt engineering?",
        "answer": "Prompt engineering is the practice of designing effective inputs (prompts) to guide an LLM to produce accurate, relevant outputs. Techniques include chain-of-thought prompting, few-shot examples, and role assignment."
    },
    {
        "question": "What is RAG in AI?",
        "answer": "RAG (Retrieval-Augmented Generation) combines an LLM with a retrieval system. The model fetches relevant documents from a database before generating an answer, reducing hallucinations and improving factual accuracy."
    },
    {
        "question": "What is fine tuning an LLM?",
        "answer": "Fine-tuning is the process of further training a pre-trained LLM on a smaller, task-specific dataset. It allows the model to specialize in a particular domain like medicine, law, or customer support."
    },
    {
        "question": "What is hallucination in AI?",
        "answer": "Hallucination is when an AI model generates confident-sounding but factually incorrect information. It happens because LLMs predict probable text rather than retrieving verified facts. RAG and fact-checking help reduce it."
    },
    {
        "question": "What is BERT?",
        "answer": "BERT (Bidirectional Encoder Representations from Transformers) is a Google NLP model trained to understand context from both directions of a sentence. It excels at tasks like question answering and text classification."
    },
    {
        "question": "How do LLMs work?",
        "answer": "LLMs are trained on billions of text tokens using the Transformer architecture. They learn to predict the next word given context. During inference, they generate text token-by-token based on probability distributions."
    },
    {
        "question": "What is generative AI?",
        "answer": "Generative AI refers to AI systems that can create new content — text, images, audio, video, or code — by learning patterns from training data. Examples include ChatGPT, DALL-E, Midjourney, and Stable Diffusion."
    },
    {
        "question": "How can I use LLMs in daily life?",
        "answer": "You can use LLMs to draft emails, summarize documents, write code, answer questions, translate languages, create content, study for exams, plan trips, debug programs, and automate repetitive writing tasks."
    },
    {
        "question": "What is the difference between GPT and BERT?",
        "answer": "GPT is a decoder-only model optimized for text generation. BERT is an encoder-only model optimized for understanding and classification tasks. GPT reads left-to-right; BERT reads in both directions simultaneously."
    },
    {
        "question": "What is an embedding in AI?",
        "answer": "An embedding is a numerical vector representation of text, images, or other data in a high-dimensional space. Similar items have similar embeddings. They are used in semantic search, recommendation systems, and RAG."
    },
    {
        "question": "What is the context window of an LLM?",
        "answer": "The context window is the maximum amount of text (measured in tokens) an LLM can process at once. Larger context windows let the model handle longer documents. GPT-4 supports up to 128K tokens; Claude supports up to 200K."
    },
    {
        "question": "What is tokenization in NLP?",
        "answer": "Tokenization is the process of splitting text into smaller units called tokens (words, subwords, or characters) that a model can process. For example, 'unhappiness' might split into 'un', 'happi', 'ness'."
    },

    # ════════════════════════════════════════════
    #   PYTHON
    # ════════════════════════════════════════════
    {
        "question": "What is Python?",
        "answer": "Python is a high-level, interpreted, general-purpose programming language known for its simple, readable syntax. It is widely used in AI, web development, data science, automation, and scripting."
    },
    {
        "question": "How do I start with Python?",
        "answer": "Download Python from python.org, install it, and write your first program: print('Hello, World!'). Use VS Code or PyCharm as your IDE. Learn variables, loops, functions, and lists before moving to libraries."
    },
    {
        "question": "What are Python data types?",
        "answer": "Python's core data types are int (integers), float (decimals), str (strings), bool (True/False), list (ordered mutable), tuple (ordered immutable), dict (key-value pairs), and set (unique unordered values)."
    },
    {
        "question": "What is a Python list?",
        "answer": "A list is an ordered, mutable collection in Python defined with square brackets: my_list = [1, 2, 3]. You can add, remove, and modify elements. Lists support indexing, slicing, and iteration."
    },
    {
        "question": "What is a Python dictionary?",
        "answer": "A dictionary stores key-value pairs: {'name': 'Alice', 'age': 25}. Keys must be unique and immutable. Use dict['key'] to access values. Dictionaries are very fast for lookups."
    },
    {
        "question": "What is a function in Python?",
        "answer": "A function is a reusable block of code defined with the def keyword: def greet(name): return f'Hello {name}'. Functions take parameters, perform operations, and return values."
    },
    {
        "question": "What is object oriented programming in Python?",
        "answer": "OOP in Python uses classes and objects. A class is a blueprint: class Dog: def __init__(self, name): self.name = name. OOP principles include encapsulation, inheritance, polymorphism, and abstraction."
    },
    {
        "question": "What is a Python lambda function?",
        "answer": "A lambda is an anonymous single-expression function: square = lambda x: x**2. Lambdas are used for short operations, often with map(), filter(), and sorted()."
    },
    {
        "question": "What are Python decorators?",
        "answer": "Decorators are functions that wrap other functions to add behavior without modifying the original code. They use the @decorator syntax and are commonly used for logging, authentication, and caching."
    },
    {
        "question": "What is pip in Python?",
        "answer": "pip is Python's package manager used to install external libraries: pip install pandas. It downloads packages from PyPI (Python Package Index). Use pip list to see installed packages."
    },
    {
        "question": "What is NumPy?",
        "answer": "NumPy is a Python library for numerical computing. It provides fast multi-dimensional arrays (ndarray) and mathematical functions. It is the foundation of most scientific Python libraries."
    },
    {
        "question": "What is Python used for in AI?",
        "answer": "Python is the most popular language for AI and ML due to its simplicity and powerful libraries like NumPy, Pandas, Scikit-learn, TensorFlow, PyTorch, and Keras."
    },
    {
        "question": "What is TensorFlow?",
        "answer": "TensorFlow is an open-source deep learning framework developed by Google. It is used to build and train neural network models for tasks like image recognition, NLP, and time-series analysis."
    },
    {
        "question": "What is PyTorch?",
        "answer": "PyTorch is an open-source deep learning framework developed by Meta (Facebook). It is popular in research due to its dynamic computation graphs and ease of debugging."
    },
    {
        "question": "What is scikit learn?",
        "answer": "Scikit-learn is a Python library for classical machine learning algorithms. It provides tools for classification, regression, clustering, dimensionality reduction, and model evaluation."
    },
    {
        "question": "What is pandas in data science?",
        "answer": "Pandas is a Python library for data manipulation and analysis. It provides DataFrame structures to load, clean, filter, merge, and analyze structured data efficiently."
    },
    {
        "question": "What is NLTK?",
        "answer": "NLTK (Natural Language Toolkit) is a Python library for NLP tasks such as tokenization, stemming, stopword removal, part-of-speech tagging, and parsing text data."
    },
    {
        "question": "What is exception handling in Python?",
        "answer": "Exception handling uses try-except blocks to catch and manage runtime errors gracefully: try: x = 1/0 except ZeroDivisionError: print('Cannot divide by zero'). Use finally for cleanup code."
    },
    {
        "question": "What is a Python virtual environment?",
        "answer": "A virtual environment is an isolated Python environment for a project. Create one with: python -m venv venv. Activate it, then install packages. This prevents version conflicts between projects."
    },

    # ════════════════════════════════════════════
    #   JAVA
    # ════════════════════════════════════════════
    {
        "question": "What is Java?",
        "answer": "Java is a high-level, object-oriented, platform-independent programming language. It follows the 'Write Once, Run Anywhere' principle using the JVM. Used in Android apps, enterprise software, and web backends."
    },
    {
        "question": "How do I start with Java?",
        "answer": "Install the JDK (Java Development Kit) from oracle.com, set up VS Code or IntelliJ IDEA, and write: public class Main { public static void main(String[] args) { System.out.println('Hello World'); } }"
    },
    {
        "question": "What is the JVM?",
        "answer": "The Java Virtual Machine (JVM) is an engine that runs Java bytecode on any operating system. It handles memory management, garbage collection, and makes Java platform-independent."
    },
    {
        "question": "What is OOP in Java?",
        "answer": "OOP in Java uses four pillars: Encapsulation (hiding data with private fields), Inheritance (extending classes), Polymorphism (one interface, many forms), and Abstraction (hiding implementation details)."
    },
    {
        "question": "What is the difference between JDK, JRE, and JVM?",
        "answer": "JDK (Java Development Kit) is for developers — it includes the compiler and JRE. JRE (Java Runtime Environment) is for running Java programs. JVM (Java Virtual Machine) executes the bytecode inside JRE."
    },
    {
        "question": "What are Java collections?",
        "answer": "Java Collections Framework provides data structures like ArrayList (dynamic array), LinkedList, HashMap (key-value), HashSet (unique values), and TreeMap (sorted). All are in the java.util package."
    },
    {
        "question": "What is multithreading in Java?",
        "answer": "Multithreading allows a Java program to execute multiple threads simultaneously. Create threads by extending Thread class or implementing Runnable interface. Use synchronized keyword to prevent race conditions."
    },
    {
        "question": "What is JDBC?",
        "answer": "JDBC (Java Database Connectivity) is an API that allows Java programs to interact with databases. You load a driver, create a Connection, write SQL queries using Statement or PreparedStatement, and process ResultSet."
    },
    {
        "question": "What is Spring Framework in Java?",
        "answer": "Spring is a powerful Java framework for building enterprise applications. It provides Dependency Injection, Spring MVC for web apps, Spring Boot for microservices, and Spring Data for database access."
    },
    {
        "question": "What is the difference between ArrayList and LinkedList in Java?",
        "answer": "ArrayList stores elements in a dynamic array — fast for random access (O(1)) but slow for insertions/deletions in the middle. LinkedList uses nodes — fast for insertions/deletions (O(1)) but slow for random access (O(n))."
    },
    {
        "question": "What is exception handling in Java?",
        "answer": "Java exception handling uses try-catch-finally blocks. Checked exceptions (like IOException) must be handled. Unchecked exceptions (like NullPointerException) are runtime errors. Use throw to raise exceptions manually."
    },
    {
        "question": "What is interface in Java?",
        "answer": "An interface in Java is a contract that a class must follow. It defines method signatures without implementation. A class implements an interface using the implements keyword. Supports multiple inheritance."
    },
    {
        "question": "What is Java Stream API?",
        "answer": "The Stream API (Java 8+) allows functional-style processing of collections. You can filter, map, and reduce data in a clean pipeline: list.stream().filter(x -> x > 10).map(x -> x * 2).collect(Collectors.toList())."
    },

    # ════════════════════════════════════════════
    #   C++
    # ════════════════════════════════════════════
    {
        "question": "What is C++?",
        "answer": "C++ is a high-performance, compiled, general-purpose programming language. It extends C with object-oriented features. Used in game development, system programming, embedded systems, and competitive programming."
    },
    {
        "question": "How do I start with C++?",
        "answer": "Install a compiler (MinGW on Windows or GCC on Linux), use VS Code or Code::Blocks, and write: #include <iostream> using namespace std; int main() { cout << 'Hello World'; return 0; }"
    },
    {
        "question": "What is a pointer in C++?",
        "answer": "A pointer is a variable that stores the memory address of another variable. Declared as int* ptr = &x;. Pointers enable dynamic memory allocation, arrays, and efficient data structure manipulation."
    },
    {
        "question": "What is the difference between C and C++?",
        "answer": "C is procedural — it focuses on functions and structs. C++ extends C with OOP (classes, objects, inheritance), templates, the STL, exception handling, and references. C++ is more feature-rich but also more complex."
    },
    {
        "question": "What is the STL in C++?",
        "answer": "The Standard Template Library (STL) provides reusable data structures and algorithms: vector (dynamic array), map (key-value), set (unique values), stack, queue, and algorithms like sort() and find()."
    },
    {
        "question": "What is memory management in C++?",
        "answer": "C++ gives manual control over memory. Use new to allocate heap memory and delete to free it. Failing to delete causes memory leaks. Modern C++ uses smart pointers (unique_ptr, shared_ptr) to manage memory automatically."
    },
    {
        "question": "What are templates in C++?",
        "answer": "Templates allow writing generic code that works with any data type. A function template: template<typename T> T add(T a, T b) { return a + b; } works for int, float, double without duplication."
    },
    {
        "question": "What is operator overloading in C++?",
        "answer": "Operator overloading lets you redefine operators (+, -, *, ==) for user-defined classes. For example, overloading + for a Vector class allows writing v1 + v2 to add two vectors naturally."
    },
    {
        "question": "What is the difference between struct and class in C++?",
        "answer": "In C++, struct members are public by default and class members are private by default. Both support OOP features. Structs are typically used for simple data grouping; classes for more complex objects with behavior."
    },
    {
        "question": "What is inheritance in C++?",
        "answer": "Inheritance allows a derived class to inherit properties and methods from a base class. C++ supports single, multiple, multilevel, and hierarchical inheritance. Use public, protected, or private access specifiers."
    },

    # ════════════════════════════════════════════
    #   HTML
    # ════════════════════════════════════════════
    {
        "question": "What is HTML?",
        "answer": "HTML (HyperText Markup Language) is the standard language for creating web pages. It uses tags like <h1>, <p>, <a>, and <img> to structure content that browsers display."
    },
    {
        "question": "How do I start with HTML?",
        "answer": "Open any text editor (VS Code recommended), create a file with .html extension, and write the basic structure: <!DOCTYPE html><html><head><title>Page</title></head><body><h1>Hello World</h1></body></html>. Open in a browser."
    },
    {
        "question": "What is the basic structure of an HTML page?",
        "answer": "An HTML page has: <!DOCTYPE html> declares the document type, <html> is the root element, <head> contains meta info and title, and <body> contains all visible content like text, images, and links."
    },
    {
        "question": "What are HTML tags?",
        "answer": "HTML tags are the building blocks of web pages. Common tags: <h1>-<h6> for headings, <p> for paragraphs, <a> for links, <img> for images, <div> for containers, <ul>/<ol> for lists, <table> for tables."
    },
    {
        "question": "What is the difference between div and span in HTML?",
        "answer": "<div> is a block-level element that takes the full width and starts on a new line — used for layout sections. <span> is an inline element that wraps text within a line — used for styling small parts of text."
    },
    {
        "question": "What are HTML forms?",
        "answer": "HTML forms collect user input using <form> with elements like <input>, <textarea>, <select>, and <button>. The action attribute specifies where to send data and method specifies GET or POST."
    },
    {
        "question": "What is semantic HTML?",
        "answer": "Semantic HTML uses meaningful tags that describe content: <header>, <nav>, <main>, <article>, <section>, <aside>, and <footer>. It improves accessibility, SEO, and code readability."
    },
    {
        "question": "What is an HTML attribute?",
        "answer": "Attributes provide additional information about HTML elements. Example: <a href='url' target='_blank'>Link</a>. Common attributes include href, src, class, id, style, type, and alt."
    },

    # ════════════════════════════════════════════
    #   CSS
    # ════════════════════════════════════════════
    {
        "question": "What is CSS?",
        "answer": "CSS (Cascading Style Sheets) is the language used to style HTML elements. It controls layout, colors, fonts, spacing, animations, and responsiveness of web pages."
    },
    {
        "question": "How do I start with CSS?",
        "answer": "Link a CSS file to your HTML using <link rel='stylesheet' href='style.css'> in the <head>. Then write selectors and rules: body { background-color: #fff; font-family: Arial; }. Save and refresh the browser."
    },
    {
        "question": "What is the CSS box model?",
        "answer": "The CSS box model describes every element as a box with: content (the actual content), padding (space inside the border), border (surrounding line), and margin (space outside the border)."
    },
    {
        "question": "What is the difference between class and id in CSS?",
        "answer": "An id (#) targets a single unique element on the page. A class (.) can be reused on multiple elements. Use id for one-of-a-kind elements and class for groups of similarly styled elements."
    },
    {
        "question": "What is flexbox in CSS?",
        "answer": "Flexbox is a CSS layout model that arranges items in a row or column with easy alignment. Set display: flex on the container, then use justify-content, align-items, flex-wrap, and gap to control layout."
    },
    {
        "question": "What is CSS Grid?",
        "answer": "CSS Grid is a two-dimensional layout system for rows and columns. Set display: grid on the container, then define grid-template-columns and grid-template-rows to create precise layouts."
    },
    {
        "question": "What is responsive design in CSS?",
        "answer": "Responsive design makes web pages look good on all devices. Use media queries: @media (max-width: 768px) { ... } to apply different styles for mobile. Combine with flexible units like %, em, rem, and vw."
    },
    {
        "question": "What is CSS specificity?",
        "answer": "Specificity determines which CSS rule applies when multiple rules target the same element. Inline styles > IDs > Classes > Tags. Specificity is calculated as a score: inline=1000, id=100, class=10, tag=1."
    },

    # ════════════════════════════════════════════
    #   JAVASCRIPT
    # ════════════════════════════════════════════
    {
        "question": "What is JavaScript?",
        "answer": "JavaScript is a lightweight, interpreted programming language that runs in the browser and on servers (Node.js). It makes web pages interactive — handling events, animations, form validation, and API calls."
    },
    {
        "question": "What is the difference between var, let, and const in JavaScript?",
        "answer": "var is function-scoped and hoisted — avoid it. let is block-scoped and can be reassigned. const is block-scoped and cannot be reassigned (but objects/arrays it points to can be mutated). Always prefer const, then let."
    },
    {
        "question": "What is the DOM in JavaScript?",
        "answer": "The DOM (Document Object Model) is a programming interface for HTML documents. JavaScript uses the DOM to read, add, modify, and delete HTML elements dynamically: document.getElementById('id').innerHTML = 'Hello'."
    },
    {
        "question": "What is an event listener in JavaScript?",
        "answer": "Event listeners respond to user actions: button.addEventListener('click', function() { alert('Clicked!') }). Common events include click, keydown, mouseover, submit, and load."
    },
    {
        "question": "What is a Promise in JavaScript?",
        "answer": "A Promise represents a value that may be available now, in the future, or never. It has three states: pending, fulfilled, and rejected. Use .then() for success and .catch() for errors. Async/await is cleaner syntax for the same."
    },
    {
        "question": "What is async await in JavaScript?",
        "answer": "async/await is syntactic sugar over Promises for writing cleaner asynchronous code. Mark a function as async, then use await to pause execution until a Promise resolves: const data = await fetch(url).then(r => r.json())."
    },
    {
        "question": "What is React?",
        "answer": "React is a JavaScript library developed by Meta for building user interfaces. It uses a component-based architecture and a virtual DOM for efficient updates. State management, hooks, and JSX make UIs declarative and reusable."
    },
    {
        "question": "What is Node.js?",
        "answer": "Node.js is a JavaScript runtime built on Chrome's V8 engine that lets JavaScript run on the server side. It is non-blocking and event-driven, making it ideal for real-time applications and APIs."
    },

    # ════════════════════════════════════════════
    #   PHP
    # ════════════════════════════════════════════
    {
        "question": "What is PHP?",
        "answer": "PHP (Hypertext Preprocessor) is a server-side scripting language designed for web development. It runs on the server, generates dynamic HTML, and is widely used with MySQL for database-driven websites."
    },
    {
        "question": "How do I start with PHP?",
        "answer": "Install XAMPP or WAMP (includes Apache, PHP, MySQL), place .php files in the htdocs folder, and open them via localhost in a browser. Your first file: <?php echo 'Hello World'; ?>"
    },
    {
        "question": "What are PHP variables?",
        "answer": "PHP variables start with a $ sign: $name = 'Alice'; $age = 25;. PHP is loosely typed — no need to declare the type. Variables are case-sensitive: $Name and $name are different."
    },
    {
        "question": "What are PHP arrays?",
        "answer": "PHP supports indexed arrays: $fruits = ['apple', 'mango']; associative arrays: $person = ['name' => 'Alice', 'age' => 25]; and multidimensional arrays. Use array_push(), array_merge(), and foreach to work with them."
    },
    {
        "question": "What is a PHP session?",
        "answer": "A session stores user data on the server across multiple pages. Start with session_start(), store data in $_SESSION['key'] = value, and access it on any page. Sessions end when the browser closes or session_destroy() is called."
    },
    {
        "question": "What are PHP cookies?",
        "answer": "Cookies store small data on the client's browser. Set with setcookie('name', 'value', expiry). Access via $_COOKIE['name']. Cookies persist until expiry. Unlike sessions, they are stored on the client side."
    },
    {
        "question": "How does PHP connect to MySQL?",
        "answer": "Use MySQLi or PDO: $conn = new mysqli('localhost', 'user', 'pass', 'dbname'); Then run queries: $result = $conn->query('SELECT * FROM table'); Use PDO for better security and database portability."
    },
    {
        "question": "What is OOP in PHP?",
        "answer": "PHP supports OOP with classes, objects, inheritance, interfaces, and traits. Define a class: class Car { public $brand; public function __construct($b) { $this->brand = $b; } }. Create objects with new Car('Toyota')."
    },
    {
        "question": "What is the difference between GET and POST in PHP?",
        "answer": "GET sends data via the URL (?name=Alice) — visible, bookmarkable, used for fetching data. POST sends data in the request body — hidden, more secure, used for forms, logins, and file uploads."
    },
    {
        "question": "What is Laravel?",
        "answer": "Laravel is a popular PHP framework for building web applications. It provides routing, MVC architecture, Eloquent ORM for database operations, Blade templating, authentication scaffolding, and Artisan CLI."
    },

    # ════════════════════════════════════════════
    #   SQL & DATABASES
    # ════════════════════════════════════════════
    {
        "question": "What is SQL?",
        "answer": "SQL (Structured Query Language) is the standard language for managing relational databases. It is used to create tables, insert data, query records, update rows, and delete data."
    },
    {
        "question": "What are the basic SQL commands?",
        "answer": "Core SQL commands: SELECT (retrieve data), INSERT INTO (add data), UPDATE (modify data), DELETE (remove data), CREATE TABLE (create a table), ALTER TABLE (modify structure), DROP TABLE (delete table)."
    },
    {
        "question": "What is a SQL JOIN?",
        "answer": "A JOIN combines rows from two or more tables based on a related column. INNER JOIN returns matching rows; LEFT JOIN returns all rows from the left table; RIGHT JOIN from the right; FULL JOIN returns all rows from both."
    },
    {
        "question": "What is a primary key in SQL?",
        "answer": "A primary key is a column (or set of columns) that uniquely identifies each row in a table. It cannot be NULL and must be unique. Every table should have a primary key for efficient lookups and relationships."
    },
    {
        "question": "What is a foreign key in SQL?",
        "answer": "A foreign key is a column in one table that references the primary key of another table, creating a relationship between them. It enforces referential integrity — you can't add a foreign key value that doesn't exist."
    },
    {
        "question": "What is database normalization?",
        "answer": "Normalization organizes a database to reduce redundancy and improve data integrity. It follows normal forms: 1NF (atomic values), 2NF (no partial dependencies), 3NF (no transitive dependencies)."
    },
    {
        "question": "What is an index in a database?",
        "answer": "An index is a data structure that speeds up data retrieval on a database table column. Like a book index, it lets the database find rows without scanning every record. Indexes speed up SELECT but slow down INSERT/UPDATE."
    },
    {
        "question": "What is the difference between SQL and NoSQL?",
        "answer": "SQL databases are relational, use structured tables with fixed schemas, and are great for complex queries (MySQL, PostgreSQL). NoSQL databases are flexible, schema-less, and scale horizontally (MongoDB, Redis, Cassandra)."
    },
    {
        "question": "What is MongoDB?",
        "answer": "MongoDB is a NoSQL document database that stores data as JSON-like documents (BSON). It is schema-less, highly scalable, and great for unstructured or semi-structured data. Used with MEAN/MERN stacks."
    },
    {
        "question": "What is a stored procedure in SQL?",
        "answer": "A stored procedure is a pre-compiled set of SQL statements stored in the database. You call it by name to execute complex logic. It improves performance, reduces code repetition, and enhances security."
    },
    {
        "question": "What is a transaction in SQL?",
        "answer": "A transaction is a sequence of operations treated as a single unit. It follows ACID properties: Atomicity (all or nothing), Consistency, Isolation, Durability. Use BEGIN, COMMIT, and ROLLBACK to control transactions."
    },
    {
        "question": "What is the difference between WHERE and HAVING in SQL?",
        "answer": "WHERE filters rows before grouping — it works on individual records. HAVING filters groups after a GROUP BY clause — it works on aggregated values like COUNT(), SUM(), or AVG()."
    },

    # ════════════════════════════════════════════
    #   DATA SCIENCE & ANALYTICS TOOLS
    # ════════════════════════════════════════════
    {
        "question": "What is data science?",
        "answer": "Data science is the field of extracting insights and knowledge from structured and unstructured data using statistics, programming, machine learning, and visualization techniques."
    },
    {
        "question": "What is Matplotlib?",
        "answer": "Matplotlib is a Python library for creating static, interactive, and animated data visualizations. Use plt.plot(), plt.bar(), plt.scatter(), and plt.pie() to create charts and graphs."
    },
    {
        "question": "What is Seaborn?",
        "answer": "Seaborn is a Python data visualization library built on Matplotlib. It provides higher-level, more attractive statistical charts like heatmaps, violin plots, pairplots, and boxplots with less code."
    },
    {
        "question": "What is data visualization?",
        "answer": "Data visualization is the graphical representation of data to identify patterns, trends, and insights. Tools include Matplotlib, Seaborn, Tableau, Power BI, and Plotly."
    },
    {
        "question": "What is a Jupyter Notebook?",
        "answer": "Jupyter Notebook is an interactive web-based environment for writing Python code, visualizing outputs, and documenting analysis in one place. Widely used in data science, ML research, and academic work."
    },
    {
        "question": "What is Power BI?",
        "answer": "Power BI is a Microsoft business analytics tool for creating interactive dashboards and reports from various data sources. It is widely used in industry for business intelligence without writing code."
    },
    {
        "question": "What is the difference between mean, median, and mode?",
        "answer": "Mean is the average of all values. Median is the middle value when sorted. Mode is the most frequently occurring value. Use median when data has outliers, as mean is heavily influenced by extreme values."
    },
    {
        "question": "What is correlation in statistics?",
        "answer": "Correlation measures the strength and direction of the relationship between two variables, ranging from -1 (perfect negative) to +1 (perfect positive). A value near 0 means no linear relationship."
    },

    # ════════════════════════════════════════════
    #   NETWORKING & OPERATING SYSTEMS
    # ════════════════════════════════════════════
    {
        "question": "What is an operating system?",
        "answer": "An OS is system software that manages computer hardware and software resources. It provides services for programs and users. Examples: Windows, macOS, Linux, Android. Core functions include process, memory, and file management."
    },
    {
        "question": "What is Linux?",
        "answer": "Linux is a free, open-source Unix-like operating system. It is widely used for servers, supercomputers, Android devices, and developer machines. Popular distributions include Ubuntu, Debian, Fedora, and CentOS."
    },
    {
        "question": "What is an IP address?",
        "answer": "An IP address is a unique numerical label assigned to every device on a network. IPv4 uses 32-bit addresses like 192.168.1.1. IPv6 uses 128-bit addresses. IP addresses enable devices to locate and communicate with each other."
    },
    {
        "question": "What is HTTP and HTTPS?",
        "answer": "HTTP (HyperText Transfer Protocol) is used for transferring web pages. HTTPS is HTTP with SSL/TLS encryption. HTTPS ensures data is encrypted in transit, protecting passwords, credit card numbers, and personal data."
    },
    {
        "question": "What is DNS?",
        "answer": "DNS (Domain Name System) translates human-readable domain names (google.com) into IP addresses (142.250.80.46) that computers use. It acts like a phone book for the internet."
    },
    {
        "question": "What is the difference between TCP and UDP?",
        "answer": "TCP (Transmission Control Protocol) is reliable — it guarantees delivery and order of packets. Used for web browsing, email. UDP (User Datagram Protocol) is faster but unreliable — used for live video, gaming, DNS."
    },
    {
        "question": "What is a REST API?",
        "answer": "A REST API (Representational State Transfer) is an architectural style for building web services. It uses HTTP methods: GET (read), POST (create), PUT (update), DELETE (remove). Data is usually exchanged in JSON format."
    },
    {
        "question": "What is an API?",
        "answer": "An API (Application Programming Interface) is a set of rules that allows two software applications to communicate with each other. It defines how requests and responses are made. Examples: weather APIs, payment APIs, social media APIs."
    },

    # ════════════════════════════════════════════
    #   CLOUD & DEVOPS
    # ════════════════════════════════════════════
    {
        "question": "What is cloud computing?",
        "answer": "Cloud computing is the delivery of computing services — servers, storage, databases, networking, software — over the internet. Major providers are AWS, Microsoft Azure, and Google Cloud Platform (GCP)."
    },
    {
        "question": "What is Docker?",
        "answer": "Docker is a platform for packaging applications and their dependencies into lightweight, portable containers. Containers run consistently across any environment — development, testing, or production."
    },
    {
        "question": "What is Git?",
        "answer": "Git is a distributed version control system that tracks changes in source code. Key commands: git init, git add, git commit, git push, git pull, git branch, git merge. GitHub/GitLab host remote repositories."
    },
    {
        "question": "What is GitHub?",
        "answer": "GitHub is a web-based platform for hosting Git repositories. It enables collaboration, code review, pull requests, issue tracking, CI/CD workflows, and open-source contributions."
    },
    {
        "question": "What is DevOps?",
        "answer": "DevOps is a culture and set of practices that combines software development (Dev) and IT operations (Ops) to shorten the development lifecycle and deliver software continuously and reliably."
    },
    {
        "question": "What is CI CD?",
        "answer": "CI/CD stands for Continuous Integration and Continuous Deployment. CI automatically builds and tests code on every commit. CD automatically deploys passing builds to production. Tools include GitHub Actions, Jenkins, and GitLab CI."
    },

    # ════════════════════════════════════════════
    #   CYBERSECURITY BASICS
    # ════════════════════════════════════════════
    {
        "question": "What is cybersecurity?",
        "answer": "Cybersecurity is the practice of protecting computers, networks, and data from unauthorized access, attacks, and damage. It includes network security, application security, information security, and disaster recovery."
    },
    {
        "question": "What is encryption?",
        "answer": "Encryption is the process of converting readable data (plaintext) into an unreadable format (ciphertext) using an algorithm and a key. Only authorized parties with the decryption key can read the original data."
    },
    {
        "question": "What is SQL injection?",
        "answer": "SQL injection is a cyberattack where malicious SQL code is inserted into an input field to manipulate the database. Prevented by using prepared statements, parameterized queries, and input validation."
    },
    {
        "question": "What is two factor authentication?",
        "answer": "Two-factor authentication (2FA) adds a second layer of security beyond a password. After entering your password, you verify your identity with something you have (OTP on phone) or something you are (fingerprint)."
    },

    # ════════════════════════════════════════════
    #   CAREER & GENERAL TECH
    # ════════════════════════════════════════════
    {
        "question": "What programming language should I learn first?",
        "answer": "Python is the best first language — it has simple syntax, huge community support, and is used across AI, web dev, automation, and data science. Once you understand programming concepts, picking up other languages becomes easier."
    },
    {
        "question": "What is the difference between frontend and backend development?",
        "answer": "Frontend development is everything the user sees — HTML, CSS, JavaScript, React. Backend development is the server-side logic — databases, APIs, authentication. Full-stack developers do both."
    },
    {
        "question": "What is an IDE?",
        "answer": "An IDE (Integrated Development Environment) is a software application for writing, running, and debugging code. Popular IDEs: VS Code (universal), IntelliJ IDEA (Java), PyCharm (Python), Eclipse, and Android Studio."
    },
    {
        "question": "What is open source software?",
        "answer": "Open source software has its source code publicly available for anyone to view, use, modify, and distribute. Examples include Linux, Python, Firefox, VS Code, and TensorFlow. Open source fosters collaboration and innovation."
    },
    {
        "question": "What is agile methodology?",
        "answer": "Agile is an iterative software development approach that delivers working software in short cycles called sprints (1-4 weeks). It emphasizes collaboration, customer feedback, and adaptability over rigid planning."
    },
    {
        "question": "What is the difference between compiled and interpreted languages?",
        "answer": "Compiled languages (C, C++, Java) translate the entire source code to machine code before execution — faster at runtime. Interpreted languages (Python, JavaScript) execute code line-by-line — slower but more flexible and easier to debug."
    },
    {
        "question": "What is recursion in programming?",
        "answer": "Recursion is when a function calls itself to solve a smaller instance of the same problem. Every recursive function needs a base case to stop. Example: factorial(n) = n * factorial(n-1) with base case factorial(0) = 1."
    },
    {
        "question": "What are data structures?",
        "answer": "Data structures are ways of organizing and storing data for efficient access and modification. Core types: Array, Linked List, Stack, Queue, Hash Table, Tree, Graph, and Heap. Choosing the right one impacts performance significantly."
    },
    {
        "question": "What is time complexity?",
        "answer": "Time complexity measures how an algorithm's runtime grows with input size, expressed in Big O notation. O(1) = constant, O(log n) = logarithmic, O(n) = linear, O(n²) = quadratic. Lower is always better."
    },
    {
        "question": "How do I prepare for a technical interview?",
        "answer": "Practice data structures and algorithms on LeetCode/HackerRank. Understand OOP, system design basics, and your primary language deeply. Do mock interviews, review your projects, and know complexity analysis. Consistency beats cramming."
    },

    # ════════════════════════════════════════════
    #   PYTHON — ADVANCED
    # ════════════════════════════════════════════
    {
        "question": "What is list comprehension in Python?",
        "answer": "List comprehension is a concise way to create lists: squares = [x**2 for x in range(10)]. You can add conditions: evens = [x for x in range(20) if x % 2 == 0]. It is faster and more readable than a for loop."
    },
    {
        "question": "What is the difference between a list and a tuple in Python?",
        "answer": "Lists are mutable — you can change their contents after creation. Tuples are immutable — once created, they cannot be changed. Tuples are faster and used for fixed data like coordinates; lists for dynamic collections."
    },
    {
        "question": "What is a generator in Python?",
        "answer": "A generator is a function that yields values one at a time using the yield keyword, instead of returning all at once. It is memory-efficient for large datasets: def count(): yield 1; yield 2; yield 3."
    },
    {
        "question": "What is the difference between deep copy and shallow copy in Python?",
        "answer": "A shallow copy (copy.copy) creates a new object but references the same nested objects. A deep copy (copy.deepcopy) creates a completely independent clone including all nested objects. Use deep copy when working with nested data."
    },
    {
        "question": "What is multiprocessing vs multithreading in Python?",
        "answer": "Multithreading runs threads in the same process but is limited by Python's GIL for CPU tasks. Multiprocessing spawns separate processes with their own memory — truly parallel for CPU-heavy work. Use threading for I/O tasks, multiprocessing for computation."
    },

    # ════════════════════════════════════════════
    #   JAVA — ADVANCED
    # ════════════════════════════════════════════
    {
        "question": "What is garbage collection in Java?",
        "answer": "Java's garbage collector automatically reclaims memory occupied by objects that are no longer referenced. This prevents memory leaks without manual memory management. The JVM runs the GC in the background using algorithms like G1, CMS, or ZGC."
    },
    {
        "question": "What is the difference between abstract class and interface in Java?",
        "answer": "An abstract class can have both implemented and abstract methods, and state (fields). An interface (pre-Java 8) only has method signatures. A class can implement multiple interfaces but extend only one abstract class."
    },
    {
        "question": "What is Java 8 Lambda expression?",
        "answer": "Lambda expressions (Java 8+) allow passing behavior as a method argument. Syntax: (parameters) -> expression. Example: list.forEach(item -> System.out.println(item)). They enable functional programming in Java."
    },
    {
        "question": "What is Hibernate in Java?",
        "answer": "Hibernate is a Java ORM (Object-Relational Mapping) framework that maps Java objects to database tables. Instead of writing raw SQL, you work with Java objects and Hibernate generates the SQL automatically."
    },

    # ════════════════════════════════════════════
    #   HTML/CSS — ADVANCED
    # ════════════════════════════════════════════
    {
        "question": "What is the difference between inline, block, and inline-block in CSS?",
        "answer": "Inline elements (span, a) don't start a new line and ignore width/height. Block elements (div, p) start on a new line and take full width. Inline-block elements flow inline but respect width and height settings."
    },
    {
        "question": "What is z-index in CSS?",
        "answer": "z-index controls the vertical stacking order of positioned elements. Higher z-index = on top. Only works on elements with position: relative, absolute, fixed, or sticky. Default z-index is auto (0)."
    },
    {
        "question": "What is a CSS pseudo-class?",
        "answer": "A pseudo-class targets elements in a specific state. Examples: a:hover (mouse over), input:focus (selected input), li:first-child (first list item), button:disabled. Written as selector:pseudo-class { }."
    },
    {
        "question": "What is the difference between px em and rem in CSS?",
        "answer": "px is an absolute unit — fixed pixel size. em is relative to the parent element's font size. rem is relative to the root (<html>) font size. Use rem for scalable, accessible layouts that respect user font preferences."
    },

    # ════════════════════════════════════════════
    #   WEB DEVELOPMENT — CONCEPTS
    # ════════════════════════════════════════════
    {
        "question": "What is MVC architecture?",
        "answer": "MVC (Model-View-Controller) separates an application into three parts: Model (data and business logic), View (UI presentation), Controller (handles user input and updates model/view). Used in Laravel, Spring MVC, Django, and Rails."
    },
    {
        "question": "What is the difference between GET and POST request?",
        "answer": "GET requests data from a server — parameters are visible in the URL, bookmarkable, cached. POST sends data to the server in the request body — used for forms, logins, file uploads. POST is more secure for sensitive data."
    },
    {
        "question": "What is JSON?",
        "answer": "JSON (JavaScript Object Notation) is a lightweight data format for exchanging data between a server and client. It uses key-value pairs: {'name': 'Alice', 'age': 25}. It is language-independent and easy for humans to read."
    },
    {
        "question": "What is localhost?",
        "answer": "Localhost refers to your own computer as a server, accessed via the IP address 127.0.0.1 or the hostname 'localhost'. It is used to test web applications locally before deploying them to a live server."
    },

    # ════════════════════════════════════════════
    #   SQL — ADVANCED
    # ════════════════════════════════════════════
    {
        "question": "What is a view in SQL?",
        "answer": "A view is a virtual table created by a SELECT query. It doesn't store data physically but presents it from underlying tables. Views simplify complex queries, provide security by hiding columns, and improve code reuse."
    },
    {
        "question": "What is the difference between UNION and JOIN in SQL?",
        "answer": "JOIN combines columns from multiple tables horizontally based on a condition. UNION combines results from multiple SELECT queries vertically (rows stacked), requiring the same number and type of columns."
    },
    {
        "question": "What is GROUP BY in SQL?",
        "answer": "GROUP BY groups rows with the same values in a column and lets you apply aggregate functions. Example: SELECT department, COUNT(*) FROM employees GROUP BY department — counts employees per department."
    },

    # ════════════════════════════════════════════
    #   CLOUD & TOOLS
    # ════════════════════════════════════════════
    {
        "question": "What is Kubernetes?",
        "answer": "Kubernetes (K8s) is an open-source container orchestration platform. It automates deployment, scaling, and management of containerized applications (Docker containers) across clusters of machines."
    },
    {
        "question": "What is the difference between AWS Azure and GCP?",
        "answer": "AWS (Amazon) is the market leader with the most services. Azure (Microsoft) integrates well with enterprise Windows environments. GCP (Google) excels in data analytics and ML (BigQuery, Vertex AI). All three offer computing, storage, and AI services."
    },
    {
        "question": "What is a CDN?",
        "answer": "A CDN (Content Delivery Network) is a geographically distributed network of servers that delivers web content from the server closest to the user. It reduces latency, speeds up page loads, and handles high traffic. Examples: Cloudflare, AWS CloudFront."
    },

    # ════════════════════════════════════════════
    #   GENERAL CS CONCEPTS
    # ════════════════════════════════════════════
    {
        "question": "What is an algorithm?",
        "answer": "An algorithm is a step-by-step procedure for solving a problem or completing a task. Good algorithms are correct, efficient, and readable. Examples: binary search, quicksort, Dijkstra's shortest path."
    },
    {
        "question": "What is binary search?",
        "answer": "Binary search finds an element in a sorted array by repeatedly halving the search range. It has O(log n) time complexity — far faster than linear search O(n) for large sorted datasets."
    },
    {
        "question": "What is a stack and a queue?",
        "answer": "A Stack is a LIFO (Last In First Out) data structure — like a stack of plates. Operations: push (add) and pop (remove from top). A Queue is FIFO (First In First Out) — like a waiting line. Operations: enqueue and dequeue."
    },
    {
        "question": "What is the difference between compiler and interpreter?",
        "answer": "A compiler translates the entire source code to machine code before execution (C, C++, Java). An interpreter translates and executes code line-by-line at runtime (Python, JavaScript). Compiled code is faster; interpreted code is more portable."
    },
    {
        "question": "What is a hash table?",
        "answer": "A hash table stores key-value pairs and uses a hash function to map keys to indices for O(1) average-time lookups. Python's dict and Java's HashMap are hash tables. Collisions are handled via chaining or open addressing."
    },
]