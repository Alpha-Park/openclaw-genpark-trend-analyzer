from client import TrendAnalyzerEngine

if __name__ == "__main__":
    res = TrendAnalyzerEngine.detect_trends([
        {"item": "Smart Noise-Canceling Earbuds", "baseline_impressions": 1000, "current_impressions": 2800, "positive_sentiment_ratio": 0.92},
        {"item": "Vintage Wool Trenchcoat", "baseline_impressions": 500, "current_impressions": 600, "positive_sentiment_ratio": 0.85}
    ])
    print("Detected Trends:", res)
