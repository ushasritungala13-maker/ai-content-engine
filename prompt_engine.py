def build_prompt(data):

    prompt = f"""
    Generate a {data['content_type']}.

    Tone: {data['tone']}
    Target Audience: {data['audience']}
    Length: {data['length']}
    Include these keywords: {data['keywords']}
    """

    if data["content_type"] == "LinkedIn Post":
        prompt += "\nAdd relevant hashtags at the end."

    elif data["content_type"] == "Email":
        prompt += "\nInclude subject line and proper professional structure."

    elif data["content_type"] == "Ad Copy":
        prompt += "\nInclude a strong Call-To-Action at the end."

    return prompt