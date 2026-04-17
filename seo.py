from llm_client import generate_with_retry

def improve_seo(blog, model):
    prompt = f"""
Improve this blog for SEO:
- Better headings
- Keyword optimization
- More engaging tone

Blog:
{blog}
"""
    return generate_with_retry(prompt, model)