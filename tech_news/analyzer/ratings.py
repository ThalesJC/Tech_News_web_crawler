from tech_news.database import find_news


def top_5_categories():
    news = find_news()
    categories = [new["category"] for new in news]
    counter = {}
    for category in categories:
        counter[category] = counter.get(category, 0) + 1
    top_5 = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    return [category for category, count in top_5[:5]]
