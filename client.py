"""Commerce Trend Analyzer Engine.
100% Python Standard Library.
"""

class TrendAnalyzerEngine:
    """Analyzes engagement velocity, search spikes, and product sentiment momentum."""

    @staticmethod
    def detect_trends(signals: list, velocity_threshold: float = 1.5) -> dict:
        surging_trends = []
        for s in signals:
            item = s.get("item", "unknown")
            baseline = max(1.0, float(s.get("baseline_impressions", 100.0)))
            current = float(s.get("current_impressions", 100.0))
            velocity = current / baseline
            sentiment = float(s.get("positive_sentiment_ratio", 0.8))

            if velocity >= velocity_threshold:
                surging_trends.append({
                    "item": item,
                    "velocity_ratio": round(velocity, 2),
                    "sentiment_score": round(sentiment, 2),
                    "trend_label": "BREAKOUT" if velocity > 2.5 else "EMERGING"
                })

        surging_trends.sort(key=lambda x: x["velocity_ratio"], reverse=True)
        return {
            "total_signals_analyzed": len(signals),
            "surging_trends_count": len(surging_trends),
            "trends": surging_trends
        }
