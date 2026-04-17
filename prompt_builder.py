def build_blog_prompt(title, keywords, words, style):
    return f"""
Write a {style} blog post.

Title: {title}
Keywords: {keywords}
Length: {words} words

Requirements:
- Use headings and subheadings
- Include intro and conclusion
- Make it engaging and readable
"""