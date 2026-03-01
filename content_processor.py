def generate_content(data):
    tone = data.get('tone', 'professional')
    audience = data.get('audience', '')
    length = data.get('length', 'medium')
    keywords = data.get('keywords', '')
    content_type = data.get('contentType', 'linkedin')

    # Dynamic prompt
    prompt = f"Write a {length} {content_type} content with {tone} tone"
    if audience:
        prompt += f" for {audience}"
    if keywords:
        prompt += f" including these keywords: {keywords}"
    
    # Here you would call OpenAI API or any model
    # For now, let's return a placeholder
    generated_text = f"Generated content based on prompt:\n{prompt}"

    # Post-processing based on content type
    if content_type == 'linkedin':
        generated_text += "\n\n#Example #LinkedIn"
    elif content_type == 'email':
        generated_text = "Subject: Your Subject Here\n\n" + generated_text
    elif content_type == 'ad':
        generated_text += "\nCall to Action: Buy Now!"

    return generated_text