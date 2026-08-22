import requests
import os
import re
import yaml

NEWS_API_KEY = "aea1bba28a83406084929c7d5fbc565f"

def sanitize_filename(title):
    """Sanitize the title to create a valid filename."""
    sanitized_title = re.sub(r'[^\w\s-]', '', title)  # Remove special characters
    sanitized_title = sanitized_title.replace(" ", "-").lower()
    return sanitized_title

def download_image(image_url, save_path):
    """Download and save the image locally, ensuring the directory exists."""
    if not image_url:
        return None  # Skip if no image

    os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Ensure directory exists

    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(save_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            return save_path
    except Exception as e:
        print(f"❌ Failed to download image: {e}")
    
    return None

def fetch_news():
    url = f"https://newsapi.org/v2/top-headlines?category=technology&language=en&apiKey={NEWS_API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"❌ Failed to fetch news. Status Code: {response.status_code} | Response: {response.text}")
        return []

    articles = response.json().get("articles", [])[:5]
    news_list = []

    for article in articles:
        news_data = {
            "title": article["title"],
            "url": article["url"],  # Use `url` instead of `news_url`
            "summary": article["description"],
            "image": article.get("urlToImage", ""),
            "date": article["publishedAt"]
        }
        news_list.append(news_data)
        save_news_as_markdown(news_data)

    return news_list

def save_news_as_markdown(news):
    file_title = sanitize_filename(news['title'])
    filename = f"content/news/{file_title}/index.md"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    os.makedirs("static/news_images", exist_ok=True)  # ✅ Ensure image directory exists

    # Download image and save it locally
    image_filename = sanitize_filename(news["title"]) + ".jpg"
    image_path = f"static/news_images/{image_filename}"
    downloaded_image_path = download_image(news["image"], image_path)

    content_dict = {
        "title": news["title"],
        "date": news["date"],
        "summary": news["summary"],
        "external_link": news["url"],  # ✅ Use `external_link` instead of `news_url`
        "image": {"filename": f"news_images/{image_filename}" if downloaded_image_path else ""},
    }

    yaml_content = yaml.dump(content_dict, default_flow_style=False, allow_unicode=True)

    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"---\n{yaml_content}---\n")

    print(f"✅ Created: {filename}")

if __name__ == "__main__":
    fetch_news()
    print("🎉 News updated successfully!")
