import sys
import json
from client import TrendAnalyzerEngine

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "detect_trends",
                "description": "Analyze velocity and sentiment signals to identify breakout product trends",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "signals": {"type": "array"},
                        "velocity_threshold": {"type": "number", "default": 1.5}
                    },
                    "required": ["signals"]
                }
            }]
        }
    elif method == "tools/call":
        args = req.get("params", {}).get("arguments", {})
        out = TrendAnalyzerEngine.detect_trends(args.get("signals", []), float(args.get("velocity_threshold", 1.5)))
        return {"content": [{"type": "text", "text": json.dumps(out, indent=2)}]}
    return {"error": "Unsupported method"}

if __name__ == "__main__":
    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()
