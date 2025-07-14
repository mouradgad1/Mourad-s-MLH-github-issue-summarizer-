def mourad_sum(x):
    a = x['title']
    b = x['body'] or "No description available."
    c = b.strip().replace("\n", " ")[:400] + "..."
    return f"Issue: {a}\nSummary: {c}\n"
