# src/event_engine/event_classifier.py

class EventClassifier:

    @staticmethod
    def classify_event(news_title):

        title = news_title.lower()

        # =========================
        # EVENT RULES
        # =========================

        if any(word in title for word in ["war", "conflict", "attack", "missile"]):
            return {
                "event": "WAR",
                "impact": "Oil Up → Market Negative",
                "severity": "HIGH"
            }

        elif any(word in title for word in ["rbi", "repo rate", "inflation", "policy"]):
            return {
                "event": "RBI_POLICY",
                "impact": "Banking & Market Volatility",
                "severity": "HIGH"
            }

        elif any(word in title for word in ["fed", "interest rate", "us inflation"]):
            return {
                "event": "GLOBAL_MACRO",
                "impact": "IT Stocks & Global Impact",
                "severity": "MEDIUM"
            }

        elif any(word in title for word in ["oil", "crude"]):
            return {
                "event": "OIL_MOVEMENT",
                "impact": "Energy Sector Impact",
                "severity": "MEDIUM"
            }

        elif any(word in title for word in ["profit", "earnings", "results"]):
            return {
                "event": "EARNINGS",
                "impact": "Stock Specific Movement",
                "severity": "MEDIUM"
            }

        else:
            return {
                "event": "GENERAL",
                "impact": "No major impact",
                "severity": "LOW"
            }
