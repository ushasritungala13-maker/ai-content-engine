def build_prompt(content_type, tone, audience, length, keywords):

    prompt = f"""
    Generate structured content in JSON format:
    headline, two_lines, cta, body.

    Content Type: {content_type}
    Tone: {tone}
    Target Audience: {audience}
    Length: {length}
    Keywords: {keywords}
    """

    if content_type == "LinkedIn Post":
        prompt += "\nInclude hashtags and make it engaging."

    elif content_type == "Email":
        prompt += "\nUse formal tone and include greeting and closing."

    elif content_type == "Advertisement":
        prompt += "\nMake it persuasive with strong call-to-action."

    return prompt