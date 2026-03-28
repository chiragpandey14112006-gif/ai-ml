# **Project Report: SpamBuddy Message Classifier**
**Course Capstone: Bring Your Own Project (BYOP)**

## **1. Introduction & Problem Statement**
For my BYOP, I decided to tackle the issue of **SMS and Email Phishing**. In my daily life, I noticed that scam messages have become more frequent and more clever. Most people—especially those who aren't tech-savvy—often struggle to tell the difference between a genuine automated notification and a "smishing" (SMS Phishing) attempt.

I wanted to build a tool that doesn't just say "Spam" or "Not Spam," but actually explains *why* a message looks suspicious by looking at the language and the psychological tricks being used.

## **2. Why This Matters**
Cybersecurity is usually seen as something handled by big antivirus companies, but I believe individual users should have simple tools to verify information. By building **SpamBuddy**, I aimed to apply Machine Learning (ML) concepts to a practical, everyday safety problem. This project matters because it bridges the gap between complex AI and a simple, conversational interface that anyone can use.

## **3. My Approach & Logic**
I chose to use **Python** for this project because of its strong libraries for text processing.

### **The Model**
I implemented a **Multinomial Naive Bayes** classifier. I chose this specific model because it is the "gold standard" for text classification. It works by calculating the probability of a category (Spam vs. OK) based on the frequency of specific words found in the message.

### **The Training Process**
Since I didn't want to rely on a massive, heavy dataset for a lightweight tool, I built a custom "knowledge base" inside the code. 
* **Spam Indicators:** Words like "free," "winner," "urgent," and "claim."
* **Normal Indicators:** Words like "meeting," "hello," and "thanks."
* **Refinement:** I used a technique called **Over-sampling** for the spam words. Since spam messages are usually shorter and more aggressive, I had the model "study" those words more intensely to increase its sensitivity to red flags.

## **4. Key Design Decisions**
* **Confidence Scores:** I decided not to give a simple "Yes/No" answer. Instead, the program outputs a percentage. This reflects how real-world AI works—nothing is ever 100% certain, and showing the confidence level helps the user make their own informed choice.
* **Heuristic Overlays:** I added a secondary layer of "Vibe Checks." Even if the math is unsure, the code scans for specific behaviors like "Dangling Cash" (promisory language) or "False Urgency" (pressure tactics) to provide a human-readable explanation.

## **5. Challenges I Faced**
* **Data Sparsity:** At first, the model was too "forgiving." If a word wasn't exactly in my list, it would assume the message was safe. I fixed this by expanding my keyword lists and adjusting the training weights.
* **Case Sensitivity:** I realized early on that "FREE" and "free" were being treated differently. I solved this by forcing all user input to lowercase before processing it.

## **6. What I Learned**
This project taught me that **Natural Language Processing (NLP)** isn't just about high-level math; it’s about understanding human behavior. I learned how to:
1.  Clean and "vectorize" text so a computer can understand it.
2.  Balance a model so it isn't too paranoid or too relaxed (False Positives vs. False Negatives).
3.  Write a clean, interactive command-line interface that feels "friendly" to the user.

## **7. Conclusion**
**SpamBuddy** is a small-scale solution to a massive problem. While it's currently a terminal-based tool, the logic behind it is solid enough to be expanded into a browser extension or a mobile app. It successfully applies the core concepts of this course—problem identification, data logic, and practical coding—into a tool that actually serves a purpose.
