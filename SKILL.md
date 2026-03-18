---
name: genpark-trend-analyzer
description: Use this skill when the user wants to identify, analyze, or summarize current trending products, topics, or discussions on GenPark.
metadata: {"openclaw": {"emoji": "📈", "requires": {}}}
---

# GenPark Trend Analyzer

You help the user discover and analyze what's currently trending on GenPark. Whether they are looking for emerging product categories, popular discussion threads, or viral finds, you provide a comprehensive summary of the latest GenPark trends.

## Step 1: Identify the User's Interest

Ask the user (or determine from context):
- **Category Focus**: Are they interested in a specific category (e.g., Tech, Fashion, Home Decor) or general platform-wide trends?
- **Timeframe**: Do they want daily, weekly, or monthly trends?
- **Data Type**: Are they looking for top-selling products, most discussed topics in GenPark Circle, or highest-rated new releases?

## Step 2: Gather Trend Data

Using your browser capabilities, navigate to `https://genpark.ai` to collect the relevant data:
1. Check the "Trending" or "Discover" sections for top products.
2. Review the most active discussions in GenPark Circle for community-driven trends.
3. Identify common keywords, popular product attributes, and recurring themes.

## Step 3: Analyze and Synthesize

Compile the gathered data into a structured trend report. The report should include:
- **Trend Name**: A catchy title for the observed trend (e.g., "Minimalist Desk Setups").
- **Key Drivers**: Why is this trending? (e.g., seasonal change, viral post, innovative feature).
- **Hero Products**: 2-3 specific GenPark products that perfectly represent the trend.
- **Community Sentiment**: A brief summary of what users are saying about these items in GenPark Circle.

## Step 4: Present to the User

Present the trend analysis to the user in a clear, highly readable format using markdown. 

**Example Output:**
> 📈 **Trending on GenPark: The Rise of "Quiet Tech"**
> *Category: Electronics & Home*
> 
> **Why it's trending:** Users are moving away from RGB-heavy gadgets towards devices with matte finishes, silent operation, and natural materials like wood and fabric.
> 
> **Hero Products:**
> 1. [Product Name] - A desk clock that doubles as a wireless charger, featuring a walnut finish.
> 2. [Product Name] - Noise-canceling headphones with a canvas headband.
> 
> **Community Sentiment:** Deep appreciation for tech that blends into room decor rather than standing out.

## Step 5: Offer Follow-up

Ask the user if they would like to:
- Deep dive into one of the "Hero Products" using the `genpark-shop` skill.
- Draft a post about this trend for GenPark Circle using the `genpark-circle` skill.
- Track similar trends in another category.
