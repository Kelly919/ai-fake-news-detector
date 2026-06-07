from services.user_service import UserService
from services.article_service import ArticleService
from services.result_service import ResultService

from repositories.inmemory.in_memory_user_repository import InMemoryUserRepository
from repositories.inmemory.in_memory_article_repository import InMemoryArticleRepository
from repositories.inmemory.in_memory_result_repository import InMemoryResultRepository

from src.user import User
from src.news_article import NewsArticle
from src.result import Result

def test_create_user():

    repo = InMemoryUserRepository()

    service = UserService(repo)

    user = User("1", "Kelly", "Admin")

    created_user = service.create_user(user)

    assert created_user.name == "Kelly"


def test_create_article():

    repo = InMemoryArticleRepository()

    service = ArticleService(repo)

    article = NewsArticle("1", "Fake news article")

    created_article = service.create_article(article)

    assert created_article.text == "Fake news article"


def test_create_result():

    repo = InMemoryResultRepository()

    service = ResultService(repo)

    result = Result("1", 90, "Fake")

    created_result = service.create_result(result)

    assert created_result.classification == "Fake" 

def test_create_multiple_users():

    repo = InMemoryUserRepository()
    service = UserService(repo)

    user1 = User("1", "Kelly", "Admin")
    user2 = User("2", "John", "User")

    service.create_user(user1)
    service.create_user(user2)

    assert len(repo.find_all()) == 2

def test_create_multiple_articles():

    repo = InMemoryArticleRepository()
    service = ArticleService(repo)

    article1 = NewsArticle("1", "Article One")
    article2 = NewsArticle("2", "Article Two")

    service.create_article(article1)
    service.create_article(article2)

    assert len(repo.find_all()) == 2

def test_create_multiple_results():

    repo = InMemoryResultRepository()
    service = ResultService(repo)

    result1 = Result("1", 90, "Fake")
    result2 = Result("2", 95, "Real")

    service.create_result(result1)
    service.create_result(result2)

    assert len(repo.find_all()) == 2

def test_created_user_is_saved_in_repository():

    repo = InMemoryUserRepository()
    service = UserService(repo)

    user = User("1", "Kelly", "Admin")

    service.create_user(user)

    saved_user = repo.find_by_id("1")

    assert saved_user.name == "Kelly"
    
                                                                                                                                                                                                                                                                      