import pytest
from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
from unittest.mock import patch


def mock_data():
    return [
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana",
            "title": "Notícia bacana",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 5,
            "summary": "Algo muito bacana aconteceu",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana",
            "title": "Notícia super bacana",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 10,
            "summary": "Algo muito bacana aconteceu",
            "category": "Ferramentas",
        }
    ]


@pytest.fixture
def mock_res():
    return {
        "readable": [
            {
                "unfilled_time": 0,
                "chosen_news": [
                    (
                        "Notícia bacana",
                        5,
                    )
                ],
            },
        ],
        "unreadable": [
            ('Notícia super bacana', 10)
        ],
    }


def test_reading_plan_group_news(mock_res):
    with patch('tech_news.analyzer.reading_plan.find_news', mock_data):
        assert ReadingPlanService.group_news_for_available_time(5) == mock_res
        with pytest.raises(ValueError):
            ReadingPlanService.group_news_for_available_time(-1)
