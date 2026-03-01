def process_content(content_type, content):

    if content_type == "LinkedIn Post":
        content["body"] += "\n\n#AI #Innovation #Technology"

    elif content_type == "Email":
        content["body"] = f"Dear Customer,\n\n{content['body']}\n\nBest Regards,\nYour Company"

    elif content_type == "Advertisement":
        content["cta"] += " 🔥 Limited Offer!"

    return content