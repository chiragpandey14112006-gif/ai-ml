import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

class SpamBuddy:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()

    def teach_me_good_and_bad(self):
        spam_words = "free money win prize urgent viagra lottery click claim winner congratulations".split()
        normal_words = "hey hi hello meeting lunch call thanks tomorrow update how are you".split()

        # spam is rarer irl so we over-sample it a bit
        texts = spam_words * 12 + normal_words * 8
        labels = [1] * (len(spam_words)*12) + [0] * (len(normal_words)*8)  # 1 = spam

        X = self.vectorizer.fit_transform(texts)
        self.model.fit(X, labels)
        print("alright i learned something")

    def yo_is_this_spam(self, msg):
        vec = self.vectorizer.transform([msg])
        prob = self.model.predict_proba(vec)[0]
        prediction = self.model.predict(vec)[0]

        verdict = "SPAM" if prediction else "OK"
        confidence = prob[1] if prediction else prob[0]
        return verdict, confidence


# —————————— let's go ——————————
buddy = SpamBuddy()
buddy.teach_me_good_and_bad()

print("\ntesting a few...")
for text in [
    "you won a free iphone",
    "lunch at 1?",
    "claim your $1M prize now",
    "hey long time no see"
]:
    tag, conf = buddy.yo_is_this_spam(text)
    print(f"{tag} ({conf:.0%}) → {text}")

print("\n" + "—" * 50)
print("type anything (or q to quit)\n")

while True:
    msg = input("> ").strip()
    if msg.lower() in {"q", "quit", ""}:
        print("later skater")
        break

    tag, conf = buddy.yo_is_this_spam(msg.lower())
    print(f"\n→ {tag} ({conf:.0%})")

    low = msg.lower()
    if any(x in low for x in ["free", "win", "prize", "money", "claim", "congrat"]):
        print("   smells like they're dangling cash")
    if any(x in low for x in ["urgent", "asap", "now", "immediately"]):
        print("   rushing you = classic scam move")
    if any(x in low for x in ["hi", "hey", "lunch", "call", "thanks", "tomorrow"]):
        print("   nah this feels like a real human")
