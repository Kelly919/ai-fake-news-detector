from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import re
import uuid

from services.article_service import ArticleService
from repositories.inmemory.in_memory_article_repository import InMemoryArticleRepository
from src.news_article import NewsArticle

router = APIRouter()

repo = InMemoryArticleRepository()
service = ArticleService(repo)


# Request model for article creation
class ArticleCreateRequest(BaseModel):
    title: str
    content: str
    url: Optional[str] = None


# Validation function
def validate_article(title: str, content: str, url: str = None):
    """Validate article data before submission"""
    
    # Title validation
    if not title or not title.strip():
        raise ValueError("Title cannot be empty")
    
    if len(title) < 3:
        raise ValueError("Title must be at least 3 characters")
    
    if len(title) > 200:
        raise ValueError("Title cannot exceed 200 characters")
    
    # Content validation
    if not content or not content.strip():
        raise ValueError("Content cannot be empty")
    
    if len(content) < 50:
        raise ValueError("Content must be at least 50 characters")
    
    if len(content) > 5000:
        raise ValueError("Content cannot exceed 5000 characters")
    
    # URL validation (if provided)
    if url:
        url_pattern = re.compile(r'^https?://[^\s]+$')
        if not url_pattern.match(url):
            raise ValueError("Please provide a valid URL starting with http:// or https://")
    
    return True


@router.get("/api/articles")
def get_articles():
    return service.get_all_articles()


@router.post("/api/articles")
def create_article(request: ArticleCreateRequest):
    # Validate the input
    try:
        validate_article(
            title=request.title,
            content=request.content,
            url=request.url
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    # Combine title and content for the NewsArticle text field
    combined_text = f"Title: {request.title}\n\nContent: {request.content}"
    
    # Create article with validated data
    article_id = str(uuid.uuid4())  # Generate unique ID
    article = NewsArticle(article_id, combined_text)
    
    # Store URL separately if needed (optional)
    if request.url:
        article.url = request.url
    
    service.create_article(article)
    return {
        "message": "Article created successfully",
        "article_id": article_id,
        "title": request.title,
        "content_preview": request.content[:100] + "..." if len(request.content) > 100 else request.content
    }


@router.put("/api/articles/{article_id}")
def update_article(article_id: str):
    updated_article = NewsArticle(article_id, "Updated article text")
    service.update_article(article_id, updated_article)
    return {"message": "Article updated"}


@router.delete("/api/articles/{article_id}")
def delete_article(article_id: str):
    service.delete_article(article_id)
    return {"message": "Article deleted"}


@router.post("/api/articles/{article_id}/analyze")
def analyze_article(article_id: str):
    return {
        "article_id": article_id,
        "classification": "Fake",
        "credibility_score": 25
    }